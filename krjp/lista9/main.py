import asyncio
import aiohttp
import json

import matplotlib.pyplot as plt
 
class RequestError(Exception):
    pass

async def fetch(session, url):
    async with session.get(url) as response:
        try:
            return await response.json()
        except aiohttp.client_exceptions.ContentTypeError:
            raise RequestError(f"Cannot decode response body as JSON: {response}")
        except aiohttp.client_exceptions.ClientError as e:
            raise RequestError(f"Client error: {e}")
        except aiohttp.web.HTTPServerError as e:
            raise RequestError(f"Server error: {e}")
        except aiohttp.web.HTTPException as e:
            raise RequestError(f"Unknown error: {e}")
        except Exception as e:
            raise RequestError(f"Unknown error: {e}")

async def get_from_urls(*urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        # Flatten list of lists
        return [item for response in responses for item in response]

def plot_data(data):
    dates = [item["data"] for item in data]
    prices = [item["cena"] for item in data]
    plt.plot(dates, prices)
    plt.xlabel("Data")
    plt.ylabel("Cena")
    plt.title("Cena złota")
    plt.show()

def main():
    gold_prices_urls = [
        "https://api.nbp.pl/api/cenyzlota/2021-01-01/2021-12-31/",
        "https://api.nbp.pl/api/cenyzlota/2022-01-01/2022-12-31/",
    ]
    gold_prices = asyncio.run(get_from_urls(*gold_prices_urls))
    plot_data(gold_prices)

if __name__ == "__main__":
    main()
