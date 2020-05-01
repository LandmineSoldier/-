
import discord, asyncio
import random
import time
from random import *
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("논란!"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    #made by LandmineSoldier (지뢰군인)

    if message.content.startswith("논란!"):
        await message.channel.send("논란이다!")
    elif message.content.endswith("논란!"):
        await message.channel.send("논란이다!")

    if message.content.startswith("윤X현/논란"):
        embed=discord.Embed(title="윤X현/논란", description="그의 논란 어록", color=0x696969)
        embed.add_field(name="1", value="-개보다 못한사람...강아지 비하발언", inline=True)
        embed.add_field(name="2", value="-옆집에 박X아 어머니가 모내기...", inline=True)
        embed.add_field(name="3", value="-반성할 기미 없이 '새X들아 발언'", inline=True)
        embed.add_field(name="4", value="-욕에 이어 '니네가 먼저 했잖아' 적반하장", inline=True)
        embed.add_field(name="5", value="-하프라이프3을 위해 김X진 죽어라 발언", inline=True)
        embed.add_field(name="6", value="-김X성 딸기맛 아픈 친구를 먹으려 해 식인발언", inline=True)
        embed.add_field(name="7", value="-박X아의 밝은 장래 비하", inline=True)
        embed.add_field(name="8", value="-저소득층 비하발언", inline=True)
        embed.add_field(name="9", value="-친구 손절", inline=True)
        embed.add_field(name="10", value="-심신마약", inline=True)
        embed.add_field(name="11", value="-어장관리 양식장 운영중인걸로 밝혀져", inline=True)
        embed.add_field(name="12", value="-친구를 새우잡이 보낸다고 발언", inline=True)
        embed.add_field(name="13", value="-HTML색상코드 회색을 추천하는데 하필이면 696969 발언", inline=True)
        embed.add_field(name="14", value="-신X규 전X현 팬클럽 붕어빵가게 회장 명예훼손", inline=True)
        embed.add_field(name="15", value="-지킬앤 하이드 조커발언", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)

    if message.content.startswith("박X아/논란"):
        embed=discord.Embed(title="박X아/논란", description="그녀?의 논란 어록", color=0xffff90)
        embed.add_field(name="1", value="-아재개그 논란", inline=True)
        embed.add_field(name="2", value="-'오뚜기 3분 윤X현' 식인발언", inline=True)
        embed.add_field(name="3", value="-'윤X현 역겹다' 발언", inline=True)
        embed.add_field(name="4", value="-자신의 정체 코끼리라고 밝혀 다소 충격적인 발언", inline=True)
        embed.add_field(name="5", value="-전교1등 발언 논란", inline=True)
        embed.add_field(name="6", value="-윤X현 살해협박발언", inline=True)
        embed.add_field(name="7", value="-북한인 논란", inline=True)
        embed.add_field(name="8", value="-성별 논란", inline=True)
        embed.add_field(name="9", value="-돈세탁 논란", inline=True)
        embed.add_field(name="10", value="-학생협박발언", inline=True)
        embed.add_field(name="11", value="-최X진 성희롱 논란", inline=True)
        embed.add_field(name="12", value="-성별 색상 고정관념 논란", inline=True)
        embed.add_field(name="13", value="-특정 정당 지지논란", inline=True)
        embed.add_field(name="14", value="-다른 유저의 사생활 메시지 도배 논란", inline=True)
        embed.add_field(name="15", value="-'7쨜'발언 논란", inline=True)
        embed.add_field(name="16", value="-수업태도 태만 논란", inline=True)
        embed.add_field(name="17", value="-남좌 논란", inline=True)
        embed.add_field(name="18", value="-'3반 이쁜이는 나다' 나르시시즘 논란", inline=True)
        embed.add_field(name="19", value="-민주주의 부정발언", inline=True)
        embed.add_field(name="20", value="-자기 입으로 슈퍼스타라고 주장 논란", inline=True)
        embed.add_field(name="21", value="-혼잣말 논란", inline=True)
        embed.add_field(name="22", value="-과한 자기애로 인한 비호감 논란", inline=True)
        embed.add_field(name="23", value="-류X준 외 3명 살해협박 논란", inline=True)
        embed.add_field(name="24", value="-꼰대 논란", inline=True)
        embed.add_field(name="25", value="-논란킹이 되고자 자가신고 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)

    if message.content.startswith("최X진/논란"):
        embed=discord.Embed(title="최X진/논란", description="그의 논란 어록", color=0xb2ebf4)
        embed.add_field(name="1", value="-ZOOM에서 시공간을 왜곡하여 수업에 혼란을 줌", inline=True)
        embed.add_field(name="2", value="-수업도중 취침논란", inline=True)
        embed.add_field(name="3", value="-관리자 기만 논란", inline=True)
        embed.add_field(name="4", value="-엄X식 사칭논란", inline=True)
        embed.add_field(name="5", value="-졸업사진으로 사람들의 눈을 위협하는 논란", inline=True)
        embed.add_field(name="6", value="-로봇 성추행 논란", inline=True)
        embed.add_field(name="7", value="-'이X현 부웅신' 친구 비방 발언", inline=True)
        embed.add_field(name="8", value="-'킹갓 엔버짱' 10Duck 논란", inline=True)
        embed.add_field(name="9", value="-대소고 무시발언", inline=True)
        embed.add_field(name="10", value="-'섹' 발언으로 인한 논란", inline=True)
        embed.add_field(name="11", value="-가슴 보형물 논란", inline=True)
        embed.add_field(name="12", value="-'하악하악' 전X현과 함께 발언", inline=True)
        embed.add_field(name="13", value="-초능력좌 행위 논란", inline=True)
        embed.add_field(name="14", value="-단체 채팅방에서 성적발언 논란", inline=True)
        embed.add_field(name="15", value="-사적 채팅방에서 성적인 발언", inline=True)
        embed.add_field(name="16", value="-비선실세 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)

    if message.content.startswith("이X경/논란"):
        embed=discord.Embed(title="이X경/논란", description="그의 논란 어록", color=0xff6600)
        embed.add_field(name="1", value="-논란 작성 논란", inline=True)
        embed.add_field(name="2", value="-전세계 '우민'이라는 이름을 가진 사람 비하 발언", inline=True)
        embed.add_field(name="3", value="-친구의 이름앞'성'을 바꾸어 '성'희롱 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)

    if message.content.startswith("전X현/논란"):
        embed=discord.Embed(title="전X현/논란", description="그흐녀의 논란 어록", color=0xff6a6a)
        embed.add_field(name="1", value="-김X성 명예훼손 논란", inline=True)
        embed.add_field(name="2", value="-허위사실유포로 학생기만논란", inline=True)
        embed.add_field(name="3", value="-엄X식봇 해방요청 논란", inline=True)
        embed.add_field(name="4", value="-이중읭격 논란", inline=True)
        embed.add_field(name="5", value="-아잉좌 2호 논란", inline=True)
        embed.add_field(name="6", value="-아잉 도배 논란", inline=True)
        embed.add_field(name="7", value="-ㅗㅜㅑ 논란", inline=True)
        embed.add_field(name="8", value="-일본사이트 우회에 호감행동 논란", inline=True)
        embed.add_field(name="9", value="-'미X자식' 발언", inline=True)
        embed.add_field(name="10", value="-'하악하악' 최X진과 함께 발언", inline=True)
        embed.add_field(name="11", value="-'약빨면 삐용삐용' 약팔이 논란", inline=True)
        embed.add_field(name="12", value="-박X아의 '오뚜기 3분 윤X현' 식인 동조발언", inline=True)
        embed.add_field(name="13", value="-'킹'으로 박X아 성별 조작 논란", inline=True)
        embed.add_field(name="14", value="-1학년 전교생 비하발언", inline=True)
        embed.add_field(name="15", value="-'나만 아니면 돼' 발언", inline=True)
        embed.add_field(name="16", value="-'나는 클린해' 발언 다수가 의심 논란", inline=True)
        embed.add_field(name="17", value="-많고많은 숫자들중 '58774485' 추천 논란", inline=True)
        embed.add_field(name="18", value="-기만좌 논란", inline=True)
        embed.add_field(name="19", value="-숫자를 위장한 욕설사용 논란", inline=True)
        embed.add_field(name="20", value="-약으로 인한 돌발행동 논란", inline=True)
        embed.add_field(name="21", value="-친구에게 누명씌우기 논란", inline=True)
        embed.add_field(name="22", value="-친구에게 다소 폭력적인 발언", inline=True)
        embed.add_field(name="23", value="-2반으로 위장잠입 논란", inline=True)
        embed.add_field(name="24", value="-논란퀸칭호를 즐기고있어 논란", inline=True)
        embed.add_field(name="25", value="-친구에게 선생님으로 협박 논란", inline=True)
        embed.set_footer(text="목록이 많아서 2장까지 넘어갔습니다")
        await message.channel.send(embed=embed)
        embed=discord.Embed(title="전X현/논란", description="그흐녀의 논란 어록 2장", color=0xff6a6a)
        embed.add_field(name="26", value="-친구에게 살인 협박 논란", inline=True)
        embed.add_field(name="27", value="-'이런 양아치가..' 발언 논란", inline=True)
        embed.add_field(name="28", value="-'1반 이쁜이는 나 하는거 어때' 나르시시즘 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)
        

    if message.content.startswith("서X우/논란"):
        embed=discord.Embed(title="서X우/논란", description="그의 논란 어록", color=0xffec2b)
        embed.add_field(name="1", value="-서승우 증거조작 논란", inline=True)
        embed.add_field(name="2", value="-누군가를 핥는 시늉 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)

    if message.content.startswith("이X주/논란"):
        embed=discord.Embed(title="이X주/논란", description="그의 논란 어록", color=0xff4d4d)
        embed.add_field(name="1", value="-'홍콩갈까' 발언 논란", inline=True)
        embed.add_field(name="2", value="-'홍콩갔다' 발언 논란", inline=True)
        embed.add_field(name="3", value="-권력 < 검열되었습니다. >", inline=True)
        embed.add_field(name="4", value="-불순한 언행유도 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)

    if message.content.startswith("이X우/논란"):
        embed=discord.Embed(title="이X우/논란", description="그의 논란 어록", color=0x6c2c00)
        embed.add_field(name="1", value="-'이X경'을 이경으로 변경논란", inline=True)
        embed.add_field(name="2", value="-있지도 않은 5반 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)
    
    if message.content.startswith("류X규/논란"):
        embed=discord.Embed(title="류X규/논란", description="그의 논란 어록", color=0xffb2f5)
        embed.add_field(name="1", value="-자가박제 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)
    
    if message.content.startswith("신X빈/논란"):
        embed=discord.Embed(title="신X빈/논란", description="그의 논란 어록", color=0xffe400)
        embed.add_field(name="1", value="-포교논란", inline=True)
        embed.add_field(name="2", value="-타사 제품 비하 논란", inline=True)
        embed.add_field(name="3", value="-대리게임 논란", inline=True)
        embed.add_field(name="4", value="-자기 비하 발언", inline=True)
        embed.add_field(name="5", value="-이X욱에게 공개고백 논란", inline=True)
        embed.add_field(name="6", value="-무지개 혐오 논란", inline=True)
        embed.add_field(name="7", value="-자신은 청정하다 발언 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)

    if message.content.startswith("지X혁/논란"):
        embed=discord.Embed(title="지X혁/논란", description="그의 논란 어록", color=0x00aeff)
        embed.add_field(name="1", value="-여성에게 '킹' 칭호 부여하여 성별 변경 논란", inline=True)
        embed.add_field(name="2", value="-오타를 위장한 욕설 논란", inline=True)
        embed.add_field(name="3", value="-자신의 애교로 덮으려 했으나 역효과 발생 논란", inline=True)
        embed.add_field(name="4", value="-아잉좌 1호 논란", inline=True)
        embed.add_field(name="5", value="-'수박 애호가 이해불가..' 발언 논란", inline=True)
        embed.set_footer(text="추가 하고 싶은 논란은 DM으로")
        await message.channel.send(embed=embed)

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
