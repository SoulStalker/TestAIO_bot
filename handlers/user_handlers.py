from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

# initializing module level router
router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """ handler for start command """
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    """ handler for help command """
    await message.answer(text=LEXICON_RU['/help'])
