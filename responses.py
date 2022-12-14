import utils
import scrape

def handle_response(message) -> str:
    p_message = message.lower()
    
    try:
        message_parts = p_message.split(" ")
        command = message_parts[0]
        user = message_parts[1]
        user_id = utils.get_user_id(user)
        count = 10 if len(message_parts) < 3 else int(message_parts[2])
        
        if command == '!matches':
            matches_info = scrape.get_matches_info(user_id, count)
            mi_formatted = utils.format_matches_info(matches_info)
            table = utils.create_matches_table(mi_formatted, user)
            return table
        
        if command == "!topmaps":
            maps_info = scrape.get_maps_info(user_id, count)
            mi_formatted = utils.format_maps_info(maps_info)
            table = utils.create_maps_table(mi_formatted, user)
            return table
            
        if command == '!topweapons':
            weapons_info = scrape.get_weapons_info(user_id, count)
            wi_formatted = utils.format_weapons_info(weapons_info)
            table = utils.create_weapons_table(wi_formatted, user)
            return table
        
    except IndexError:
        if p_message == '!commands':
            return "```yaml\nCommands list:\n -!matches {user} {quantity}    (max 10) \n -!topmaps {user} {quantity}    (max 10) \n -!topweapons {user} {quantity}    (max 10) \n\nList of predefined users: user1, user2, user3, user4, user5\n\nIf you want to get information about a user who is not predefined, you need to enter the steam id of the user instead of the alias.\n\nIf you want the response to arrive as a private message, add '?' at the beginning of the command```"