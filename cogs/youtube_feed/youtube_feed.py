import feedparser

from .video import Video


class YouTubeFeed:
    """Feed for checking for new videos in a YouTube channel"""

    def __init__(self, channel_id: str):
        self.__channel_id = channel_id
        self.update_feed()

    def update_feed(self):
        """Parse the feed again and update the last update id"""
        self.__feed = feedparser.parse(
            f"https://www.youtube.com/feeds/videos.xml?channel_id={self.__channel_id}"
        )
        most_recent = self.get_most_recent_video()
        self.__last_publish_date = max(self.__last_publish_date, most_recent.published)

    def get_most_recent_video(self) -> Video:
        """return first entry in feed"""
        return Video(self.__feed.entries[0])

    def has_new_video(self) -> bool:
        """check if the last update is newer than what it was previously"""
        prev_last_publish_date = self.__last_publish_date
        self.update_feed()
        return self.__last_publish_date > prev_last_publish_date
