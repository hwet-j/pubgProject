import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

def opggCrawling(name):
    URL = 'https://pubg.op.gg/'

    driver = webdriver.Chrome(executable_path='chromedriver')
    # 브라우저 위치 설정
    driver.set_window_position(0,0)
    # 브라우저 크기 설정
    driver.set_window_size(720, 800)

    driver.get(url=URL)
    # 암시적 대기 (무조건 대기하지 않고 최대 5초)
    driver.implicitly_wait(time_to_wait=5)

    # 아이디 검색
    input_id = name
    search_id = driver.find_element(By.XPATH, '//*[@id="searchPlayerText"]')
    search_id.send_keys(input_id)
    search_id.submit()            # 해당 위치에서 Enter 효과
    driver.implicitly_wait(time_to_wait=5)

    # 플랫폼 확인
    platform = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH , '/html/body/div[1]/section/div[2]/div/div/div/div/div[2]/div[1]/span')).text
        )
    platform_text = platform.find(r'([0-9A-Za-z]+)\_')


