from typing import Dict
from time import struct_time


class Video:
    """Class for storing data about a YouTube video"""
    def __init__(self, data: Dict[str, str]):
        self.__id: str = data.yt_videoid
        self.__link: str = data.link
        self.__title: str = data.title
        self.__author: str = data.author
        self.__published: struct_time = data.published_parsed
        self.__description: str = data.summary

    @property
    def id(self) -> str:
        return self.__id

    @property
    def link(self) -> str:
        return self.__link

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def published(self) -> struct_time:
        return self.__published

    @property
    def description(self) -> str:
        return self.__description
