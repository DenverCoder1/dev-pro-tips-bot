from datetime import datetime
from typing import Optional
import traceback
from nextcord.ext import commands
import nextcord


class ErrorLogger:
	def __init__(self, log_file: str, log_channel_id: int, bot: commands.Bot) -> None:
		self.log_file = log_file
		self.log_channel_id = log_channel_id
		self.bot = bot


	def log_to_file(
		self, error: BaseException, message: Optional[nextcord.Message] = None
	):
		"""appends the date and logs text to a file"""
		with open(self.log_file, "a", encoding="utf-8") as f:
			# write the current time and log text at end of file
			f.write(str(datetime.now()) + "\n")
			f.write(self.__get_err_text(error, message) + "\n")
			f.write("--------------------------\n")

	async def log_to_channel(
		self, error: BaseException, message: Optional[nextcord.Message] = None
	):
		log_channel = self.bot.get_channel(self.log_channel_id)
		assert isinstance(log_channel, nextcord.TextChannel)
		if message is None:
			await log_channel.send(f"```{self.__get_err_text(error)}```")
		else:
			channel = (
				message.channel.mention
				if isinstance(message.channel, nextcord.TextChannel)
				else "DM"
			)
			await log_channel.send(
				f"Error triggered by {message.author.mention} in"
				f" {channel}\n```{self.__get_err_text(error, message)}```"
			)

	def __get_err_text(
		self, error: BaseException, message: Optional[nextcord.Message] = None
	):
		description = "".join(
			traceback.format_exception(error.__class__, error, error.__traceback__)
		)
		if message is None:
			return description
		return self.__attach_context(description, message)

	def __attach_context(self, description: str, message: nextcord.Message):
		"""returns human readable command error for logging in log channel"""
		return (
			f"Author:\n{message.author} ({message.author.display_name})\n\n"
			f"Channel:\n{message.channel}\n\n"
			f"Message:\n{message.content}\n\n"
			f"{description}\n"
		)

	def read_logs(self, n_lines, char_lim: int = 2000) -> str:
		try:
			with open(self.log_file, "r", encoding="utf-8") as f:
				# read logs file
				lines = f.readlines()
				last_n_lines = "".join(lines[-n_lines:])
				# trim the logs if too long
				if len(last_n_lines) > char_lim - 10:
					last_n_lines = f"․․․\n{last_n_lines[-(char_lim - 10):]}"
				return f"```{last_n_lines}```"
		except FileNotFoundError:
			return "https://tenor.com/view/nothing-to-see-here-explosion-explode-bomb-fire-gif-4923610"