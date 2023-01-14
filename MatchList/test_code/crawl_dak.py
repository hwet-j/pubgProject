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


def dakggCrawling(name):
    URL = 'https://dak.gg/pubg'

    driver = webdriver.Chrome(executable_path='chromedriver')
    # 브라우저 위치 설정
    driver.set_window_position(-2500, -400)
    # driver.set_window_position(0, 0)
    # 브라우저 크기 설정
    driver.set_window_size(1250, 1200)
    # driver.set_window_size(700, 800)

    driver.get(url=URL)
    # 암시적 대기 (무조건 대기하지 않고 최대 5초)
    driver.implicitly_wait(time_to_wait=5)

    # 아이디 검색
    input_id = name
    search_id = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/section[1]/div/form/input')
    search_id.send_keys(input_id)
    search_id.submit()  # 해당 위치에서 Enter 효과
    driver.implicitly_wait(time_to_wait=10)

    # 플랫폼 확인
    user_platform = "None"
    while True:
        try:
            platform = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                       '#__layout > div > main > header > div.Header__option > div > div'))).text
            print(platform)
            # print('위치3')
            if "Steam" in platform or "스팀" in platform:
                user_platform = "Steam"
            elif "Kakao" in platform or "카카오" in platform:
                user_platform = "Kakao"
            else:
                print("Steam, kakao의 정보가 아닙니다.")
            break
        except Exception as e:
            print("플랫폼 정보 업데이트에 실패")
            # print(e)

    print(input_id, "의 플랫폼 :", user_platform)
    # 매치기록 페이지로 이동 (클릭으로 해결하려 했으나 클릭이 안됨)
    '''# 매치기록 버튼 클릭
    match_button = driver.find_element(By.CSS_SELECTOR,
                                   '#__layout > div > main > nav > a.ProfileTabs__tab.nuxt-link-exact-active.nuxt-link-active')
    driver.execute_script("arguments[0].click();", match_button)
    driver.implicitly_wait(time_to_wait=5)'''
    match_URL = URL + "/profile/" + user_platform.lower() + "/" + input_id + "/pc-2018-21/matches"
    driver.get(match_URL)
    driver.implicitly_wait(time_to_wait=5)

    # 전적갱신
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, '#__layout > div > main > header > div.Header__player > div > div > button.Header__button.Header__button--update.Header__button--latest'))).click()
    # driver.implicitly_wait(time_to_wait=5)

    # page 개수를 가져온다.(각 시즌 마다 플레이)
    li_list = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '#__layout > div > main > div:nth-child(4) > section > nav > ul > li')))
    
    # 페이지 수에 따라 페이지 별로 정보 파악
    for page_num in range(len(li_list)):
        match_page = match_URL + "/" + str(page_num + 1)
        driver.get(match_page)
        driver.implicitly_wait(time_to_wait=5)
        stat_li_list = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
              '#__layout > div > main > div:nth-child(4) > section > ul > li')))
        for stat_li in stat_li_list:
            # 상세보기 클릭 (숨겨져있어 클릭하지 않으면 크롤링 안됨)
            stat_li.find_element(By.CSS_SELECTOR, "li > div > section.Match > div > button").click()
            driver.implicitly_wait(time_to_wait=5)
            map = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section > dl > div.Info.Match__info--map > dd'))).text
            rank_data = WebDriverWait(stat_li, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li > div > section.Match > header > p.Match__rank > span')))
            my_rank = rank_data[0].text[1:]
            total_team = rank_data[1].text[1:]
            damage = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(1) > dd'))).text
            kill = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(2) > dd'))).text
            head_kill = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(3) > dd'))).text
            assist = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(4) > dd'))).text
            load_kill = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(5) > dd'))).text
            destroy_vehicle = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(6) > dd'))).text
            dbno = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(7) > dd'))).text
            revive = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(8) > dd'))).text
            time_survived = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(1) > dd'))).text
            boost = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(2) > dd'))).text
            heal = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(3) > dd'))).text
            acquired_weapon = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(4) > dd'))).text
            total_distance = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(5) > dd'))).text
            walk_distance = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(6) > dd'))).text
            ride_distance = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(7) > dd'))).text
            swim_distance = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(8) > dd'))).text
            longest_kill = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match > dl > div.Info.Match__info--longest.d-none.d-md-flex > dd'))).text[:-1]
            # 전체 순위 클릭 (1위 생존시간을 기준으로 게임의 지속시간을 추출)
            stat_li.find_element(By.CSS_SELECTOR, "li > div > section.Match__section-detail > ul > li:nth-child(3) > button").click()
            winner_list = WebDriverWait(stat_li, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > ul > li:nth-child(1) > ul > li')))
            temp_minute = 0
            temp_second = 0

            for winner in winner_list:
                live_time = WebDriverWait(winner, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'li > ul > li.Team__stat.col.col-11.d-none.d-md-flex'))).text
                minute = live_time[:live_time.find(":")]
                second = live_time[live_time.find(":")+1:]

                temp_minute = minute
                temp_second = second
                print(live_time)


            time.sleep(10)
            # ul > li:nth-child(1) > ul > li.Team__stat.col.col-11.d-none.d-md-flex
            # __layout > div > main > div:nth-child(4) > section > ul > li:nth-child(1) > div > section.Match__section-detail > ul > li:nth-child(3) > button
            #__layout > div > main > div:nth-child(4) > section > ul > li:nth-child(1) > div > section.Match__section-detail > div > ul > li:nth-child(1)
            print(longest_kill)


        sys.exit()

    while True:       # 브라우저가 자동으로 종료되는 것을 막기위해 while문 작성
        pass

if __name__ == "__main__":
    game_id = "Hwet_J"
    dakggCrawling(game_id)


