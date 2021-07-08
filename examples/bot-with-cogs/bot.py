from discord import VoiceChannel
from discord.ext import commands
from vcactivity import VCActivity

bot = commands.Bot(command_prefix='!')
bot.vcactivity = VCActivity(bot)

bot.load_extension('cogs.cog') # Simple Example with Cog
bot.load_extension('cogs.cog_advanced') # Advanced Example with Cog

bot.run('token')