import nextcord

class RoleAssignment:
    def __init__(self, member: nextcord.Member, role: nextcord.Role):
        self.member = member
        self.role = role