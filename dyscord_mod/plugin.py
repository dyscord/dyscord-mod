from dyscord_plugin import DyscordPlugin
from dyscord_plugin.message import DyscordContext
from discord.ext.commands import command


class DyscordMod(DyscordPlugin):
    @command(pass_context=True)
    def test(self, ctx: DyscordContext):
        ctx.channel.send("Hey")
