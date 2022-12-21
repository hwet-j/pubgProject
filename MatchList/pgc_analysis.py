# 대회 기록 - PGC 데이터를 사용
# 데이터 분석에 활용할 데이터를 추출
import sys

import matplotlib.pyplot as plt


def pro_anal():
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    from chicken_dinner.pubgapi import PUBGCore
    from chicken_dinner.constants import map_dimensions
    import time
    import numpy as np
    import os
    import warnings
    warnings.filterwarnings('ignore')

    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)
    pubgCore = PUBGCore(api_key=api_key, shard='pc-tournament', gzip=True)

    pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")
    # 전체 데이터를 저장할 데이터 프레임
    all_data = pd.DataFrame()
    # 남은 데이터 확인
    leng = len(pgc_data)

    attack_df = pd.DataFrame()
    teamCount = {}
    whiteCenter_df = pd.DataFrame()
    blueBorder_df = pd.DataFrame()
    playerMove_df = pd.DataFrame()
    firstVehicle_df = pd.DataFrame()

    for cnt, mat in enumerate(pgc_data['match_id']):
        # 이미 저장된 데이터는 생략
        if os.path.isfile(
                "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/Anal/" + mat + ".csv") or cnt == 2:
            print(leng, "개 데이터 중,", cnt + 1, "번째 데이터 SKIP")
            break
        current_match = pubg.match(mat)  # 매치 기록 하나를 가져옴
        telemetry = current_match.get_telemetry()  # 현재 매치의 Telemetry값을 가져옴
        positions = telemetry.player_positions()  # 각플레이어의 위치값을 가져온다.
        circles = telemetry.circle_positions()  # 자기장(원)에 대한 위치 정보를 가져온다. (white, blue, red)
        players = np.array(telemetry.player_names())  # 매치에 참가한 플레이어 목록

        whiteCenter_means = {}
        blueBorder_means = {}
        playerMove_means = {}

        # 플레이어 하나씩 진행
        for player in players:
            curpos = np.array(positions[player])  # 해당 플레이어의 위치 정보를 가져옴

            # 자기장(흰 원)이 존재하지 않는 데이터를 제외
            white_count = 0
            while len(circles['white']) < len(curpos): curpos = curpos[:-1]
            while circles['white'][white_count][4] == 0:
                white_count += 1
            length = len(curpos)
            landing = np.where(curpos[:, 3] < 30000)[0][
                0]  # z좌표(높이)를 확인해서 비행기에서 내린 이후 특정 높이 이하로 내려온 처음 값을 지정(플에이어 마다 다름)
            # 비행기에서 내린 시점과 자기장 정보가 등록된 정보의 길이를 비교하여 시작점을 지정 -> 일반적으로 자기장이 더욱 짧음 하지만 예외는 존재
            start = landing if landing > white_count else white_count

            # 사람 위치 정보 최대 길이에 맞춰 자기장 정보 가져오기 ( 사실상 흰 자기장의 끝 길이에 맞춤, curpos는 white에 맞춰짐)
            curpos = curpos[start:]  # 설정된 start 값 이전 값은 제외
            whites = np.array(circles['white'])[start:length]
            blues = np.array(circles['blue'])[start:length]

            # 사람 위치 정보를 white, blue 존에서 부터 거리의 차를 x,y축으로 나눠 저장
            white_xDiff = (whites[:, 1] - curpos[:, 1])  # 하얀 자기장 x 좌료 이전값과의 차
            white_yDiff = (whites[:, 2] - curpos[:, 2])  # 하얀 자기장 y 좌표 이전값과의 차
            blue_xDiff = (blues[:, 1] - curpos[:, 1])  # 파란 자기장 x 좌표 이전값과의 차
            blue_yDiff = (blues[:, 2] - curpos[:, 2])  # 파란 자기장 y 좌표 이전값과의 차
            map_id = telemetry.map_id()  # 해당 매치의 맵 이름을 반환
            mapx, mapy = map_dimensions[map_id]
            phases = np.where(whites[1:, 4] - whites[:-1, 4] < 0)[0] + 1  # 자기장 페이즈 구분
            phases = np.append(phases, len(whites))  # 게임 종료 index 추가
            white_means = []
            blue_means = []
            moves = []
            pre = 0  # 이전 자기장을 저장할 변수
            for phase in phases:  # 자기장 별 데이터 분리
                cur_white_xDiff = white_xDiff[pre:phase]  # 현 자기장 페이즈의  x 차
                cur_white_yDiff = white_yDiff[pre:phase]  # 현 자기장 페이즈의  y 차
                cur_blue_xDiff = blue_xDiff[pre:phase]
                cur_blue_yDiff = blue_yDiff[pre:phase]

                # white, blue zone로 부터의 거기를 계산
                whiteCenter_diff = np.sqrt(np.square(cur_white_xDiff) + np.square(cur_white_yDiff)) / whites[pre:phase,
                                                                                                      4]
                blueBorder_diff = (blues[pre:phase, 4] - np.sqrt(
                    np.square(cur_blue_xDiff) + np.square(cur_blue_yDiff))) / blues[pre:phase, 4]
                white_means.append(whiteCenter_diff.mean())
                blue_means.append(blueBorder_diff.mean())
                # 길이가 1일때 NaN값 오류 발생 (길이가 1인 0값으로 나누어 주게 된다.)
                if len(whiteCenter_diff) == 1:
                    moves.append(0)
                else:
                    moves.append((whiteCenter_diff[1:] - whiteCenter_diff[:-1]).mean())

                pre = phase

            # 자기장 페이즈 별로 저장된 정보를
            whiteCenter_means[player] = white_means
            blueBorder_means[player] = blue_means
            playerMove_means[player] = moves

        whiteCenter_df = pd.concat(
            [whiteCenter_df, pd.DataFrame.from_dict(whiteCenter_means, orient='index').T.mean(axis=1)],
            axis=1, sort=False)
        blueBorder_df = pd.concat(
            [blueBorder_df, pd.DataFrame.from_dict(blueBorder_means, orient='index').T.mean(axis=1)],
            axis=1, sort=False)
        playerMove_df = pd.concat(
            [playerMove_df, pd.DataFrame.from_dict(playerMove_means, orient='index').T.mean(axis=1)],
            axis=1, sort=False)

        # 게임 시작 시간
        startTime = pd.to_timedelta(telemetry.started()[telemetry.started().find('T') + 1:-1])
        endTime = telemetry.events[-1].timestamp  # 마지막 이벤트 시간
        endTime = (pd.to_timedelta(endTime[endTime.find('T') + 1:-1]) - startTime).total_seconds()
        circles = telemetry.circle_positions()
        whites = np.array(circles['white'])
        phases = np.where(whites[1:, 4] - whites[:-1, 4] != 0)[0] + 1
        phaseTimes = whites[phases, 0]
        phaseTimes = np.append(phaseTimes, endTime)

        attackLog = telemetry.filter_by('log_player_attack')  # 교전 (공격한 경우) 데이터
        attackData = [(log['attacker']['name'],
                       (pd.to_timedelta(log.timestamp[log.timestamp.find('T') + 1:-1]) - startTime).total_seconds())
                      for log in attackLog if
                      pd.to_timedelta(log.timestamp[log.timestamp.find('T') + 1:-1]) > startTime]
        attackData = pd.DataFrame(attackData, columns=['name', 'time'])
        attackData['teamName'] = attackData['name'].str.extract(r'([0-9A-Za-z]+)\_')  # 팀명 추출
        attackData['phase'] = np.nan
        for i in range(len(phaseTimes) - 1):
            attackData.loc[
                (attackData['time'] < phaseTimes[i + 1]) & (attackData['time'] > phaseTimes[i]), 'phase'] = i + 1
        attack_df = pd.concat([attack_df, attackData], axis=0)
        print(attack_df)
        for team in attackData['teamName'].unique():
            try:
                teamCount[team] += 1
            except KeyError:
                teamCount[team] = 1

        vehicles = telemetry.filter_by('log_vehicle_ride')  # 차량 탑승 데이터
        firstVehicle = {}
        used_teamId = []

        # 팀에서 첫 차량 탑승 경우만 구하기
        for vehicle in vehicles:
            if vehicle['vehicle']['vehicle_type'] != 'WheeledVehicle' or \
                    vehicle['character']['name'] in firstVehicle.keys() or \
                    vehicle['character']['name'][:vehicle['character']['name'].find('_')] in used_teamId: continue
            firstVehicle[vehicle['character']['name'][:vehicle['character']['name'].find('_')]] = \
                ((pd.to_timedelta(vehicle.timestamp[vehicle.timestamp.find('T') + 1:-1]) - startTime).total_seconds(), \
                 vehicle['character']['location']['x'], mapy - vehicle['character']['location']['y'])
            used_teamId.append(vehicle['character']['name'][:vehicle['character']['name'].find('_')])
        firstVehicle_df = pd.concat([firstVehicle_df, pd.DataFrame(firstVehicle)], axis=1, sort=False)

        print(leng, "개 데이터 중,", cnt + 1, "번 째 데이터 진행 중.....")

    firstVehicle_df = firstVehicle_df.T
    firstVehicle_df.columns = ['time', 'x', 'y']
    firstVehicle_df['teamName'] = firstVehicle_df.index
    firstVehicle_team = pd.concat([firstVehicle_df[['teamName', 'time']].groupby('teamName').mean(),
                                   firstVehicle_df[['teamName', 'time']].groupby('teamName').count()], axis=1,
                                  sort=False)
    firstVehicle_team.columns = ['time', 'count']
    firstVehicle_team = firstVehicle_team[firstVehicle_team['count'] > 10]
    print(teamCount)
    teamCount = pd.DataFrame(pd.Series(teamCount))
    teamCount.columns = ['name']
    teamCount.index.name = 'teamName'

    teamAttack_df = attack_df[['teamName', 'phase', 'name']].groupby(['teamName', 'phase']).count()
    teamAttack_df['countMean'] = (teamAttack_df / teamCount).round()
    teamAttack_df = teamAttack_df.drop('name', axis=1)
    teamAttack_df['phasePercent'] = (teamAttack_df['countMean'] / teamAttack_df['countMean'].sum(level=0)).round(
        4) * 100

    print(teamAttack_df.sum(level=0))
    print(teamAttack_df)


