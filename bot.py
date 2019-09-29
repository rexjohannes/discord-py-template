import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("GAME"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.utils.oauth_url(bot.user.id))

    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing Argument!")
        
bot.remove_command('help')

@bot.command()
async def help(ctx):
  await ctx.send("Commands: \nhelp - View this message.")
  
  
bot.run('TOKEN')

        
  


