import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="검열"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
    message_content=message.content
    a = message_content.find("윤")
    b = message_content.find("정")
    c = message_content.find("윰")
    word_list = ["윰정","느"]
    if(a>=0):
      d=1
    await client.process_commands(message)
    if ((a>=0 or c>=0) and b>=0) or (d>=0 and b>=0):
        await message.channel.send("금기어 입니다.")
        await message.delete()
        d=0
    await client.process_commands(message)

client.run(os.environ['token'])


