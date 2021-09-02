import os
import nextcord
from nextcord.ext import commands
import config


def main():
    # allows privledged intents for monitoring members joining, roles editing, and role assignments
    intents = nextcord.Intents.default()
    intents.guilds = True
    intents.members = True

    client = commands.Bot(command_prefix=config.PREFIX, intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    # load all cogs
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            client.load_extension(f"cogs.{folder}.cog")

    # run the bot
    client.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
