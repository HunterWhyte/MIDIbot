
from twitchio.ext import commands
import os

note = ""
count = 0
name = ""


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='', client_id='BotKeys', nick='BotKeys', prefix='!',
                         initial_channels=[''])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='play')
    async def play(self, ctx):
        #check count
        try:
            os.mkfifo("count")
        except:
            pass  # In case one of your other files already started
        if True:
            file = open("count", "r")
            count = int(file.read())
            print(count)
        if count <20:
            note = ctx.content
            name = ctx.author.name
            try:
                os.mkfifo("data.txt")
            except:
                pass  # In case one of your other files already started
            if True:
                file = open("data.txt", "w")
                file.write(note + "~" + name)
                file.close()
                try:
                    os.mkfifo("count")
                except:
                    pass  # In case one of your other files already started
                if True:
                    count = count + 1
                    file = open("count", "w")
                    file.write(str(count))
                    file.close()
                    await ctx.send(f'your notes have been added to the queue {ctx.author.name}')


        else:
            await ctx.send(f'the queue is full right now please try later {ctx.author.name}')

    @commands.command(name='chords')
    async def chords(self, ctx):
        # check count
        try:
            os.mkfifo("count")
        except:
            pass  # In case one of your other files already started
        if True:
            file = open("count", "r")
            count = int(file.read())
            print(count)
        if count < 20:
            note = ctx.content
            name = ctx.author.name
            try:
                os.mkfifo("data.txt")
            except:
                pass  # In case one of your other files already started
            if True:
                file = open("data.txt", "w")
                file.write(note + "~" + name)
                file.close()
                try:
                    os.mkfifo("count")
                except:
                    pass  # In case one of your other files already started
                if True:
                    count = count + 1
                    file = open("count", "w")
                    file.write(str(count))
                    file.close()
                    await ctx.send(f'your notes have been added to the queue {ctx.author.name}')


        else:
            await ctx.send(f'the queue is full right now please try later {ctx.author.name}')

bot = Bot()
bot.run()

