#main.py
import asyncio, discord, os, time, BackUp, threading, shutil
from typing_extensions import Required
from discord import Member
from discord.utils import get
from discord.ext import commands, bridge
from discord.commands import *
import numpy as np
import random
import zlib
import sys
from dotenv import load_dotenv
from datetime import date
from datetime import datetime

from game import *
from user import *

boot_start = datetime.today()

intents = discord.Intents()
intents.message_content = True

load_dotenv()

bot = discord.Bot()

today = date.today()
date_format = time.strftime("%Y-%m-%d_%H시%M분%S초")
date_form = time.strftime("%Y. %m. %d.")
dst_name=date_format+'_UserDB_BackUp'
dstpy_name=date_format+'_SHbot_BackUp'

def ATBU():
    shutil.copy(os.getenv('DB_PT'), f'./BackUp/{dst_name}.xlsx')
    shutil.copy(os.getenv('PY_PT'), f'./BackUp/{dstpy_name}.py')

ATBU()

@bot.event
async def on_ready():
    boot_end = datetime.today()
    boot_time = boot_end - boot_start
    channel = bot.get_channel(1008004079743672432)
    embed = discord.Embed(title="🚧 서하 기상 🚧", description = " " ,color = 0xFFC300)
    embed.add_field(name = "기상 시간", value = date_format, inline = False)
    embed.add_field(name = "걸린 시간", value = f'{boot_time.total_seconds()}초 걸렸어요!', inline = False)
    embed.add_field(name = "안녕하세요! 서하님!", value = "즐거운 하루 되세요!", inline = False)
    await channel.send(embed=embed)

    print("We have loggedd in as {0.user}".format(bot))
        
@bot.slash_command(name="핑", description = '간단한 핑체크!')
async def 핑(ctx):
    await ctx.respond(f"퐁! {round(bot.latency * 1000)}ms")
        
@bot.slash_command(name = '안녕', description = '간단한 인사기능')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
async def 안녕(ctx, name: str = None):
    name = name or ctx.author.name
    RM = await ctx.respond(f"안녕 {name}!")
    time.sleep(1.5)
    await RM.edit_original_message(content = "헤헷..")

@bot.slash_command(name = '도움말', description = '말그대로')
async def 도움(ctx):
    embed = discord.Embed(title = "서하봇", description = "V2", color = 0x6E17E3) 
    embed.add_field(name = "❓도움", value = "도움말을 봅니다", inline = False)
    embed.add_field(name = "🎲주사위", value = "주사위를 굴려 봇과 대결합니다", inline = False)
    embed.add_field(name = "📋내정보", value = "자신의 정보를 확인합니다", inline = False)
    embed.add_field(name = "🔎정보 [대상]", value = "멘션한 [대상]의 정보를 확인합니다", inline = False)
    embed.add_field(name = "📨송금 [대상] [돈]", value = "멘션한 [대상]에게 [돈]을 보냅니다", inline = False)
    embed.add_field(name = "🎰도박 [돈]", value = "[돈]을 걸어 도박을 합니다. 올인도 가능합니다", inline = False)
    embed.add_field(name = "🧧용돈", value = "랜덤으로 용돈을 지급한다", inline = False)
    embed.add_field(name = "💳환전 [미무포인트]", value = "미무포인트로 환전한다. ex)서하야 환전 10000 | 10만원 = 1만 포인트", inline = False)
    await ctx.respond(embed=embed)
    
@bot.slash_command(name = '주사위', description = '주사위를 굴릴수 있다!')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
async def 주사위(ctx):
    result, _color, bot1, bot2, user1, user2, a, b = dice()

    embed = discord.Embed(title = "주사위 게임 결과", description = "\n", color = _color)
    embed.add_field(name = "서하봇의 숫자 " + bot1 + "+" + bot2, value = ":game_die: " + a, inline = False)
    embed.add_field(name = ctx.author.name+"의 숫자 " + user1 + "+" + user2, value = ":game_die: " + b, inline = False)
    embed.set_footer(text="결과: " + result)
    await ctx.respond(embed=embed)

