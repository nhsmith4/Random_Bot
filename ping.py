import os
import discord
import random
import time
from discord.ext import bot
from discord.utils import find
from keep_alive import keep_alive

class ping(bot.Cog):
  @bot.command()
  async def ping(ctx, member: discord.Member, ping_message):
    global m
    m = member
    global a
    a = True
    full_message = member.mention + " " + ping_message
    while a == True:
      await ctx.channel.send(full_message)
      @bot.event
      async def on_message(message):
        global m
        global a
        if message.author == m:
          a = False
        if message.author.id == 638412875370725392 and ".override" in message.content:
          a = False
    time.sleep(10)

def setup(bot):
  bot.add_cog(ping(bot))