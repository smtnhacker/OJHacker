import discord

async def show_instructions(ctx):
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

    await ctx.send(embed=embed)