@bot.slash_command(name = '도박', description = '도박상담은 1366')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
async def 도박(ctx, 
금액:Option(int,'금액을 입력해주세요',min_value=1000,max_value=1000000)):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    win = gamble()
    result = ""
    betting = 0
    _color = 0x000000
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        cur_money = getMoney(ctx.author.name, userRow)

        if 금액 == "올인":
            betting = cur_money
            if win:
                result = "성공"
                _color = 0x00ff56
                print(result)

                modifyMoney(ctx.author.name, userRow, int(0.5*betting))

            else:
                result = "실패"
                _color = 0xFF0000
                print(result)

                modifyMoney(ctx.author.name, userRow, -int(betting))
                addLoss(ctx.author.name, userRow, int(betting))

            embed = discord.Embed(title = "🎰도박 결과🎰", description = result, color = _color)
            embed.add_field(name = "🪙배팅금액", value = betting, inline = False)
            embed.add_field(name = "💰현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)
            embed.add_field(name = "도박은 질병입니다.", value = ctx.author.mention, inline = False)
            embed.set_footer(text="도박상담 1336")

            await ctx.respond(embed=embed)
            
        elif int(금액) >= 1000:
            if cur_money >= int(금액):
                betting = int(금액)
                print("배팅금액: ", betting)
                print("")

                if win:
                    result = "성공"
                    _color = 0x00ff56
                    print(result)

                    modifyMoney(ctx.author.name, userRow, int(0.5*betting))

                else:
                    result = "실패"
                    _color = 0xFF0000
                    print(result)

                    modifyMoney(ctx.author.name, userRow, -int(betting))
                    addLoss(ctx.author.name, userRow, int(betting))

                embed = discord.Embed(title = "🎰도박 결과🎰", description = result, color = _color)
                embed.add_field(name = "🪙배팅금액", value = betting, inline = False)
                embed.add_field(name = "💰현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)
                embed.add_field(name = "도박은 질병입니다.", value = ctx.author.mention, inline = False)
                embed.set_footer(text="도박상담 1336")

                await ctx.respond(embed=embed)

            else:
                print("돈이 부족합니다.")
                print("배팅금액: ", 금액, " | 현재자산: ", cur_money)
                await ctx.respond("돈이 부족합니다. 현재자산: " + str(cur_money), ephemeral =True)
        else:
            print("배팅금액", 금액, "가 1000보다 작습니다.")
            await ctx.respond("1000원 이상만 배팅 가능합니다.", ephemeral =True)
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.respond("도박은 회원가입 후 이용 가능합니다.", ephemeral =True)

    print("------------------------------\n")

@bot.slash_command(name = '랭킹', description = '누가누가 레벨이 높을까?')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
async def 랭킹(ctx):
    rank = ranking()
    embed = discord.Embed(title = "🏆레벨 랭킹", description = "", color = 0x4A44FF)

    for i in range(0,len(rank)):
        if i%2 == 0:
            name = rank[i]
            lvl = rank[i+1]
            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="🎟️레벨: "+str(lvl), inline=False)

    await ctx.respond(embed=embed) 

@bot.slash_command(name = '번호표', description = '안내를 받고싶다면 번호표를 뽑아봐!')
@commands.has_any_role(1004739278720483418)
async def 번호표(ctx,
이름:Option(str,'저희 서버에서 사용하실 이름을 적어주세요!'),
나이:Option(int,'본인의 나이를 적어주세요!(주민등록상의 세는나이 기준)',min_value=12),
공개여부:Option(str,'공개여부를 선택해주세요!',choices=['공개','비공']),
성별:Option(str,'성별을 선택해주세요!',choices=['남성','여성']),
경로:Option(str,'저희 서버에는 어떻게 들어오시게 되었나요?')):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    channel = bot.get_channel(1005029973695922258)
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await channel.send(f'{ctx.author.mention}님의 입장 정보입니다\n\n닉네임 : {이름}\n나이 : {나이}\n공개 여부 : {공개여부}\n성별 : {성별}\n경로 : {경로}')
        await ctx.respond('성공적으로 번호표가 발급되었습니다. 잠시만 기다려주세요.', ephemeral =True)
        await ctx.send(f'번호표가 발급되었습니다.\n\n<@&1004688586093887528>\n{ctx.author.mention}님의 안내를 도와주세요')
    else:
        if 나이 < 12:
            await ctx.respond('저희 서버는 2022년 기준 11년생 12살 부터 입장 가능합니다.')
        else:
            print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
            print("")

            Signup(ctx.author.name, ctx.author.id)

            print("회원가입이 완료되었습니다.")    
            print("------------------------------\n")
            await channel.send(f'{ctx.author.mention}님의 입장 정보입니다\n\n닉네임 : {이름}\n나이 : {나이}\n공개 여부 : {공개여부}\n성별 : {성별}\n경로 : {경로}')
            await ctx.respond('성공적으로 번호표가 발급되었습니다. 잠시만 기다려주세요.', ephemeral =True)
            await ctx.send(f'번호표가 발급되었습니다.\n\n<@&1004688586093887528>\n{ctx.author.mention}님의 안내를 도와주세요')
        
@bot.slash_command(name = '연합번호표', description = '연합관련 멤버 전용이야!')
@commands.has_any_role(1004739278720483418)
async def 연합번호표(ctx,
이름:Option(str,'저희 서버에서 사용하실 이름을 적어주세요!'),
성별:Option(str,'성별을 선택해주세요!',choices=['남성','여성']),
연합서버:Option(str,'어느서버에서 연합하러 오셨나요?')):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    channel = bot.get_channel(1005029973695922258)
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await channel.send(f'{ctx.author.mention}님의 입장 정보입니다\n\n닉네임 : {이름}\n성별 : {성별}\n경로 : {연합서버}\n\n연합역할 지급해주시고 안내패스 부탁드려요!\n\n<@&1004688586093887528>')
        await ctx.respond('성공적으로 번호표가 발급되었습니다. 잠시만 기다려주세요.', ephemeral =True)
        await ctx.send(f'번호표가 발급되었습니다.\n\n<@&1004688586093887528>\n{ctx.author.mention}님의 안내를 도와주세요')
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("")

        Signup(ctx.author.name, ctx.author.id)

        print("회원가입이 완료되었습니다.")
        print("------------------------------\n")
        await channel.send(f'{ctx.author.mention}님의 입장 정보입니다\n\n닉네임 : {이름}\n성별 : {성별}\n경로 : {연합서버}\n\n연합역할 지급해주시고 안내패스 부탁드려요!\n\n<@&1004688586093887528>')
        await ctx.respond('성공적으로 번호표가 발급되었습니다. 잠시만 기다려주세요.', ephemeral =True)
        await ctx.send(f'번호표가 발급되었습니다.\n\n<@&1004688586093887528>\n{ctx.author.mention}님의 안내를 도와주세요')


@bot.slash_command(name = '내정보', description = '나의 정보를 확인 할 수 있어!')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
async def 내정보(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.respond("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, exp, money, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        expToUP = level*level + 6*level
        boxes = int(exp/expToUP*20)
        print("------------------------------\n")
        embed = discord.Embed(title="📋유저 정보", description = ctx.author.name, color = 0x62D0F6)
        embed.add_field(name = "🎟️레벨", value = level)
        embed.add_field(name = "🏆순위", value = str(rank) + "/" + str(userNum))
        embed.add_field(name = "✨XP: " + str(exp) + "/" + str(expToUP), value = boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline = False)
        embed.add_field(name = "💰보유 자산", value = money, inline = False)
        embed.add_field(name = "💸도박으로 날린 돈", value = loss, inline = False)

        await ctx.respond(embed=embed)

@bot.slash_command(name = '정보', description = '정보가 궁금한 사람이 있어?')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
async def 정보(ctx, 
환자:Option(discord.User,'원하는 환자를 태그해주세요')):
    userExistance, userRow = checkUser(환자.name, 환자.id)
    if not userExistance:
        print("DB에서 ", 환자.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.respond(환자.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        level, exp, money, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        print("------------------------------\n")
        embed = discord.Embed(title="🔎유저 정보", description = 환자.name, color = 0x62D0F6)
        embed.add_field(name = "🎟️레벨", value = level)
        embed.add_field(name = "✨경험치", value = str(exp) + "/" + str(level*level + 6*level))
        embed.add_field(name = "🏆순위", value = str(rank) + "/" + str(userNum))
        embed.add_field(name = "💰보유 자산", value = money, inline = False)
        embed.add_field(name = "💸도박으로 날린 돈", value = loss, inline = False)

        await ctx.respond(embed=embed)

@bot.slash_command(name = '송금', description = '누구한테 돈을 보낼래?')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
async def 송금(ctx, 
받는이:Option(discord.User,'누구한테 송금하실 건가요?'),
금액:Option(int,'얼마를 송금하시겠습니까?',min_value=10000)):

    print("송금이 가능한지 확인합니다.")
    senderExistance, senderRow = checkUser(ctx.author.name, ctx.author.id)
    receiverExistance, receiverRow = checkUser(받는이.name, 받는이.id)

    if not senderExistance:
        print("DB에서", ctx.author.name, "을 찾을수 없습니다")
        print("------------------------------\n")
        await ctx.respond("회원가입 후 송금이 가능합니다.", ephemeral =True)
    elif not receiverExistance:
        print("DB에서 ", 받는이.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.respond(받는이.name  + " 은(는) 등록되지 않은 사용자입니다.", ephemeral =True)
    else:
        print("송금하려는 돈: ", 금액)

        s_money = getMoney(ctx.author.name, senderRow)
        r_money = getMoney(받는이.name, receiverRow)

        if s_money >= int(금액) and int(금액) != 0:
            print("돈이 충분하므로 송금을 진행합니다.")
            print("")

            remit(ctx.author.name, senderRow, 받는이.name, receiverRow, 금액)

            print("송금이 완료되었습니다. 결과를 전송합니다.")

            embed = discord.Embed(title="송금 완료📨", description = f'송금된 돈: {금액}', color = 0x77ff00)
            embed.add_field(name = "보낸 사람: " + ctx.author.name, value = "현재 자산: " + str(getMoney(ctx.author.name, senderRow)))
            embed.add_field(name = "→", value = ":moneybag:")
            embed.add_field(name="받은 사람: " + 받는이.name, value="현재 자산: " + str(getMoney(받는이.name, receiverRow)))
                    
            await ctx.respond(embed=embed, ephemeral =True)
        elif int(금액) == 0:
            await ctx.respond("0원을 보낼 필요는 없죠", ephemeral =True)
        else:
            print("돈이 충분하지 않습니다.")
            print("송금하려는 돈: ", 금액)
            print("현재 자산: ", s_money)
            await ctx.respond("돈이 충분하지 않습니다. 현재 자산: " + str(s_money), ephemeral =True)

        print("------------------------------\n")

@bot.slash_command(name = '환전', description = '미무포인트로 환전하고 싶어?')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
async def 환전(ctx, 
환전금액:Option(int,'금액을 입력해주세요',min_value=10000)):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        cur_money = getMoney(ctx.author.name, userRow)
        if int(cur_money) >= 100000:
            await ctx.respond(f"<@&998046067964776578>\n\n{ctx.author.mention}님이 {환전금액}만큼의 환전을 요청하셨습니다!")
        else:
            await ctx.respond(f"{ctx.author.mention}님의 잔고가 부족하여 환전요청에 실패하였습니다.\n\n현재 잔고 {str(cur_money)}", ephemeral =True)
    else:
        await ctx.respond("회원정보가 등록되어있지않습니다", ephemeral =True)

@bot.slash_command(name = '용돈', description = '용돈받고싶은사람~')
@commands.has_any_role(1004771045091323944, 1004685377682026516)
@commands.cooldown(1, 3600, commands.BucketType.user)
async def 용돈(ctx):
    rmm = [10, 30, 50, 70, 100, 300, 500, 700, 1000, 1500, 2000, 2500, 3500, 5000, 7500, 10000, 50000, 100000]
    rm = np.random.choice(rmm, 1, replace=False, p=[0.01, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.125, 0.1, 0.08, 0.07, 0.05, 0.02, 0.01, 0.005, 0.003, 0.0015, 0.0005])
    user, row = checkUser(ctx.author.name, ctx.author.id)
    await ctx.respond(f'{ctx.author.mention}님에게 성공적으로 {rm}원을 지급하였습니다.\n\n다음 사용 가능시간까지 1시간 남았습니다')
    addMoney(row, int(rm))
    print("MONEY add Success")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        userExistance, userRow = checkUser(message.author.name, message.author.id)
        channel = bot.get_channel(1005349277947670528)
        if userExistance:
            levelUp, lvl = levelupCheck(userRow)
            if levelUp:
                print(message.author, "가 레벨업 했습니다")
                print("")
                embed = discord.Embed(title = "🧪약물치료🧪", description = "", color = 0x00A260)
                embed.set_footer(text = message.author.name + " 님이 약물치료 " + str(lvl) + "회를 받으셨습니다")
                await channel.send(embed=embed)
            else:
                modifyExp(userRow, 1)
                addMoney(userRow, int(10))
                print("------------------------------\n")


@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.respond("명령어를 찾지 못했습니다", ephemeral =True)
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.respond("명령어를 사용하기에 권한이 부족합니다", ephemeral =True)    
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f"아직 명령어를 사용할 수 없습니다. {int(error.retry_after)}초 후에 다시 시도하세요", ephemeral =True)
    else:
        raise error
        
################<관리자>################
@bot.slash_command(name = '서하', description = '서하 전용')
@commands.has_any_role(998046067964776578)
async def 서하(ctx):
    embed = discord.Embed(title = "서하봇", description = "V2", color = 0x6E17E3) 
    embed.add_field(name = "========================", value = "관리자 전용 커맨드", inline = False)
    embed.add_field(name = "🧧지급 [대상] [돈]", value = "멘션한 [대상]에게 [돈]을 지급합니다", inline = False)
    embed.add_field(name = "✨경험치 [대상] [경험치]", value = "멘션한 [대상]에게 [경험치]을 지급합니다", inline = False)
    embed.add_field(name = "🎟️레벨 [대상] [레벨]", value = "멘션한 [대상]에게 [레벨]을 지급합니다", inline = False)
    embed.add_field(name = "💸차감 [대상] [돈]", value = "멘션한 [대상]에게서 [돈]을 차감합니다", inline = False)
    embed.set_footer(text="주인장")
    await ctx.respond(embed=embed)

@bot.slash_command(name = '원무과', description = '원무과 전용 도움말')
@commands.has_any_role(1004771045091323944)
async def 원무과(ctx):
    embed = discord.Embed(title = "원무과 전용 커맨드", description = "이거 쓰느라 머리아파요", color = 0x6E17E3) 
    embed.add_field(name = "========================", value = "원무과 전용 커맨드", inline = False)
    embed.add_field(name = "📢a", value = "원무과 전용 | 병동에 [대상] ~ [대상3]을 멘션하여 환영멘트를 보냅니다", inline = False)
    embed.add_field(name = "📣b", value = "원무과 전용 | 안내기록 작성", inline = False)
    embed.add_field(name = "🆘c", value = "원무과 전용 | 안내중 문제 발생시 보안팀 호출", inline = False)
    embed.set_footer(text="주인장")
    await ctx.respond(embed=embed)

@bot.slash_command(name = '간호사', description = '간호사 전용 도움말')
@commands.has_any_role(1004771045091323944)
async def 간호사(ctx):
    embed = discord.Embed(title = "간호사 전용 커맨드", description = "이거 쓰느라 머리아파요", color = 0x6E17E3) 
    embed.add_field(name = "========================", value = "간호사 전용 커맨드", inline = False)
    embed.add_field(name = "📢f [대상]", value = "간호사 전용 | 병동에 [대상] ~ [대상3]을 멘션하여 환영멘트를 보냅니다", inline = False)
    embed.set_footer(text="주인장")
    await ctx.respond(embed=embed)

@bot.slash_command(name = '보안팀', description = '보안팀 전용 도움말')
@commands.has_any_role(1004771045091323944)
async def 보안팀(ctx):
    embed = discord.Embed(title = "보안팀 전용 커맨드", description = "이거 쓰느라 머리아파요", color = 0x6E17E3) 
    embed.add_field(name = "========================", value = "보안팀 전용 커맨드", inline = False)
    embed.add_field(name = "🚫k", value = "보안팀 전용 | 중환자실에 [대상]을 멘션하여 주의, 경고, 차단을 지급합니다", inline = False)
    embed.set_footer(text="주인장")
    await ctx.respond(embed=embed)

@bot.slash_command(name = '정신과', description = '정신과 전용 도움말')
@commands.has_any_role(1004771045091323944)
async def 정신과(ctx):
    embed = discord.Embed(title = "정신과 전용 커맨드", description = "이거 쓰느라 머리아파요", color = 0x6E17E3) 
    embed.add_field(name = "========================", value = "정신과 전용 커맨드", inline = False)
    embed.add_field(name = "🆘p", value = "정신과 전용 | 상담중 문제 발생시 보안팀 호출", inline = False)
    embed.set_footer(text="주인장")
    await ctx.respond(embed=embed)

@bot.slash_command(name = '영상과', description = '영상과 전용 도움말')
@commands.has_any_role(1004771045091323944)
async def 영상과(ctx):
    embed = discord.Embed(title = "영상과 전용 커맨드", description = "이거 쓰느라 머리아파요", color = 0x6E17E3) 
    embed.add_field(name = "========================", value = "영상과 전용 커맨드", inline = False)
    embed.add_field(name = "🎉r [대상] [담당자]", value = "영상과 전용 | 생일 축하 메세지를 올려!", inline = False)
    embed.set_footer(text="주인장")
    await ctx.respond(embed=embed)

@bot.slash_command(name = '외과', description = '외과 전용 도움말')
@commands.has_any_role(1004771045091323944)
async def 외과(ctx):
    embed = discord.Embed(title = "외과 전용 커맨드", description = "이거 쓰느라 머리아파요", color = 0x6E17E3) 
    embed.add_field(name = "========================", value = "외과 전용 커맨드", inline = False)
    embed.add_field(name = "🔔u [대상] [담당자]", value = "외과 전용 | 에블핑과 [대상] [담당자]을 언급한다", inline = False)
    embed.set_footer(text="주인장")
    await ctx.respond(embed=embed)
    
    
################<원무과>################
@bot.slash_command(name = 'a', description = '환영멘트를 올려보자!')
@commands.has_any_role(1004688586093887528, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def a(ctx, 
환자:Option(discord.User,'멘션할 환자를 태그해주세요'),
환자1:Option(discord.User,'멘션할 환자를 태그해주세요', required=False),
환자2:Option(discord.User,'멘션할 환자를 태그해주세요', required=False),
환자3:Option(discord.User,'멘션할 환자를 태그해주세요', required=False)):
    channel = bot.get_channel(1004742567759466536)
    if 환자1:
        if 환자2:
            if 환자3:
                await channel.send(f'<@&1005458692470222900>\n<a:sehan_4028:1008051922974023741> 저희 병원에 새로오신 환자분을 환영해주세요! :tada:\n\n<a:sehan_4019:1008051896906432582> {환자.mention}, {환자1.mention}, {환자2.mention}, {환자3.mention}님! 저희 서버에 오신걸 환영해요!\n\n<a:sehan_4019:1008051896906432582> 서버 적응이 어려우시다면 간호사를 불러주세요! :person_raising_hand:\n\n<a:sehan_4019:1008051896906432582> 문의 하실게있으시다면 <#1005166621914058782>에 편하게 문의해주세요!  :envelope_with_arrow:\n\n<a:sehan_4019:1008051896906432582> 공지는 <#1022459113105530953>에서 확인해주세요! :loudspeaker:')
                await ctx.respond(f'성공적으로 {환자.mention}, {환자1.mention}, {환자2.mention}, {환자3.mention}님을 멘션하여 환영멘트를 전송하였습니다 | 작성자 : {ctx.author.mention}')
            else:
                await channel.send(f'<@&1005458692470222900>\n<a:sehan_4028:1008051922974023741> 저희 병원에 새로오신 환자분을 환영해주세요! :tada:\n\n<a:sehan_4019:1008051896906432582> {환자.mention}, {환자1.mention}, {환자2.mention}님! 저희 서버에 오신걸 환영해요!\n\n<a:sehan_4019:1008051896906432582> 서버 적응이 어려우시다면 간호사를 불러주세요! :person_raising_hand:\n\n<a:sehan_4019:1008051896906432582> 문의 하실게있으시다면 <#1005166621914058782>에 편하게 문의해주세요!  :envelope_with_arrow:\n\n<a:sehan_4019:1008051896906432582> 공지는 <#1022459113105530953>에서 확인해주세요! :loudspeaker:')
                await ctx.respond(f'성공적으로 {환자.mention}, {환자1.mention}, {환자2.mention}님을 멘션하여 환영멘트를 전송하였습니다 | 작성자 : {ctx.author.mention}')
        else:
            await channel.send(f'<@&1005458692470222900>\n<a:sehan_4028:1008051922974023741> 저희 병원에 새로오신 환자분을 환영해주세요! :tada:\n\n<a:sehan_4019:1008051896906432582> {환자.mention}, {환자1.mention}님! 저희 서버에 오신걸 환영해요!\n\n<a:sehan_4019:1008051896906432582> 서버 적응이 어려우시다면 간호사를 불러주세요! :person_raising_hand:\n\n<a:sehan_4019:1008051896906432582> 문의 하실게있으시다면 <#1005166621914058782>에 편하게 문의해주세요!  :envelope_with_arrow:\n\n<a:sehan_4019:1008051896906432582> 공지는 <#1022459113105530953>에서 확인해주세요! :loudspeaker:')
            await ctx.respond(f'성공적으로 {환자.mention}, {환자1.mention}님을 멘션하여 환영멘트를 전송하였습니다 | 작성자 : {ctx.author.mention}')
    else:
        await channel.send(f'<@&1005458692470222900>\n<a:sehan_4028:1008051922974023741> 저희 병원에 새로오신 환자분을 환영해주세요! :tada:\n\n<a:sehan_4019:1008051896906432582> {환자.mention}님! 저희 서버에 오신걸 환영해요!\n\n<a:sehan_4019:1008051896906432582> 서버 적응이 어려우시다면 간호사를 불러주세요! :person_raising_hand:\n\n<a:sehan_4019:1008051896906432582> 문의 하실게있으시다면 <#1005166621914058782>에 편하게 문의해주세요!  :envelope_with_arrow:\n\n<a:sehan_4019:1008051896906432582> 공지는 <#1022459113105530953>에서 확인해주세요! :loudspeaker:')
        await ctx.respond(f'성공적으로 {환자.mention}님을 멘션하여 환영멘트를 전송하였습니다 | 작성자 : {ctx.author.mention}')

@bot.slash_command(name = 'b', description = '안내 기록을 남겨!')
@commands.has_any_role(1004688586093887528, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def b(ctx, 
이름:Option(discord.User,'환자의 이름을 적어주세요!'),
나이:Option(int,'나이를 적어주세요!(주민등록상의 세는나이 기준)', min_value=12),
공개여부:Option(str,'공개여부를 선택해주세요!', choices=['공개','비공']),
성별:Option(str,'성별을 선택해주세요!', choices=['남성','여성']),
경로:Option(str,'저희 서버에는 어떻게 들어오시게 되었나요?', choices=['디스보드','디코올','디스니티','초대','연합링크']),
초대자:Option(discord.User,'누가 초대하였나요?', required=False),
서버명:Option(discord.TextChannel,'어느서버를 통해 오시게 되었나요?', required=False)):
    channel = bot.get_channel(1026861536020533349)
    if 경로 == '초대':
        await channel.send(f'{date_form} {이름.mention} {나이} {공개여부} {성별} {경로} {초대자.mention} | 안내자 : {ctx.author.mention}')
        await ctx.respond(f'성공적으로 기록하였습니다.', ephemeral =True)
    elif 경로 == '연합링크':
        await channel.send(f'{date_form} {이름.mention} {나이} {공개여부} {성별} {경로} {서버명.mention} | 안내자 : {ctx.author.mention}')
        await ctx.respond(f'성공적으로 기록하였습니다.', ephemeral =True)
    else:
        await channel.send(f'{date_form} {이름.mention} {나이} {공개여부} {성별} {경로} | 안내자 : {ctx.author.mention}')
        await ctx.respond(f'성공적으로 기록하였습니다.', ephemeral =True)

@bot.slash_command(name = 'c', description = '안내중 문제가 발생한다면?')
@commands.has_any_role(1004688586093887528, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def c(ctx):
    channel = bot.get_channel(1005089714266701925)

    embed = discord.Embed(title="⚠️코드블루⚠️", description = "📢<@&1004688586093887528>에서 알립니다.\n\n안내 중 문제가 발생 하였으니 보안팀은 신속히 출동 부탁드립니다.", color = 0x24008D)
    embed.add_field(name = "호출" ,value = "<@&1004688567613784175> <@&1004688539914608640> <@&998046067964776578> <@&1004689605305585704>")

    await channel.send(embed=embed)
    await channel.send("<@&1004688567613784175> <@&1004688539914608640> <@&998046067964776578> <@&1004689605305585704>")
    await ctx.respond('성공적으로 코드를 발송하였습니다', ephemeral =True)

################<간호사>################
@bot.slash_command(name = 'f', description = '환영멘트를 올려보자!')
@commands.has_any_role(1004688954089537667, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def f(ctx, 
환자:Option(discord.User,'멘션할 환자를 태그해주세요'),
환자1:Option(discord.User,'멘션할 환자를 태그해주세요', required=False),
환자2:Option(discord.User,'멘션할 환자를 태그해주세요', required=False),
환자3:Option(discord.User,'멘션할 환자를 태그해주세요', required=False)):
    channel = bot.get_channel(1004742567759466536)
    if 환자1:
        if 환자2:
            if 환자3:
                await channel.send(f'------৹⟦ {환자.mention} {환자1.mention} {환자2.mention} {환자3.mention}님 어서오세요! ⟧৹------\n\n🌹 ⟦저희 세한 병원에 오신것을 진심으로 환영합니다!⟧\n\n🌹 ⟦저는 여러분의 담당 간호사 {ctx.author.mention}입니다!⟧\n\n🌹 ⟦세한 병원에서의 적응이 어려우시다면 <@&1004688954089537667> 혹은 저를 멘션해주세요!⟧\n\n🌹 ⟦남들에게 말 못할 고민이나 서버내에서의 고민이 있으시다면 <@&1004688920694501406>에서 상담을 도와드려요!⟧\n\n🌹 ⟦편안한 병원 생활 되시길 바랍니다!⟧ ')
                await ctx.respond(f'성공적으로 {환자.mention}, {환자1.mention}, {환자2.mention}, {환자3.mention}님을 멘션하여 환영멘트를 전송하였습니다 | 작성자 : {ctx.author.mention}')
            else:
                await channel.send(f'------৹⟦ {환자.mention} {환자1.mention} {환자2.mention}님 어서오세요! ⟧৹------\n\n🌹 ⟦저희 세한 병원에 오신것을 진심으로 환영합니다!⟧\n\n🌹 ⟦저는 여러분의 담당 간호사 {ctx.author.mention}입니다!⟧\n\n🌹 ⟦세한 병원에서의 적응이 어려우시다면 <@&1004688954089537667> 혹은 저를 멘션해주세요!⟧\n\n🌹 ⟦남들에게 말 못할 고민이나 서버내에서의 고민이 있으시다면 <@&1004688920694501406>에서 상담을 도와드려요!⟧\n\n🌹 ⟦편안한 병원 생활 되시길 바랍니다!⟧ ')
                await ctx.respond(f'성공적으로 {환자.mention}, {환자1.mention}, {환자2.mention}님을 멘션하여 환영멘트를 전송하였습니다 | 작성자 : {ctx.author.mention}')
        else:
            await channel.send(f'------৹⟦ {환자.mention} {환자1.mention}님 어서오세요! ⟧৹------\n\n🌹 ⟦저희 세한 병원에 오신것을 진심으로 환영합니다!⟧\n\n🌹 ⟦저는 여러분의 담당 간호사 {ctx.author.mention}입니다!⟧\n\n🌹 ⟦세한 병원에서의 적응이 어려우시다면 <@&1004688954089537667> 혹은 저를 멘션해주세요!⟧\n\n🌹 ⟦남들에게 말 못할 고민이나 서버내에서의 고민이 있으시다면 <@&1004688920694501406>에서 상담을 도와드려요!⟧\n\n🌹 ⟦편안한 병원 생활 되시길 바랍니다!⟧ ')
            await ctx.respond(f'성공적으로 {환자.mention}, {환자1.mention}님을 멘션하여 환영멘트를 전송하였습니다 | 작성자 : {ctx.author.mention}')
    else:
        await channel.send(f'------৹⟦ {환자.mention}님 어서오세요! ⟧৹------\n\n🌹 ⟦저희 세한 병원에 오신것을 진심으로 환영합니다!⟧\n\n🌹 ⟦저는 {환자.mention}님의 담당 간호사 {ctx.author.mention}입니다!⟧\n\n🌹 ⟦세한 병원에서의 적응이 어려우시다면 <@&1004688954089537667> 혹은 저를 멘션해주세요!⟧\n\n🌹 ⟦남들에게 말 못할 고민이나 서버내에서의 고민이 있으시다면 <@&1004688920694501406>에서 상담을 도와드려요!⟧\n\n🌹 ⟦편안한 병원 생활 되시길 바랍니다!⟧ ')
        await ctx.respond(f'성공적으로 {환자.mention}님을 멘션하여 환영멘트를 전송하였습니다 | 작성자 : {ctx.author.mention}')

################<보안팀>################
@bot.slash_command(name = 'k', description = '환자에게 경고를 줘!')
@commands.has_any_role(1004688567613784175, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def k(ctx, 
환자:Option(discord.User,'주의를 줄 환자를 태그해줘!'),
종류:Option(str,'지급하려는 종류를 선택해줘!',choices=['주의','경고','차단']),
횟수:Option(str,'경고 횟수를 선택해줘!',choices=['1','2','3'], required=False),
사유:Option(str,'지급 하는 사유를 적어줘!', required=False),
규칙번호:Option(str,'해당하는 규칙 번호를 적어줘! e.g.)1-1', required=False)):
    if 종류 == '주의':
        channel = bot.get_channel(1004748420898103326)
        if 사유:
            await channel.send(f'{환자.mention}||({환자.id})|| 주의 {횟수}회 지급되었습니다.\n사유 : {사유}')
            await ctx.respond(f'성공적으로 {환자}에게 주의를 지급하였습니다', ephemeral =True)
        else:
            await channel.send(f'{환자.mention}||({환자.id})|| 주의 {횟수}회 지급되었습니다.\n사유 : <#1005092364118925383> {규칙번호} 을 참고해주세요!')
            await ctx.respond(f'성공적으로 {환자}에게 주의를 지급하였습니다', ephemeral =True)
    elif 종류 == '경고':
        channel = bot.get_channel(1004748420898103326)
        if 사유:
            await channel.send(f'{환자.mention}||({환자.id})|| 경고 {횟수}회 지급되었습니다.\n사유 : {사유}')
            await ctx.respond(f'성공적으로 {환자}에게 경고를 지급하였습니다', ephemeral =True)
        else:
            await channel.send(f'{환자.mention}||({환자.id})|| 경고 {횟수}회 지급되었습니다.\n사유 : <#1005092364118925383> {규칙번호} 을 참고해주세요!')
            await ctx.respond(f'성공적으로 {환자}에게 경고를 지급하였습니다', ephemeral =True)
    elif 종류 == '차단':
        channel = bot.get_channel(1004748585629388913)
        if 사유:
            await channel.send(f'{환자.mention}||({환자.id})|| 차단되었습니다.\n사유 : {사유}')
            await ctx.respond(f'성공적으로 {환자}를 차단하였습니다', ephemeral =True)
        else:
            await channel.send(f'{환자.mention}||({환자.id})|| 차단되었습니다.\n사유 : <#1005092364118925383> {규칙번호} 을 참고해주세요!')
            await ctx.respond(f'성공적으로 {환자}를 차단하였습니다', ephemeral =True)

################<정신과>################    
@bot.slash_command(name = 'p', description = '상담 중 문제가 발생한다면?')
@commands.has_any_role(1004688920694501406, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def p(ctx):
    channel = bot.get_channel(1005089714266701925)

    embed = discord.Embed(title="⚠️코드레드⚠️", description = "📢<@&1004688920694501406>에서 알립니다.\n\n상담 중 문제가 발생 하였으니 보안팀은 신속히 출동 부탁드립니다.", color = 0xA70800)
    embed.add_field(name = "호출" ,value = "<@&1004688567613784175> <@&1004688539914608640> <@&998046067964776578> <@&1004689605305585704>")

    await channel.send(embed=embed)
    await channel.send("<@&1004688567613784175> <@&1004688539914608640> <@&998046067964776578> <@&1004689605305585704>")
    await ctx.respond('성공적으로 코드를 발송하였습니다', ephemeral =True)

################<영상과>################
@bot.slash_command(name = 'r', description = '담당자를 올려보자!')
@commands.has_any_role(998527437237387334, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def r(ctx, 
문의:Option(discord.User,'상대 서버의 담당장를 태그해!'),
담당자:Option(discord.User,'우리 서버의 담당자를 태그해!')):
    await ctx.respond('성공적으로 멘트가 발송되었습니다.', ephemeral =True)
    await ctx.send(f'||<@&997116215224975440>||\n\n문의 : {문의.mention}\n\n담당자 : {담당자.mention}')

################<외과>################
@bot.slash_command(name = 'u', description = '생일자를 올려보자!')
@commands.has_any_role(1004688899475509279, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def u(ctx, 
생일자:Option(discord.User,'생일자를 태그해!'),
하고싶은말:Option(str,'생일자에게 하고싶은말은 뭐야?')):
    await ctx.respond('성공적으로 생일멘트가 발송되었습니다.', ephemeral =True)
    await ctx.send(f'🎉𝗛𝗮𝗽𝗽𝘆 𝗕𝗶𝗿𝘁𝗵𝗱𝗮𝘆🎉\n\n🎉오늘은 {today.month}월 {today.day}일, {생일자.mention}님의 생일을 진심으로 축하드립니다!\n\n🎉모두 축하해 주시길 바랍니다!!\n\n🎉{하고싶은말}\n\n||<@&1004685377682026516> <@&1004771045091323944>||')

################<서하전용>################
@bot.slash_command(name = 'z', description = '원무과와 간호과의 환영멘트를 동시에!')
@commands.has_any_role(998046067964776578)
async def 환영(ctx,
환자:Option(discord.User,'환자의 태그를 입력해주세요')):
    channel = bot.get_channel(1004742567759466536)
    await channel.send(f'<@&1005458692470222900>\n<a:sehan_4028:1008051922974023741> 저희 병원에 새로오신 환자분을 환영해주세요! :tada:\n\n<a:sehan_4019:1008051896906432582> {환자.mention}님! 저희 서버에 오신걸 환영해요!\n\n<a:sehan_4019:1008051896906432582> 서버 적응이 어려우시다면 간호사를 불러주세요! :person_raising_hand:\n\n<a:sehan_4019:1008051896906432582> 문의 하실게있으시다면 <#1005166621914058782>에 편하게 문의해주세요!  :envelope_with_arrow:\n\n<a:sehan_4019:1008051896906432582> 공지는 <#1022459113105530953>에서 확인해주세요! :loudspeaker:')
    await channel.send(f'------৹⟦ {환자.mention}님 어서오세요! ⟧৹------\n\n🌹 ⟦저희 세한 병원에 오신것을 진심으로 환영합니다!⟧\n\n🌹 ⟦저는 {환자.mention}님의 담당 간호사 {ctx.author.mention}입니다!⟧\n\n🌹 ⟦세한 병원에서의 적응이 어려우시다면 <@&1004688954089537667> 혹은 저를 멘션해주세요!⟧\n\n🌹 ⟦남들에게 말 못할 고민이나 서버내에서의 고민이 있으시다면 <@&1004688920694501406>에서 상담을 도와드려요!⟧\n\n🌹 ⟦편안한 병원 생활 되시길 바랍니다!⟧ ')
    await ctx.respond(f'성공적으로 {환자}님을 멘션하여 환영멘트를 전송하였습니다.')

@bot.slash_command(name = '등록', description = '강제로 회원등록!')
@commands.has_any_role(998046067964776578)
async def 등록(ctx, 
환자:Option(discord.User,'환자의 태그를 입력해주세요')):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(환자.name, 환자.id)
    if userExistance:
        print("DB에서 ", 환자.name, "을 찾았습니다.")
        print("------------------------------\n")
        await ctx.respond("이미 등록하셨습니다.")
    else:
        print("DB에서 ", 환자.name, "을 찾을 수 없습니다")
        print("")

        Signup(환자.name, 환자.id)

        print("회원가입이 완료되었습니다.")
        print("------------------------------\n")
        await ctx.respond(f'{환자.mention}님의 추가 등록이 완료되었습니다. 즐거운 병원생활하세요.')

@bot.slash_command(name = '탈퇴', description = '강제로 회원을 탈퇴 시킵니다.')
@commands.has_any_role(998046067964776578)
async def 탈퇴(ctx, 
환자:Option(discord.User,'환자의 태그를 입력해주세요')):
    print("탈퇴가 가능한지 확인합니다.")
    userExistance, userRow = checkUser(환자.name, 환자.id)
    if userExistance:
        DeleteAccount(userRow)
        print("탈퇴가 완료되었습니다.")
        print("------------------------------\n")

        await ctx.respond("탈퇴가 완료되었습니다.", ephemeral =True)
    else:
        print("DB에서 ", 환자.name, "을 찾을 수 없습니다")
        print("------------------------------\n")

        await ctx.respond("등록되지 않은 사용자입니다.", ephemeral =True)

@bot.slash_command(name = '초기화', description = '회원정보 초기화')
@commands.has_any_role(998046067964776578)
async def 초기화(ctx):
    resetData()

@bot.slash_command(name = '지급', description = '돈을 주자!')
@commands.has_any_role(998046067964776578)
async def 지급(ctx, 
대상자:Option(discord.User,'누구한테 지급하실 건가요?'),
금액:Option(int,'얼마를 지급하시겠습니까?',min_value=1)):
    await ctx.respond(f'{대상자.mention}님에게 성공적으로 {금액}원을 지급하였습니다.', ephemeral =True)
    user, row = checkUser(대상자.name, 대상자.id)
    addMoney(row, int(금액))
    print("MONEY add Success")

@bot.slash_command(name = '경험치', description = '누구한테 경험치를 줘볼까?')
@commands.has_any_role(998046067964776578)
async def 경험치(ctx, 
대상자:Option(discord.User,'누구한테 지급하실 건가요?'),
경험치:Option(int,'얼마를 지급하시겠습니까?',min_value=1)):
    await ctx.respond(f'{대상자.mention}님에게 성공적으로 {경험치} 경험치를 지급하였습니다.', ephemeral =True)
    user, row = checkUser(대상자.name, 대상자.id)
    addExp(row, int(경험치))
    print("EXP add Success")

@bot.slash_command(name = '레벨', description = '레벨을 주고싶어?')
@commands.has_any_role(998046067964776578)
async def 레벨(ctx, 
대상자:Option(discord.User,'누구를 설정하실 건가요?'),
레벨:Option(int,'얼마로 설정하시겠습니까?',min_value=1)):
    await ctx.respond(f'{대상자.mention}님에게 성공적으로 {레벨} 레벨을 설정하였습니다.', ephemeral =True)
    user, row = checkUser(대상자.name, 대상자.id)
    adjustlvl(row, int(레벨))
    print("LEVEL add Success")

@bot.slash_command(name = '차감', description = '돈을 뺏자!')
@commands.has_any_role(998046067964776578)
async def 차감(ctx, 
대상자:Option(discord.User,'누구를 차감하실 건가요?'),
금액:Option(int,'얼마를 차감하시겠습니까?',min_value=1)):
    await ctx.respond(f'{대상자.mention}님의 자산을 성공적으로 {금액}원을 차감하였습니다.', ephemeral =True)
    user, row = checkUser(대상자.name, 대상자.id)
    modifyMoney(user, row, -int(금액))
    print("MONEY min Success")
     
@bot.slash_command(name = '점검', description = '점검 시간을 알리는거야!')
@commands.has_any_role(998046067964776578)
async def 점검(ctx, 
시작시각:Option(str,'시작 시각을 입력해주세요'),
종료시각:Option(str,'시작 시각을 입력해주세요'),
점검내용:Option(str,'점검 내용을 입력해주세요')):
    channel = bot.get_channel(1006571303211372544)
    channel1 = bot.get_channel(1005089714266701925)
    channel2 = bot.get_channel(1005029396874285116)

    embed = discord.Embed(title="🚧 점검 공지 🚧", description = " " ,color = 0xFFC300)
    embed.add_field(name = "일시 점검 안내", value = "서하봇의 점검이 진행 될 예정입니다.", inline = False)
    embed.add_field(name = "점검 시간", value = 시작시각 +" ~ "+ 종료시각+"까지", inline = False)
    embed.add_field(name = "점검 내용", value = 점검내용, inline = False)
    embed.add_field(name = "점검시 유의사항", value = "주사위, 도박, 정보 등 전체 기능 일시 마비", inline = False)
    
    embed1 = discord.Embed(title="🚧 점검 공지 🚧", description = " " ,color = 0xFFC300)
    embed1.add_field(name = "일시 점검 안내", value = "서하봇의 점검이 진행 될 예정입니다.", inline = False)
    embed1.add_field(name = "점검 시간", value = 시작시각 +" ~ "+ 종료시각+"까지", inline = False)
    embed1.add_field(name = "점검 내용", value = 점검내용, inline = False)
    embed1.add_field(name = "점검시 유의사항", value = "번호표, 환영멘트, 경고 등 전체 기능 일시 마비", inline = False)

    embed2 = discord.Embed(title="🚧 점검 공지 🚧", description = " " ,color = 0xFFC300)
    embed2.add_field(name = "일시 점검 안내", value = "서하봇의 점검이 진행 될 예정입니다.", inline = False)
    embed2.add_field(name = "점검 시간", value = 시작시각 +" ~ "+ 종료시각+"까지", inline = False)
    embed2.add_field(name = "점검 내용", value = 점검내용, inline = False)
    embed2.add_field(name = "점검시 유의사항", value = "번호표 기능 일시 마비 <@&1004688586093887528>를 멘션하여 안내를 받아주세요", inline = False)

    await channel.send(embed=embed)
    await channel1.send(embed=embed1)
    await channel1.send('<@&1004771045091323944>')
    await channel2.send(embed=embed2)
    await channel2.send('<@&1004739278720483418>')
    EX = await ctx.respond('성공적으로 전송되었습니다.', ephemeral = False)
    time.sleep(0.5)
    await EX.edit_original_message(content = "백업을 시작합니다.")
    print('백업 실행중...')
    time.sleep(0.5)
    ATBU()
    time.sleep(0.5)
    print('백업 완료!')
    await EX.edit_original_message(content = "백업이 완료 되었습니다!")
    time.sleep(0.5)
    await EX.edit_original_message(content = "안전종료 프로세스 가동")
    time.sleep(0.5)
    SE()

@bot.slash_command(name = '백업', description = '데이터 베이스 백업')
@commands.has_any_role(998046067964776578)
async def 백업(ctx):
    rm = await ctx.respond("백업 실행중...")
    print('백업 실행중...')
    time.sleep(0.5)
    ATBU()
    time.sleep(0.5)
    print('백업 완료!') 
    time.sleep(0.5)
    await rm.edit_original_message(content = "백업 완료!")

class Info_Button(discord.ui.View):
    @discord.ui.button(label="봇 안내", style=discord.ButtonStyle.primary)
    async def Bot_Info(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f"봇을 통하여 안내를 진행합니다! DM을 확인해주세요!", ephemeral =True)
        await interaction.user.send('안녕하세요! 서하봇 안내를 선택해주셔서 감사합니다!\n\n가장 먼저 작성하신 서류를 토대로 역할 지급 먼저 도와드리겠습니다!')
        

    @discord.ui.button(label="원무과 안내", style=discord.ButtonStyle.primary)
    async def Human_Info(self, button: discord.ui.Button, interaction: discord.Interaction):
        channel = bot.get_channel(1008004079743672432)
        rm = await interaction.response.send_message(f"원무과를 통하여 안내를 진행합니다! 잠시만 기다려주세요!", ephemeral =True)
        time.sleep(0.5)
        await rm.edit_original_message(content = "원무과 호출중...")
        time.sleep(0.5)
        await channel.send(f'번호표가 발급되었습니다.\n\n<@&1004688586093887528>\n{interaction.user.mention}님의 안내를 도와주세요')

class Exit_Button(discord.ui.View):
    @discord.ui.button(label="종료", style=discord.ButtonStyle.red)
    async def exit(self, button: discord.ui.Button, interaction: discord.Interaction):
        rm = await interaction.response.send_message(f"재시동 프로세스 실행", ephemeral =True)
        time.sleep(0.5)
        await rm.edit_original_message(content = "백업을 시작합니다.")
        print('백업 실행중...')
        time.sleep(0.5)
        shutil.copy('./userDB.xlsx', f'./BackUp/{dst_name}.xlsx')
        shutil.copy('./SHbot.py', f'./BackUp/{dstpy_name}.py')
        time.sleep(0.5)
        print('백업 완료!')
        await rm.edit_original_message(content = "백업이 완료되었습니다")
        time.sleep(0.5)
        await rm.edit_original_message(content = "안전종료 프로세스 가동중..")
        time.sleep(0.5)
        SE()

    @discord.ui.button(label="재시동", style=discord.ButtonStyle.primary)
    async def restart(self, button: discord.ui.Button, interaction: discord.Interaction):
        rm = await interaction.response.send_message(f"재시동 프로세스 실행", ephemeral =True)
        time.sleep(0.5)
        await rm.edit_original_message(content = "백업을 시작합니다.")
        print('백업 실행중...')
        time.sleep(0.5)
        shutil.copy('./userDB.xlsx', f'./BackUp/{dst_name}.xlsx')
        shutil.copy('./SHbot.py', f'./BackUp/{dstpy_name}.py')
        time.sleep(0.5)
        print('백업 완료!')
        await rm.edit_original_message(content = "백업이 완료되었습니다")
        time.sleep(0.5)
        await rm.edit_original_message(content = f"시스템 재시동 상태로 진입합니다...")
        print('시스템 재시동 상태로 진입합니다...')
        time.sleep(0.5)
        RS()

    @discord.ui.button(label="백업", style=discord.ButtonStyle.green)
    async def back(self, button: discord.ui.Button, interaction: discord.Interaction):
        rm = await interaction.response.send_message(f"백업을 시작합니다.", ephemeral =True)
        print('백업 실행중...')
        time.sleep(0.5)
        shutil.copy('./userDB.xlsx', f'./BackUp/{dst_name}.xlsx')
        shutil.copy('./SHbot.py', f'./BackUp/{dstpy_name}.py')
        time.sleep(0.5)
        print('백업 완료!') 
        await rm.edit_original_message(content = '백업완료!')

    @discord.ui.button(label="취소", style=discord.ButtonStyle.gray)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f"시스템 종료를 취소합니다.", ephemeral =True)


@bot.slash_command(name = '관리', description = '관리 옵션')
@commands.has_any_role(998046067964776578)
async def 관리(ctx):
    await ctx.respond("선택해주세요", view=Exit_Button(timeout=15), ephemeral =True)  

@bot.slash_command(name = '테스트', description = '번호표 테스트')
@commands.has_any_role(998046067964776578)
async def 테스트(ctx,
이름:Option(str,'저희 서버에서 사용하실 이름을 적어주세요!'),
나이:Option(int,'본인의 나이를 적어주세요!(주민등록상의 세는나이 기준)',min_value=12),
비공여부:Option(str,'성별을 선택해주세요!',choices=['공개','비공']),
성별:Option(str,'성별을 선택해주세요!',choices=['남성','여성']),
경로:Option(str,'저희 서버에는 어떻게 들어오시게 되었나요?')):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    channel = bot.get_channel(1005029973695922258)
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await channel.send(f'{ctx.author.mention}님의 입장 정보입니다\n\n닉네임 : {이름}\n나이 : {나이}\n비공 여부 : {비공여부}\n성별 : {성별}\n경로 : 재입장')
        await ctx.respond("재입장의 경우 안내 패스가 진행됩니다")
    else:
        if 나이 < 12:
            await ctx.respond('저희 서버는 2022년 기준 11년생 12살 부터 입장 가능합니다.')
        else:
            print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
            print("")

            Signup(ctx.author.name, ctx.author.id)

            print("회원가입이 완료되었습니다.")    
            print("------------------------------\n")
            await channel.send(f'{ctx.author.mention}님의 입장 정보입니다\n\n닉네임 : {이름}\n나이 : {나이}\n비공 여부 : {비공여부}\n성별 : {성별}\n경로 : {경로}')
            await ctx.respond("선택해주세요", view=Info_Button(timeout=15), ephemeral =True)

@bot.slash_command(name = '테스트2', description = '번호표 테스트2')
@commands.has_any_role(998046067964776578)
async def 테스트2(ctx,
이름:Option(str,'저희 서버에서 사용하실 이름을 적어주세요!'),
나이:Option(int,'본인의 나이를 적어주세요!(주민등록상의 세는나이 기준)',min_value=12),
비공여부:Option(str,'성별을 선택해주세요!',choices=['공개','비공']),
성별:Option(str,'성별을 선택해주세요!',choices=['남성','여성']),
경로:Option(str,'저희 서버에는 어떻게 들어오시게 되었나요?')):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    channel = bot.get_channel(1005029973695922258)
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await channel.send(f'{ctx.author.mention}님의 입장 정보입니다\n\n닉네임 : {이름}\n나이 : {나이}\n비공 여부 : {비공여부}\n성별 : {성별}\n경로 : 재입장')
        await ctx.respond("선택해주세요", view=Info_Button(timeout=15), ephemeral =True)
    else:
        if 나이 < 12:
            await ctx.respond('저희 서버는 2022년 기준 11년생 12살 부터 입장 가능합니다.')
        else:
            print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
            print("")

            Signup(ctx.author.name, ctx.author.id)

            print("회원가입이 완료되었습니다.")    
            print("------------------------------\n")
            await channel.send(f'{ctx.author.mention}님의 입장 정보입니다\n\n닉네임 : {이름}\n나이 : {나이}\n비공 여부 : {비공여부}\n성별 : {성별}\n경로 : {경로}')
            await ctx.respond("선택해주세요", view=Info_Button(timeout=15), ephemeral =True)

def SE():
    sys.exit("안전종료 프로세스 가동")

def RS():
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

threading.Timer(43200, RS).start()

bot.run(os.getenv('TOKEN_TK'))