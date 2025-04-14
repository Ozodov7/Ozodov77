import aiogram.types
from aiogram import Bot,Dispatcher,Router,F
from aiogram.filters import Command
from aiogram.handlers import CallbackQueryHandler
from aiogram.types import Message
from asyncio import run
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
def get_inline()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="UZ Uzbekiston",callback_data="UZ")
    inline.button(text="KZ Qazaqiston", callback_data="KZ")
    inline.button(text="KG Qirgiz", callback_data="KG")
    inline.button(text="UAE UnitedArabEmirets", callback_data="UAE")
    inline.button(text="RU Russia", callback_data="RU")
    # inline.button(text="Ha", callback_data="Ha")
    # inline.button(text="Yo'q", callback_data="Yo'q")
    inline.adjust(2)
    return inline.as_markup()

def get_ha_yoq() ->ReplyKeyboardMarkup:
    kb=ReplyKeyboardBuilder()
    kb.button(text="Ha")
    kb.button(text="Yo'q")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def tozalash()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Ha",callback_data="Ha")
    inline.button(text="Yo'q",callback_data="Yo'q")
    return inline.as_markup()


dd=Dispatcher()
tokenim="7794731820:AAFHKLqR6U7xVd9-70igF2J_3N7Nlov15Hg"
global tanlov

#@dd.startup()
my_router=Router()
dd.include_router(my_router)
@my_router.startup()
async def bot_ishlaganda(bot:Bot):
    await bot.send_message(chat_id="7783577416",text="Bot ishladi")
@my_router.shutdown()
async def bot_toxtaganda(bot:Bot):
    await bot.send_message(chat_id="7783577416",text="Bot to'xtadi")
@my_router.message(Command('start'))
async def start_boslganda(m:Message):
    await m.answer("Xush kelibsiz")
    await m.answer("Biror davlat tanla?:",reply_markup=get_inline())
from aiogram.handlers import CallbackQueryHandler

@my_router.callback_query(F.data == "UZ")
async  def UZ_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Sen haqiqatdan Uzbekistonni tanladingmi?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov = "Uzbekiston"

@my_router.callback_query(F.data == "KZ")
async  def KZ_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Sen haqiqatdan Qazaqistonni tanladingmi?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov = "Qazaqiston"

@my_router.callback_query(F.data == "KG")
async  def KG_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Sen haqiqatdan Qirg'izni tanladingmi?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov = "Qirg'iz"

@my_router.callback_query(F.data == "UAE")
async  def UAE_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Sen haqiqatdan UAEni tanladingmi?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov = "UAE"

@my_router.callback_query(F.data == "RU")
async  def RU_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Sen haqiqatdan Rassiyani tanladingmi?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    global tanlov
    tanlov = "Rassiya"

@my_router.callback_query(F.data == "Ha")
async  def Ha_tanlanganda(call:CallbackQuery):
    await call.message.delete_reply_markup()
    # await call.message.delete()
    global tanlov
    matn=str(tanlov)
    await call.message.edit_text(f"{tanlov}ni tanlading!")
    # await call.message.edit_reply_markup(reply_markup=tozalash())




@my_router.callback_query(F.data == "Yo'q")
async  def Yoq_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Biror davlat tanla?")
    await call.message.edit_reply_markup(reply_markup=get_inline())






@my_router.message(F.text.lower()=="Ha")
async def ha_tanlanganda(m:Message):
    await m.answer("Ooooo vatanparvar",reply_markup=aiogram.types.ReplyKeyboardRemove())
@my_router.message(F.text.lower()=="Yo'q")
async def yoq_tanlanganda(m:Message):
    await m.answer("Greencardda omad😂👌",reply_markup=aiogram.types.ReplyKeyboardRemove())
@my_router.message()
async def xabar_kelganda(m:Message,bot:Bot):
    await m.copy_to(chat_id=m.from_user.id)

    await m.copy_to(chat_id="7783577416")
    await bot.send_message(chat_id="7783577416",\
          text=f"{m.from_user.full_name} \
sizning botingizga '{m.text}' deb yozdi",)




async def start():
    botim=Bot(token=tokenim)
    dd.startup.register(bot_ishlaganda)
    await dd.start_polling(botim)







run(start())
#7783577416
#7794731820:AAFHKLqR6U7xVd9-70igF2J_3N7Nlov15Hg