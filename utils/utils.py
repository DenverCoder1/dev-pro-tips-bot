import re
import discord

def blockquote(string: str) -> str:
    """Add blockquotes to a string"""
    # inserts > at the start of string and after new lines
    # as long as it is not at the end of the string
    return re.sub(r"(^|\n)(?!$)", r"\1> ", string.strip())


def embed_success(
    title: str,
    description: str = None,
    colour: discord.Colour = discord.Colour.green(),
) -> discord.Embed:
    """Embed a success message and an optional description"""
    embed = discord.Embed(title=title, colour=colour)
    if description:
        embed.description = description
    return embed