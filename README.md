# restock-alerts

## Setup

### Dependencies
* [Python 3](https://www.python.org/downloads/)
* [Pip](https://pypi.org/project/pip/)
* [Selenium](https://www.selenium.dev/downloads/)
* [fake-useragent](https://pypi.org/project/fake-useragent/)

### Install
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
4. Find the following line of code in restock-alerts.py
 ```python
 driver = webdriver.Firefox(options=options)
 ```
5. Replace it with the following
 ```python
 driver = webdriver.Firefox(options=options, executable_path=r'your\path\geckodriver.exe')
 ```