def moveRoute():
    import pandas as pd
    from chicken_dinner.pubgapi import PUBG
    from chicken_dinner.pubgapi import PUBGCore
    from chicken_dinner.constants import map_dimensions
    import time
    import numpy as np
    import os
    import warnings
    warnings.filterwarnings('ignore')

    # API KEY 설정
    api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2ZGNjNzNhMC0yMDk5LTAxMzctYjNjMi0wMmI4NjZkNzliOGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTUxNjk2NzA2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InB1YmctYmVzdC1wbGF5In0.Oz7GmLsWF7038XIO4vKd5sivhLreOnizxTNcARAEFQs'
    # PUBG 인스턴스 가져오기
    pubg = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)
    pubgCore = PUBGCore(api_key=api_key, shard='pc-tournament', gzip=True)

    pgc_data = pd.read_csv("C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/PGC_MATCH.csv")

    # 남은 데이터 확인
    leng = len(pgc_data)


    for cnt, mat in enumerate(pgc_data['match_id']):
        # 이미 저장된 데이터는 생략
        if os.path.isfile(
                "C:/Users/HC/PycharmProjects/pubgProject/MatchList/datas/pgc/Anal/" + mat + ".csv") or cnt == 1:
            print(leng, "개 데이터 중,", cnt + 1, "번째 데이터 SKIP")
            break
        current_match = pubg.match(mat)  # 매치 기록 하나를 가져옴
        telemetry = current_match.get_telemetry()  # 현재 매치의 Telemetry값을 가져옴
        positions = telemetry.player_positions()  # 각플레이어의 위치값을 가져온다.
        circles = telemetry.circle_positions()  # 자기장(원)에 대한 위치 정보를 가져온다. (white, blue, red)
        map_id = telemetry.map_id()  # 해당 매치의 맵 이름을 반환
        mapx, mapy = map_dimensions[map_id]
        whites = np.array(circles['white'])
        whites[:,2] = mapy - whites[:,2]
        phases = np.where(whites[1:,4] - whites[:-1,4] != 0)[0] + 1

        fig = plt.Figure(figsize=(12,8))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')      # 축 삭제

        img_path = ""




if __name__ == "__main__":
    pro_anal()
