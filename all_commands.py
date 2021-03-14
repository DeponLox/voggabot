import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from asyncio import sleep
import random
import Cybernator
from Cybernator import Paginator as pag
import json
import requests
from PIL import Image, ImageFont, ImageDraw
import io
from discord.utils import get
import youtube_dl
import os

bot = commands.Bot(command_prefix='v!')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title = "Помощь по командам.", description = '''
    `v!coin` - подбросить монетку
    `v!magicball <вопрос>` - задать вопрос магическому шару
    `v!say <сообщение>` - написать сообщение от имени бота
    `v!dice` - подбросить кубик
    ''', colour = discord.Color.blue())
    embed1.add_field(name = 'Админ-команды', value = '''
    `v!clear <кол-во сообщений>` - очистить указанное кол-во сообщений в чате
    ''', inline = True)
    embed2 = discord.Embed(title = 'Особая благодарность', description = '''
    `@Depon#1269` - главный разработчик бота
    `@Polyhedron#4563` - огромная помощь в разработке бота
    ''', colour = discord.Color.blue())
    embeds = [embed1, embed2]
    message = await ctx.send(embed=embed1)
    page = pag(bot, message, only=ctx.author, use_more=False, embeds=embeds)
    await page.start()

@bot.command()
async def coin(ctx):
  days = ('упала и выпала Решка', 'упала и выпал Орёл', 'встала ребром')
  day = random.choice(days)
  emb = discord.Embed(title = 'Подкинуть монетку', description = 'Монетка падает...', colour = discord.Color.blue())
  emb2 = discord.Embed(title = 'Подкинуть монетку', description = f'Монетка {day}', colour = discord.Color.blue())
  emb2.set_thumbnail(url=f'https://cdn.discordapp.com/emojis/773218476952256583.gif')
  msg = await ctx.send(embed = emb)
  await asyncio.sleep(2.5)
  await msg.edit(embed = emb2)

@bot.command()
async def dice(ctx):
    mal = discord.Embed(title = 'Кубик', description = '**Кубик падает...**', colour = discord.Color.blue())
    rets = ('1', '2', '3', '4', '5', '6')
    ret = random.choice(rets)
    mal2 = discord.Embed(title = 'Кубик', description = f'**Кубик упал, и выпало: `{ret}`**', colour = discord.Color.blue())
    msg = await ctx.send(embed = mal)
    await asyncio.sleep(2.5)
    await msg.edit(embed = mal2)

@bot.command()
async def magicball(ctx, *, message = None):
    if message == None:
      await ctx.send("**`Напишите вопрос.`**")
    else:
      emb = discord.Embed(title = ':8ball: Магический шар', description = f'**{ctx.message.author.mention} задал вопрос: ```{message}```**', colour = discord.Color.blue())
      msg = await ctx.send(embed = emb)
      await asyncio.sleep(2.5)
      answs = ('Конечно!','Ни в коем случае!','Да','Нет', 'Я не знаю')
      answ = random.choice(answs)
      emb2 = discord.Embed(title = ':8ball: Магический шар', description = f'**Ты задал вопрос: ```{message}```**\n\n**Ответ: ```{answ}```**', colour = discord.Color.blue())
      await msg.edit(embed = emb2)

@bot.command()
async def say(ctx, *, lol):
  await ctx.message.delete()
  await ctx.send(lol)

@bot.event
async def on_ready():
  print('Бот запущен')

@bot.command()
@commands.has_permissions(view_audit_log = True)
async def clear(ctx, amount = 10):
  deleted = await ctx.message.channel.purge(limit = amount + 1)

token = os.environ.get('BOT_TOKEN')
