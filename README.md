# Discord CS:GO Bot

Discord bot for CS:GO players info (such as match history, most played maps, etc.). Application is scraping the data from [csgostats](https://csgostats.gg/) website.

## Installation:

- Execute `pip install -r requirements.txt`
- Change the `TOKEN` variable inside `run_discord_bot()` function in `bot.py` file to be your bot's token.
- If you want to add user aliases, edit the `get_user_id()` function in `utils.py` file.

## Usage:

- Run `main.py` file.
- Invite your Discord bot to your server.
- Your bot is ready now, send a command and wait for a response. Available commands:
  - !commands - basic info about available commands
  - !matches {user_alias/steam_id} {quantity} - info about the user's recent matches (quantity is optional)
  - !topmaps {user_alias/steam_id} {quantity} - info about the user's most played maps (quantity is optional)
  - !topweapons {user_alias/steam_id} {quantity} - info about the user's most played weapons (quantity is optional)
