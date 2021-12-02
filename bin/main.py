import re
from datetime import datetime, timedelta

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from sqlalchemy.orm import Session

from cfg.config import BOT_ID, BUG, WIKI, SPONSOR, BOT, DOC, SHOWCASE, YT
from database import models
from database.database import engine

db_session = Session(engine)

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='.', help_command=None, intents=intents)

ALLOWED_CLIENTS = ()
ALLOWED_CHANNEL = ()

with open('badword.txt') as file:
    file = file.read().split(',')

with open('code') as file1:
    file1 = file1.read().split(',')


@client.event
async def on_ready():
    print('Bot ready')
    models.Base.metadata.create_all(bind=engine)
    await client.change_presence(activity=discord.Game(name="! DPG ! .doc for infos"))


@client.event
async def on_command_error(ctx, error):
    print(error)


@client.event
async def on_message_edit(before, after):
    if after.channel.id in ALLOWED_CHANNEL:
        return
    bad_word = 0
    bad_word_list = []
    check_content = after.content.lower().split(' ')
    user = client.get_user(after.author.id)
    for badword in file:
        for word in check_content:
            if badword == word:
                bad_word = 1
                bad_word_list.append(badword)

    if bad_word == 1:
        new_message = ""
        await after.delete()
        for word in check_content:
            if word in bad_word_list:
                new_message = new_message + ' ' + '`' + word + '`'
            else:
                new_message = new_message + ' ' + word
        embed = discord.Embed(title="Bad Word Filter",
                              description=f"Hi {after.author.name} There are some swear words in your message:\n\n\n{new_message}",
                              color=0xe74c3c)
        await user.send(embed=embed)

        channel = client.get_channel(846463649861730344)
        embed = discord.Embed(title="Bad Word Filter # Message Changed",
                              description=f"From {after.author.name}:\n{new_message}",
                              color=0xe74c3c)
        await channel.send(embed=embed)


@client.event
async def on_message(message):
    bad_word = 0
    ctx = await client.get_context(message)
    user = client.get_user(ctx.author.id)
    # Showcase
    if message.attachments and message.channel.id == 761721971129843712:
        channel = client.get_channel(870374675644026940)
        embed = discord.Embed(title=f"Showcase from {ctx.author.name}",
                              description=f"{message.content}\n\n{message.jump_url}",
                              color=0o00255000)
        embed.set_image(url=message.attachments[0].url)
        embed.set_footer(text=f"Showcase by {ctx.author.name}")
        await channel.send(embed=embed)
        for x in message.attachments:
            if 'mp' in str(x.filename):
                video = await x.to_file()
                await channel.send(file=video)

    if message.channel.id not in ALLOWED_CHANNEL:
        check_content = message.content.lower().split(' ')
        bad_word_list = []
        for badword in file:
            for word in check_content:
                if badword == word:
                    bad_word = 1
                    bad_word_list.append(badword)

        if bad_word == 1:
            new_message = ""
            await message.delete()
            for word in check_content:
                if word in bad_word_list:
                    new_message = new_message + ' ' + '`' + word + '`'
                else:
                    new_message = new_message + ' ' + word
            embed = discord.Embed(title="Bad Word Filter",
                    description=f"Hi {ctx.author.name} There are some swear words in your message:\n\n\n{new_message}",
                                  color=0xe74c3c)
            await user.send(embed=embed)

            channel = client.get_channel(846463649861730344)
            embed = discord.Embed(title="Bad Word Filter",
                    description=f"From {ctx.author.name}:\nChannel:{message.channel.name}\n{new_message}",
                                  color=0xe74c3c)
            await channel.send(embed=embed)

    if message.channel.id == 852624162396831744:
        cnt = 0
        for word in file1:
            for text in check_content:
                if word == text:
                    cnt += 1

        if cnt > 2 and '```' not in message.content and 'Traceback' not in message.content and 'SystemError' not in message.content:
            embed = discord.Embed(title=f"Discord Code Syntax",
                                  description=f"Hi {ctx.author.name}\nIt seems like you wrote a code message without the Discord Syntax:\n"
                                              f"Please use the tripple backtick + the keyword python and end it with the tripple backtick",
                                  color=0xe74c3c)
            embed.set_footer(text=f"MessageID: {message.id}")
            await ctx.send(embed=embed)
            await ctx.send(file=discord.File('images/unknown.png'))

    if ctx.author.id != BOT_ID:
        await client.process_commands(message)
    if message.content == '.sponsor':
        await message.delete()


@client.command()
async def time(ctx, args):
    if 'hoffi' in args:
        local_date = datetime.now() - timedelta(hours=7)
        embed = discord.Embed(title="Hoffi",
                              description=f"Time is right now {local_date}",
                              color=0xe74c3c)
    else:
        local_date = datetime.now()
        embed = discord.Embed(title="EU",
                              description=f"Time is right now {local_date}",
                              color=0xe74c3c)
    await ctx.send(embed=embed)


