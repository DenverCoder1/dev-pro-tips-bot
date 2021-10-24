from typing import Optional, Union

import nextcord
from nextcord.embeds import EmptyEmbed, _EmptyEmbed

DEFAULT_COLOR = nextcord.Colour.blurple()
MAX_EMBED_DESCRIPTION_LENGTH = 4096
MAX_EMBED_FIELD_TITLE_LENGTH = 256
MAX_EMBED_FIELD_FOOTER_LENGTH = 2048


def __trim(text: str, limit: int) -> str:
    """limit text to a certain number of characters"""
    return text[: limit - 3].strip() + "..." if len(text) > limit else text


def embed_success(
    title: str,
    description: Optional[str] = None,
    footer: Optional[str] = None,
    url: Union[str, _EmptyEmbed] = EmptyEmbed,
    image: Optional[str] = None,
    thumbnail: Optional[str] = None,
) -> nextcord.Embed:
    """Embed a success message and an optional description, footer, and url"""
    return build_embed(
        title, description, footer, url, nextcord.Colour.green(), image, thumbnail
    )


def embed_warning(
    title: str,
    description: Optional[str] = None,
    footer: Optional[str] = None,
    url: Union[str, _EmptyEmbed] = EmptyEmbed,
    image: Optional[str] = None,
    thumbnail: Optional[str] = None,
) -> nextcord.Embed:
    """Embed a warning message and an optional description, footer, and url"""
    return build_embed(
        title, description, footer, url, nextcord.Colour.gold(), image, thumbnail
    )


def embed_error(
    title: str,
    description: Optional[str] = None,
    footer: Optional[str] = None,
    url: Union[str, _EmptyEmbed] = EmptyEmbed,
    image: Optional[str] = None,
    thumbnail: Optional[str] = None,
) -> nextcord.Embed:
    """Embed an error message and an optional description, footer, and url"""
    return build_embed(
        title, description, footer, url, nextcord.Colour.red(), image, thumbnail
    )


def build_embed(
    title: str,
    description: Optional[str] = None,
    footer: Optional[str] = None,
    url: Union[str, _EmptyEmbed] = EmptyEmbed,
    colour: nextcord.Colour = DEFAULT_COLOR,
    image: Optional[str] = None,
    thumbnail: Optional[str] = None,
) -> nextcord.Embed:
    """Embed a message and an optional description, footer, and url"""
    # create the embed
    embed = nextcord.Embed(
        title=__trim(title, MAX_EMBED_FIELD_TITLE_LENGTH), url=url, colour=colour
    )
    if description:
        embed.description = __trim(description, MAX_EMBED_DESCRIPTION_LENGTH)
    if footer:
        embed.set_footer(text=__trim(footer, MAX_EMBED_FIELD_FOOTER_LENGTH))
    if image:
        embed.set_image(url=image)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    return embed
