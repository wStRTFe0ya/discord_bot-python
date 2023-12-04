# -*- coding: utf-8 -*-
import os
import asyncio
import discord

from discord import commands
from config import Config

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(
	command_prefix=commands.when_mentioned_or(Config.prefix),
	intents=intents
)
client.remove_command('help')


async def load_extensions():
	for file in os.listdir('./commands'):
		if file.endswith('.js'):
			await client.load_extension(f'commands.{file[:-3]}')

	for file in os.listdir('./events'):
		if file.endswith('.js'):
			await client.load_extension(f'events.{file.[:-3]}')


async def main():
	async with client:
		await load_extensions()
		await client.start(Config.token)


if __name__ == '__main__':
	asyncio.run(main())
