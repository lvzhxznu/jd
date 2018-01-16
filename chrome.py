from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

import time
# import pickle
# import requests
#

chrome_options = Options()

#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')

browser = webdriver.Chrome(chrome_options = chrome_options)
wait = WebDriverWait(browser, 10)

try:
    browser.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fa.jd.com')

    #click account for display
    account = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div.login-wrap > div.w > div > div.login-tab.login-tab-r > a'))
    )
    account.click()

    #input username
    userName = wait.until(
            EC.presence_of_element_located((By.ID, 'loginname'))
    )
    userName.send_keys('lvzhxznu@163.com')

    #input password
    pwd = wait.until(
            EC.presence_of_element_located((By.ID, 'nloginpwd'))
    )
    pwd.send_keys('gj19780526')

    #click for login
    loginBtn = wait.until(
        EC.presence_of_element_located((By.ID, 'loginsubmit'))
    )
    loginBtn.click()

    #coupoun
    browser.get('https://a.jd.com')

    #滚动条拖到底部
    js = "var q=document.documentElement.scrollTop=10000"
    browser.execute_script(js)

    # itemAll = wait.until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'btn-def'))

    # )

    itemAll = browser.find_elements_by_class_name('btn-def')

    for item in itemAll:
        item.click()
        time.sleep(1)

    #time.sleep(10)

    #html = browser.page_source
    #print(html)
except TimeoutException:
    browser.close()

#browser.close()


