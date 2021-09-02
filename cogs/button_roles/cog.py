from nextcord.ext import commands
from .role_view import RoleView


class ButtonRolesCog(commands.Cog, name="Button Roles"):
    """Give and remove roles based on button presses"""

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """When the bot is ready, load the role view"""
        self.__bot.add_view(RoleView())
        print("Button view added")

    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx: commands.Context):
        """Starts a role view"""
        await ctx.send("Click a button to add or remove a role.", view=RoleView())


# setup functions for bot
def setup(bot):
    bot.add_cog(ButtonRolesCog(bot))
