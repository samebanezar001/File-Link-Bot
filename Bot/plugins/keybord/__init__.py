#!/usr/bin/env python3
# This is bot coded by FoxmanTech and used for educational purposes only
# https://github.com/samebanezar001/File-Link-Bot
# Copyright FOXMANTECH
# Thank you https://github.com/pyrogram/pyrogram

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def server_select():
    upload_selection = [
        [
            InlineKeyboardButton(
                "MixDrop",
                callback_data="MixDrop"
            ),
            InlineKeyboardButton(
                "File.io",
                callback_data="File.io"
            )
        ],
    ]
    return InlineKeyboardMarkup(upload_selection)
