from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from more_itertools import chunked
import os, shelve

db = shelve.open("channels.db")

@Client.on_message(filters.command("setting"))
def set_stream_quality(c, m):
    try:
        for att in m.command:
            if att.startswith("audio"):
                os.environ["AUDIO_QUAL"] = att.split("=")[1]
            if att.startswith("video"):
                os.environ["VIDEO_QUAL"] = att.split("=")[1]
            if att.startswith("ffmpeg"):
                os.environ["FFMPEG"] = att.split("=")[1]
    except:
        pass
    aq = os.getenv("AUDIO_QUAL")
    vq = os.getenv("VIDEO_QUAL")
    ffmpeg = on.getenv("FFMPEG")
    m.reply(f"Thông tin cài đặt:\nAudio: `{aq}`\nVideo: `{vq}`\nffmpeg: `{ffmpeg}`")