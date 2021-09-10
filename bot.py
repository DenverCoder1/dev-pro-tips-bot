import os
import nextcord
from nextcord.ext import commands
import config


def main():
    # allows privledged intents for monitoring members joining, roles editing, and role assignments
    intents = nextcord.Intents.default()
    intents.guilds = True
    intents.members = True

    activity = nextcord.Activity(type=nextcord.ActivityType.listening, name=f"{config.PREFIX}help")

    bot = commands.Bot(command_prefix=config.PREFIX, intents=intents, activity=activity)

    # boolean that will be set to true when views are added
    bot.persistent_views_added = False

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} has connected to Discord.")

    # load all cogs
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            bot.load_extension(f"cogs.{folder}.cog")

    # run the bot
    bot.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
