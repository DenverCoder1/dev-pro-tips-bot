import discord
from discord.ext import commands
from .reaction_handler import ReactionHandler

class ReactionRolesCog(commands.Cog, name="Reaction Roles"):
    """Give and remove roles based on reactions"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.reaction_handler = ReactionHandler(bot)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji"""
        role_assignment = self.reaction_handler.validate_reaction(payload)
        if role_assignment is not None:
            await role_assignment.member.add_roles(role_assignment.role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji"""
        role_assignment = self.reaction_handler.validate_reaction(payload)
        if role_assignment is not None:
            await role_assignment.member.remove_roles(role_assignment.role)
        

# setup functions for bot
def setup(bot):
    bot.add_cog(ReactionRolesCog(bot))