# Add predefined users here
def get_user_id(user):
    match user:
        case 'user1':
            return 'user1_steam_id'
        case 'user2':
            return 'user2_steam_id'
        case 'user3':
            return 'user3_steam_id'
        case 'user4':
            return 'user4_steam_id'
        case 'user5':
            return 'user5_steam_id'
        case other:
            if len(user) == 17:
                return user
            return 'unknown'
        
def create_matches_table(matches_info, user):
    text = f"```yaml\nUser {user} matches:\n\nDate                Map           Score    K    D    A    HS%    ADR \n-------------------------------------------------------------------- \n"

    for match in matches_info:
        text += f"{match['date']}{match['map']}{match['score']}{match['kills']}{match['deaths']}{match['assists']}{match['hsp']}{match['adr']} \n"
    
    text += "```"
    return text

def create_maps_table(maps_info, user):
    text = f"```yaml\nUser {user} most played maps\n\nMap            WR%     Times played \n----------------------------------- \n"

    for map in maps_info:
        text += f"{map['name']}{map['wrp']}{map['times_played']} \n"
    
    text += "```"
    return text

def create_weapons_table(weapons_info, user):
    text = f"```yaml\nUser {user} most played weapons\n\nWeapon            Kills     HS     HS%    Shots    DMG      Accuracy \n-------------------------------------------------------------------- \n"

    for weapon in weapons_info:
        text += f"{weapon['name']}{weapon['kills']}{weapon['hs']}{weapon['hsp']}{weapon['shots']}{weapon['dmg']}{weapon['accuracy']} \n"
    
    text += "```"
    return text
        
def format_matches_info(matches_info):
    formatted_info = matches_info
    
    for match in formatted_info:
        date_len = len(match["date"])
        map_len = len(match["map"])
        score_len = len(match["score"])
        kills_len = len(match["kills"])
        deaths_len = len(match["deaths"])
        assists_len = len(match["assists"])
        hsp_len = len(match["hsp"])
        
        match["date"] += ((20 - date_len) * " ")
        match["map"] += ((14 - map_len) * " ")
        match["score"] += ((9 - score_len) * " ")
        match["kills"] += ((5 - kills_len) * " ")
        match["deaths"] += ((5 - deaths_len) * " ")
        match["assists"] += ((5 - assists_len) * " ")
        match["hsp"] += ((7 - hsp_len) * " ")
        
    return formatted_info

def format_maps_info(maps_info):
    formatted_info = maps_info
    
    for map in formatted_info:
        name_len = len(map["name"])
        wrp_len = len(map["wrp"])
        
        map["name"] += ((15 - name_len) * " ")
        map["wrp"] += ((8 - wrp_len) * " ")
        
    return formatted_info

def format_weapons_info(weapons_info):
    formatted_info = weapons_info
    
    for weapon in formatted_info:
        name_len = len(weapon["name"])
        kills_len = len(weapon["kills"])
        hs_len = len(weapon["hs"])
        hsp_len = len(weapon["hsp"])
        shots_len = len(weapon["shots"])
        dmg_len = len(weapon["dmg"])
        
        weapon["name"] += ((18 - name_len) * " ")
        weapon["kills"] += ((10 - kills_len) * " ")
        weapon["hs"] += ((7 - hs_len) * " ")
        weapon["hsp"] += ((7 - hsp_len) * " ")
        weapon["shots"] += ((9 - shots_len) * " ")
        weapon["dmg"] += ((9 - dmg_len) * " ")
        
    return formatted_info