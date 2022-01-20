async def print_tc(ctx, typ, idx, tcs, op):
	"""Formats the testcase and sends it to the right reciever.

	Given a valid test case, this function formats the testcase
	into a single string of readable form. It then sends it
	to the appropriate reciever via op.
	
	Parameters
	-------------
	ctx : miniContext
		Contains important discord-related information
	typ : str
		Can be either "LE"/"PA"/"MP". Refers to what type of
		activity the query is.
	idx : int
		Must be > 0. Refers the the activity number of the query.
	tcs : (str, str, str, int)
		A tuple containing: (label, inputs, outputs, UID)
	op : function
		A function that tells where to send the resulting string
	"""

	to_printA = f"**UID#{tcs[3]} {typ}{idx}: {tcs[0]}**\n\n"
	to_printB = f"INPUT\n```python\n{tcs[1]}\n```"
	to_printC = f"OUTPUT\n```python\n{tcs[2]}\n```"

	await op(to_printA + to_printB + to_printC)