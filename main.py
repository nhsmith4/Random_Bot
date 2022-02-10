import os
import discord
import random
import time
from discord.ext import commands
from discord.utils import find
from keep_alive import keep_alive
import help
import math1
import roll

bot = commands.Bot(command_prefix=["."])
bot.remove_command("help")

help = [help]
math1 = [math1]
roll = [roll]

# help
for i in range(len(help)):
  help[i].setup(bot)

# math
for i in range(len(math1)):
  math1[i].setup(bot)

# join message
@bot.event
async def on_guild_join(server):
  general = find(lambda x: x.name == "general", server.text_channels)
  if general and general.permissions_for(server.me).send_messages:
    await general.send("Hello {}!".format(server.name))
    await general.send("I am the Random Bot")
    await general.send("Type .help for a list of commands")

# user info
@bot.command()
async def info(ctx, *, member: discord.Member):
  fmt = "{0} joined on {0.joined_at} and has {1} roles."
  await ctx.send(fmt.format(member, len(member.roles)))
@info.error
async def info_error(ctx, error):
  if isinstance(error, bot.BadArgument):
    await ctx.send("That member is not on this server.")

# roll
for i in range(len(roll)):
  roll[i].setup(bot)

# chicken avocado sandwich
@bot.command()
async def pog(ctx):
  await ctx.reply("""
  **Grilled Chicken with Avocado Sandwich**
  4 servings
  
  **Ingredients**
  3 tablespoons extra virgin olive oil
  1 tablespoon lime juice
  1/2 teaspoon chipotle chili powder (less or more depending on how much heat you want)
  1 pound boneless skinless chicken breasts (about 2 breast halves)
  4 small slices Monterey Jack cheese
  4 sets hamburger buns
  1 avocado, peeled, seeded and slicedIceberg or lettuce of preference
  Mayonnaise
  
  **Method**
  1) Make the marinade:
  In a shallow bowl, stir together the olive oil, lime juice, and chipotle chile powder.
  
  2) Pound chicken breasts to even thickness:
  Place the chicken breasts between two sheets of wax paper. Use a meat pounder to pound the breasts to an even thickness of about 1/2 inch. Cut off excess fat. If you are starting with 2 half-pound chicken breast halves, cut each one in half so that you have 4 pieces (to better fit the buns).
  
  3) Marinate the chicken:
  Place the chicken breasts in the marinade, turning to coat. Cover with plastic wrap. Let marinate for at least 15 minutes, preferably an hour.
  
  4) Grill the chicken breasts and buns:
  Heat your grill on high heat if you are using a gas grill, or prepare coals for direct heat if you are using charcoal. You can also use a cast-iron grill pan on your stove if you do not have a grill.
  Grill the chicken pieces a couple minutes on each side, until cooked through. Once you have cooked the chicken pieces on one side and flipped them, add a slice of cheese to the chicken. Cover the grill for half a minute to melt the cheese.
  Toast the buns on the grill as well.
  
  5) Assemble:
  Assemble the sandwiches - bun bottom, chicken with melted cheese, avocado and lettuce, mayonnaise on the top bun.
  
  **Nutritional Information (per serving)**
  722 calories
  44g fat
  39g carbs
  45g protein
  """)

global a
global m
@bot.command()
async def ping(ctx, member: discord.Member, ping_message = None):
  global m
  m = member
  global a
  a = True
  if ping_message == None:
    full_message = member.mention
  else:
    full_message = member.mention + " " + ping_message
  while a == True:
    @bot.event
    async def on_message(message):
      global m
      global a
      if message.author == m:
        a = False
      if message.author.id == 638412875370725392 and ".override" in message.content:
        print("Ping overridden")
        a = False
      await bot.process_commands(message)
    time.sleep(5)
    await ctx.channel.send(full_message)

@bot.command()
async def override(ctx):
  pass

keep_alive()

print("Random Bot is on!")

discord_TOKEN = os.environ["TOKEN"]
bot.run(discord_TOKEN)