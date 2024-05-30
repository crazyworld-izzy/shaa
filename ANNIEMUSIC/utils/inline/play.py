import math
from typing import Union
from pyrogram.types import InlineKeyboardButton

from ANNIEMUSIC.utils.formatters import time_to_seconds

from ANNIEMUSIC import app

def track_markup(_, user_id, channel, fplay):
    buttons = [

            [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",), 
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",),
        ],
        [
            InlineKeyboardButton(text="ღ ʀᴇᴘʟᴀʏ ღ", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="ღ sᴛᴏᴘ ღ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ღ ᴍᴏʀᴇ ღ", callback_data=f"PanelMarkup None|{chat_id}",),
        ],
    ]

    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
 if 0 < umm < 10
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 10 < umm < 20:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 20 <= umm < 30:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 30 <= umm < 40:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 40 <= umm < 50:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 50 <= umm < 60:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 60 <= umm < 70:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 70 <= umm < 80:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 80 <= umm < 95:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    else:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    buttons = [
        
        [
            InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer",)
        ],
          [
            InlineKeyboardButton(text="ღ ʀᴇsᴜᴍᴇ ღ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ღ ᴘᴀᴜsᴇ ღ", callback_data=f"ADMIN Pause|{chat_id}",),
            InlineKeyboardButton(text="ღ sᴋɪᴘ ღ", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ღ sᴛᴏᴘ ღ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ღ ʀᴇᴘʟᴀʏ ღ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ღ ᴍᴏʀᴇ ღ", callback_data=f"PanelMarkup None|{chat_id}",),
        ],
    ]

    return buttons

def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 10 < umm < 20:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 20 <= umm < 30:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 30 <= umm < 40:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 40 <= umm < 50:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 50 <= umm < 60:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 60 <= umm < 70:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 70 <= umm < 80:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    elif 80 <= umm < 95:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    else:
        bar = "𝓢𝓱𝓪𝓪 𝓜𝓾𝓼𝓲𝓬"
    buttons = [
        
        [
            InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer",)
        ],
          [
            InlineKeyboardButton(text="ღ ʀᴇsᴜᴍᴇ ღ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ღ ᴘᴀᴜsᴇ ღ", callback_data=f"ADMIN Pause|{chat_id}",),
            InlineKeyboardButton(text="ღ sᴋɪᴘ ღ", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ღ sᴛᴏᴘ ღ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ღ ʀᴇᴘʟᴀʏ ღ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ღ ᴍᴏʀᴇ ღ", callback_data=f"PanelMarkup None|{chat_id}",),
        ],
    ]

    return buttons

def stream_markup(_, chat_id):
    buttons  = [

        [
            InlineKeyboardButton(text="ღ ʀᴇsᴜᴍᴇ ღ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ღ ᴘᴀᴜsᴇ ღ", callback_data=f"ADMIN Pause|{chat_id}",),
            InlineKeyboardButton(text="ღ sᴋɪᴘ ღ", callback_data=f"ADMIN Skip|{chat_id}"),
            
        ],
        [
            InlineKeyboardButton(text="▢ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ღ ᴍᴏʀᴇ ღ", callback_data=f"PanelMarkup None|{chat_id}",),
        ],
    ]

    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"JARVISPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"JARVISPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text=_["ღ ᴄʟᴏsᴇ ღ"], callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        
        [
            InlineKeyboardButton(text=_["P_B_3"], callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text=_["ღ ᴄʟᴏsᴇ ღ"], callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",),
            InlineKeyboardButton(text=_["ღ ᴄʟᴏsᴇ ღ"], callback_data=f"forceclose {query}|{user_id}",),
            InlineKeyboardButton(text="▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",),
        ],
     ]
    return buttons

## Telegram Markup

def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text= "ღ ɴᴇxᴛ ღ", callback_data=f"PanelMarkup None|{chat_id}",),
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
        
## Queue Markup

def queue_markup(_, videoid, chat_id):

    buttons = [
        
          [
            InlineKeyboardButton(text="ღ ᴘᴀᴜsᴇ ღ", callback_data=f"ADMIN Pause|{chat_id}",),
            InlineKeyboardButton(text="ღ sᴛᴏᴘ ღ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ღ sᴋɪᴘ ღ", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ღ ʀᴇsᴜᴍᴇ ღ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ღ ʀᴇᴘʟᴀʏ ღ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="ღ ᴍᴏʀᴇ ღ", callback_data=f"PanelMarkup None|{chat_id}"),
        ],
    ]

    return buttons



                
def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text= "ღ ᴀᴅᴅ ɪɴ ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ ღ", callback_data=f"add_playlist {videoid}")
        ],
        [
            InlineKeyboardButton(text="ღ sᴜғғʟᴇ ღ", callback_data=f"ADMIN Shuffle|{chat_id}",),
            InlineKeyboardButton(text="ღ ʟᴏᴏᴘ ღ", callback_data=f"ADMIN Loop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="◁ 10 sᴇᴄ", callback_data=f"ADMIN 1|{chat_id}",),
            InlineKeyboardButton(text="10 sᴇᴄ ▷", callback_data=f"ADMIN 2|{chat_id}",),
        ],
        [
            InlineKeyboardButton(text="ღ ʜᴏᴍᴇ ღ", callback_data=f"MainMarkup {videoid}|{chat_id}",),
            InlineKeyboardButton(text="ღ ɴᴇxᴛ ღ", callback_data=f"Pages Forw|0|{videoid}|{chat_id}",),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
       
        [
                InlineKeyboardButton(text="🕒 0.5x", callback_data=f"SpeedUP {chat_id}|0.5",),
                InlineKeyboardButton(text="🕓 0.75x", callback_data=f"SpeedUP {chat_id}|0.75",),
                InlineKeyboardButton(text="🕤 1.0x", callback_data=f"SpeedUP {chat_id}|1.0",),
            ],
            [
                InlineKeyboardButton(text="🕤 1.5x", callback_data=f"SpeedUP {chat_id}|1.5",),
                InlineKeyboardButton(text="🕛 2.0x", callback_data=f"SpeedUP {chat_id}|2.0",),
            ],
        [
            InlineKeyboardButton(text="ღ ʙᴀᴄᴋ ღ", callback_data=f"Pages Back|1|{videoid}|{chat_id}",),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
                InlineKeyboardButton(text="🕒 0.5x", callback_data=f"SpeedUP {chat_id}|0.5",),
                InlineKeyboardButton(text="🕓 0.75x", callback_data=f"SpeedUP {chat_id}|0.75",),
                InlineKeyboardButton(text="🕤 1.0x", callback_data=f"SpeedUP {chat_id}|1.0",),
            ],
            [
                InlineKeyboardButton(text="🕤 1.5x", callback_data=f"SpeedUP {chat_id}|1.5",),
                InlineKeyboardButton(text="🕛 2.0x", callback_data=f"SpeedUP {chat_id}|2.0",),
            ],
        [
            InlineKeyboardButton(text="ღ ʙᴀᴄᴋ ღ", callback_data=f"Pages Back|2|{videoid}|{chat_id}",),
        ],
    ]
    return buttons
