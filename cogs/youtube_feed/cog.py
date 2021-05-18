import config
import discord
from discord.ext import commands
from discord.ext.tasks import loop

from .youtube_feed import YouTubeFeed

CHECK_INTERVAL = 60  # number of seconds before checking again


class YouTubeFeedCog(commands.Cog, name="YouTube Feed"):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot
        self.__feed = YouTubeFeed(config.YT_CHANNEL_ID)

    @commands.Cog.listener()
    async def on_ready(self):
        """When discord is connected"""
        # get channel object
        self.__channel: discord.TextChannel = self.__bot.get_channel(
            config.YOUTUBE_VIDEOS_CHANNEL_ID
        )
        # check that channel exists
        assert isinstance(self.__channel, discord.TextChannel)
        # start YouTube feed
        self.feed_loop.start()
        print("Starting YouTube feed...")

    @loop(seconds=CHECK_INTERVAL)
    async def feed_loop(self):
        """Loop to check YouTube and post new videos"""
        # check for new video
        if not self.__feed.has_new_video():
            return
        video = self.__feed.get_most_recent_video()
        await self.__channel.send(
            f"@everyone **{video.author}** just posted a video! Go check it out!\n{video.link}"
        )


def setup(bot: commands.Bot):
    bot.add_cog(YouTubeFeedCog(bot))
