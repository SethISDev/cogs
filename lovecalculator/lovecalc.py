import discord
from redbot.core import commands
import random


class LoveCalc(commands.Cog):
	"""Calcule l'amour entre deux personnes !"""
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def lovecalc(self, ctx, p1: discord.Member, p2: discord.Member=None):
		"""
		Calcule le pourcentage d'amour entre deux personnes.
		
		Si une seule personne est mentionnée l'aueur du message sera la deuxième..
		"""
		if p2 is None:
			p2 = ctx.author
		state = random.getstate()
		new_seed = str(p1.id + p2.id)
		random.seed(new_seed)
		love = random.randint(0, 101)
		random.setstate(state)
		love_dict = {
			0: '\N{BROKEN HEART}',
			1: '\N{HEAVY BLACK HEART}',
			2: '\N{SPARKLING HEART}',
			3: '\N{HEART WITH RIBBON}',
			4: '\N{GROWING HEART}\N{GROWING HEART}\N{GROWING HEART}'
		}
		await ctx.send(
			f'{love_dict[love//25]} **{p1.display_name}** et **{p2.display_name}** '
			f'sont compatibles a {love}% ! {love_dict[love//25]}'
		)
