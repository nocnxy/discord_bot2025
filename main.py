import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intent=discord.Intents.all())

# Token สำหรับรันบอท
TOKEN = 'MTMzOTE1ODc5OTMwNjcxOTM2Mg.GnflG9.-s05SSzNUGdBHhl8-iT9GGnNnaFqRh6OezfajA'

server_on()

bot.run(TOKEN)