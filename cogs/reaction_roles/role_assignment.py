import discord

class RoleAssignment:
    def __init__(self, member: discord.Member, role: discord.Role):
        self.member = member
        self.role = role