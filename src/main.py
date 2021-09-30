import asyncio
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

import config
import utils

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	print('Logged in as {0.user}'.format(bot))
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!start"))

@bot.command()
async def start(ctx):
	"""Shows the instructions. Try it!"""
	
	msg = await ctx.channel.send(file=discord.File('hacker.png'))
	emojs = ['🧠', '👀', '🏆', '🥺', '🤟', '🎓']
	for zzz in emojs:
		await msg.add_reaction(zzz)
	await ctx.channel.send(utils.show_instructions())

if __name__ == '__main__':
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            extension = file[:-3]
            try:
                bot.load_extension(f'cogs.{extension}')
                print(config.MSG_COG_LOAD_SUCCESS.format(extension))
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(config.MSG_COG_LOAD_ERROR.format(extension, exception))

load_dotenv()
bot.run(os.environ['TOKEN'])