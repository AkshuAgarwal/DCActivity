from discord import VoiceChannel
from discord.ext import commands
from dcactivity import DCActivity

bot = commands.Bot(command_prefix='!')
bot.dcactivity = DCActivity(bot)

bot.load_extension('cogs.cog') # Simple Example with Cog
bot.load_extension('cogs.cog_advanced') # Advanced Example with Cog

bot.run('token')