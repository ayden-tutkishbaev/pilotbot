from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton)

main_kb = [
    [KeyboardButton(text='Oshi no ko S1'),
     KeyboardButton(text='The 100 Girlfriends Who Really, Really, Really, Really, REALLY Love You')],
    [KeyboardButton(text='Alya Sometimes Hides Her Feelings in Russian'),
     KeyboardButton(text='Death Note')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder="Все аниме:")

kb_link_100_gf = [[InlineKeyboardButton(text='Watch!',
                                        url='https://aniwave.to/watch/kimi-no-koto-ga-dai-dai-dai-dai-daisuki-na-100-nin-no-kanojo.7j048/ep-1')]]

kb_link_oshi_no_ko = [[InlineKeyboardButton(text='Watch!',
                                            url='https://aniwave.to/watch/oshi-no-ko2.4q1jm/ep-1')]]

kb_link_alya_rus = [[InlineKeyboardButton(text="Watch trailer!",
                                          url='https://www.youtube.com/watch?v=TemtlPERSfk')]]

kb_link_death_note = [[InlineKeyboardButton(text='Watch series!',
                                            url='https://aniwave.to/watch/death-note.z02/ep-1')],
                      [InlineKeyboardButton(text='Watch Relight!',
                                            url='https://aniwave.to/watch/death-note-relight.jw02/ep-1')]]

link_100_gf = InlineKeyboardMarkup(inline_keyboard=kb_link_100_gf)

# kb_link_answers = [[InlineKeyboardButton(text='1'), InlineKeyboardButton(text='2'), InlineKeyboardButton(text='3'),
#                     InlineKeyboardButton(text='4'), InlineKeyboardButton(text='5')]]

answers = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='1'), InlineKeyboardButton(text='2', callback_data='2')],
    [InlineKeyboardButton(text='3', callback_data='3'), InlineKeyboardButton(text='4', callback_data='4')],
    [InlineKeyboardButton(text='5', callback_data='5')]
])



link_100_gf = InlineKeyboardMarkup(inline_keyboard=kb_link_100_gf)
link_oshi_no_ko = InlineKeyboardMarkup(inline_keyboard=kb_link_oshi_no_ko)
link_alya_rus = InlineKeyboardMarkup(inline_keyboard=kb_link_alya_rus)
link_death_note = InlineKeyboardMarkup(inline_keyboard=kb_link_death_note)