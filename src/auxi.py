"""Auxillary Functions

All of the functions used by the bot, but are not directly bot
commands or server functions are stored here.
"""

import discord
import time

import constants as cnst


def show_instructions():
    """
    Prints the instructions to the channel using an embed
    """
    embed = discord.Embed(
        title="List of Commands:",
        author="OJ Hacker",
        description="~ use this to access its features",
        color=0x709bff,
    )
    embed.add_field(
        name="1. !insert_tc (or !it) {LE/PA/MP}{number} {label}",
        value="- insert a test case for a specific problem",
        inline=False,
    )
    embed.add_field(
        name="2. !penge_tc (or !ptc) {LE/PA/MP}{number}",
        value="- get all testcases for a specific problem",
        inline=False,
    )
    embed.add_field(
        name="3. !penge_random (or !pr) {LE/PA/MP}{number}",
        value="- get a randomly generated testcase for a specific problem",
        inline=False,
    )
    embed.add_field(
        name="4. !tcs_nga (or !tn) {LE/PA/MP}{number}",
        value="- shows the list of stored testcases for a specific problem",
        inline=False,
    )
    embed.add_field(
        name="5. !share_ko_lang (or !skl) {UID}",
        value="- shows the test case with given uid",
        inline=False,
    )
    embed.add_field(
        name="Example:",
        value="!insert_tc PA05 test",
        inline=False,
    )
    return embed

async def print_tc(ctx, typ, idx, tcs, op):
    """
    Formats the testcase and sends it to the right reciever.

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

async def get_inputs(ctx, inp):
    """
    Parses the input and returns the relevant values

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
        return 0, 0, 0, 0
    if len(inp[0]) < 2 or inp[0][:2] not in cnst.VALID_TYPES:
        await ctx.channel.send(show_instructions())
        return 0, 0, 0, 0

    typ = inp[0][:2]
    try:
        idx = int(inp[0][2:])
    except ValueError:
        await ctx.channel.send(show_instructions())
        return 0, 0, 0, 0

    if idx <= 0 or idx > cnst.LEN_TYP[typ]:
        embed = discord.Embed(
        title="No Testcases Yet",
        author="OJ Hacker",
        description="~ with the possible following reasons:",
        color=0x709bff,
        )
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
        return 0, 0, 0, 0

    name = inp[1] if len(inp) > 1 else "no name"

    return True, typ, idx, name


async def wait_response(bot, ctx, author):
    """Gets the response of the author.

    Waits for the response of the original sender for a
    maximum of 2 minutes and returns it, if it exists.

    Parameters
    -----------
    bot : discord.ext.commands.bot
        The discord bot!
    ctx : miniContext
        Contains important discord-related information
    author : abc.User
        Contains discord information on the author

    Returns
    ----------
    If the user is able to send a message fast enough, returns
    a tuple (content, message)
    content : str
        The actual content of the message
    message : Message
    """

    end_time = time.perf_counter() + 60
    while True:
        resp = await bot.wait_for('message', timeout=60)
        if resp.author == author:
            return resp.content, resp
        if time.perf_counter() > end_time:
            break
    await ctx.channel.send("TLE :(")
    return "", ""

async def wait_for_thumbs_up(ctx, bot):
    """Returns True if the intended user reacted a thumbs-up, Else otherwise"""
    try:
        reaction, _user = await bot.wait_for(
            'reaction_add',
            timeout=30,
            check=lambda reax, user: user == ctx.message.author and str(reaction.emoji) == cnst.THUMBS_UP_EMOJI
        )
        return reaction.emoji == cnst.THUMBS_UP_EMOJI
    except Exception:
        return False
