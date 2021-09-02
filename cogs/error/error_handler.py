from cogs.error.quiet_warning import QuietWarning
import nextcord
from cogs.error.error_logger import ErrorLogger
from cogs.error.friendly_error import FriendlyError
import nextcord.ext.commands.errors as nextcord_err
import config


class ErrorHandler:
    """
    Class that handles raised exceptions
    """

    def __init__(self, error_logger: ErrorLogger) -> None:
        self.logger = error_logger

    async def handle(self, error: Exception, message: nextcord.Message = None):
        if isinstance(error, FriendlyError):
            await self.__handle_friendly(error, message)

        elif isinstance(error, QuietWarning):
            self.__handle_quiet_warning(error)

        elif isinstance(error, nextcord_err.CommandInvokeError):
            await self.handle(error.original, message)

        else:
            self.logger.log_to_file(error, message)
            user_error, to_log = self.__user_error_message(error)
            if to_log:
                await self.logger.log_to_channel(error, message)
            if message is not None:
                friendly_err = FriendlyError(
                    user_error, message.channel, message.author, error,
                )
                await self.handle(friendly_err, message)

    async def __handle_friendly(
        self, error: FriendlyError, message: nextcord.Message = None
    ):
        if error.inner is not None:
            self.logger.log_to_file(error.inner, message)
        await error.reply()

    def __handle_quiet_warning(self, warning: QuietWarning):
        self.logger.log_to_file(warning)

    def __user_error_message(self, error: Exception):
        """Given an error, will return a user-friendly string, and whether or not to log the error in the channel"""
        if isinstance(error, nextcord_err.CommandNotFound):
            return (
                "That command does not exist. Check your spelling or see all available"
                f" commands with `{config.PREFIX}help`",
                False,
            )
        elif isinstance(error, nextcord_err.MissingRequiredArgument):
            return f"Argument {error.param} required.", True
        elif isinstance(error, nextcord_err.TooManyArguments):
            return f"Too many arguments given.", True
        elif isinstance(error, nextcord_err.BadArgument):
            return f"Bad argument: {error}", True
        elif isinstance(error, nextcord_err.NoPrivateMessage):
            return f"That command cannot be used in DMs.", False
        elif isinstance(error, nextcord_err.MissingPermissions):
            return (
                "You are missing the following permissions required to run the"
                f' command: {", ".join(error.missing_perms)}.',
                False,
            )
        elif isinstance(error, nextcord_err.MissingRole):
            return f"You do not have the required role to run this command.", False
        elif isinstance(error, nextcord_err.DisabledCommand):
            return f"That command is disabled or under maintenance.", True
        elif isinstance(error, nextcord_err.CommandInvokeError):
            return f"Error while executing the command.", True
        else:
            return f"An unknown error occurred.", True
