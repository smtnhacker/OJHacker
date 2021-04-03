import time
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
  return "",""