import asyncio
import aiohttp
import json
import time

import prywatne

async def fetch(session, url, headers=None, params=None):
    async with session.get(url, headers=headers, params=params) as response:
        return await response.json()

async def main():
    weather_url = "https://weatherapi-com.p.rapidapi.com/current.json"
    weather_headers = {
        "X-RapidAPI-Key": prywatne.API_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
    }
    weather_params = [
        {"q": "Warsaw"}, {"q": "London"}, {"q": "Paris"}, {"q": "Berlin"},
        {"q": "Madrid"}, {"q": "Rome"}, {"q": "Moscow"},
        {"q": "Kiev"}, {"q": "Budapest"}, {"q": "Prague"},
    ]

    jokes_url = "https://dad-jokes.p.rapidapi.com/random/joke"
    jokes_headers = {
        "X-RapidAPI-Key": prywatne.API_KEY,
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
    }

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, weather_url, weather_headers, p) for p in weather_params]
        tasks += [fetch(session, jokes_url, jokes_headers) for _ in range(5)]
        return await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())
    print(json.dumps(result, indent=2))
    print(f'Execution time: {time.time() - start}')
