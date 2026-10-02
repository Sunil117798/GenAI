import os
import httpx
import asyncio
from dotenv import load_dotenv


load_dotenv()


API_URL = os.getenv(
    "API_URL",
    "https://jsonplaceholder.typicode.com"
)


async def get_users() -> list[dict]:

    try:

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{API_URL}/users"
            )

            response.raise_for_status()

            return response.json()

    except httpx.HTTPError as error:

        print(f"API request failed: {error}")

        return []


async def get_user_by_id(user_id:int)->dict:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{API_URL}/users/{user_id}"
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as error:
        print(f"API request failed: {error}")
        return {}





async def main():
    results = await asyncio.gather(
        get_users(),
        get_user_by_id(1)
    )
    
    users, posts = results
    print(users)
    print(posts)


asyncio.run(main())