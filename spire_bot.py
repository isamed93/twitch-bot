import os
from twitchio.ext import commands

# Set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

## Global parameters
multitwitch_base = 'www.multitwitch.tv'
multitwitch_link = ''
multitwitch_on = False


@bot.event
async def event_ready():
    '''Called once when the bot goes online'''
    # Print log to console
    print(f"{os.environ['BOT_NICK']} is online")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    '''Runs every time a message is sent in chat'''
    # Make sure the bot ignores itself
    if ctx.author.name.lower()==os.environ['BOT_NICK'].lower():
        return
    # Handle the commands of the message
    await bot.handle_commands(ctx)

#----------------------------------------
#   Commands
#----------------------------------------
## General
@bot.command(name='discord')
async def comm_discord(ctx):
    await ctx.send_me('Discord link: https://discord.gg/EksFrcd')


@bot.command(name='engineer')
async def comm_engineer(ctx):
    await ctx.send_me('Spire graduated from Industrial Electronics and Automation Engineering (think robots) and she works as a Digital Signal Processing Engineer. Feel free to ask her about it!')


@bot.command(name='discordmute')
async def comm_discordmute(ctx):
    await ctx.send_me('Discord is muted sometimes because not everyone is comfortable with having their voice on stream.')


@bot.command(name='sens')
async def comm_sens(ctx):
    await ctx.send_me('DPI: 1500 | Ingame: 5 | Scoped: 40')


## Mod
@bot.command(name='multitwitch')
async def comm_multitwitch(ctx):
    global multitwitch_base
    global multitwitch_link
    global multitwitch_on
    # If the command is run by a mod
    if (ctx.author.is_mod):
        # If command is run with arguments, set up multitwitch
        if(bool(ctx.content.replace("!multitwitch","").strip())):
            multitwitch_link = multitwitch_base + ctx.content
            multitwitch_link = multitwitch_link.replace('!multitwitch', '')
            multitwitch_link = multitwitch_link.replace(' ', '/')
            multitwitch_on = True
            print(f"{ctx.author.name} has set the multitwitch to {multitwitch_link}")
        if(multitwitch_on):
            await ctx.send_me("Watch multiple PoVs at {}".format(multitwitch_link))
    # If the command is run by anyone else
    else:
        if(multitwitch_on):
            print(f"{ctx.author.name} has disabled multitwitch")
            await ctx.send_me("Watch multiple PoVs at {}".format(multitwitch_link))


@bot.command(name='multitwitchoff')
async def comm_multitwitchoff(ctx):
    global multitwitch_on
    # If the command is run by a mod
    if (ctx.author.is_mod):
        multitwitch_on = False


## User-related
@bot.command(name='lurk')
async def comm_lurk(ctx):
    await ctx.send_me('Thanks for leaving a lurk, {}! See you around :)'.format(ctx.author.name))


@bot.command(name='bonk')
async def comm_bonk(ctx):
    print(f"{ctx.author.name} has timed themselves out")
    await ctx.timeout(ctx.author.name, 10)


## Guild Wars 2
@bot.command(name='info')
async def comm_info(ctx):
    await ctx.send_me('Here\'s a few commands for info on the different gamemodes: !pvp !pve !wvw !training')


@bot.command(name='pve')
async def comm_pve(ctx):
    await ctx.send_me('Raid builds + guides + training: snowcrows.com  --Fractals builds + guides: discretize.eu -- Gear guide: https://wiki.guildwars2.com/wiki/User:Tanetris/So_You_Want_To_Gear_a_Character')


@bot.command(name='pvp')
async def comm_pvp(ctx):
    await ctx.send_me('PvP builds + guides: godsofpvp.net')


@bot.command(name='wvw')
async def comm_wvw(ctx):
    await ctx.send_me('WvW builds: general builds metabattle.com')


@bot.command(name='training')
async def comm_training(ctx):
    await ctx.send_me('Raid training: https://snowcrows.com/raids/training/ Fractals training: https://discord.gg/2ReUP7p')


if __name__ == "__main__":
    bot.run()
