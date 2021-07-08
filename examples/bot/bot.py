from discord import VoiceChannel
from discord.ext import commands
from vcactivity import VCActivity, VCApplication

bot = commands.Bot(command_prefix='!')
vcactivity = VCActivity(bot) # or `bot.vcactivity = VCActivity(bot)` to use it as a BotVar

@bot.command()
async def youtube(ctx, channel: VoiceChannel):
    link = await vcactivity.get_link(channel, VCApplication.youtube)
    await ctx.send(link)

bot.run('token')