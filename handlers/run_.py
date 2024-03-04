from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.dinemic_kb import make_row_keyboard as mrk
from aiogram.fsm.state import StatesGroup, State
from .db import *


greeting = ["Привет! Если у тебя проблемы с памятью, тебе ко мне🗳️\nЧтобы получать уведолмения, нажми на кнопку 'Регистрация' ниже."]

router = Router()

class User_data(StatesGroup):
    ID=State()

@router.message(Command('start','choice','menu','help'))
async def cmd_start_menu(message: Message, state: FSMContext):
    try:    
        await state.clear()
        await message.answer(f'{greeting[0]}',reply_markup=mrk(['Регистрация']))
        await state.set_state(User_data.ID)
    except Exception as e: await message.answer(f'Ошибка вида: {e}')    
    

@router.message(User_data.ID, F.text.in_(['Регистрация']))
async def setting_departmant(message: Message, state: FSMContext):
    try:
        if check(message.from_user.id) is True: 
            register_user([str(message.from_user.id)])
            await message.answer(f'Регистрация прошла успешно📅!',reply_markup=ReplyKeyboardRemove())
            await state.clear()
        else:  
            await message.answer(f'Вы уже зарегистрированы', reply_markup=ReplyKeyboardRemove())
            await state.clear()  #получаем результаты голосования
    except Exception as e: await message.answer(f'Ошибка вида: {e}')        