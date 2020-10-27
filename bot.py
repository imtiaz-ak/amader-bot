import discord
from discord.ext import commands

SECRET_KEY = config["SECRET_KEY"]

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is ready")

client.run(SECRET_KEY)
