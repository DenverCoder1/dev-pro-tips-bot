import config
from nextcord.ext import commands
from .confirm_view import ConfirmView
from .self_role_view import SelfRoleView


class ButtonRolesCog(commands.Cog, name="Button Roles"):
    """Give and remove roles based on button presses"""

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """When the bot is ready, load the role views"""
        # skip this function if views are already added
        if self.__bot.persistent_views_added:
            return
        self.__bot.add_view(SelfRoleView())
        self.__bot.add_view(ConfirmView())
        # set flag
        self.__bot.persistent_views_added = True
        print("Button views added")

    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx: commands.Context):
        """Starts a role view"""
        await ctx.send("Click a button to add or remove a role.", view=SelfRoleView())

    @commands.command()
    @commands.is_owner()
    async def add_confirm(self, ctx: commands.Context, message_id: str):
        """Starts a confirm view"""
        rules_channel = await ctx.guild.fetch_channel(config.RULES_CHANNEL_ID)
        message = await rules_channel.fetch_message(message_id)
        await message.edit(view=ConfirmView())


# setup functions for bot
def setup(bot):
    bot.add_cog(ButtonRolesCog(bot))
