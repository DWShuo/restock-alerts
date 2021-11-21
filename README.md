# restock-alerts
Python script used to monitor and notify the user when an item is restocked.

Monitor multiple items with multithreading

Text notification with link is sent to the user when item is restocked.

## Dependencies
* [Python 3](https://www.python.org/downloads/)
* [Pip](https://pypi.org/project/pip/)
* [Selenium](https://www.selenium.dev/downloads/)
* [fake-useragent](https://pypi.org/project/fake-useragent/)

## Install
#### Linux
1. Install python dependencies.
```sh
pip install -r requirements.txt
```
2. Install latest version of Firefox
3. Find the latest release of Mozilla [Geckodriver](https://github.com/mozilla/geckodriver/releases)
```sh
wget <link to latest tar.gz release> -O /tmp/geckodriver.tar.gz \
tar -C /opt -xzf /tmp/geckodriver.tar.gz
chmod 755 /opt/geckodriver
ln -fs /opt/geckodriver /usr/bin/geckodriver
ln -fs /opt/geckodriver /usr/local/bin/geckodriver
```
#### Windows
1. Install python dependencies.
```sh
pip install -r requirements.txt
```
2. Install latest version of Firefox
3. Find and download the latest release of Mozilla [Geckodriver](https://github.com/mozilla/geckodriver/releases)
4. Find the following line of code in *-restock-alerts.py
 ```python
 driver = webdriver.Firefox(options=options)
 ```
5. Replace it with the following
 ```python
 driver = webdriver.Firefox(options=options, executable_path=r'your\path\geckodriver.exe')
 ```
## Usage

### SMS alerts
Following variables need to be edited
```
#========================== Edit items =========================
SKU = ["6356670", "6454329", "6468928", "6452573", "6468931"]
EMAIL = "example@gmail.com"
PWD = "example"
CARRIER = "att" # att, tmobile, verizon, sprint, cricket, boost
SMSNUMBER = "1231231234"
#===============================================================
```
* **SKU**: contains a list of the SKUs to be monitored
* **EMAIL**: email used to communicate with various carrier's email-to-text systems
* **PWD**: password to said email
* **CARRIER**: specify which carrier you mobile device is using
* **SMSNUMBER**: phone number where you want to receive alerts 

### Discord alerts
Following variables need to be edited
```
#==================  Edit item =================================
SKU = ["6356670", "6454329", "6468928", "6452573", "6468931"]
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/..."
#===============================================================
```
* **SKU**: contains a list of the SKUs to be monitored
* **DISCORD_WEBHOOK**: webhooks can be generated under "edit channel -> integration"
