# discord-bot

## Description:
It is a discord bot that creates a SQLite database. 

The database keeps track of people when they send a message, and it scans the message for the words used. With this, we have a leaderboard of most active individuals and most used words.

I made it because my friends have a message considered an inside joke, so initally it would just keep track of how many times that word was used. I extended it to this because it seemed like an interesting challenge, and I've always wondered who are most active on what servers.

## Requirements:
`discord-bot` requires Python >= 3.6.9 (others are untested).

You also have to install discord.py and SQLite
```
sudo apt-get install sqlite3 libsqlite3-dev
python3 -m pip install -U discord.py
```

## Installation:
Download the files and run

```
python3 stat-bot.py
```
