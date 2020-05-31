from pyrogram import Client, Filters

from ffmpegbot import (HELP_STICKER, MSAADA_TXT, JUZUU, JM, JP, JT, JN,
JO, JS, JB, JE, JST, JKM,
JKT, JKN, JKNT, JTS, JKMN)


@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(HELP_STICKER, quote=True)

@Client.on_message(Filters.command(["help"]))
async def msaada(client, message):
    await message.reply_text(MSAADA_TXT, quote=True)

@Client.on_message(Filters.command(["1na2"]))
async def moja(client, message):
    await message.reply_text(JM, quote=True)

@Client.on_message(Filters.command(["4na4"]))
async def mbili(client, message):
    await message.reply_text(JP, quote=True)

@Client.on_message(Filters.command(["5na6"]))
async def tatu(client, message):
    await message.reply_text(JT, quote=True)

@Client.on_message(Filters.command(["7na8"]))
async def nne(client, message):
    await message.reply_text(JN, quote=True)

@Client.on_message(Filters.command(["9na10"]))
async def tano(client, message):
    await message.reply_text(JO, quote=True)

@Client.on_message(Filters.command(["11na12"]))
async def sita(client, message):
    await message.reply_text(JS, quote=True)

@Client.on_message(Filters.command(["13na14"]))
async def saba(client, message):
    await message.reply_text(JB, quote=True)

@Client.on_message(Filters.command(["15na16"]))
async def nane(client, message):
    await message.reply_text(JE, quote=True)

@Client.on_message(Filters.command(["17na18"]))
async def tisa(client, message):
    await message.reply_text(JTS, quote=True)

@Client.on_message(Filters.command(["09"]))
async def tisa(client, message):
    await message.reply_text(JST, quote=True)

@Client.on_message(Filters.command(["19na20"]))
async def kumi(client, message):
    await message.reply_text(JKM, quote=True)

@Client.on_message(Filters.command(["21na22"]))
async def kumi_namoja(client, message):
    await message.reply_text(JKMN, quote=True)

@Client.on_message(Filters.command(["22na23"]))
async def kumi_nwmbili(client, message):
    await message.reply_text(JKM, quote=True)

@Client.on_message(Filters.command(["23na24"]))
async def kumi_natatu(client, message):
    await message.reply_text(JKT, quote=True)

@Client.on_message(Filters.command(["25&26"]))
async def Kumi_nne(client, message):
    await message.reply_text(JKN, quote=True)

@Client.on_message(Filters.command(["27&28"]))
async def kumi_tano(client, message):
    await message.reply_text(JKNT, quote=True)

@Client.on_message(Filters.command(["juzuu"]))
async def juzuu(client, message):
    await message.reply_text(JUZUU, quote=True)
