import nextcord
from nextcord.ext import commands

# Botのインテントを設定
intents = nextcord.Intents.default()
intents.members = True
client = commands.Bot(intents=intents)

# Botが起動したときの処理
@client.event
async def on_ready():
    print(f'Botが起動しました！ログイン: {client.user}')

# メンバーが参加したときの処理
@client.event
async def on_member_join(member):
    channel_id = # channelIDを入力
    channel = client.get_channel(channel_id)
    embed = nextcord.Embed(
        title="ようこそ！",
        description=f"{member.mention} さん\n私たちのコミュニティで素晴らしい時間を過ごしてください。",
        color=nextcord.Color.green()
    )
    embed.set_thumbnail(url=member.avatar.url)
    if channel:
        await channel.send(embed=embed)

# Botを実行するためのトークン
client.run('TOKEN')
