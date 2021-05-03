import discord
from discord.ext import commands
import config


class WelcomeCog(commands.Cog, name="Welcome"):
    """Welcome users when they join"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Welcome members when they join"""
        guild = self.bot.get_guild(config.GUILD_ID)
        intro_channel = guild.get_channel(config.INTRO_CHANNEL_ID)
        rules_channel = guild.get_channel(config.RULES_CHANNEL_ID)
        if not member.bot and guild == member.guild:
            await intro_channel.send(
                f"Welcome to the Dev Pro Tips Server, {member.mention}!\n"
                f"Please read the rules in {rules_channel.mention} to gain access to the rest of the server!"
            )


# setup functions for bot
def setup(bot):
    bot.add_cog(WelcomeCog(bot))