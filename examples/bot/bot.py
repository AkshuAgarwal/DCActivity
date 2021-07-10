from discord import VoiceChannel
from discord.ext import commands
from dcactivity import DCActivity, DCApplication

bot = commands.Bot(command_prefix='!')
dcactivity = DCActivity(bot) # or `bot.dcactivity = DCActivity(bot)` to use it as a BotVar

@bot.command()
async def youtube(ctx, channel: VoiceChannel):
    link = await dcactivity.create_link(channel, DCApplication.youtube)
    await ctx.send(link)

bot.run('token')