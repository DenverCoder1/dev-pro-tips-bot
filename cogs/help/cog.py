from nextcord.ext import commands
from .help_command import NewHelpCommand


class HelpCog(commands.Cog, name="Help"):
    """Displays help information for commands and cogs"""

    def __init__(self, bot: commands.Bot):
        self.__bot = bot
        self.__original_help_command = bot.help_command
        bot.help_command = NewHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.__bot.help_command = self.__original_help_command


# setup functions for bot
def setup(bot: commands.Bot):
    bot.add_cog(HelpCog(bot))