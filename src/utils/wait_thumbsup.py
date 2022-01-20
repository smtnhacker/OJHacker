import constants as cnst

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