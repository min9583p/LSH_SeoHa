#main.py
import asyncio, discord
from discord.ext import commands
client = discord.Client()
bot = commands.Bot(command_prefix=["서하야 ", "a ", "ㅅㅎ "])

@bot.event
async def on_ready():
	print("We have loggedd in as {0.user}".format(bot))

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕!!")

@bot.command()
async def 저리가(ctx):
    await ctx.send("어..? 잘있어...")

@bot.command()
async def 서하야(ctx):
    await ctx.send("나 불렀어?")

@bot.command()
async def 바보(ctx):
    await ctx.send("으잉...? 바보아닌뒙...")

@bot.command()
async def 만든사람(ctx):
    await ctx.send("공고생 개발자 이서하님이세요!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
        
@bot.command()
async def a(ctx, user: discord.User):
    channel = bot.get_channel(1004742567759466536)
    await channel.send(f'<@&1005458692470222900>\n᛭저희 병원에 새로오신 환자분을 환영해주세요! :tada:\n\n {user.mention}님! 저희 서버에 오신걸 환영해요!\n\n᛭서버 적응이 어려우시다면 간호사를 불러주세요! :person_raising_hand:\n\n᛭문의 하실게있으시다면 <#1005166621914058782>에 편하게 문의해주세요!  :envelope_with_arrow:\n\n᛭공지는 <#1005092490061291580>에서 확인해주세요! :loudspeaker:')

@bot.command()
async def 경고(ctx, user: discord.User, text):
    channel = bot.get_channel(1004748420898103326)
    await channel.send(f'{user.mention}({user.id}) 경고 1회 지급되었습니다.\n사유 : {text}')

@bot.command()
async def 주의(ctx, user: discord.User, text):
    channel = bot.get_channel(1004748420898103326)
    await channel.send(f'{user.mention}({user.id}) 경고 1회 지급되었습니다.\n사유 : {text}')

bot.run('OTg2MjkwODk4ODg5NDkwNTIy.G-KYG2.2aL57gTttzgZ2UJbtZMfoW1xJZ1vay9tv_MWj8')