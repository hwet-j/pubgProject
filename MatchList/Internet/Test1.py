def kill(platform,match_id,erangel,miramar,taego):
    try:
        pubg = PUBG(api_key=api_key, shard=f"{platform}")
        match = pubg.match(f"{match_id}")
        telemetry = match.get_telemetry()
        if "Erangel" in telemetry.map_name():
            kill_events = telemetry.filter_by("log_player_kill_v2")
            for kill in kill_events:
                try:
                    info = kill['killer_damage_info']
                    kill_dict = {'zone': kill['killer']['zone'][0],
                    'additional_info': info['additional_info'],
                    'damage_causer_name': info['damage_causer_name'],
                    'damage_reason': info['damage_reason'],
                    'damage_type_category': info['damage_type_category'],
                    'distance': info['distance'],
                    'is_through_penetrable_wall': info['is_through_penetrable_wall']
                    }
                    erangel.append(kill_dict)
                except:
                    pass
        elif "Miramar" in telemetry.map_name():
            kill_events = telemetry.filter_by("log_player_kill_v2")
            for kill in kill_events:
                try:
                    info = kill['killer_damage_info']
                    kill_dict = {'zone': kill['killer']['zone'][0],
                    'additional_info': info['additional_info'],
                    'damage_causer_name': info['damage_causer_name'],
                    'damage_reason': info['damage_reason'],
                    'damage_type_category': info['damage_type_category'],
                    'distance': info['distance'],
                    'is_through_penetrable_wall': info['is_through_penetrable_wall']
                    }
                    miramar.append(kill_dict)
                except:
                    pass
        elif "Tiger" in telemetry.map_name():
            kill_events = telemetry.filter_by("log_player_kill_v2")
            for kill in kill_events:
                try:
                    info = kill['killer_damage_info']
                    kill_dict = {'zone': kill['killer']['zone'][0],
                    'additional_info': info['additional_info'],
                    'damage_causer_name': info['damage_causer_name'],
                    'damage_reason': info['damage_reason'],
                    'damage_type_category': info['damage_type_category'],
                    'distance': info['distance'],
                    'is_through_penetrable_wall': info['is_through_penetrable_wall']
                    }
                    taego.append(kill_dict)
                except:
                    pass
        else:
            print(telemetry.map_name())
            pass
    except:
        time.sleep(1)
        pass
