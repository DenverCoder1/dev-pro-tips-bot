from nextcord.ext import commands

class Ping(commands.Cog, name="Ping"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Checks for a response from the bot"""
        await ctx.send(f"Pong! (Latency: {round(self.bot.latency * 1000)}ms)")

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))