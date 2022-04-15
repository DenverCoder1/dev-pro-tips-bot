import config
import nextcord
from nextcord.ext import commands
from nextcord.ext.tasks import loop

from .youtube_feed import YouTubeFeed

CHECK_INTERVAL = 60  # number of seconds before checking again


class YouTubeFeedCog(commands.Cog, name="YouTube Feed"):
    def __init__(self, bot: commands.Bot):
        self.__bot = bot
        self.__feed = YouTubeFeed(config.YT_CHANNEL_ID)
        self.__started = False

    @commands.Cog.listener()
    async def on_ready(self):
        """When discord is connected"""
        if self.__started:
            return
        # get channel object
        self.__channel: nextcord.TextChannel = self.__bot.get_channel(
            config.YOUTUBE_VIDEOS_CHANNEL_ID
        )
        assert isinstance(self.__channel, nextcord.TextChannel)
        # get role
        self.__youtube_ping_role: nextcord.Role = self.__channel.guild.get_role(
            config.YOUTUBE_PING_ROLE_ID
        )
        assert isinstance(self.__youtube_ping_role, nextcord.Role)
        # check that channel exists
        assert isinstance(self.__channel, nextcord.TextChannel)
        # start YouTube feed
        self.feed_loop.start()
        # set flag
        self.__started = True
        print("YouTube feed started")

    @loop(seconds=CHECK_INTERVAL)
    async def feed_loop(self):
        """Loop to check YouTube and post new videos"""
        # check for new video
        if not self.__feed.has_new_video():
            return
        video = self.__feed.get_most_recent_video()
        await self.__channel.send(
            f"{self.__youtube_ping_role.mention} **{video.author}** just posted a video! Go check it out!\n{video.link}"
        )


def setup(bot: commands.Bot):
    bot.add_cog(YouTubeFeedCog(bot))
