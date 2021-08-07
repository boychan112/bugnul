import discord
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print("datetime 버전 : "+str(datetime.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("버그널 리턴"))

@client.event
async def on_message(message):
    content = message.content
    
    if content.startswith("!자기소개"):
        await message.channel.send("응애 나 아기 디코 봇")

    if content.startswith("!이원찬"):
        embed=discord.Embed(description="https://dak.gg/bser/players/plati", color=0x00ff56)
        embed.set_author(name="plati")
        await message.channel.send(embed=embed)

    if content.startswith("!최현영"):
        embed=discord.Embed(description="https://dak.gg/bser/players/light00", color=0x00ff56)
        embed.set_author(name="light00")
        await message.channel.send(embed=embed)

    if content.startswith("!최승민"):
        embed=discord.Embed(description="https://dak.gg/bser/players/kokoakim", color=0x00ff56)
        embed.set_author(name="kokoakim")
        await message.channel.send(embed=embed)

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
