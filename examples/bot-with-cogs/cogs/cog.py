from discord import VoiceChannel
from discord.ext import commands
from dcactivity import DCApplication


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def youtube(self, ctx, channel: VoiceChannel):
        invite = await self.bot.dcactivity.create_invite(channel, DCApplication.youtube)
        await ctx.send(invite)

def setup(bot):
    bot.add_cog(MyCog(bot))