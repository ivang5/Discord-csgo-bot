from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_matches_info(user_id, count):
    WINDOW_SIZE = "1920,1080"
    
    options = Options()
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"https://csgostats.gg/player/{user_id}#/matches")
    
    match_row = "/html/body/div[@id='outer-wrapper']/div[@id='content-wrapper']/div[@class='main-container']/div[@id='player-outer-section']/div[@class='content-sub-nav-outer']/div[@class='main-content']/div[2]/div[@class='content-tabs']/div[@id='player-matches']/div[@id='match-list-outer']/table[@class='table table-striped']/tbody/tr[@class='p-row js-link ']"
    matches = driver.find_elements("xpath", match_row)
    matches_quantity = count + 1 if count <= 10 and len(matches) >= count else len(matches) + 1
    matches_info = []
    
    for i in range (1, matches_quantity):
        date = driver.find_element("xpath", f"{match_row}[{i}]/td[1]").text
        map_name = driver.find_element("xpath", f"{match_row}[{i}]/td[3]").text
        match_score = driver.find_element("xpath", f"{match_row}[{i}]/td[4]/span").text
        kill_score = driver.find_element("xpath", f"{match_row}[{i}]/td[7]").text
        death_score = driver.find_element("xpath", f"{match_row}[{i}]/td[8]").text
        assist_score = driver.find_element("xpath", f"{match_row}[{i}]/td[9]").text
        hs_score = driver.find_element("xpath", f"{match_row}[{i}]/td[11]").text
        adr_score = driver.find_element("xpath", f"{match_row}[{i}]/td[12]").text
        
        match_info = {
            "date": date,
            "map": map_name,
            "score": match_score,
            "kills": kill_score,
            "deaths": death_score,
            "assists": assist_score,
            "hsp": hs_score,
            "adr": adr_score,
        }
        
        matches_info.append(match_info)
    return matches_info

def get_maps_info(user_id, count):
    WINDOW_SIZE = "1920,1080"
    
    options = Options()
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"https://csgostats.gg/player/{user_id}#/maps")
    
    map_row = "/html/body/div[@id='outer-wrapper']/div[@id='content-wrapper']/div[@class='main-container']/div[@id='player-outer-section']/div[@class='content-sub-nav-outer']/div[@class='main-content']/div[2]/div[@class='content-tabs']/div[@id='player-maps']/div/div"
    maps = driver.find_elements("xpath", map_row)
    maps_quantity = count + 2 if count <= 10 and len(maps) - 1 >= count else len(maps) + 1
    maps_info = []
    
    for i in range (2, maps_quantity):
        name = driver.find_element("xpath", f"{map_row}[{i}]/div/div[1]/div/span").text
        wr = driver.find_element("xpath", f"{map_row}[{i}]//div/div[2]/div/div/div[@class='stat-large stat']/span").text
        times_played = driver.find_element("xpath", f"{map_row}[{i}]/div/div[3]/div").text
        
        map_info = {
            "name": name,
            "wrp": wr,
            "times_played": times_played,
        }
        
        maps_info.append(map_info)
    return maps_info
    
def get_weapons_info(user_id, count):
    WINDOW_SIZE = "1920,1080"
    
    options = Options()
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"https://csgostats.gg/player/{user_id}#/weapons")
    
    weapon_row = "/html/body/div[@id='outer-wrapper']/div[@id='content-wrapper']/div[@class='main-container']/div[@id='player-outer-section']/div[@class='content-sub-nav-outer']/div[@class='main-content']/div[2]/div[@class='content-tabs']/div[@id='player-weapons']/div/table[@class='table table-striped']/tbody/tr[@class='p-row']"
    weapons = driver.find_elements("xpath", weapon_row)
    weapons_quantity = count + 1 if count <= 10 and len(weapons) >= count else len(weapons) + 1
    weapons_info = []
    
    for i in range (1, weapons_quantity):
        name = driver.find_element("xpath", f"{weapon_row}[{i}]/td[2]").text
        kills = driver.find_element("xpath", f"{weapon_row}[{i}]/td[3]").text
        hs = driver.find_element("xpath", f"{weapon_row}[{i}]/td[4]").text
        hsp = driver.find_element("xpath", f"{weapon_row}[{i}]/td[5]/div/div[1]").text
        shots = driver.find_element("xpath", f"{weapon_row}[{i}]/td[6]").text
        dmg = driver.find_element("xpath", f"{weapon_row}[{i}]/td[7]").text
        accuracy = driver.find_element("xpath", f"{weapon_row}[{i}]/td[8]/div/div[1]").text
        
        weapon_info = {
            "name": name,
            "kills": kills,
            "hs": hs,
            "hsp": hsp,
            "shots": shots,
            "dmg": dmg,
            "accuracy": accuracy,
        }
        
        weapons_info.append(weapon_info)
    return weapons_info
