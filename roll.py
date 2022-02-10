from discord.ext import commands
import random

class roll(commands.Cog, ):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="2")
  async def _2(self, ctx):
    await ctx.reply(random.randint(1,2))
  @commands.command(name="4")
  async def _4(self, ctx):
    await ctx.reply(random.randint(1,4))
  @commands.command(name="6")
  async def _6(self, ctx):
    await ctx.reply(random.randint(1,6))
  @commands.command(name="8")
  async def _8(self, ctx):
    await ctx.reply(random.randint(1,8))
  @commands.command(name="10")
  async def _10(self, ctx):
    await ctx.reply(random.randint(1,10))
  @commands.command(name="12")
  async def _12(self, ctx):
    await ctx.reply(random.randint(1,12))
  @commands.command(name="20")
  async def _20(self, ctx):
    await ctx.reply(random.randint(1,20))
  @commands.command(name="100")
  async def _100(self, ctx):
    await ctx.reply(random.randint(1,100))

def setup(bot):
  bot.add_cog(roll(bot))