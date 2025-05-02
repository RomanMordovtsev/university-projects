import asyncio
import random

async def weather(): # Реализация асинхронности
    await asyncio.sleep(random.random())
    poss = ['sunny', 'cloudy', 'snowy', 'windy', 'foggy', 'frosty']
    return 'It was ' + random.choice(poss) + ' weather'

