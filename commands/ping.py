# -*- coding: utf-8 -*-
import discord
from discord.ext import commands


class ping(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ping(self, context):
		await context.reply(f'Pong! **{self.client.latency * 1000}** ms', mention_author=False)


async def setup(client):
	await client.add_cog(ping(client))
