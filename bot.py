#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging
from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Please remember to grab a token from Botfather
telegram_api_token = 'YOUR TOKEN HERE'

@run_async
def fiveday(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416W5.gif")
    bot.sendPhoto(chat_id, photo="https://icons.wunderground.com/data/images/at201614_5day.gif")
    
@run_async
def threeday(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416W.gif")
    bot.sendPhoto(chat_id, photo="https://icons.wunderground.com/data/images/at201614.gif")

@run_async
def wind(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416R.gif")

@run_async
def swath(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416S.gif")

@run_async
def trop(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416_PROB34_F24.gif")

@run_async
def trop3(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416_PROB34_F72.gif")

@run_async
def trop5(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416_PROB34_F120.gif")

@run_async
def hurr(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416_PROB64_F24.gif")

@run_async
def hurr3(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416_PROB64_F72.gif")

@run_async
def hurr5(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="http://www.nhc.noaa.gov/storm_graphics/AT14/AL1416_PROB64_F120.gif")

@run_async
def advisory(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendMessage(chat_id, text='<a href="http://www.nhc.noaa.gov/text/refresh/MIATCPAT4+shtml/">Click here for the latest advisory on Matthew</a>', parse_mode="HTML")

@run_async
def discussion(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendMessage(chat_id, text='<a href="http://www.nhc.noaa.gov/text/refresh/MIATCDAT4+shtml/">Click here for the latest discussion of Matthew</a>', parse_mode="HTML")

@run_async
def windtable(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendMessage(chat_id, text='<a href="http://www.nhc.noaa.gov/text/refresh/MIAPWSAT4+shtml/">Click here for wind speed probability tables for Matthew</a>', parse_mode="HTML")

@run_async
def satx1(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="https://icons.wunderground.com/data/images/at201614_sat.jpg")

@run_async
def satx2(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="https://icons.wunderground.com/data/images/at201614_sat_2.jpg")
    
@run_async
def satx3(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id, photo="https://icons.wunderground.com/data/images/at201614_sat_1.jpg")

@run_async
def radar(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendVideo(chat_id, video="https://radblast.wunderground.com/cgi-bin/radar/WUNIDS_map?station=CLX&brand=wui&num=10&delay=15&type=N0R&frame=0&scale=1.000&noclutter=1&showstorms=0&mapx=400&mapy=240&centerx=400&centery=240&transx=0&transy=0&showlabels=1&severe=0&rainsnow=0&lightning=0&smooth=1&rand=24597990&lat=32.77650070&lon=-79.93051910&label=Charleston%2C+SC")

@run_async
def radar2(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendVideo(chat_id, video="https://radblast.wunderground.com/cgi-bin/radar/WUNIDS_map?station=CLX&brand=wui&num=10&delay=15&type=N0Z&frame=0&scale=1.000&noclutter=1&showstorms=0&mapx=400&mapy=240&centerx=400&centery=240&transx=0&transy=0&showlabels=1&severe=0&rainsnow=0&lightning=0&smooth=1&rand=24597992&lat=32.77650070&lon=-79.93051910&label=Charleston%2C+SC")

@run_async
def musto(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendSticker(chat_id, sticker="BQADAQADTgEAAtZy8AWDUnrbceWhXAI")

@run_async
def radarloop(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendVideo(chat_id=chat_id, video="https://icons.wunderground.com/data/storm_radar/at201614_radar.gif")

@run_async
def model(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id=chat_id, photo="https://icons.wunderground.com/data/images/at201614_model.gif")

@run_async
def ensemble(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id=chat_id, photo="https://icons.wunderground.com/data/images/at201614_ensmodel.gif")

@run_async
def sat2vis(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id=chat_id, photo="http://www.ssd.noaa.gov/PS/TROP/floaters/14L/imagery/vis0-lalo.gif")

@run_async
def sat2sw(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id=chat_id, photo="http://www.ssd.noaa.gov/PS/TROP/floaters/14L/imagery/swir0-lalo.gif")

@run_async
def sat2wv(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id=chat_id, photo="http://www.ssd.noaa.gov/PS/TROP/floaters/14L/imagery/wv0-lalo.gif")
    
@run_async
def sat2rgb(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="upload_photo")
    bot.sendPhoto(chat_id=chat_id, photo="http://www.ssd.noaa.gov/PS/TROP/floaters/14L/imagery/rgb0-lalo.gif")
    
@run_async
def center(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, action="find_location")
    res = requests.get("http://www.nhc.noaa.gov/index-at.xml")
    soup = BeautifulSoup(res.content, 'html.parser')
    ll_raw = soup.find_all('nhc:center')[0].string
    ll = ll_raw.split(', ')
    lat = float(ll[0])
    log = float(ll[1])
    bot.sendLocation(chat_id, latitude=lat, longitude=log)

# Error Handler
@run_async
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    u = Updater(token=telegram_api_token)
    d = u.dispatcher
    d.add_handler(CommandHandler('track', threeday))
    d.add_handler(CommandHandler('forecast', fiveday))
    d.add_handler(CommandHandler('center', center))
    d.add_handler(CommandHandler('windfield', wind))
    d.add_handler(CommandHandler('windswath', swath))
    d.add_handler(CommandHandler('tropwind', trop))
    d.add_handler(CommandHandler('tropwind3', trop3))
    d.add_handler(CommandHandler('tropwind5', trop5))
    d.add_handler(CommandHandler('hurrwind', hurr))
    d.add_handler(CommandHandler('hurrwind3', hurr3))
    d.add_handler(CommandHandler('hurrwind5', hurr5))
    d.add_handler(CommandHandler('advisory', advisory))
    d.add_handler(CommandHandler('discussion', discussion))
    d.add_handler(CommandHandler('windtable', windtable))
    d.add_handler(CommandHandler('musto', musto))
    d.add_handler(CommandHandler('sat', satx1))
    d.add_handler(CommandHandler('satzoom', satx2))
    d.add_handler(CommandHandler('satzoomzoom', satx3))
    d.add_handler(CommandHandler('radarchs', radar))
    d.add_handler(CommandHandler('radarchsregion', radar2))
    d.add_handler(CommandHandler('radarmatt', radarloop))
    d.add_handler(CommandHandler('model', model))
    d.add_handler(CommandHandler('ensemble', ensemble))
    d.add_handler(CommandHandler('sat2visible', sat2vis))
    d.add_handler(CommandHandler('sat2shortwave', sat2sw))
    d.add_handler(CommandHandler('sat2watervapor', sat2wv))
    d.add_handler(CommandHandler('sat2rgb', sat2rgb))

    d.add_error_handler(error)

    u.start_polling()
    u.idle()

if __name__ == '__main__':
    main()
