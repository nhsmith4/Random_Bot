import discord
from discord.ext import commands
from discord.errors import Forbidden

async def send_embed(ctx, embed):
  try:
    await ctx.send(embed = embed)
  except Forbidden:
    try:
      await ctx.send("Seems like I can't send embeds. Please check my permissions and try again.")
    except Forbidden:
      await ctx.author.send(f"Seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"f"Please inform the server moderators about this issue.", embed = embed)

class help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def help(self, ctx, *input):

    prefix = "."
    version = "v0.1.1"

    if not input:

      # starting to build embed
      emb = discord.Embed(title = "Commands", color = discord.Color.magenta(), description = f"Use {prefix}help <module> to gain more information about that module\n")

      # iterating trough cogs, gathering descriptions
      cogs_desc = ""
      for cog in self.bot.cogs:
        cogs_desc += f"{cog} - {self.bot.cogs[cog].__doc__}\n"

      # adding "list" of cogs to embed
      emb.add_field(name = "Modules", value = cogs_desc, inline = False)

      # integrating trough uncategorized commands
      commands_desc = ""
      for command in self.bot.walk_commands():
        # if cog not in a cog
        # listing command if cog name is None and command isn"t hidden
        if not command.cog_name and not command.hidden:
          commands_desc += f"{command.name} - {command.help}\n"

      # adding those commands to embed
      if commands_desc:
        emb.add_field(name = "Not belonging to a module", value = commands_desc, inline = False)

      # setting information about author
      emb.add_field(name = "About", value = f"The Random Bot is developed by select_L0L#0421 using discord.py on Replit.")
      emb.set_footer(text = f"Bot is running {version}")

    # block called when one cog-name is given
    # trying to find matching cog and it's commands
    elif len(input) == 1:
      # iterating trough cogs
      for cog in self.bot.cogs:
        # check if cog is the matching one
        if cog.lower() == input[0].lower():
          # making title - getting description from doc-string below class
          emb = discord.Embed(title = f"{cog} - Commands", description = self.bot.cogs[cog].__doc__, color = discord.Color.magenta())
          # getting commands from cog
          for command in self.bot.get_cog(cog).get_commands():
            # if cog is not hidden
            if not command.hidden:
              emb.add_field(name = f"{prefix}{command.name}", value = command.help, inline = False)
          # found cog - breaking loop
          break
      
      # if input not found
      # yes, for-loops have an else statement, it's called when no "break" was issued
      else:
        emb = discord.Embed(title = "What's that?!", description = f"I've never heard from a module called '{input[0]}' before :scream:", color = discord.Color.magenta())

    # too many cogs requested - only one at a time allowed
    elif len(input) > 1:
      emb = discord.Embed(title = "That's too much.", description = "Please request only one module at once :sweat_smile:", color = discord.Color.magenta())

    else:
      emb = discord.Embed(title = "Secret??? :scream:", description = "I don't know how you got here, but very well done", color = discord.Color.magenta())
    
    # sending reply embed using our own function defined above
    await send_embed(ctx, emb)

def setup(bot):
  bot.add_cog(help(bot))