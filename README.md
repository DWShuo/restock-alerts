# restock-alerts
Python script used to monitor and notify the user when an item is restocked (currently only bestbuy is supported).

Discord server notification script is used by default, notification utilizes discord webhooks. Webhooks can be
generated under

`Edit channel -> Integrations`

I have also included code for SMS text notification, it utilizes the carrier's mail-to-text service. Depending on the 
carrier there seems to be some serious reliability issues.

### New features
Looking to integrate more stores and alert platforms soon.

## Dependencies
* [Python 3](https://www.python.org/downloads/)
* [Pip](https://pypi.org/project/pip/)
* [Selenium](https://www.selenium.dev/downloads/)
* [geckodriver](https://github.com/mozilla/geckodriver/releases)

## Install and usage
#### Docker container
1. Install [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/)
2. Clone and navigate to this repository
3. Edit the following in the docker-compose.yml file:
```
x-var: &SKU
  "[6321917,6435180,6429442]" # Replace with your Bestbuy SKU
x-var: &WEBHOOK
  "https://discord.com/api/webhooks/..." # Replace with your discord server webhook
 ```
 4. Run `docker-compose up -d`

## Variables

Following variables can be edited
```
#========================== Edit items =========================
SKU = ["6356670", "6454329", "6468928", "6452573", "6468931"]
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/..."
EMAIL = "example@gmail.com"
PWD = "example"
CARRIER = "att" # att, tmobile, verizon, sprint, cricket, boost
SMSNUMBER = "1231231234"
#===============================================================
```
* **SKU**: contains a list of the SKUs to be monitored
* **DISCORD_WEBHOOK**: webhooks can be generated under "edit channel -> integration"
* **EMAIL**: email used to communicate with various carrier's email-to-text systems
* **PWD**: password to said email
* **CARRIER**: specify which carrier you mobile device is using
* **SMSNUMBER**: phone number where you want to receive alerts 
