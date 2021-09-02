import re
import nextcord
import config


def blockquote(string: str) -> str:
    """Add blockquotes to a string"""
    # inserts > at the start of string and after new lines
    # as long as it is not at the end of the string
    return re.sub(r"(^|\n)(?!$)", r"\1> ", string.strip())


def custom_id(view: str, id: int) -> str:
    """create a custom id from the bot name : the view : the identifier"""
    return f"{config.BOT_NAME}:{view}:{id}"


def embed_success(
    title: str,
    description: str = None,
    colour: nextcord.Colour = nextcord.Colour.green(),
) -> nextcord.Embed:
    """Embed a success message and an optional description"""
    embed = nextcord.Embed(title=title, colour=colour)
    if description:
        embed.description = description
    return embed
