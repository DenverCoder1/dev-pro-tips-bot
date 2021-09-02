import os
from dotenv.main import load_dotenv

load_dotenv()

# Bot setup
PREFIX = "!"
BOT_NAME = "DevProTips"
BOT_TOKEN = os.getenv("DISCORD_TOKEN", "")

# Discord Guild ID
GUILD_ID = int(os.getenv("GUILD_ID", ""))

# Discord Channel IDs
INTRO_CHANNEL_ID = int(os.getenv("INTRO_CHANNEL_ID", ""))
RULES_CHANNEL_ID = int(os.getenv("RULES_CHANNEL_ID", ""))
BOT_LOG_CHANNEL_ID = int(os.getenv("BOT_LOG_CHANNEL_ID", ""))
YOUTUBE_VIDEOS_CHANNEL_ID = int(os.getenv("YOUTUBE_VIDEOS_CHANNEL_ID", ""))

# Discord Role IDs
CONTENT_CREATOR_ROLE_ID = int(os.getenv("CONTENT_CREATOR_ROLE_ID", ""))
DEVELOPER_ROLE_ID = int(os.getenv("DEVELOPER_ROLE_ID", ""))
SUBSCRIBER_ROLE_ID = int(os.getenv("SUBSCRIBER_ROLE_ID", ""))
MEMBER_ROLE_ID = int(os.getenv("MEMBER_ROLE_ID", ""))
UNASSIGNED_ROLE_ID = int(os.getenv("UNASSIGNED_ROLE_ID", ""))
YOUTUBE_PING_ROLE_ID = int(os.getenv("YOUTUBE_PING_ROLE_ID", ""))

# Discord Message IDs
RULES_MESSAGE_ID = int(os.getenv("RULES_MESSAGE_ID", ""))

# YouTube Channel ID
YT_CHANNEL_ID = os.getenv("YT_CHANNEL_ID", "")
