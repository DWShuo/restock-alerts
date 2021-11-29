import sys
import ast
import requests
import logging as log
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as driverWait

def urlBuilder(sku, SMS=False): # bypass sms filtering links as spam
    if not SMS:
        return "https://www.bestbuy.com/site/" + sku + ".p?skuId=" + sku
    else:
        return "bestbuy.com/site/" + sku + ".p?skuId=" + sku

def discordSend(msg):
    data = {"content": "{}".format(msg)}
    response = requests.post(DISCORD_WEBHOOK, json=data)
    log.info(response.status_code)
    log.info(response.content)

def restockChecker(sku):
    # Basic anti-bot detection countermeasures
    options = Options()
    options.headless = True
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    driver = webdriver.Firefox(options=options)
    driver.get(urlBuilder(sku))
    while True:
        # Check if add to cart button is clickable, check every 10 seconds
        try:
            addToCartBtn = driverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button")))
            log.info("Add to cart found, item restocked")
        except Exception as e:
            # Error during add to cart button check, refresh page
            log.error(repr(e))
            log.info("Error encounterd in clickability check, refreshing page")
            driver.refresh()
            continue
        # Attemp to send text notification
        try:
            log.info("Sending discord notifications")
            skuName = driver.find_element(By.CLASS_NAME, "sku-title").text
            skuName = skuName.encode('ascii', 'ignore').decode('ascii')
            msg = "ITEM RESTOCK:\n" + skuName + "\n" + urlBuilder(sku)
            discordSend(msg)
            break
        except Exception as e:
            log.error(repr(e))
            discordSend("notification script failed, manual intervention required")
            break
    driver.quit()

if __name__ == "__main__":
    SKU = ast.literal_eval(sys.argv[1])  # read argv[1] as list of SKUs
    DISCORD_WEBHOOK = sys.argv[2]  # read argc[2] as webhook url

    print(SKU)
    print(DISCORD_WEBHOOK)

    log.basicConfig(filename='events.log', filemode='w', encoding='utf-8', level=log.WARNING)
    # spin up new process for each item in back ground
    threads = []
    for each in SKU:
        t = Thread(target=restockChecker, args=[str(each)])
        t.start()
        threads.append(t)
    for each in threads:
        each.join()
