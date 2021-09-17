import os
from dotenv import load_dotenv
load_dotenv

#admin
prefix="?"

#music options
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

YDL_OPTIONS = {
    'format': 'bestaudio[ext=m4a]',
    'noplaylist': 'True',
    'cookiefile': os.getenv('COOKIES')
}

queued_music = {
    'header': "▷ **Queue:**",
    'color': 0xe67e22,
    'info3': "Position in queue:"
}

playing_music = {
    'header': "🎵  **Playing:**",
    'color': 0xff0000,
    'info3': "Songs in queue:"
}

max_songs_in_queue = 10
disconnect_time = 900

#anime function options
hentai_categories = ['waifu', 'neko', 'trap', 'blowjob']
hentai_color = 0xd59de0

waifu_categories =['waifu', 'neko' , 'shinobu', 'megumin' , 'bully',
                'cuddle'  ,'cry'   , 'hug'    , 'awoo'    , 'kiss',
                'lick'    , 'pat'  , 'smug'   , 'bonk'    , 'yeet',
                'blush'   , 'smile','wave'    , 'highfive', 'handhold',
                'nom'     , 'bite' , 'glomp'  , 'slap'    , 'kill', 'kick',
                'happy'   , 'wink' , 'poke'   , 'dance'   , 'cringe'
]
waifu_color = 0x007acc

anime_color = 0x2e51a2
manga_color = 0xebab37
anime_character_color = 0x2e51a2
manga_character_color = 0xebab37
seiyuu_color = 0x2e51a2
staff_color = 0x2e51a2

characters_number = 10
language = "Japanese"