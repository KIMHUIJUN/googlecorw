from urllib.parse import quote_plus as qp
from urllib.request import urlopen
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import urllib.request
from selenium.webdriver.common.keys import Keys

plusurl = input('검색할 태그를 입력하세요: ')
url = f'https://www.google.com/search?q={qp(plusurl)}&source=lnms&tbm=isch&sa=X&ved'

driver = webdriver.Chrome("C:/Users/chromedriver.exe")
driver.get(url)
time.sleep(10)

#스크롤 횟수
body = driver.find_element(By.CSS_SELECTOR, 'body')
for x in range(3):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

get_img = 1000
s = 1
a = 1
for i in range(get_img):
    if a % 25 == 0:
        a += 1

    thumbnails = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(a)).get_attribute('src')
    time.sleep(3)
    urllib.request.urlretrieve(thumbnails, "{}.jpg".format(s))
    time.sleep(3)
    print(a)
    a += 1
    s += 1
    if a % 30 == 0:
        for x in range(3):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(3)




