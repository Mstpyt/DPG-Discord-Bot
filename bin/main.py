import discord
from discord.ext import commands
from database import db_create, sqlite3db
from messages import examples
from messages import documentation
from cfg import common, initial_load
from cfg.config import DBNAME, BOT_ID, BUG, WIKI, SPONSOR, BOT

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='.', help_command=None, intents=intents)


@client.event
async def on_ready():
    print('Bot ready')
    db_create.create_database(DBNAME)
    await client.change_presence(activity=discord.Game(name="! DPG ! .doc for infos"))


@client.event
async def on_command_error(ctx, error):
    print(error)


@client.event
async def on_message(message):
    ctx = await client.get_context(message)
    if ctx.author.id != BOT_ID:
        await client.process_commands(message)
    if message.content == '.sponsor':
        await message.delete()


@client.command()
async def bug(ctx):
    await ctx.send('Hi {}\nYou can report a Bug here:\n{}'.format(ctx.author.name, BUG))


@client.command()
async def wiki(ctx):
    await ctx.send('Hi {}\nYou can see the Wiki here:\n{}'.format(ctx.author.name, WIKI))


@client.command()
async def sponsor(ctx):
    user = client.get_user(ctx.author.id)
    await user.send('Hi {}\nWe would love to have you in our Sponsor list:\n{}'.format(ctx.author.name, SPONSOR))


@client.command()
async def dpg(ctx, *args):
    cmd = args[0]
    print(cmd)
    if len(args) > 1:
        pattern = args[1]
    if cmd.lower() == 'search':
        Lists = sqlite3db.TExecSqlReadMany(DBNAME, """
                                           SELECT Command FROM DPG_API where Command like ?
                                           """,
                                           '%'+pattern.lower()+'%')
        Lists = common.listToStringForStatistics(Lists)
        await ctx.send("Hey {} \nHere are all commands that match with your pattern: **{}**\n``` {} ```"
                       .format(ctx.author.mention, pattern, Lists))
    else:
        Command = sqlite3db.TExecSqlReadMany(DBNAME, """
                                            SELECT Message FROM DPG_API where Command = ?
                                            """,
                                             cmd)
        Command = common.listToStringWithoutBracketsAndAT(Command)
        if Command:
            await ctx.send('Hey {} \nCheck out on the API-Doc:\n{}'
                           .format(ctx.author.mention, Command))
        else:
            await ctx.send('Hey {} \nSorry i can not find this Command `{}` in the API-Docs !'
                           .format(ctx.author.mention, cmd))


@client.command()
async def exam(ctx, arg):
    acExam = arg
    if acExam.lower() == 'list':
        user = client.get_user(ctx.author.id)
        List = common.listToStringForStatistics_exam(examples.Example_List)
        await user.send("Hey {} you can use: .exam \n {}"
                        .format(ctx.author.mention, List))
    else:
        acExample = common.get_exampe(acExam)
        if acExample:
            await ctx.send("Here is your example for **{}**{}".format(acExam, acExample))
        else:
            await ctx.send('`No example found with **{}**`'.format(acExam))


@client.command(name="help", description="Returns all commands available")
async def help(ctx):
    user = client.get_user(ctx.author.id)
    helptext = "```"
    for command in client.commands:
        helptext += f"{command}\n"
    helptext += "```"
    await user.send(helptext)


@client.command()
async def doc(ctx):
    user = client.get_user(ctx.author.id)
    await user.send(documentation.DOC1.format(ctx.author.name))
    await user.send(documentation.DOC2)


@client.command()
async def loadapi(ctx):
    nI = 0
    if ctx.author.id != 219155482961641472:
        user = client.get_user(ctx.author.id)
        await user.send('Hi {}\n You are not allowed to use the Command.'.format(ctx.author.name))
    else:
        while nI <= len(initial_load.INITIAL) - 2:
            nI = nI + 1
            load = (initial_load.INITIAL[nI][0], initial_load.INITIAL[nI][1])
            sqlite3db.TExecSql(DBNAME, """
                                INSERT INTO DPG_API VALUES (?, ?)
                                """,
                                 load)


if __name__ == "__main__":
    client.run(BOT)
