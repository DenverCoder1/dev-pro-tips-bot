import config
import sys
from discord.ext import commands
from .error_handler import ErrorHandler
from .error_logger import ErrorLogger


class ErrorLogCog(commands.Cog, name="Error Logs"):
    """Show recent error logs"""

    def __init__(self, bot: commands.Bot):
        self.logger = ErrorLogger("err.log", config.BOT_LOG_CHANNEL_ID, bot)
        self.handler = ErrorHandler(self.logger)

    @commands.command(hidden=True)
    async def logs(self, ctx: commands.Context, num_lines: int = 50):
        """Show recent logs from err.log

        Usage:
        ```
        !logs
        ```
        """
        await ctx.send(self.logger.read_logs(num_lines))

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        """When a command exception is raised, log it in err.log and bot log channel"""
        await self.handler.handle(error, ctx.message)

    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        """When an exception is raised, log it in err.log and bot log channel"""

        _, error, _ = sys.exc_info()
        if error:
            await self.handler.handle(error)


# setup functions for bot
def setup(bot: commands.Bot):
    cog = ErrorLogCog(bot)
    bot.add_cog(cog)
    setattr(bot, "on_error", cog.on_error)