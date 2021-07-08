# DCActivity
An unofficial module used to access Discord's Beta features like YouTube, Poker Night, etc. by your Bot

<br>

# Installation
- **Python 3.8 or higher is required**
- **[discord.py](https://github.com/Rapptz/discord.py) V1.5.0 or higher is required**

To install the library, simply run the following command in your terminal:
```
# Windows
py -m pip install dcactivity

# Linux/macOS
python3 -m pip install dcactivity
```

<br>

# Usage
To use the library, you must first import it into your script and create a new instance of the DCActivity class:
```python
from discord.ext import commands
from dcactivity import DCActivity

bot = commands.Bot(command_prefix='!')
bot.dcact = DCActivity(bot)
```

To create the invite link, you need to use create_link() function:
```py

link = await bot.dcact.create_link(voice_channel, app_id)
```

* voice_channel: The Voice channel you want to create the invite link for. Can be Channel ID or discord.VoiceChannel object
 
* app_id: The Application ID of the Voice Channel game. For this, you need to follow either of the three steps:
   
  * Import DCApplication from dcactivity:
    ```python
    from dcactivity import DCApplication

    link = await bot.dcact.create_link(voice_channel, DCApplication.youtube) # or DCApplication.poker, etc.
    ```

  * Directly use Application Name or ID (use ID only if you know the exact ID of an activity):
    ```python
    link = await bot.dcact.create_link(voice_channel, 'youtube') # or poker, chess, etc.
    ```


# Examples
## Bot:
```python
# bot.py

from discord import VoiceChannel
from discord.ext import commands
from dcactivity import DCActivity, DCApplication

bot = commands.Bot(command_prefix='!')
dcactivity = DCActivity(bot) # or "bot.dcactivity = DCActivity(bot)" to use it as a BotVar

@bot.command()
async def youtube(ctx, channel: VoiceChannel):
    link = await dcactivity.create_link(channel, DCApplication.youtube)
    await ctx.send(link)

bot.run('token')
```

<br>

## Bot with Cogs:
  - bot:
      ```python
      # bot.py

      from discord import VoiceChannel
      from discord.ext import commands
      from dcactivity import DCActivity

      bot = commands.Bot(command_prefix='!')
      bot.dcactivity = DCActivity(bot)

      bot.load_extension('cogs.cog') # Simple Example with Cog
      bot.load_extension('cogs.cog_advanced') # Advanced Example with Cog

      bot.run('token')
      ```

  - cog (simple):
      ```python
      # cog.py

      from discord import VoiceChannel
      from discord.ext import commands
      from dcactivity import DCApplication


      class MyCog(commands.Cog):
          def __init__(self, bot):
              self.bot = bot
          
          @commands.command()
          async def youtube(self, ctx, channel: VoiceChannel):
              link = await self.bot.dcactivity.create_link(channel, DCApplication.youtube)
              await ctx.send(link)

      def setup(bot):
          bot.add_cog(MyCog(bot))
      ```

  - cog (advanced):
      ```python
      # cog_advanced.py
      
      from typing import Optional
      from discord import VoiceChannel
      from discord.ext import commands
      from dcactivity import DCApplication
      from dcactivity.errors import InvalidChannel


      class MyAdvancedCog(commands.Cog):
          def __init__(self, bot):
              self.bot = bot

          @commands.command()
          async def custom_link(self, ctx, channel=None):
              if not channel:
                  if not ctx.author.voice:
                      return await ctx.send('You need to connect to a voice channel first')
                  if not isinstance(ctx.author.voice.channel, VoiceChannel):
                      return await ctx.send('This feature is not supported in Stage Channels.')
                  _channel = ctx.author.voice.channel
              else:
                  _channel = channel
              
              link = await self.bot.dcactivity.create_link(
                  ctx.author.voice.channel, DCApplication.youtube, max_age=0, max_uses=10)
              await ctx.send(link)

          @custom_link.error
          async def custom_link_error(self, ctx, exc):
              exc = getattr(exc, 'original', exc)
              if isinstance(exc, InvalidChannel):
                  await ctx.send('Invalid Channel given as argument.')

      def setup(bot):
          bot.add_cog(MyAdvancedCog(bot))
      ```

<br>

# Note
* A minimum of one person needs to click on the invite link to start the Voice Channel Activity.
* Activity resets when everyone exits. Though it can again be joined from the same link but from the starting and not resuming.
* Games like chess/betrayal may not work in Stable Client for now. To use them, you need install [Discord PTB](https://ptb.discord.com/) or [Discord Canary](https://canary.discord.com/) Client or use them in the web browser.

<br>

# Info
This package is licensed under MIT License. Any contributions are welcomed.

Need to contribute? Just Open a Pull Request with your changes and some information about your changes.

Found a bug or having an issue? Open an Issue at [Github](https://github.com/AkshuAgarwal/DCActivity/issues)!

<br>

# Links
Github: https://github.com/AkshuAgarwal/DCActivity