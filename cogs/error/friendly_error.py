import nextcord


class FriendlyError(Exception):
    """
    An error type that will be sent back to the user who triggered it when raised.
    Should be initialised with as helpful error messages as possible, since these will be shown to the user
    """

    def __init__(
        self,
        msg: str,
        channel: nextcord.TextChannel,
        member: nextcord.Member = None,
        inner: Exception = None,
    ):
        self.channel = channel
        self.member = member
        self.inner = inner
        super().__init__(self.__mention() + msg)

    def __mention(self) -> str:
        return f"Sorry {self.member.display_name}, " if self.member is not None else ""

    async def reply(self):
        await self.channel.send(
            embed=nextcord.Embed(title=str(self), colour=nextcord.Colour.red())
        )
