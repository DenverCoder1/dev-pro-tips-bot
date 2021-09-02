from typing import Optional
from nextcord.ext import commands
from .role_assignment import RoleAssignment
import nextcord
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
            "🚀": config.MEMBER_ROLE_ID,
        }

    async def validate_reaction(self, payload: nextcord.RawReactionActionEvent) -> RoleAssignment:
        # check that user reacted to the rules message
        if payload.message_id != self.role_message_id:
            return None
        # get guild
        guild: Optional[nextcord.Guild] = self.bot.get_guild(payload.guild_id)
        assert(guild is not None)
        # get channel
        channel: Optional[nextcord.TextChannel] = guild.get_channel(payload.channel_id)
        assert(channel is not None)
        # get message
        message: Optional[nextcord.Message] = await channel.fetch_message(payload.message_id)
        assert(message is not None)
        # get member
        member = payload.member or guild.get_member(payload.user_id)
        assert(member is not None)
        # check that user is not a bot
        if (member.bot):
            return None
        # find role to assign based on reaction
        try:
            role_id = self.emoji_to_role[payload.emoji.name]
        except KeyError:
            # reaction is not in the dict, so remove it
            await message.remove_reaction(payload.emoji, member)
            return None
        # get role from the role id
        role: Optional[nextcord.Role] = guild.get_role(role_id)
        assert(role is not None)
        # return RoleAssignment containing member and role
        return RoleAssignment(member, role)