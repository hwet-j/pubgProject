def dakggCrawling(name, platform):
    import pandas as pd
    import os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    import time
    URL = 'https://dak.gg/pubg'

    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")

    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=options)
    # driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    # 브라우저 위치 설정
    # driver.set_window_position(-2500, -400)
    driver.set_window_position(0, 0)
    # 브라우저 크기 설정
    # driver.set_window_size(1250, 1200)
    driver.set_window_size(820, 800)

    try:
        driver.get(url=URL)
        # 암시적 대기 (무조건 대기하지 않고 최대 5초)
        driver.implicitly_wait(time_to_wait=5)

        # 아이디 검색
        input_id = name
        search_id = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/section[1]/div/form/input')
        search_id.send_keys(input_id)
        search_id.submit()  # 해당 위치에서 Enter 효과
        driver.implicitly_wait(time_to_wait=10)

        if "Steam" in platform or "스팀" in platform or 'steam' in platform:
            user_platform = "Steam"
        elif "Kakao" in platform or "카카오" in platform or 'kakao' in platform:
            user_platform = "Kakao"
        else:
            user_platform = "None"

        time.sleep(2.5)
        match_URL = URL + "/profile/" + user_platform.lower() + "/" + input_id + "/pc-2018-21/matches"
        driver.get(match_URL)
        driver.implicitly_wait(time_to_wait=5)

        # 전적갱신
        # WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, '#__layout > div > main > header > div.Header__player > div > div > button.Header__button.Header__button--update.Header__button--latest'))).click()
        # driver.implicitly_wait(time_to_wait=10)

        # page 개수를 가져온다.(각 시즌 마다 플레이)
        li_list = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#__layout > div > main > div:nth-child(4) > section > nav > ul > li')))

        if os.path.isfile("./datas/" + name + ".csv"):
            be_player_data = pd.read_csv("./datas/" + name + ".csv")
        else:
            be_player_data = pd.DataFrame()

        # 데이터 프레임의 각 칼럼을 생성할 리스트 목록
        dbnos_list = []
        assists_list = []
        boosts_list = []
        damage_dealt_list = []
        headshot_kills_list = []
        heals_list = []
        kills_list = []
        longest_kill_list = []
        revives_list = []
        total_distance_list = []
        ride_distance_list = []
        road_kills_list = []
        swim_distance_list = []
        vehicle_destroys_list = []
        time_survived_list = []
        walk_distance_list = []
        weapons_acquired_list = []
        win_place_list = []
        team_count_list = []
        map_name_list = []
        duration_list = []

        # 페이지 수에 따라 페이지 별로 정보 파악 (최대 5페이지 까지만)
        for page_num in range(len(li_list)):
            if page_num >= 5:
                break
            match_page = match_URL + "/" + str(page_num + 1)
            driver.get(match_page)
            driver.implicitly_wait(time_to_wait=5)
            stat_li_list = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#__layout > div > main > div:nth-child(4) > section > ul > li')))
            for stat_li in stat_li_list:
                # 상세보기 클릭 (숨겨져있어 클릭하지 않으면 크롤링 안됨)
                stat_li.find_element(By.CSS_SELECTOR, "li > div > section.Match > div > button").send_keys(Keys.ENTER)
                driver.implicitly_wait(time_to_wait=5)
                game_map = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section > dl > div.Info.Match__info--map > dd'))).text
                rank_data = WebDriverWait(stat_li, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li > div > section.Match > header > p.Match__rank > span')))
                game_mode = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match > header > strong'))).text
                my_rank = rank_data[0].text[1:]
                total_team = rank_data[1].text[1:]
                # 경쟁전 데이터를 가져오고 싶으나 dakgg에는 구분하지않아 팀의 수로 판별 (스쿼드 이면서 19팀 이하만)
                if int(total_team) >= 20 or game_mode != "스쿼드" or game_map not in ['에란겔', '태이고', '미라마']:
                    continue
                damage = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(1) > dd'))).text
                kill = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(2) > dd'))).text
                head_kill = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(3) > dd'))).text
                assist = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(4) > dd'))).text
                road_kill = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(5) > dd'))).text
                destroy_vehicle = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(6) > dd'))).text
                dbno = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(7) > dd'))).text
                revive = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(4) > div:nth-child(8) > dd'))).text
                survival_time = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(1) > dd'))).text
                boost = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(2) > dd'))).text
                heal = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(3) > dd'))).text
                acquired_weapon = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(4) > dd'))).text
                total_distance = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(5) > dd'))).text
                walk_distance = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(6) > dd'))).text
                ride_distance = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(7) > dd'))).text
                swim_distance = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > dl:nth-child(6) > div:nth-child(8) > dd'))).text
                longest_kill = WebDriverWait(stat_li, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li > div > section.Match > dl > div.Info.Match__info--longest.d-none.d-md-flex > dd'))).text[:-1]
                total_distance = total_distance[:total_distance.find("km")]
                walk_distance = walk_distance[:walk_distance.find("km")]
                ride_distance = ride_distance[:ride_distance.find("km")]
                swim_distance = swim_distance[:swim_distance.find("km")]
                # 전체 순위 클릭 (1위 생존시간을 기준으로 게임의 지속시간을 추출)
                stat_li.find_element(By.CSS_SELECTOR, "li > div > section.Match__section-detail > ul > li:nth-child(3) > button").click()
                winner_list = WebDriverWait(stat_li, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li > div > section.Match__section-detail > div > ul > li:nth-child(1) > ul > li')))
                time_minn = int(survival_time[:survival_time.find("분")])
                time_secc = int(survival_time[survival_time.find("분") + 1:survival_time.find("초")])
                time_survived = 60 * time_minn + time_secc
                longest_kill = float(int(longest_kill) / 1000)
                minute = 0
                second = 0
                temp_minute = 0
                temp_second = 0
                for winner in winner_list:
                    # 브라우저 크기에 따라 출력이 안되는 문제가 발생한다...
                    live_time = WebDriverWait(winner, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'li > ul > li.Team__stat.col.col-11.d-none.d-md-flex'))).text
                    minute = int(live_time[:live_time.find(":")])
                    second = int(live_time[live_time.find(":")+1:])
                    if minute > temp_minute:
                        temp_minute = minute
                        temp_second = second
                    elif minute == temp_minute:
                        if second >= temp_second:
                            temp_second = second
                    else:
                        pass
                duration = 60 * temp_minute + temp_second
                dbnos_list.append(dbno)
                assists_list.append(assist)
                boosts_list.append(boost)
                damage_dealt_list.append(damage)
                headshot_kills_list.append(head_kill)
                heals_list.append(heal)
                kills_list.append(kill)
                longest_kill_list.append(longest_kill)
                revives_list.append(revive)
                total_distance_list.append(total_distance)
                ride_distance_list.append(ride_distance)
                road_kills_list.append(road_kill)
                swim_distance_list.append(swim_distance)
                vehicle_destroys_list.append(destroy_vehicle)
                time_survived_list.append(time_survived)
                walk_distance_list.append(walk_distance)
                weapons_acquired_list.append(acquired_weapon)
                win_place_list.append(my_rank)
                team_count_list.append(total_team)
                map_name_list.append(game_map)
                duration_list.append(duration)

        player_data = pd.DataFrame(
                    zip(dbnos_list,
                        assists_list,
                        boosts_list,
                        damage_dealt_list,
                        headshot_kills_list,
                        heals_list,
                        kills_list,
                        longest_kill_list,
                        revives_list,
                        total_distance_list,
                        ride_distance_list,
                        road_kills_list,
                        swim_distance_list,
                        vehicle_destroys_list,
                        time_survived_list,
                        walk_distance_list,
                        weapons_acquired_list,
                        win_place_list,
                        team_count_list,
                        map_name_list,
                        duration_list))
        if player_data.empty:   # 추출된 데이터가 없으면 칼럼지정이 불가능하여 스킵
            print("경쟁전 데이터가 존재하지 않습니다.")
        player_data.columns = ['dbnos',
                            'assists',
                            'boosts',
                            'damage_dealt',
                            'headshot_kills',
                            'heals',
                            'kills',
                            'longest_kill',
                            'revives',
                            'total_distance',
                            'ride_distance',
                            'road_kills',
                            'swim_distance',
                            'vehicle_destroys',
                            'time_survived',
                            'walk_distance',
                            'weapons_acquired',
                            'win_place',
                            'team_count',
                            'map_name',
                            'duration']
        player_data['user_id'] = name
        player_data = pd.concat([player_data, be_player_data], ignore_index=True)
        player_data.drop_duplicates(inplace=True)
        player_data = player_data[['user_id', 'dbnos', 'assists', 'boosts', 'damage_dealt',
         'headshot_kills', 'heals', 'kills', 'longest_kill', 'revives',
         'total_distance', 'ride_distance', 'road_kills', 'swim_distance',
         'vehicle_destroys', 'time_survived', 'walk_distance',
         'weapons_acquired', 'team_count', 'map_name', 'duration', 'win_place']]
        player_data.to_csv("C:/Users/ghlck/PycharmProjects/pubg/MatchList/django_apply/datas/" + name + ".csv", index=False)
    except:
        pass
    finally:
        # 옵션으로 창 숨겨서 실행 했으므로 종료(background에서 리소스를 사용할 수 있음)
        driver.quit()

if __name__ == "__main__":
    name = "Hwet_J"
    platform = "스팀"
    dakggCrawling(name, platform)