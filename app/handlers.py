from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb


rt = Router()


@rt.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer(f'Hello and welcome, {message.from_user.first_name}!')


@rt.message(F.text == '/id')
async def cmd_start(message: Message):
    await message.answer(f'Your ID - {message.from_user.id}!')


@rt.message(F.text == '/photo')
async def cmd_photo(message: Message):
    await message.answer_photo(photo='https://desu.shikimori.one/uploads/poster/animes/55791/7a21a37de333ca74389a8bac35ff629b.jpeg',
                               caption='"Oshi no ko" season 2 is announced!')


# @dp.message(F.text == '/post')
# async def cmd_get_doc_id(message: Message):
#     await message.answer("Accepted!")
#     await bot.send_message(chat_id='515457460', text=message.text, caption='You have been sent a proposal')

@rt.message(F.text == '/anime')
async def anime(message: Message):
    await message.answer('Choose!', reply_markup=kb.main)


@rt.message(F.text == 'The 100 Girlfriends Who Really, Really, Really, Really, REALLY Love You')
async def watch(message: Message):
    await message.answer('Status: ongoing', reply_markup=kb.link_100_gf)


@rt.message(F.text == 'Death Note')
async def watch(message: Message):
    await message.answer('Status: aired in 2006-2007', reply_markup=kb.link_death_note)


@rt.message(F.text == 'Alya Sometimes Hides Her Feelings in Russian')
async def watch(message: Message):
    await message.answer('Status: will start airing in April 2024', reply_markup=kb.link_alya_rus)


@rt.message(F.text == 'Oshi no ko S1')
async def watch(message: Message):
    await message.answer('Status: aired in 2023', reply_markup=kb.link_oshi_no_ko)


@rt.message(F.text == '/template')
async def test(message: Message):
    await message.answer('''⁉️ Часто задаваемые вопросы:

1️⃣ Для чего этот бот?

2️⃣ Как попасть на интервью?

3️⃣ Когда был основан канал и для чего?

4️⃣ Сколько работает человек на канале?

5️⃣ У вас есть другие соцсети?
''', reply_markup=kb.answers)


@rt.callback_query(F.data == '1')
async def answer1(callback: CallbackQuery):
    await callback.answer("💬 Этот бот создан с целью облегчить игрокам стать участниками интервью на этом канале",
                          show_alert=True)


@rt.callback_query(F.data == '2')
async def answer1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('💬 Нажмите на кнопку «интервью» в главном меню чтобы узнать больше информации')


@rt.message(F.data == '/survey')
async def start(message: Message):
    await message.answer('What is your name?')


@rt.message(F.text)
async def start(message: Message):
    await message.answer('Nice!')




@rt.message()
async def echo(message: Message):
    await message.answer(f'What do you mean?')