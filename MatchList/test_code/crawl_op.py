import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys

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
    '''user_platform = "None"
    try:
        platform = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,
                  '/html/body/div[1]/section/div[2]/div/div/div/div/div[2]/div[1]/span'))).text
        # print('위치3')
        if "Steam" in platform:
            user_platform = "Steam"
        elif "Kakao" in platform:
            user_platform = "Kakao"
        else:
            print("Steam, kakao의 정보가 아닙니다.")
    except Exception as e:
        print(e)
        # print("플랫폼 정보 업데이트에 실패")

    print(name, "의 플랫폼 :",user_platform)'''

    # 전적갱신
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, '#renewBtn'))).click()
    # driver.implicitly_wait(time_to_wait=5)
    
    # 경쟁전 버튼 클릭
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
         '#matchDetailWrap > div.user-content-layer__matches-filter > div > ul > li:nth-child(2) > button'))).click()

    # 더보기 버튼을 클릭하여 정보를 더 가져온다.(전체 정보가 아닌 3번만 클릭)  -> click 함수로 작동 되지 않음 (script 명령어로 해결 / 숨겨진 정보?에서 이런 문제가 발생한다고함)
    '''for i in range(3):
        add_more = driver.find_element(By.CSS_SELECTOR, '#matchDetailWrap > div.user-content-layer__matches-content > div:nth-child(1) > div > div > div.user-content-layer__matches-list > button')
        driver.execute_script("arguments[0].click();", add_more)
        driver.implicitly_wait(time_to_wait=5)
        time.sleep(2)'''

    # 전적 가져오기
    li_data = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '#matchDetailWrap > div.user-content-layer__matches-content > div:nth-child(1) > div > div > div.user-content-layer__matches-list > ul > li')))

    # print(len(li_data))
    for element in li_data:
        kill = WebDriverWait(element, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.matches-item__summary > div.matches-item__column.matches-item__column--kill > div.matches-item__value'))).text
        damage = WebDriverWait(element, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.matches-item__summary > div.matches-item__column.matches-item__column--damage > div.matches-item__value'))).text
        rank = element.find_element(By.CSS_SELECTOR,
                     'div.matches-item__summary > div.matches-item__column.matches-item__column--rank > div > div.matches-item__ranking').get_attribute("innerHTML")
        extract_roster = rank.split("/")[-1]      # 총 참가팀
        extract_rank = rank[rank.rfind("#</span>")+8:rank.rfind("</span>/")]        # 플레이어의 팀 순위

        sys.exit()
        #  > div.matches-item__ranking > span.matches-item__my-ranking > span
        #                       div.matches-item__summary > div.matches-item__column.matches-item__column--rank > div > div.matches-item__ranking > span


    # while (True):       # 브라우저가 자동으로 종료되는 것을 막기위해 while문 작성
    #     pass


if __name__ == "__main__":
    game_id = "Hwet_J"
    opggCrawling(game_id)


