import smtplib
import logging as log
from threading import Thread
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as driverWait

#==================  Edit item =================================
SKU = ["6356670", "6454329", "6468928", "6452573", "6468931"]
EMAIL = "example@gmail.com"
PWD = "example"
CARRIER = "att" # att, tmobile, verizon, sprint, cricket, boost
SMSNUMBER = "1231231234"
#===============================================================

carriers = {
    'att':    '@txt.att.net',
    'tmobile': ' @tmomail.net',
    'verizon':  '@vtext.com',
    "boost": "smsmyboostmobile.com",
    "cricket": "sms.cricketwireless.net",
    "sprint": "messaging.sprintpcs.com",
}

def sendSMS(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = '{}{}'.format(SMSNUMBER, carriers[CARRIER])
    auth = (EMAIL, PWD)
    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])
    # Send text message through SMS gateway of destination number
    server.sendmail( auth[0], to_number, message)

def urlBuilder(sku, SMS=False):
    if not SMS:
        return "https://www.bestbuy.com/site/" + sku + ".p?skuId=" + sku
    else:
        return "bestbuy.com/site/" + sku + ".p?skuId=" + sku

def restockChecker(sku):
    # Basic anti-bot detection countermeasures
    ua = UserAgent()
    uaRand = ua.random
    options=Options()
    options.headless = True
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    options.set_preference("general.useragent.override", f"{uaRand}")
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
            log.info("Sending text notifications")
            skuName = driver.find_element(By.CLASS_NAME, "sku-title").text
            skuName = skuName.encode('ascii', 'ignore').decode('ascii')
            msg = skuName + " <==*==> " + urlBuilder(sku, True)
            sendSMS(msg)
            break
        except Exception as e:
            log.error(repr(e))
            log.info("sms notification attempt failed")
            sendSMS("text-notify script failed, manual restart required")
            break
    driver.quit()

if __name__ == "__main__":
    log.basicConfig(filename='events.log', filemode='w', encoding='utf-8', level=log.WARNING)
    
    #spin up new process for each item in back ground
    threads = []
    for each in SKU:
        t = Thread(target=restockChecker, args=[each])
        t.start()
        threads.append(t)

    for each in threads:
        each.join()
