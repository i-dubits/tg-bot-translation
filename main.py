import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from pathlib import Path

from IPython.core.debugger import set_trace

from aiogram.utils.helper import Helper, HelperMode, ListItem

from bot import config, messages, utils
from transformer import run_model

from IPython.core.debugger import set_trace
#from config import TOKEN, file_path_to_download
#from messages import MESSAGES
#from utils import Nst, Cycle

#from nst import nst_2 as nstk
#from run_cyclegan import RunCycle

SRC_vocab = None
TRG_vocab = None
model = None

logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(state = '*', commands=['start'])
async def process_start_command(message: types.Message):
    
    global SRC_vocab
    global TRG_vocab
    global model
    
    #set_trace()   
    run_model.init_vocab_and_model()
    
    await message.reply(messages.MESSAGES['start'])
    await utils.Translate.waiting_for_input_text.set()
    
@dp.message_handler(state = '*', commands=['help'])
async def process_help_command(message: types.Message):
    
    global SRC_vocab
    global TRG_vocab
    global model
    
    
    run_model.init_vocab_and_model()
    await message.reply(messages.MESSAGES['help'])
    await utils.Translate.waiting_for_input_text.set()
 

#Translate
#_______________________________


@dp.message_handler(state = utils.Translate.waiting_for_input_text)
async def procces_input_text(message: types.Message):
    
    input_text = message.text

    result =  run_model.translate_text(input_text)
    
    await message.answer(result)


# General handlers
#_______________________________
    

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
    
    
if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)