from datetime import datetime

from selenium import webdriver
from time import sleep

from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def login():
    global key_email, key_pwd
    # 设置自动化打开的浏览器访问网址
    url = 'http://sys.12348.gov.cn/resources/#/lawyer/lawyerIndex'
    # 打开浏览器，并访问设置的网址。
    browser.get(url)
    # 登录
    browser.find_element_by_name('email').send_keys(key_email)
    browser.find_element_by_name('password').send_keys(key_pwd)
    browser.find_element_by_xpath('//input[@value="登录"]').click()
    print("登陆完成 - 5秒后开始自动抢题")
    sleep(5)


key_email = input('请输入账户名：')
key_pwd = input('请输入密码：')

# 设置谷歌浏览器driver的目录所在
path = 'chromedriver.exe'

# 无UI
chrome_options = Options()
# chrome_options.add_argument('--headless')

browser = webdriver.Chrome(executable_path=path, options=chrome_options)
# browser.implicitly_wait(5)  # 隐式等待，确保每一个你查找的元素都能够有足够的load时长

login()
while True:
    try:
        browser.find_element_by_xpath('//div[text()="留言咨询"]').click()
    except:
        # 设置自动化打开的浏览器访问网址
        url = 'http://sys.12348.gov.cn/resources/#/lawyer/lawyerIndex'
        # 打开浏览器，并访问设置的网址。
        browser.get(url)

    try:
        WebDriverWait(browser, 0.15, poll_frequency=0.001).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(string(),"解答")]')))
    except TimeoutException:
        pass
    except StaleElementReferenceException:
        pass
    else:
        # print('"订单出现"')
        try:
            browser.find_element_by_xpath('//button[contains(string(),"解答")]').click()
            # print('"解答"-clicked')
        except:
            pass

        try:
            WebDriverWait(browser, 1.5, poll_frequency=0.001).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(string(),"确定")]')))
        except TimeoutException:
            pass
        except StaleElementReferenceException:
            pass
        else:
            try:
                browser.find_element_by_xpath('//button[contains(string(),"确定")]').click()
                # print('"确定"-clicked')
            except:
                pass
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：尝试抢题')
