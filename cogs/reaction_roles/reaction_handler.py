from discord.ext import commands
from .role_assignment import RoleAssignment
import discord
import config

class ReactionHandler():
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # ID of message that can be reacted to to add role
        self.role_message_id = config.RULES_MESSAGE_ID
        # Emoji to role mapping
        self.emoji_to_role = {
            "💖": config.SUBSCRIBER_ROLE_ID,
            "💻": config.DEVELOPER_ROLE_ID,
            "✍️": config.CONTENT_CREATOR_ROLE_ID,
        }

    def validate_reaction(self, payload: discord.RawReactionActionEvent) -> RoleAssignment:
        if payload.message_id != self.role_message_id:
            return None
        try:
            role_id = self.emoji_to_role[payload.emoji.name]
        except KeyError:
            return None
        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return None
        role = guild.get_role(role_id)
        if role is None:
            return None
        member = payload.member or guild.get_member(payload.user_id)
        if member is None:
            return None
        return RoleAssignment(member, role)