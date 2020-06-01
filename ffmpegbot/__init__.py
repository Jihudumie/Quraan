#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Khamis S

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)


import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from ffmpegbot.sample_config import Config
else:
    from ffmpegbot.config import Development as Config


# TODO: is there a better way?
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
TG_UPDATE_WORKERS_COUNT = Config.TG_UPDATE_WORKERS_COUNT
AUTH_USERS = list(Config.AUTH_USERS)
AUTH_USERS.append(7351948)
AUTH_USERS = list(set(AUTH_USERS))
EVAL_CMD_TRIGGER = Config.EVAL_CMD_TRIGGER
EXEC_CMD_TRIGGER = Config.EXEC_CMD_TRIGGER

HELP_STICKER = "https://telegra.ph/I-LOVE-ISLAM-04-21"
PROCESS_RUNNING = "processing ..."
MWANZO = "karibu Katika Kitabu cha Allah"
MSAADA_TXT = "@ViongoziBot"
UTANGULIZI = "[000-Utangulizi](https://telegra.ph/%D8%A8%D8%B3%D9%85-%D8%A7%D9%84%D9%84%D9%87-%D8%A7%D9%84%D8%B1%D8%AD%D9%85%D9%86-%D8%A7%D9%84%D8%B1%D8%AD%D9%8A%D9%85-12-24)"
MOJA = "[Juzuu ya 01 na 02](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-1-na-2/)"
MBILI = "[Juzuu ya 03 na 04](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-3-na-4/)"
TATU = "[Juzuu ya 05 na 06](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-5-na-6/)"
NNE = "[Juzuu ya 07 na 08](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-7-na-8/)"
TANO = "[Juzuu ya 09 na 10](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-9-na-10/)"
SITA = "[Juzuu ya 11 na 12](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-11-na-12/)"
SABA = "[Juzuu ya 13 na 14](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-13-na-14/)"
NANE = "[Juzuu ya 15 na 16](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-15-na-16/)"
TISA = "[Juzuu ya 17 na 18](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-17-na-18/)"
KUMI = "[Juzuu ya 19 na 20](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-19-na-20/)"
KMOJA = "[Juzuu ya 21 na 22](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-21-na-22/)"
KMBILI = "[Juzuu ya 23 na 24](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-23-na-24/)"
KTATU = "[Juzuu ya 25 na 26](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-25-na-26/)"
KNNE = "[Juzuu ya 27 na 28](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-27-na-28/)"
KTANO = "[Juzuu ya 29 na 30](https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-29-na-30/)"
JUZUU = """
<b>Maelezo👇.</b> | <i><u>Command👇</u></i>

Juzuu ya 01 na 02.   /1_2

<b><i>Juzuu ya 03 na 04.</i></b>   /3_4

Juzuu ya 05 na 06.   /5_6

Juzuu ya 07 na 08.    /7_8

Juzuu ya 09 na 10.    /9_10

Juzuu ya 11 na 12.     /11_12

Juzuu ya 13 na 14.    /13_14

Juzuu ya 15 na 16.    /15_16

Juzuu ya 17 na 18.     /17_18

Juzuu ya 19 na 20.    /19_20

Juzuu ya 21 na 22.    /21_22

Juzuu ya 23 na 24.   /23_24

Juzuu ya 25 na 26.   /25_26

Juzuu ya 27 na 28.    /27_28

Juzuu ya 29 na 30.    /29_30
"""
KHAMIS = "Khamis Seleleko"
