import subprocess

from discord.ext import commands

class OJCCog(commands.Cog, name = 'ojc'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def run(self, ctx):
        subprocess.call('gcc mock_c_program.c -o mock_c')
        raw_output = subprocess.run(['mock_c'], stdout=subprocess.PIPE, input="5 7", encoding="ascii", universal_newlines=True)
        output = raw_output.stdout
        await ctx.send(output)

def setup(bot):
    bot.add_cog(OJCCog(bot))