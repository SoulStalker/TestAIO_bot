from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LexiconRu

# initializing module level router
router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """ handler for start command """
    await message.answer(text=LexiconRu.start)


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    """ handler for help command """
    await message.answer(text=LexiconRu.help)
