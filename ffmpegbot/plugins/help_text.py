from pyrogram import Client, Filters

from ffmpegbot import (MWANZO, MSAADA_TXT, JUZUU, KHAMIS, MOJA, MBILI, TATU, NNE, TANO, SITA, SABA, NANE, TISA, KUMI, KMOJA, KMBILI, KTATU, KNNE, KTANO)


@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(MWANZO, quote=True)

@Client.on_message(Filters.command(["help"]))
async def msaada(client, message):
    await message.reply_text(MSAADA_TXT, quote=True)

@Client.on_message(Filters.command(["1na2"]))
async def moja(client, message):
    await message.reply_text(MOJA, quote=True)

@Client.on_message(Filters.command(["3na4"]))
async def mbili(client, message):
    await message.reply_text(MBILI, quote=True)

@Client.on_message(Filters.command(["5na6"]))
async def tatu(client, message):
    await message.reply_text(TATU, quote=True)

@Client.on_message(Filters.command(["7na8"]))
async def nne(client, message):
    await message.reply_text(NNE, quote=True)

@Client.on_message(Filters.command(["9na10"]))
async def tano(client, message):
    await message.reply_text(TANO, quote=True)

@Client.on_message(Filters.command(["11na12"]))
async def sita(client, message):
    await message.reply_text(SITA, quote=True)

@Client.on_message(Filters.command(["13na14"]))
async def saba(client, message):
    await message.reply_text(SABA, quote=True)

@Client.on_message(Filters.command(["15na16"]))
async def nane(client, message):
    await message.reply_text(NANE, quote=True)

@Client.on_message(Filters.command(["17na18"]))
async def tisa(client, message):
    await message.reply_text(TISA, quote=True)

@Client.on_message(Filters.command(["19na20"]))
async def kumi(client, message):
    await message.reply_text(KUMI, quote=True)

@Client.on_message(Filters.command(["21na22"]))
async def kumi_namoja(client, message):
    await message.reply_text(KMOJA, quote=True)

@Client.on_message(Filters.command(["23na24"]))
async def kumi_nwmbili(client, message):
    await message.reply_text(KMBILI, quote=True)

@Client.on_message(Filters.command(["25na26"]))
async def kumi_natatu(client, message):
    await message.reply_text(KTATU, quote=True)

@Client.on_message(Filters.command(["27na28"]))
async def Kumi_nne(client, message):
    await message.reply_text(KNNE, quote=True)

@Client.on_message(Filters.command(["29na30"]))
async def kumi_tano(client, message):
    await message.reply_text(KTANO, quote=True)

@Client.on_message(Filters.command(["khamis", "about"]))
async def kumi_tano(client, message):
    await message.reply_text(KHAMIS, quote=True)

@Client.on_message(Filters.command(["juzuu"]))
async def juzuu(client, message):
    await message.reply_text(JUZUU, quote=True)

