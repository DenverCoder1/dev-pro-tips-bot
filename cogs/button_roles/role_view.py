import nextcord
import config


class RoleView(nextcord.ui.View):
    def __init__(self, add_only: bool = False):
        """
        Args:
            add_only - if True, only add the role, if False, remove it too
        """
        super().__init__(timeout=None)
        self.__add_only = add_only

    async def handle_click(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        # get role from the role id
        role = interaction.guild.get_role(int(button.custom_id.split(":")[-1]))
        assert isinstance(role, nextcord.Role)
        # if member has the role, remove it
        if role in interaction.user.roles and not self.__add_only:
            await interaction.user.remove_roles(role)
            # send confirmation message
            await interaction.response.send_message(
                f"Your {role.name} role has been removed", ephemeral=True
            )
        # if the member does not have the role, add it
        else:
            await interaction.user.add_roles(role)
            # remove unassigned role
            unassigned_role = interaction.guild.get_role(config.UNASSIGNED_ROLE_ID)
            if unassigned_role in interaction.user.roles:
                await interaction.user.remove_roles(unassigned_role)
            # send confirmation message
            await interaction.response.send_message(
                f"You have been given the {role.name} role", ephemeral=True
            )
