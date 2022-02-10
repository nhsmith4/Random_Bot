from discord.ext import commands

class math1(commands.Cog, name = "math"):

  def __init__(self, commands):
    self.commands = commands

  @commands.command()
  async def add(self, ctx, *nums):
    operation = " + ".join(nums)
    await ctx.send(f"{operation} = {eval(operation)}")
  @commands.command()
  async def subtract(self, ctx, *nums):
    operation = " - ".join(nums)
    await ctx.send(f"{operation} = {eval(operation)}")
  @commands.command()
  async def multiply(self, ctx, *nums):
    operation = " * ".join(nums)
    await ctx.send(f"{operation} = {eval(operation)}")
  @commands.command()
  async def divide(self, ctx, *nums):
    try:
      operation = " / ".join(nums)
      await ctx.send(f"{operation} = {eval(operation)}")
    except ZeroDivisionError:
      await ctx.reply("Cannot divide by zero.")

def setup(commands):
  commands.add_cog(math1(commands))