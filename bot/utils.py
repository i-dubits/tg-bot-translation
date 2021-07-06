
from aiogram.dispatcher.filters.state import State, StatesGroup

class Translate(StatesGroup):
    waiting_for_input_text = State()
    waiting_for_translate_result = State()







