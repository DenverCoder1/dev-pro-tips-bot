from typing import Optional, Union
import nextcord
from utils.embedder import embed_error


class FriendlyError(Exception):
	"""
	An error type that will be sent back to the user who triggered it when raised.
	Should be initialised with as helpful error messages as possible, since these will be shown to the user

	Attributes
	----------
	msg: :class:`str`
			The message to display to the user.
	sender: :class:`nextcord.abc.Messageable`
			An object which can be used to call send.
	member: Optional[:class:`Member`]
			The member who caused the error.
	inner: Optional[:class:`Exception`]
			An exception that caused the error.
	description: Optional[:class:`str`]
			Description for the FriendlyError embed.
	image: Optional[:class:`str`]
			Image for the FriendlyError embed.
	"""

	def __init__(
		self,
		msg: str,
		sender: nextcord.abc.Messageable,
		member: Union[nextcord.Member, nextcord.User, None] = None,
		inner: Optional[BaseException] = None,
		description: Optional[str] = None,
		image: Optional[str] = None,
	):
		self.sender = sender
		self.member = member
		self.inner = inner
		self.description = description
		self.image = image
		super().__init__(self.__mention() + msg)

	def __mention(self) -> str:
		return f"Sorry {self.member.display_name}, " if self.member else ""

	async def reply(self):
		await self.sender.send(
			embed=embed_error(
				str(self), description=self.description, image=self.image
			)
		)
