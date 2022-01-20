import discord

import constants as cnst
from .show_instructions import show_instructions

async def get_inputs(ctx, inp, name='no name'):
	"""Parses the input and returns the relevant values

	Checks if the input is of the form:
		<LE/PA/MP><valid number> <label>
	and if it is not, responds appropriately by showing
	the right syntax. Also, it checks if the problem
	number (idx) is valid, e.g. positive and within the
	bounds of the current programming problems.

	Parameters
	----------
	ctx : miniContext
		Contains important discord-related information
	inp : str
		Contains what the user typed
	
	Returns
	---------
	if the input is valid, returns the tuple (ok, typ, idx, name)
	ok : Boolean
		Tells if the input is valid
	typ : str
		Contains what type of problem the input is. It is either
		"LE", "PA", or "MP".
	idx : int
		Refers to which problem the input is.
	name : str
		Contains a description or title of the input. It may be
		empty, in which a default "no name" is returned.
	"""

	if not inp:
		return 0,0,0,0
	if len(inp) < 2 or inp[:2] not in cnst.VALID_TYPES:
		print(inp)
		await show_instructions(ctx)
		return 0,0,0,0
	
	typ = inp[:2]
	try:
		idx = int(inp[2:])
	except ValueError:
		await show_instructions(ctx)
		return 0,0,0,0
	
	if idx <= 0 or idx > cnst.LEN_TYP[typ]:
		embed=discord.Embed(
			title="No Testcases Yet", 
			description="~ with the possible following reasons:", 
			color=0x709bff
		)
		embed.set_author(name="OJ Hacker")
		embed.add_field(
			name="1. No one has solved it yet", 
			value="So sad.", 
			inline=False
		)
		embed.add_field(
			name="2. The problem does not exist.", 
			value="Baka na-typo ka ser!", 
			inline=False
		)
		await ctx.channel.send(embed=embed)
		return 0,0,0,0

	return True, typ, idx, name