from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LexiconRu

# initializing module level router
router = Router()


@router.message()
async def other_handler(message: Message):
    """ handler for any not command messages """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LexiconRu.no_echo)
