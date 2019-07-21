from selenium import webdriver
import time
m=input()
browser=webdriver .Chrome ()
url='http://wap.cnki.net/touch/web/guide'
browser.get(url)
input=browser .find_element_by_xpath('//*[@id="keyword"]')
input.send_keys(m)
put=browser.find_element_by_xpath('//*[@id="btnSearch "]')
put.click()
for i in range(0,5):
    pput = browser.find_element_by_xpath('//*[@id="nextpage_a"]')
    pput.click()
time.sleep(5)
result=browser.find_element_by_xpath('//*[@id="searchlist_div"]')
with open('zhiwang.text','a',encoding= 'utf-8')as fp:
    fp.write(result.text)
print(result.text)
