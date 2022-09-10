import discord
import sys
import os
from discord.ext import commands

@bot.event
async def on_ready():
  print(f"I am alive:)")

@bot.command()
async def restart(ctx):
    if not owner(ctx):
        return
    else:
        await ctx.message.delete()
        await ctx.send(f"Restarting...", delete_after=1.5)
        await asyncio.sleep(2)
        restart_bot()
        
bot.run('input token')
