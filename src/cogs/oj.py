from discord.ext import commands
import config

import testcases as tc
import generators as gen
import solutions as ans
import constants as cnst
import utils

class OJCog(commands.Cog, name = 'oj'):
    def __init__(self, bot):
        self.bot = bot
    
    RANDOMERS = gen.TCGenerator(ans)

    @staticmethod
    def non():
	    return ("Cannot generate random test case. :((", "pogi si gab, pero hakdog.")

    # ======= FOR INSERTING TEST CASES =========== #
    @commands.command(aliases = ['it'])
    async def insert_tc(self, ctx):
        """
        Inserts a new test case into the system.

        Syntax:
            !insert_tc <LE/PA/MP><problem #> <test case label>
            !it <LE/PA/MP><problem #> <test case label>
        """

        msg = ctx.message.content
        auth = ctx.message.author

        inp = "".join(msg.split("!insert_tc ", 1)).split(maxsplit=1)

        is_ok, typ, idx, name = await utils.get_inputs(ctx, inp)

        if not is_ok:
            return

        await ctx.channel.send("Please enter your input (w/o formatting)")
        tc_input, _ = await utils.wait_response(bot, ctx, auth)

        await ctx.channel.send("Please enter your output (w/o formatting)")
        tc_output, _ = await utils.wait_response(bot, ctx, auth)

        confirm_msg = await ctx.channel.send("Upload the testcase? (thumbs up)")
        await confirm_msg.add_reaction(cnst.THUMBS_UP_EMOJI)

        tc_yes = await utils.wait_for_thumbs_up(ctx, bot)
        uid = tc.get_id()

        if tc_yes:
            tc.insert_testcase(uid, typ, idx, name, tc_input, tc_output)
            await ctx.channel.send(f"Testcase with UID {uid} added. Thanks!")
        else:
            await ctx.channel.send("Testcase ignored!")

    # ======== PANG-DM NG TEST CASES ========= #
    @commands.command(aliases = ['ptc'])
    async def penge_tc(self, ctx):
        """
        DMs all the stored test cases for a certain problem.

        Syntax:
            !penge_tc <LE/PA/MP><problem #>
            !ptc <LE/PA/MP><problem #>
        """

        msg = ctx.message.content
        author = ctx.message.author

        inp = "".join(msg.split("!penge_tc ", 1)).split(maxsplit=1)

        is_ok, typ, idx, _ = await utils.get_inputs(ctx, inp)

        if not is_ok:
            return

        # retrieve test cases from db
        all_tc = tc.get_all(typ, idx)

        await author.create_dm()
        if not all_tc:
            await author.dm_channel.send("There are no testcases.")
        for tcs in all_tc:
            await utils.print_tc(ctx, typ, idx, tcs, author.dm_channel.send)
        try:
            await ctx.channel.send("DM SENT!")
        except Exception:
            await ctx["channel"].send("DM SENT!")

    # ========= RANDOM GENERATOR ========== #
    @commands.command(aliases = ['pr'])
    async def penge_random(self, ctx):
        """DMs a randomly generated test case with the correct output.

        Syntax:
            !penge_random <LE/PA/MP><problem #>
            !pr <LE/PA/MP><problem #>
        """

        msg = ctx.message.content
        author = ctx.message.author

        inp = "".join(msg.split("!penge_random ", 1)).split(maxsplit=1)

        is_ok, typ, idx, _ = await utils.get_inputs(ctx, inp)

        if not is_ok:
            return

        await author.create_dm()
        OJ_msg = "DM Sent!"
        rand, rand2 = self.non()
        try:
            tc, ans_tc = RANDOMERS.create(typ, idx)

            if tc:
                rand = "TEST CASE\n```python\n" + tc + "```"
            else:
                rand = "```There is no input generated```"
            if ans_tc:
                rand2 = "ANSWER\n```python\n" + ans_tc + "```"
            else:
                rand2 = "``` ```"
        except Exception as e:
            print(f"Tried to create random for {typ}{idx}.")
            print(f"Error:\n{e}")
            OJ_msg = "Sorry! There is no generator for that problem yet. Please contact the mods."
            rand, rand2 = self.non()

        await author.dm_channel.send(rand+"\n"+rand2)
        await ctx.channel.send(OJ_msg)

    # ======== Share mo lang yung tc sa channel ====== #
    @commands.command(aliases = ['skl'])
    async def share_ko_lang(self, ctx, uid=None):
        """Sends the test case with a given UID.

        Syntax:
            !penge_random <uid>
            !skl <uid>
        """
        if not uid:
            await ctx.channel.send("Invalid UID. The syntax for sharing is:\n\
            `!share_ko_lang <uid>`\
            ")
            return

        try:
            typ, idx, io = tc.get_entry(uid)
        except Exception:
            await ctx.channel.send("Problem not found. Please use a valid UID.")
            return

        await utils.print_tc(ctx, typ, idx, io, ctx.channel.send)

    # ========= Prints the available testcases ======= #
    @commands.command(aliases = ['tn'])
    async def tcs_nga(self, ctx):
        """Shows a list of all stored test case for a certain problem.

        Syntax:
            !tcs_nga <LE/PA/MP><problem #>
            !tn <LE/PA/MP><problem #>
        """

        msg = ctx.message.content
        inp = "".join(msg.split("!tcs_nga ", 1)).split(maxsplit=1)

        is_ok, typ, idx, _ = await utils.get_inputs(ctx,inp)

        if not is_ok:
            return

        all_tc = tc.get_all(typ, idx)
        if not all_tc:
            await ctx.channel.send("There are no testcases.")

        output = [(tcs[3], tcs[0]) for tcs in all_tc]

        embed=discord.Embed(
            title="Available Testcases:",
            description="~ for " + str(typ) + str(idx),
            color=0x709bff
        )
        embed.set_author(name="OJ Hacker")

        for cur_tc, cur_output in enumerate(output):
            cur_title = str(cur_tc + 1) + ". UID: " + str(cur_output[0])
            cur_label = "Label: " + str(cur_output[1])
            embed.add_field(name=cur_title, value=cur_label, inline=False)

        await ctx.channel.send(embed=embed)

    # ======= ADMIN COMMANDS ====== #
    @commands.command(hidden=True)
    @commands.check(lambda ctx: getattr(ctx.guild, 'id', None) in cnst.ALLOWED_GUILDS)
    @commands.has_any_role(*cnst.ADMIN_ROLES)
    async def delete_tc(self, ctx):
        msg = ctx.message.content
        inp = "".join(msg.split("!delete_tc ", 1)).split(maxsplit=1)

        try:
            uid = int(inp[0])
        except ValueError:
            await ctx.channel.send("The syntax for deletion is:\n\
                `!delete_tc <uid>`\
            ")
            return

        OJ_msg = f"There exists no test case with UID {uid}"
        ok = tc.delete_entry(uid)
        if ok:
            OJ_msg = f"Test case {uid} successfully deleted!"
        else:
            OJ_msg = f"Cannot find test case {uid} :("
        await ctx.channel.send(OJ_msg)

    @commands.command(hidden=True)
    @commands.check(lambda ctx: getattr(ctx.guild, 'id', None) in cnst.ALLOWED_GUILDS)
    @commands.has_any_role(*cnst.ADMIN_ROLES)
    async def delete_problem(self, ctx):
        """UNDER CONSTRUCTION (kapag puno na database)"""
        auth = ctx.message.author
        msg = ctx.message.content
        inp = "".join(msg.split("!delete_problem ", 1)).split(maxsplit=1)

        is_ok, typ, idx, name = await utils.get_inputs(ctx,inp)

        if not is_ok:
            print("NOT OKAY", is_ok, typ, idx, name)
            return

        # warning kasi di pa naman natetest
        await ctx.channel.send("WARNING! THIS FEATURE IS NOT YET TESTED.")

        await ctx.channel.send(f"Are you sure you want to delete {typ}{idx}? (y/n)".upper())
        resp, msg = await utils.wait_response(bot,ctx,auth)

        if resp.lower() == 'y':
            try:
                tc.delete_row(typ, idx)
                await ctx.channel.send(f"Successfully deleted {typ}{idx}.")
            except Exception:
                print(f"{typ}{idx} not found. Cannot be deleted")
        else:
            await msg.add_reaction('👌')
        return

    @commands.command(hidden=True)
    @commands.check(lambda ctx: getattr(ctx.guild, 'id', None) in cnst.ALLOWED_GUILDS)
    @commands.has_any_role(*cnst.ADMIN_ROLES)
    async def HARD_RESET(self, ctx):
        """DELETES EVERYTHING. Use with caution."""

        auth = ctx.message.author
        await ctx.channel.send(cnst.WIPE_MSG.upper())
        resp, msg = await utils.wait_response(bot,ctx,auth)

        if resp.lower() == 'y':
            tc.erase_db()
            await ctx.channel.send(cnst.WIPE_SUCCESS_MSG)
        else:
            await msg.add_reaction('👌')
        return

    @commands.command(hidden=True)
    @commands.check(lambda ctx: getattr(ctx.guild, 'id', None) in cnst.ALLOWED_GUILDS)
    @commands.has_any_role(*cnst.ADMIN_ROLES)
    async def PRINT_DB(self, ctx):
        """Sends all the stored test cases in a problem

        Syntax:
        !PRINT_DB <LE/PA/MP><problem #>
        """

        msg = ctx.message.content
        inp = "".join(msg.split("!PRINT_DB ", 1)).split(maxsplit=1)

        is_ok,typ,idx,name = await utils.get_inputs(ctx,inp)

        if not is_ok:
            print("NOT OKAY", is_ok, typ, idx, name)
            return

        all_tc = tc.get_all(typ, idx)
        if not all_tc:
            await ctx.channel.send("There are no testcases.")
        for tcs in all_tc:
            await utils.print_tc(ctx, typ, idx, tcs, ctx.channel.send)

    @commands.command(hidden=True)
    @commands.check(lambda ctx: getattr(ctx.guild, 'id', None) in cnst.ALLOWED_GUILDS)
    @commands.has_any_role(*cnst.ADMIN_ROLES)
    async def PRINT_ALL(self, ctx):
        """Prints all the stored test cases

        Use with caution as large amount of data might be sent.
        """

        did_printed_smtn = False
        for typ in cnst.VALID_TYPES:
            for idx in range(1, cnst.LEN_TYP[typ]):
                for tcs in tc.get_all(typ, idx):
                    did_printed_smtn = True
                    await utils.print_tc(ctx, typ, idx, tcs, ctx.channel.send)

        if not did_printed_smtn:
            await ctx.channel.send("There are no test cases in the database")

def setup(bot):
    bot.add_cog(OJCog(bot))