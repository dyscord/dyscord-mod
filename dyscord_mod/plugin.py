import asyncio
from dyscord_plugin import DyscordPlugin
from dyscord_plugin.message import DyscordContext
from discord.ext.commands import command
import discord


class DyscordMod(DyscordPlugin):
    '''This is the moderation plugin for Dyscord.'''
    def __init__(self, b):
        super().__init__(b)

    @command(pass_context=True)
    async def kick(self, ctx: DyscordContext, user: discord.Member, *, reason):
        """Kick a member."""
        await ctx.guild.kick(user, reason)
        await ctx.channel.send(f"Kicked {user} ({user.id}) | Reason: {reason}")

    @command(pass_context=True)
    async def ban(self, ctx: DyscordContext, user : discord.Member, *, reason):
        """Ban a member."""
        await ctx.guild.ban(user, reason)
        await ctx.channel.send(f"Banned {user} ({user.id}) | Reason: {reason}")

    @command(pass_context=True)
    async def softban(self, ctx: DyscordContext, user : discord.Member, *, reason):
        """Softbanning is like kicking, but purges the user's messages."""
        await ctx.guild.ban(user, reason)
        await asyncio.sleep(15)
        await ctx.guild.unban(user, reason)
        await ctx.channel.send(f"Softbanned {user} ({user.id}) | Reason: {reason}")