@client.command()
async def syntax(ctx):
    embed = discord.Embed(title=f"Discord Code Syntax",
                          description=f"It seems like you wrote a code message without the Discord Syntax:\n"
                                      f"Please use the tripple backtick + the keyword python and end it with the tripple backtick",
                          color=0xe74c3c)
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File('images/unknown.png'))


@client.command()
async def bug(ctx):
    embed = discord.Embed(title="Bug Report", url=BUG,
                          description=f"Hi {ctx.author.name}\nYou can report a Bug here.",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def beta(ctx):
    embed = discord.Embed(title="Information about the Beta Release 0.7",
                          url="https://github.com/hoffstadt/DearPyGui/discussions/935",
                          description=f"Hi {ctx.author.name}\nYou can find here the information about the Beta 0.7",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def version(ctx):
    embed = discord.Embed(title="Pip Version",
                          description=f"Hi {ctx.author.name}\n Check out\n ```pip show dearpygui```",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def loaddocs(ctx):
    if ctx.author.id not in ALLOWED_CLIENTS:
        user = client.get_user(ctx.author.id)
        await user.send('Hi {}\n You are not allowed to use the Command.'.format(ctx.author.name))
    else:
        db_session.query(models.DPG_DOCS).delete()
        print('loading')
        urls_docs = []
        urls_together = []
        url = "https://dearpygui.readthedocs.io/en/latest/index.html"
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, "html.parser")
        for link in soup.findAll(attrs={'class': re.compile(r"^reference internal$")}):
            urls = []
            name = str(link).split('"')
            argfunc = name[3].split("/")
            urls = [argfunc[1][:-5], f"<https://dearpygui.readthedocs.io/en/latest/{name[3]}>"]
            urls_docs.append(urls)
        urls_together.append(urls_docs)
        print(urls_together)
        for nI in range(len(urls_together[0]) - 1 + 1):
            load = {"Command": urls_together[0][nI][0], "Message": urls_together[0][nI][1]}
            check_load = db_session.query(models.DPG_DOCS.Command).filter(
                models.DPG_DOCS.Command == urls_together[0][nI][0])
            if not check_load:
                db_load = models.DPG_DOCS(**load)
                db_session.add(db_load)
                db_session.commit()
        embed = discord.Embed(title="Load DOCS Finish",
                              color=0xFF5733)
        await ctx.send(embed=embed)


@client.command()
async def doc(ctx, *args):
    if args:
        cmd = args[0]
    else:
        embed = discord.Embed(title="Docs", url=DOC,
                              description=f"Hi {ctx.author.name}\n Follow the link to get access to the Docs",
                              color=0xFF5733)
        await ctx.send(embed=embed)
        return

    if len(args) > 1:
        pattern = args[1]
    url_docs = db_session.query(models.DPG_DOCS).filter(models.DPG_DOCS.Command == cmd).first()
    if url_docs:
        embed = discord.Embed(title=f"DPG DOC LINK {cmd}", url=str(url_docs.Message[1:][:-1]),
                              description=f"Hey {ctx.author.mention} \nCheck out on the DPG-Doc",
                              color=0xFF5733)
    else:
        document_commands = db_session.query(models.DPG_DOCS.Command).filter(
            models.DPG_DOCS.Command.like(f"%{cmd.lower()}%")
        ).first()
        command_list = [command for command in document_commands]
        embed = discord.Embed(title=f"DPG DOC {cmd}",
                              description=f"Hey {ctx.author.mention} \nHere are all docs that match with your pattern: **{cmd}**\n``` {command_list} ```",
                              color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def wiki(ctx):
    embed = discord.Embed(title="Wiki", url=WIKI,
                          description=f"Hi {ctx.author.name}\n Follow the link to get access to the Wiki page",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def api(ctx):
    embed = discord.Embed(title="API", url="https://hoffstadt.github.io/DearPyGui/",
                          description=f"Hi {ctx.author.name}\n Follow the link to get access to the API",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def showcase(ctx):
    embed = discord.Embed(title="Showcase", url=SHOWCASE,
                          description=f"Hi {ctx.author.name}\n Follow the link to get access to the Showcase page",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def paste(ctx):
    embed = discord.Embed(title="Pasting large amounts of code",
                          description="""If your code is too long to fit in a codeblock in discord, you can paste your code here:\n
https://paste.pydis.com/\n
After pasting your code, save it by clicking the floppy disk icon in the top right, or by typing ctrl + S. After doing that, the URL should change. Copy the URL and post it here so others can see it.""",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def sponsor(ctx):
    user = client.get_user(ctx.author.id)
    await user.send('Hi {}\nWe would love to have you in our Sponsor list:\n{}'.format(ctx.author.name, SPONSOR))


@client.command()
async def yt(ctx):
    embed = discord.Embed(title="YouTube", url=YT,
                          description=f"Hi {ctx.author.name}\n Follow the link to get access to the YouTube channel",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def image(ctx):
    embed = discord.Embed(title="How do I load an image?",
                          url="https://github.com/hoffstadt/DearPyGui/discussions/1072",
                          description=f"Hi {ctx.author.name}\n Check out this FAQ for image loading",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def box(ctx):
    embed = discord.Embed(title="How do I make a message/info/error box? ",
                          url="https://github.com/hoffstadt/DearPyGui/discussions/1002",
                          description=f"Hi {ctx.author.name}\n Check out this FAQ for message/info/error box",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def flip(ctx):
    await ctx.send(file=discord.File('images/flip.png'))


@client.command()
async def flipback(ctx):
    await ctx.send(file=discord.File('images/flipback.png'))


@client.command()
async def flipall(ctx):
    await ctx.send(file=discord.File('images/flipall.png'))


@client.command()
async def flipallback(ctx):
    await ctx.send(file=discord.File('images/flipallback.png'))


@client.command()
async def pyinstaller(ctx):
    embed = discord.Embed(title="Python Pyinstaller",
                          description=f""""```python\npyinstaller --onefile --noconsole YourstartExecutable.py --icon=sign.ico --name=YourName```\n
Please be aware to have all resource files in the same folder ( images / fonts / etc. ) as the executable""",
                          color=0xFF5733)
    await ctx.send(embed=embed)


@client.command()
async def loaddpg(ctx):
    if ctx.author.id not in ALLOWED_CLIENTS:
        user = client.get_user(ctx.author.id)
        await user.send('Hi {}\n You are not allowed to use the Command.'.format(ctx.author.name))
    else:
        db_session.query(models.DPG_API_NEW).delete()
        urls_dpg = []
        urls_logger = []
        urls_demo = []
        urls_themes = []
        urls_together = []
        url = "https://dearpygui.readthedocs.io/en/stable_08/reference/dearpygui.html"
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, "html.parser")
        for link in soup.findAll(attrs={'class': re.compile(r"^sig sig-object py$")}):
            urls = []
            name = str(link)[54:]
            name = name.split()
            urls = [name[0][:-2],
                    "<https://dearpygui.readthedocs.io/en/stable_08/reference/dearpygui.html#dearpygui.dearpygui.{}>".format(
                        name[0][:-2])]
            urls_dpg.append(urls)
        # LOGGER
        urls = ["mvLogger",
                "<https://dearpygui.readthedocs.io/en/stable_08/reference/logger.html#dearpygui.logger.mvLogger>"]
        urls_logger.append(urls)
        # THEMES
        url = "https://dearpygui.readthedocs.io/en/stable_08/reference/themes.html"
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, "html.parser")
        for link in soup.findAll(attrs={'class': re.compile(r"^py function$")}):
            urls = []
            name = str(link)[76:]
            name = name.split()
            urls = [name[0][:-2],
                    "<https://dearpygui.readthedocs.io/en/stable_08/reference/themes.html#dearpygui.themes.{}>".format(
                        name[0][:-2])]
            urls_themes.append(urls)
        urls_together.append(urls_dpg)
        urls_together.append(urls_logger)
        urls_together.append(urls_themes)
        for nI in range(len(urls_together[0]) - 1 + 1):
            load = {"Command": urls_together[0][nI][0], "Message": urls_together[0][nI][1]}
            db_load = models.DPG_API_NEW(**load)
            db_session.add(db_load)
        for nI in range(len(urls_together[1]) - 1 + 1):
            load = {"Command": urls_together[1][nI][0], "Message": urls_together[1][nI][1]}
            db_load = models.DPG_API_NEW(**load)
            db_session.add(db_load)
        for nI in range(len(urls_together[2]) - 1 + 1):
            load = {"Command": urls_together[2][nI][0], "Message": urls_together[2][nI][1]}
            db_load = models.DPG_API_NEW(**load)
            db_session.add(db_load)
        db_session.commit()
        embed = discord.Embed(title="Load API Finish",
                              color=0xFF5733)
        await ctx.send(embed=embed)


@client.command()
async def dpg(ctx, *args):
    cmd = args[0]
    dpg_message = db_session.query(models.DPG_API_NEW).filter(models.DPG_API_NEW.Command == cmd).first()
    if dpg_message:
        embed = discord.Embed(title=f"DPG API LINK {cmd}", url=dpg_message.Message[1:][:-1],
                              description=f"Hey {ctx.author.mention} \nCheck out on the API-Doc",
                              color=0xFF5733)
    else:
        api_commands = db_session.query(models.DPG_API_NEW.Command).filter(
            models.DPG_API_NEW.Command.like(f"%{cmd.lower()}%")
        ).all()
        command_list = [command[0] for command in api_commands]
        embed = discord.Embed(title=f"DPG API {cmd}",
                              description=f"Hey {ctx.author.mention} "
                                          f"\nHere are all commands that match with your pattern: **{cmd}**\n``` {command_list} ```",
                              color=0xFF5733)
    await ctx.send(embed=embed)


if __name__ == "__main__":
    client.run(BOT)
