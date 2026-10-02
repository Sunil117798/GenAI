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


async def get_user_with_id(user_id: int):
    try:

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{API_URL}/users/{user_id}"
            )

            response.raise_for_status()

            return response.json()

    except httpx.HTTPError as error:

        print(f"API request failed: {error}")

        return []

async def get_emails():
    try:

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{API_URL}/users/{email}"
            )

            response.raise_for_status()

            return response.json()

    except httpx.HTTPError as error:

        print(f"API request failed: {error}")

        return []


async def main():

    users = await get_users()

    emails = [
        user["email"]
        for user in users
    ]

    # print(emails)

    user = await get_user_with_id(999999)
    print(user)
    
    # user = await get_user_with_email("Sincere@april.biz")
    # print(user)
    


asyncio.run(main())