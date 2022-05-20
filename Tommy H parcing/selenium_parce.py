from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service
import json
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By


url = "https://usa.tommy.com/en/tommy-hilfiger-sale"
options = webdriver.ChromeOptions()
options.add_argument(
    f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")

options.add_argument(
    "accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url)
driver.find_element(By.CLASS_NAME, "closeXImg").click()

time.sleep(5)
driver.find_element(By.CLASS_NAME, "alt1").click()
time.sleep(10)
# # url = "https://usa.tommy.com/en/all-gender/tommy-hilfiger-sale/big-kids-sleeveless-pleated-dress-71j1033"
# options = webdriver.ChromeOptions()
# options.add_argument(
#     f"user-agent={UserAgent().random}")
# #
# s = Service('D:\python\Tommy H\Tommy_parce\Tommy H parcing\chromedriver\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(service=s, options=options)
# #
#
# with open("headers.json") as file:
#     headers = json.load(file)
# try:
#     driver.get(url)
#     # driver.refresh()
#     time.sleep(5)
#     # el = driver.find_element(By.CLASS_NAME, "pproductImage focusParent")
#     # for i in el:
#     #     print(i)
#     #
#     # print(el)
#
# except Exception as e:
#     print(e)
# finally:
driver.close()
driver.quit()
#
# # driver.get(url)
# el = driver.find_element(By.CLASS_NAME, "pproductImage focusParent")
