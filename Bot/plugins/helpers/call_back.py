#!/usr/bin/env python3
# This is bot coded by FoxmanTech and used for educational purposes only
# https://github.com/samebanezar001/File-Link-Bot
# Copyright FOXMANTECH
# Thank you https://github.com/pyrogram/pyrogram
from bot.filetocloud import CloudBot
from bot.plugins.helpers.dowloader import fileDownload


@CloudBot.on_callback_query()
async def server_selection(client, server):
    await fileDownload(client, server)
