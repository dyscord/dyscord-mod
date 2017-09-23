from dyscord_plugin import DyscordPlugin
from dyscord_plugin.message import DyscordContext
from discord.ext.commands import command


class DyscordMod(DyscordPlugin):
    @command(pass_context=True)
    async def test(self, ctx: DyscordContext):
        await ctx.channel.send("Hey")
