import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Streaming(name='𝘼𝙥𝙥 𝘧𝘰𝘳 𝘾𝙯/𝙎𝙠 𝘓𝘦𝘢𝘨𝘶𝘦 𝘊𝘰𝘮𝘮𝘶𝘯𝘪𝘵𝘺.', url='https://www.youtube.com/watch?v=nIuxVW6ugdk'))

bot.run('YOUR_BOT_TOKEN')
