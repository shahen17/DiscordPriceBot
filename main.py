import discord
import requests
import json
import http.client
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os

from asyncio import sleep as s
from keep_alive import keep_alive

from config import *

client = discord.Client(intents=discord.Intents.default())


def gas_track():
    my_api = Api_bsc
    response = requests.get(f'{my_api}')
    result = response.json()['result']
    result_format = json.dumps(result, indent=2)
    index1 = result_format.index('SafeGasPrice')
    index2 = result_format.index('ProposeGasPrice')
    index3 = result_format.index('FastGasPrice')
    index4 = result_format.index('UsdPrice')
    stat = result_format[index1:index2]
    stat2 = result_format[index4:200]
    statlist1 = []
    statlist2 = []
    statlist1.append(stat)
    statlist2.append(stat2)
    for i in statlist1:
        format_a = i.replace('"', '').replace(':', '').replace(',', '')
    for i in statlist2:
        format_b = i.replace('"', '').replace(':', '').replace(',', '').replace('}', '')
    return format_a


def bsc_price():
    my_api = Api_bsc
    response = requests.get(f'{my_api}')
    result = response.json()['result']
    result_format = json.dumps(result, indent=2)
    index1 = result_format.index('SafeGasPrice')
    index2 = result_format.index('ProposeGasPrice')
    index3 = result_format.index('FastGasPrice')
    index4 = result_format.index('UsdPrice')
    stat = result_format[index1:index2]
    stat2 = result_format[index4:200]
    statlist1 = []
    statlist2 = []
    statlist1.append(stat)
    statlist2.append(stat2)
    for i in statlist1:
        format_a = i.replace('"', '').replace(':', '').replace(',', '')
    for i in statlist2:
        format_b = i.replace('"', '').replace(':', '').replace(',', '').replace('}', '')
    return format_b


def price_doge():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    my_secretcmc = Api_cmc  # use apifile.env if program running outside replit
    parameters = {

        "symbol": "DOGE",

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': my_secretcmc,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        i = response.json()
        result_format = json.dumps(i, indent=2)
        index1 = result_format.index('price')
        index2 = result_format.index('volume_24h')
        stat = result_format[index1:index2]
        pricelist = []
        pricelist.append(stat)
        for i in pricelist:
            format_a = i.replace(',', '').replace('"', '').replace('price', '').replace(':', '')
        format_float = float(format_a)
        round_price = round(format_float, 3)

        return round_price




    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def price_sfm():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    my_secretcmc = Api_cmc  # use apifile.env if program running outside replit
    parameters = {

        "symbol": "SFM",

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': my_secretcmc,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        i = response.json()
        result_format = json.dumps(i, indent=2)
        index1 = result_format.index('price')
        index2 = result_format.index('volume_24h')
        stat = result_format[index1:index2]
        pricelist = []
        pricelist.append(stat)
        for i in pricelist:
            format_a = i.replace(',', '').replace('"', '').replace('price', '').replace(':', '')
        format_float = float(format_a)
        round_price = round(format_float, 10)

        return round_price




    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def price_btc():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    my_secretcmc = Api_cmc  # use apifile.env if program running outside replit
    parameters = {

        "symbol": "BTC",

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': my_secretcmc,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        i = response.json()
        result_format = json.dumps(i, indent=2)
        index1 = result_format.index('price')
        index2 = result_format.index('volume_24h')
        stat = result_format[index1:index2]
        pricelist = []
        pricelist.append(stat)
        for i in pricelist:
            format_a = i.replace(',', '').replace('"', '').replace('price', '').replace(':', '')
        format_float = float(format_a)
        round_price = round(format_float)

        return round_price

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def price_eth():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    my_secretcmc = Api_cmc  # use apifile.env if program running outside replit
    parameters = {

        "symbol": "ETH",

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': my_secretcmc,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        i = response.json()
        result_format = json.dumps(i, indent=2)
        index1 = result_format.index('price')
        index2 = result_format.index('volume_24h')
        stat = result_format[index1:index2]
        pricelist = []
        pricelist.append(stat)
        for i in pricelist:
            format_a = i.replace(',', '').replace('"', '').replace('price', '').replace(':', '')
        format_float = float(format_a)
        round_price = round(format_float)

        return round_price

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


@client.event
async def on_ready():
    print('Chicken bot is logged IN --BY SHAHEN--{0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gas'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="Gas fee in (USD)",
            value=gas_track(),
            inline=False,

        )
        await message.channel.send(embed=avc)

    if message.content.startswith('$bnb'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="BNB Price",
            value=bsc_price(),
            inline=False,

        )
        await message.channel.send(embed=avc)

    if message.content.startswith('$doge'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="DOGE Price",
            value=price_doge(),
            inline=False,

        )
        await message.channel.send(embed=avc)

    if message.content.startswith('$sfm'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="SAFEMOON Price",
            value=price_sfm(),
            inline=False,

        )
        await message.channel.send(embed=avc)

    if message.content.startswith('$btc'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="BITCOIN Price",
            value=price_btc(),
            inline=False,

        )
        await message.channel.send(embed=avc)

    if message.content.startswith('$eth'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="ETHERIUM Price",
            value=price_eth(),
            inline=False,

        )
        await message.channel.send(embed=avc)


keep_alive()
my_secret = Token
client.run(my_secret)





