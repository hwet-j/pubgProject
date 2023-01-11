import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = 'https://pubg.op.gg/'

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)
# 암시적 대기 (무조건 대기하지 않고 최대 5초)
driver.implicitly_wait(time_to_wait=5)

# 아이디 검색
input_id = 'Hwet_J'
search_id = driver.find_element(By.XPATH, '//*[@id="searchPlayerText"]')
search_id.send_keys(input_id)
search_id.submit()            # 해당 위치에서 Enter 효과
driver.implicitly_wait(time_to_wait=5)

# 플랫폼 확인
platform = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[2]/div/div/div/div/div[2]/div[1]/span').text
platform_text = platform.find(r'([0-9A-Za-z]+)\_')
