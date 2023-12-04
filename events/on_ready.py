# -*- coding: utf-8 -*-
from discord.ext import commands


class on_ready(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print(f'Client {self.client.user} ready!')


async def setup(client):
	await client.add_cog(on_ready(client))
