import random
import config
import nextcord
from nextcord.ext import commands
from nextcord.ext import application_checks


class Giveaway(commands.Cog, name="Giveaway"):
    """Giveaway command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.emoji = "\N{PARTY POPPER}"

    @nextcord.message_command(guild_ids=[config.GUILD_ID])
    @application_checks.is_owner()
    async def giveaway(
        self, interaction: nextcord.Interaction, message: nextcord.Message
    ):
        """
        Pick a winner for a giveaway if there is a party popper emoji reaction.
        Otherwise, add the party popper emoji.
        """
        # look for the giveaway emoji in the message's reactions
        reaction = nextcord.utils.find(
            lambda r: r.emoji == self.emoji, message.reactions
        )
        # if the reaction is not found, add it instead of picking a winner
        if not reaction:
            await message.add_reaction(self.emoji)
            await interaction.send(":white_check_mark: Giveaway started!", ephemeral=True)
            return
        # find all users who entered the giveaway (excluding bots)
        users = [user for user in await reaction.users().flatten() if not user.bot]
        # if no non-bot users reacted to the message
        if not users:
            await interaction.send(
                ":x: No users have entered the giveaway!", ephemeral=True
            )
            return
        # pick a random user who reacted with the emoji on the message
        winner = random.choice(users)
        await interaction.send(
            f"**The winner is... {winner.mention}!** :tada:\n\n"
            f"Send a message to <@{self.bot.owner_id}> to claim "
            "the prize (must claim within 12 hours)."
        )


# setup functions for bot
def setup(bot):
    bot.add_cog(Giveaway(bot))
