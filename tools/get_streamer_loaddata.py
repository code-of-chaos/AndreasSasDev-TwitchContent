# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from twitchAPI.twitch import Twitch, TwitchUser
from twitchAPI.helper import first
import asyncio
import os
from contextlib import asynccontextmanager

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
@asynccontextmanager
async def get_twitch_connection(client_id, client_secret):
    twitch = await Twitch(client_id, client_secret)

    try:
        yield twitch

    finally:
        await twitch.close()

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
async def main():
    async with get_twitch_connection(os.environ.get("APP_CLIENT_ID"), os.environ.get("APP_CLIENT_SECRET")) as twitch:
        user:TwitchUser = await first(twitch.get_users(logins="AndreasSasDev"))

        print(
            user.id, user.display_name
        )

    return

if __name__ == '__main__':
    asyncio.run(main())