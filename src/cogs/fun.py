from discord.ext import commands
import random

import images

class FunCog(commands.Cog, name = 'fun'):
    def __init__(self, bot):
        self.bot = bot
    
    # ===== Random command here dahil kay Jotan ===== #
    @commands.command(pass_context=True)
    async def penge_jowa(self, ctx):
        """For the bored people."""
        import random
        author = ctx.message.author

        await author.create_dm()
        OJ_msg = "Waifu Sent!"
        rt = random.randint(1,len(images.img_lst))
        rd = random.randint(1,1000)
        ct, end = '','.jpg'
        if rd >= 200 and rd < 250:
            rt = random.randint(1,len(images.kanon_lang_malakas))
            embid = discord.Embed(colour=discord.Colour(0xd55f66))
            embid.set_image(url=images.kanon_lang_malakas[rt-1]+end)
            embid.add_field(name="Kanon Kimura uwu", value="*No need to cite. Hmph. STAN ATARASHI GAKKO!*")
            await author.dm_channel.send(embed=embid)
            await ctx.channel.send('STAN ATARASHI GAKKO!')
        elif rd == 171:
            embid = discord.Embed(colour=discord.Colour(0x992d22))
            embid.set_image(url='https://imgur.com/cukHbrY.jpg')
            embid.add_field(name="Selfie Pic Galing sa Phone ng Kaklase Habang nakahiga sa Kama Prongs :o", value="**Congratulations!** You may now request a new idol to be added for the command.\n *The image was given proper consent for it to be used for special purposes*")
            await author.dm_channel.send(embed=embid)
            await ctx.channel.send('CONGRATS!')
        elif rd == 781:
            embid = discord.Embed(colour=discord.Colour(0x992d22))
            embid.set_image(url='https://imgur.com/cqdceQn.jpg')
            embid.add_field(name="Lord God Lord Lord God Miko :o", value="**Congratulations!** You may now request a new idol to be added for the command.\n *The image was given proper consent for it to be used for special purposes*")
            await author.dm_channel.send(embed=embid)
            await ctx.channel.send('CONGRATS!')
        elif rd == 913:
            embid = discord.Embed(colour=discord.Colour(0x992d22))
            embid.set_image(url='https://imgur.com/Tif00Fq.jpg')
            embid.add_field(name="Senpai Gabuuu :o", value="**Congratulations!** You may now request a new idol to be added for the command.\n *The image was given proper consent for it to be used for special purposes*")
            await author.dm_channel.send(embed=embid)
            await ctx.channel.send('CONGRATS!')
        else:
            ct = images.img_lst[rt-1]
            embid = discord.Embed(colour=discord.Colour(0xefae0))
            embid.set_image(url=ct+end)
            embid.add_field(name="Kowean Pop Idol Waifu :>", value="*This image is credited to random Twitter archives the developer downloaded from.\nThe developers are very sorry for the improper citation of the source.*")
            await author.dm_channel.send(embed=embid)
            await ctx.channel.send(OJ_msg)

def setup(bot):
    bot.add_cog(FunCog(bot))