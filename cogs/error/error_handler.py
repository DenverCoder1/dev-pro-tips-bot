from typing import Optional
from .quiet_warning import QuietWarning
from .error_logger import ErrorLogger
from .friendly_error import FriendlyError
import nextcord.ext.commands.errors as discord_err
import nextcord


class ErrorHandler:
	"""
	Class that handles raised exceptions
	"""

	def __init__(self, error_logger: ErrorLogger) -> None:
		self.logger = error_logger

	async def handle(
		self, error: BaseException, message: Optional[nextcord.Message] = None
	):
		if isinstance(error, FriendlyError):
			await self.__handle_friendly(error, message)

		elif isinstance(error, QuietWarning):
			self.__handle_quiet_warning(error)

		elif isinstance(error, discord_err.CommandInvokeError):
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
		self, error: FriendlyError, message: Optional[nextcord.Message] = None
	):
		if error.inner:
			self.logger.log_to_file(error.inner, message)
		await error.reply()

	def __handle_quiet_warning(self, warning: QuietWarning):
		self.logger.log_to_file(warning)

	def __user_error_message(self, error: BaseException):
		"""Given an error, will return a user-friendly string, and whether or not to log the error in the channel"""
		if isinstance(error, discord_err.MissingPermissions):
			return (
				"You are missing the following permissions required to run the"
				f' command: {", ".join(str(perm) for perm in error.missing_perms)}.',
				False,
			)
		elif isinstance(error, discord_err.MissingRole):
			return f"You do not have the required role to run this command.", False
		elif isinstance(error, discord_err.CommandInvokeError):
			return f"Error while executing the command.", True
		else:
			return f"An unknown error occurred.", True
