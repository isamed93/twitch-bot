# Summary
Basic twitch bot that will announce its presence in chat and performs a few simple commands

# Set up
Set up a virtual environment with the following:
 - python version 3.6
 - pip
 - twitchio

This virtual environment needs the following environment variables:
 - TMI_TOKEN=oauth:<[auth_key](https://twitchapps.com/tmi/)>
 - CLIENT_ID=<[client_id](https://dev.twitch.tv/console/apps/create)>
 - BOT_NICK=<bot_name>
 - BOT_PREFIX=! (or whatever other prefix you want)
 - CHANNEL=#<channel_name>

# Commands
## General
 - discord
 - engineer
 - discordmute
 - sens
## Mod
 - multitwitch
 - multitwitch_off
## User-related
 - lurk
 - bonk
## Guild Wars 2
 - info
 - pve
 - pvp
 - wvw
 - training

# Notes
This bot was developed by following this [tutorial](https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8)

TwitchIO library can be found [here](https://twitchio.readthedocs.io/en/rewrite/twitchio.html#)