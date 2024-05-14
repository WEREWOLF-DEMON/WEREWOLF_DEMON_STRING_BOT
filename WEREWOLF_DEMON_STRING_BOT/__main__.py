import asyncio
import importlib

from pyrogram import idle

from WEREWOLF_DEMON_STRING_BOT import LOGGER, Anony
from WEREWOLF_DEMON_STRING_BOT.modules import ALL_MODULES


async def anony_boot():
    try:
        await Anony.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("WEREWOLF_DEMON_STRING.modules." + all_module)

    LOGGER.info(f"@{Anony.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping String Gen Bot...")
