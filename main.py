import asyncio,logging
from aiogram import Bot,Dispatcher
from handlers import except_, run_
from handlers.DB import *


logging.basicConfig(level=logging.INFO)

# Настройка бота
bot = Bot(token)
dp = Dispatcher()

async def sending(): #функция цикличной рассылки оповещений
    try:
        while True:
            if check_for_day(get_dates()) is True:
                list_=get_users() #присваевыем значение функции локальному списку
                for item in list_: 
                    if item: await bot.send_message(chat_id=int(item[0]), text=f'Конечно! Вот интересный факт о котах: У взрослого кота в среднем 32 мускула контролируют уши 🐱 Эти мускулы позволяют коту поворачивать уши на 180 градусов и независимо друг от друга направлять в любую сторону для более точного прослушивания и понимания окружающего мира. Коты действительно великолепны! 😺👂')
            await asyncio.sleep(3500) 
    except KeyboardInterrupt as e: print(f'Ошибка: {e}')

async def main(): #основная функция системы
    dp.include_router(run_.router)
    dp.include_router(except_.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    
try: #последователльная обработка функциий
    if __name__ == '__main__': 
            event_loop = asyncio.get_event_loop() #цикл событий
            tasks_list = [event_loop.create_task(sending()), event_loop.create_task(main())] #список поручений
            wait_tasks = asyncio.wait(tasks_list) #ожидание выпонения
            event_loop.run_until_complete(wait_tasks) #асинхронное выпонение
except KeyboardInterrupt as e: 
    event_loop.close() #закрытие
    print(f'Работа приостановлена......') #прерывание через Ctrl+C
except Exception as e: print(f'Ошибка вида: {e}.....') #общая обработа ошибок
