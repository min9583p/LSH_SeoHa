#main.py
from game import *
from user import *
import asyncio, discord
from discord import Member
from discord.utils import get
from discord.ext import commands
import random
client = discord.Client()
bot = commands.Bot(command_prefix=["서하야 ", "a", "ㅅㅎ"])

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

@bot.command()
async def 뭐해(ctx):
    await ctx.send("계란후라이를 만드는 중이에요!")

@bot.command()
async def 눔라(ctx):
    await ctx.send("눔라...? 설마 눔하님을 말씀하시는건가요?")

@bot.command()
async def 이현(ctx):
    rmm = ["세살 이현이 나아? 아님 두살 이현이 나아?", "오전님 전담 일진 겸 셔틀", "이서하님과 말놓기로 하고 맨날 까먹는사람", "아기 이현", "심심한 이현", "노래만 부르는 이현"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 오전(ctx):
    rmm = ["아침?", "옆 학교에서 맨날 노래부르는 사람", "노래 잘부르는 눈나", "가수...?", "오전 오후!", "이현님의 친구", "이현님 전문 카운터"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 눔하(ctx):
    rmm = ["이서하님의 선배님..?", "맨날 자기방에서 안나오는 사람", "츤데레", "잘삐지는 누나", "발로란트 광팬", "눔하언니..?", "가장 바쁜사람", "옆 학교의 선도부 부장"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 나라(ctx):
    rmm = ["지나가던 옆학교 방송부원!", "어디서나 보이는 안내원", "악마...?", "뒤에선 착한데 앞에선 갈구는 사람", "옆학교에서 제일 먼저 친해진 사람", "항상 밝은 가면을 쓴 사람", "눔하님의 세컨드", "발로란트를 좋아하는 지나가는 사람"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 에그(ctx):
    rmm = ["계란후라이다!", "이 서버의 개설자 님이세요!", "계란찜..?", "계란빵 먹고싶당..", "에그타르트!", "언제나 싼가격의 계란과자!", "원무과장 에그스크램블!", "계란말이 계란말이 계란말이Yo!", "눔하님의 애착인형","계란국"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 오빠(ctx):
    await ctx.send("유하님이 세상에서 제일 완벽하고 듣기 좋은 소리라고 했어요!")

@bot.command()
async def 애교(ctx):
    rmm = ["나 띠드버거 사주세요! 띠드버거!", "우쥬 채강 귀요미 00쨩 등★쨩★ 00쨩의 채강★ 쨩★쨩★ 귀여븐 애교로★ \n온 우쥬를 지배하게쪄★ \n태양보다 밝은 서하쨩의 위풍★당당★얼굴!★ 서하쨩...귀여버...?★ 사랑스러워?★ 그러면...서하쨩이랑...뽀뽀하쟈...★뽑뽀!", "딸기우유~♥ 부농부농하구~♥ 달달하꾸우~♥ 이사나딴쏘두 마니마니있능~♥ 딸기우융 마시꾸우~♥ 쪼꼬우유 마시꾸우~♥\n우유라믄 다 주떼여!♥", "싯빵이에!\n나능.. 고미니이따!\n싯빵이에 누었는데~!\n너무 푹씨내셔 이러날 쑤가 업따...!\n오또카지...?", "슈크림빠앙~ 슈크림빠앙~ 새하얗고 달달한 슈크림빵! 너무너무 마시써요~ \n\n싯빵도 피료업쪄! 메론빵도 피료업쪄! 오직 슈크림 빵 알라뷰~❤️\n\n슈크림빵 평생 슈크림빵만 머꼬시퍼요! 새까만 쪼꼬우유도 가치 머그면 너무너무 마시써요~!\n\n새까만 쪼꼬우유와 새하얀 슈크림빵! 여러분 너무너무 마시써여!", "나빠또나빠또\n이따만큼 나빠또\n얼마만큼 나빠께?\n하늘만큼 땅만큼 나빠또\n그러니깐 사죄해 \n글구 나여기 다쳣또\n아파또아파또 아파또\n요기요기 아팠또\n얼마만큼 아파께?\n하늘만큼 땅만큼 아파또\n그러니깐 여기호해죠", "우웅~서하애교못하눈뎅ㅠㅠ이거누가시킨고야!!\n애교시킨사람미어미어!ㅠㅠ구래도해야징!!히힛~\n1도하기1은기여미☞^.^☜\n2도하기2는기여미p(>3<;)q\n3도하기3도기여미~~p(^0^)q\n어떼영? 서하기여워용?귀여우면 뽑뽀~:hearts:♡"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 무드(ctx):
    rmm = ["무드등~", "탈무드!", "옆 학교의 선도부원 무드님이세요!", "무드 무 무 무드 무드등~", "묻으등", "태권소녀 무드"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 판다(ctx):
    rmm = ["귀여운 판다!", "지존 다크써클", "죽순 드실래영?", "눈에 멍든 판다~!", "아기 판다", "이서하님과 말을 놓기로 하였는데 이서하님이 존댓말을 쓰고 있는사람이에요!"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 연희(ctx):
    rmm = ["연희님 연희님!", "연희님 프사 도아가에여?", "연희님 프사 기상술사에여?", "연희님 연희님 마이크안대여?", "연희님 로아하세여?", "이서하님이 프사에 집착하는 사람이다."]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 서하(ctx):
    rmm = ["제 주인님이요?", "이 서버의 개설자에요!", "아 그 에그님만 놀리는 사람?", "'무드등~의 창시자로 알고있어요'", "집착광공!", "에그님의 전담 카운터", "제게 다양한 지식을 알려주신 분이에요!", "저를 부르신건가요? 아님..?", "이서하님이 만드신 지정 답변 봇 서하에요!", "저는 사실 서하님이 심심해서 만들어졌답니다!", "제 원래 목적은 서하님의 말동무에요!", "에그가 찜함", f"저는 {ctx.message.author.mention}님의 충실한 봇 서하봇이에요!"]
    rm = random.choice(rmm)
    await ctx.send(rm)

@bot.command()
async def 도움(ctx):
    embed = discord.Embed(title = "서하봇", description = "1세대 봇", color = 0x6E17E3) 
    embed.add_field(name = "❓도움", value = "도움말을 봅니다", inline = False)
    embed.add_field(name = "🎲주사위", value = "주사위를 굴려 봇과 대결합니다", inline = False)
    embed.add_field(name = "🪪회원가입", value = "각종 컨텐츠를 즐기기 위한 회원가입을 합니다", inline = False)
    embed.add_field(name = "📋내정보", value = "자신의 정보를 확인합니다", inline = False)
    embed.add_field(name = "🔎정보 [대상]", value = "멘션한 [대상]의 정보를 확인합니다", inline = False)
    embed.add_field(name = "📨송금 [대상] [돈]", value = "멘션한 [대상]에게 [돈]을 보냅니다", inline = False)
    embed.add_field(name = "🎰도박 [돈]", value = "[돈]을 걸어 도박을 합니다. 올인도 가능합니다", inline = False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role(1004689605305585704, 998046067964776578)
async def 고급(ctx):
    embed = discord.Embed(title = "서하봇", description = "1세대 봇", color = 0x6E17E3) 
    embed.add_field(name = "❓도움", value = "도움말을 봅니다", inline = False)
    embed.add_field(name = "🎲주사위", value = "주사위를 굴려 봇과 대결합니다", inline = False)
    embed.add_field(name = "🪪회원가입", value = "각종 컨텐츠를 즐기기 위한 회원가입을 합니다", inline = False)
    embed.add_field(name = "📋내정보", value = "자신의 정보를 확인합니다", inline = False)
    embed.add_field(name = "🔎정보 [대상]", value = "멘션한 [대상]의 정보를 확인합니다", inline = False)
    embed.add_field(name = "📨송금 [대상] [돈]", value = "멘션한 [대상]에게 [돈]을 보냅니다", inline = False)
    embed.add_field(name = "🎰도박 [돈]", value = "[돈]을 걸어 도박을 합니다. 올인도 가능합니다", inline = False)
    embed.add_field(name = "========================", value = "관리자 전용 커맨드", inline = False)
    embed.add_field(name = "🧧지급 [대상] [돈]", value = "멘션한 [대상]에게 [돈]을 지급합니다", inline = False)
    embed.add_field(name = "✨경험치 [대상] [경험치]", value = "멘션한 [대상]에게 [경험치]을 지급합니다", inline = False)
    embed.add_field(name = "🎟️레벨 [대상] [레벨]", value = "멘션한 [대상]에게 [레벨]을 지급합니다", inline = False)
    embed.add_field(name = "💸차감 [대상] [돈]", value = "멘션한 [대상]에게서 [돈]을 차감합니다", inline = False)
    embed.set_footer(text="주인장")
    channel = bot.get_channel(997116215942193244)
    await channel.send(embed=embed)

@bot.command()
async def 주사위(ctx):
    result, _color, bot1, bot2, user1, user2, a, b = dice()

    embed = discord.Embed(title = "주사위 게임 결과", description = "\n", color = _color)
    embed.add_field(name = "서하봇의 숫자 " + bot1 + "+" + bot2, value = ":game_die: " + a, inline = False)
    embed.add_field(name = ctx.author.name+"의 숫자 " + user1 + "+" + user2, value = ":game_die: " + b, inline = False)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.command()
async def 도박(ctx, money):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    win = gamble()
    result = ""
    betting = 0
    _color = 0x000000
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        cur_money = getMoney(ctx.author.name, userRow)

        if money == "올인":
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

            embed = discord.Embed(title = "🎰도박 결과", description = result, color = _color)
            embed.add_field(name = "🪙배팅금액", value = betting, inline = False)
            embed.add_field(name = "💰현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)

            await ctx.send(embed=embed)
            
        elif int(money) >= 10:
            if cur_money >= int(money):
                betting = int(money)
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

                embed = discord.Embed(title = "🎰도박 결과", description = result, color = _color)
                embed.add_field(name = "🪙배팅금액", value = betting, inline = False)
                embed.add_field(name = "💰현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)

                await ctx.send(embed=embed)

            else:
                print("돈이 부족합니다.")
                print("배팅금액: ", money, " | 현재자산: ", cur_money)
                await ctx.send("돈이 부족합니다. 현재자산: " + str(cur_money))
        else:
            print("배팅금액", money, "가 10보다 작습니다.")
            await ctx.send("10원 이상만 배팅 가능합니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("도박은 회원가입 후 이용 가능합니다.")

    print("------------------------------\n")

@bot.command()
async def 랭킹(ctx):
    rank = ranking()
    embed = discord.Embed(title = "🏆레벨 랭킹", description = "", color = 0x4A44FF)

    for i in range(0,len(rank)):
        if i%2 == 0:
            name = rank[i]
            lvl = rank[i+1]
            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="🎟️레벨: "+str(lvl), inline=False)

    await ctx.send(embed=embed) 

@bot.command()
async def 회원가입(ctx):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await ctx.send("이미 가입하셨습니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("")

        Signup(ctx.author.name, ctx.author.id)

        print("회원가입이 완료되었습니다.")
        print("------------------------------\n")
        await ctx.send("회원가입이 완료되었습니다.")

@bot.command()
async def 탈퇴(ctx):
    print("탈퇴가 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        DeleteAccount(userRow)
        print("탈퇴가 완료되었습니다.")
        print("------------------------------\n")

        await ctx.send("탈퇴가 완료되었습니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")

        await ctx.send("등록되지 않은 사용자입니다.")

@bot.command()
async def 내정보(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, exp, money, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        expToUP = level*level + 6*level
        boxes = int(exp/expToUP*20)
        print("------------------------------\n")
        embed = discord.Embed(title="📋유저 정보", description = ctx.author.discriminator, color = 0x62D0F6)
        embed.add_field(name = "🎟️레벨", value = level)
        embed.add_field(name = "🏆순위", value = str(rank) + "/" + str(userNum))
        embed.add_field(name = "✨XP: " + str(exp) + "/" + str(expToUP), value = boxes * "```:blue_square:```" + (20-boxes) * ":white_large_square:", inline = False)
        embed.add_field(name = "💰보유 자산", value = money, inline = False)
        embed.add_field(name = "💸도박으로 날린 돈", value = loss, inline = False)

        await ctx.send(embed=embed)

@bot.command()
async def 정보(ctx, user: discord.User):
    userExistance, userRow = checkUser(user.name, user.id)

    if not userExistance:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.discriminator  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        level, exp, money, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        print("------------------------------\n")
        embed = discord.Embed(title="🔎유저 정보", description = user.discriminator, color = 0x62D0F6)
        embed.add_field(name = "🎟️레벨", value = level)
        embed.add_field(name = "✨경험치", value = str(exp) + "/" + str(level*level + 6*level))
        embed.add_field(name = "🏆순위", value = str(rank) + "/" + str(userNum))
        embed.add_field(name = "💰보유 자산", value = money, inline = False)
        embed.add_field(name = "💸도박으로 날린 돈", value = loss, inline = False)

        await ctx.send(embed=embed)

@bot.command()
async def 송금(ctx, user: discord.User, money):
    print("송금이 가능한지 확인합니다.")
    senderExistance, senderRow = checkUser(ctx.author.name, ctx.author.id)
    receiverExistance, receiverRow = checkUser(user.name, user.id)

    if not senderExistance:
        print("DB에서", ctx.author.name, "을 찾을수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 송금이 가능합니다.")
    elif not receiverExistance:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        print("송금하려는 돈: ", money)

        s_money = getMoney(ctx.author.name, senderRow)
        r_money = getMoney(user.name, receiverRow)

        if s_money >= int(money) and int(money) != 0:
            print("돈이 충분하므로 송금을 진행합니다.")
            print("")

            remit(ctx.author.name, senderRow, user.name, receiverRow, money)

            print("송금이 완료되었습니다. 결과를 전송합니다.")

            embed = discord.Embed(title="송금 완료📨", description = "송금된 돈: " + money, color = 0x77ff00)
            embed.add_field(name = "보낸 사람: " + ctx.author.name, value = "현재 자산: " + str(getMoney(ctx.author.name, senderRow)))
            embed.add_field(name = "→", value = ":moneybag:")
            embed.add_field(name="받은 사람: " + user.name, value="현재 자산: " + str(getMoney(user.name, receiverRow)))
                    
            await ctx.send(embed=embed)
        elif int(money) == 0:
            await ctx.send("0원을 보낼 필요는 없죠")
        else:
            print("돈이 충분하지 않습니다.")
            print("송금하려는 돈: ", money)
            print("현재 자산: ", s_money)
            await ctx.send("돈이 충분하지 않습니다. 현재 자산: " + str(s_money))

        print("------------------------------\n")


@bot.command()
@commands.has_any_role(998046067964776578)
async def reset(ctx):
    resetData()

@bot.command()
@commands.has_any_role(1004689605305585704, 998046067964776578)
async def 지급(ctx, user: discord.User, money):
    channel = bot.get_channel(1006571303211372544)
    await channel.send(user.mention + '님에게 성공적으로 ' + money + '원을 지급하였습니다.')
    user, row = checkUser(user.name, user.id)
    addMoney(row, int(money))
    print("MONEY add Success")

@bot.command()
@commands.has_any_role(1004689605305585704, 998046067964776578)
async def 경험치(ctx, user: discord.User, exp):
    channel = bot.get_channel(1006571303211372544)
    await channel.send(user.mention + '님에게 성공적으로 ' + exp + '경험치를 지급하였습니다.')
    user, row = checkUser(user.name, user.id)
    addExp(row, int(exp))
    print("EXP add Success")

@bot.command()
@commands.has_any_role(1004689605305585704, 998046067964776578)
async def 레벨(ctx, user: discord.User, lvl):
    channel = bot.get_channel(1006571303211372544)
    await channel.send(user.mention + '님에게 성공적으로 ' + lvl + '레벨을 지급하였습니다.')
    user, row = checkUser(user.name, user.id)
    adjustlvl(row, int(lvl))
    print("LEVEL add Success")

@bot.command()
@commands.has_any_role(1004689605305585704, 998046067964776578)
async def 차감(ctx, user: discord.User, money):
    channel = bot.get_channel(1006571303211372544)
    await channel.send(f'{user.mention}님의 자산을 성공적으로 {money}원 차감하였습니다.')
    user, row = checkUser(user.name, user.id)
    modifyMoney(user, row, -int(money))
    print("MONEY min Success")
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "!reset":
        await bot.process_commands(message)
        return
    else:
        userExistance, userRow = checkUser(message.author.name, message.author.id)
        channel = bot.get_channel(1006571303211372544)
        if userExistance:
            levelUp, lvl = levelupCheck(userRow)
            if levelUp:
                print(message.author, "가 레벨업 했습니다")
                print("")
                embed = discord.Embed(title = "레벨업", description = "", color = 0x00A260)
                embed.set_footer(text = message.author.name + " 님이 " + str(lvl) + "레벨 달성!🎉")
                await channel.send(embed=embed)
            else:
                modifyExp(userRow, 1)
                print("------------------------------\n")

        await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
        
@bot.command()
@commands.has_any_role(1004688586093887528, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def a(ctx, user: discord.User):
    channel = bot.get_channel(1004742567759466536)
    await channel.send(f'<@&1005458692470222900>\n᛭저희 병원에 새로오신 환자분을 환영해주세요! :tada:\n\n {user.mention}님! 저희 서버에 오신걸 환영해요!\n\n᛭서버 적응이 어려우시다면 간호사를 불러주세요! :person_raising_hand:\n\n᛭문의 하실게있으시다면 <#1005166621914058782>에 편하게 문의해주세요!  :envelope_with_arrow:\n\n᛭공지는 <#1005092490061291580>에서 확인해주세요! :loudspeaker:')

@bot.command()
@commands.has_any_role(1004688567613784175, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def w(ctx, user: discord.User, text):
    channel = bot.get_channel(1004748420898103326)
    await channel.send(f'{user.mention}||({user.id})|| 경고 1회 지급되었습니다.\n사유 : <#1005092364118925383> {text} 을 참고해주세요!')

@bot.command()
@commands.has_any_role(1004688567613784175, 1004688539914608640, 1004689605305585704, 998046067964776578)
async def c(ctx, user: discord.User, text):
    channel = bot.get_channel(1004748420898103326)
    await channel.send(f'{user.mention}||({user.id})|| 주의 1회 지급되었습니다.\n사유 : <#1005092364118925383> {text} 을 참고해주세요!')

bot.run('OTg2MjkwODk4ODg5NDkwNTIy.GRfRpF.XEPfLuNXhOzQiMFG8Ju7hBPxGeniUhQ04mQIEw')