from typing import List
import nextcord
import config


class RoleView(nextcord.ui.View):
    def __init__(self, add_only: bool = False, required_roles: List[int] = None):
        """
        Args:
            add_only - if True, only add the role, if False, remove it too
        """
        super().__init__(timeout=None)
        self.__add_only = add_only
        self.__required_roles = required_roles or []

    def _check_required_roles(self, user: nextcord.Member):
        user_roles_ids = [role.id for role in user.roles]
        return all(role_id in user_roles_ids for role_id in self.__required_roles)

    async def handle_click(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        # get role from the button's role id
        role = interaction.guild.get_role(int(button.custom_id.split(":")[-1]))
        assert isinstance(role, nextcord.Role)
        # if member has the role, remove it
        if role in interaction.user.roles:
            # don't remove if add_only flag is set
            if self.__add_only:
                return await interaction.response.send_message(
                    f"You already have the {role.name} role!", ephemeral=True
                )
            # remove the role
            await interaction.user.remove_roles(role)
            # send confirmation message
            return await interaction.response.send_message(
                f"Your {role.name} role has been removed", ephemeral=True
            )
        # check for required roles
        if not self._check_required_roles(interaction.user):
            return await interaction.response.send_message(
                f"Please confirm above that you have read the rules.", ephemeral=True
            )
        # if the member does not have the role, add it
        await interaction.user.add_roles(role)
        # remove unassigned role
        unassigned_role = interaction.guild.get_role(config.UNASSIGNED_ROLE_ID)
        if unassigned_role in interaction.user.roles:
            await interaction.user.remove_roles(unassigned_role)
        # send confirmation message
        await interaction.response.send_message(
            f"You have been given the {role.name} role", ephemeral=True
        )
