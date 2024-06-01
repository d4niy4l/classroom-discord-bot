import requests
import discord
import pyshorteners
from discord.ext import commands

SERVER_URL= "http://localhost:500"

BOT_TOKEN = 'MTIwMDQ5NTA0Nzc5NjMzODcyOA.GZmtXn.whvavG7tDsCIrOP5hDKdGiUmjvcw7g0TqJ46TM'

bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

channel_id = 1200498828466458674

@bot.event
async def on_ready():
    channel = bot.get_channel(channel_id)
    await channel.send('im online')

@bot.command()
async def hello(context):
    await context.send('fuck me')

@bot.command()
async def authorize(context):
    short_url = 'ITS NOT WORKING'
    try:
        auth_url_response = requests.get(f"{ SERVER_URL }/authorize")
        if auth_url_response.status_code == 200:
            authorization_url = auth_url_response.text
            s = pyshorteners.Shortener()
            print(authorization_url)
            short_url = s.tinyurl.short(authorization_url)
            await context.send(f"Click the link to authorize the application: {short_url}")
        else:
            await context.send("Error retrieving authorization URL")
    except Exception as e:
        print('An error occurred:')
    

bot.run(BOT_TOKEN)














# If modifying these scopes, delete the file token.json.
