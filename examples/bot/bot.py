from discord import VoiceChannel
from discord.ext import commands
from dcactivity import DCActivity, DCApplication

bot = commands.Bot(command_prefix='!')
dcactivity = DCActivity(bot) # or `bot.dcactivity = DCActivity(bot)` to use it as a BotVar

@bot.command()
async def youtube(ctx, channel: VoiceChannel):
    invite = await dcactivity.create_invite(channel, DCApplication.youtube)
    await ctx.send(invite)

bot.run('token')