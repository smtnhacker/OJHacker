from .. import constants as cnst

async def wait_thumbsup(ctx, bot):
  """Returns True if the intended user reacted a thumbs-up, Else otherwise"""
  def chk(reaction, user):
    return user == ctx.message.author and str(reaction.emoji) == cnst.THUMBS_UP_EMOJI

  try:
    reaction, user = await bot.wait_for('reaction_add', timeout = 30, check = chk)
    if reaction.emoji == cnst.THUMBS_UP_EMOJI:
      return True
  except:
    return False
