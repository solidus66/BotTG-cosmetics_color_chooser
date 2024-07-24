import telegram
from telegram.ext import Updater, CommandHandler
import random
from webserver import keep_alive

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telegram.Bot(token=BOT_TOKEN)

commands = [
    # telegram.BotCommand('about', 'Что я такое....'),
    telegram.BotCommand('eye_shadow', 'Выбрать цвет тенюшек'),
    telegram.BotCommand('eyelash', 'Выбрать цветную тушь'),
    telegram.BotCommand('liner', 'Выбрать подводку'),
    telegram.BotCommand('sequins', 'Выбрать блёстки'),
    # telegram.BotCommand('joke', 'Получить шутку'),
]

bot.set_my_commands(commands)

# def about(update, context):
#   context.bot.send_message(
#     chat_id=update.message.chat_id,
#     text=
#     "Приветик, дорогуша!!!☺️❤️✨\n\nЯ - бот, который поможет тебе выбрать цвет косметики "
#     "на сегодня. Я работаю с помощью сил рандома, так что использовать меня повседневно "
#     "- странная затея. Зато я отлично помогу, если ты хочешь выполнить "
#     "челлендж!\n\nЕсть одно но - в моём распоряжении <b>ограниченный набор</b> цветов, "
#     "так как я был заточен под одного конкретного человечка.\n\nЕщё я умею присылать "
#     "анекдоты, но они весьма специфичные, странные и без нормальных знаков "
#     "препинания.....\n\nНаслаждайся!\n\nПо всем вопросам к создателю - "
#     "<b>@solidus66</b>",
#     parse_mode='HTML')

# def get_anekdote():
#   connection = sqlite3.connect('anekdot2.db')
#   cursor = connection.cursor()
#   cursor.execute("SELECT * FROM anekdot ORDER BY RANDOM() LIMIT 1")
#   anekdote_row = cursor.fetchone()
#   connection.close()
#   if anekdote_row:
#     anekdote = anekdote_row[1]
#   else:
#     anekdote = "К сожалению, в базе данных пока нет анекдотов"
#   return anekdote

# def send_anekdote(update, context):
#   anekdote = get_anekdote()
#   context.bot.send_message(chat_id=update.effective_chat.id, text=anekdote)


def eye_shadow_color(update, context):
    palettes = {
        'Revolution Soph X': [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
            '21',
            '22',
            '23',
            '24',
        ],
        'Nude(скинь жопу) Huda Beauty Story': [
            '1 (BARE)', '2 (CRAVE)', '3 (PLAY)', '4 (FANTASY)',
            '5 (LOVE BITE)', '6 (SPANKED)', '7 (LACE)', '8 (DAYDREAM)',
            '9 (TICKLE)', '10 (EXCITE)', '11 (INFATUATED)', '12 (KINKY)',
            '14 (SECRET)', '15 (TEASE)', '16 (RAW)', '17 (CHARMED)',
            '18 (TEDDY)'
        ],
        'NYX(блин, отзеркалить бы) Off Tropic':
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'Revolution Tasty Avocado': [
            '1 (SMASH)', '2 (TOAST)', '3 (AVO)', '4 (CALIFORNIA)',
            '5 (SMOOTHIE)', '6 (HALF)', '7 (HASS)', '8 (GUACAMOLE)',
            '9 (BRUNCH)', '10 (GREEN GOLD)', '11 (MOUSSE)', '12 (STONE)',
            '13 (CREAMY)', '14 (BITE)', '15 (PEAR)', '16 (FOODY)', '17 (SEED)',
            '18 (LIME)'
        ],
        'Influence Luna': [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
            '13', '14', '15'
        ],
        'Nude EVELINE':
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        'Beauty Glazed Color Shades': [
            '1 на первом развороте (DREAM)',
            '2 на первом развороте (IVORY)',
            '3 на первом развороте (BROWNIE)',
            '4 на первом развороте (STRAW)',
            '5 на первом развороте (LEMON)',
            '6 на первом развороте (GOLD)',
            '7 на первом развороте (SORREL)',
            '8 на первом развороте (CAROL)',
            '9 на первом развороте (TOPAZ)',
            '10 на первом развороте (SUNRISE)',
            '11 на первом развороте (AUBURN)',
            '12 на первом развороте (CHILI)',
            '13 на первом развороте (YOLK)',
            '14 на первом развороте (AMBER)',
            '15 на первом развороте (PERSIMMON)',
            '16 на первом развороте (SUNSET)',
            '17 на первом развороте (FLESH)',
            '18 на первом развороте (SILKY)',
            '19 на первом развороте (COFFEE)',
            '20 на первом развороте (ORANGE)',
            '21 на первом развороте (CITRINE)',
            '22 на первом развороте (CLAY)',
            '23 на первом развороте (TANK)',
            '24 на первом развороте (CHESTNUT)',
            '1 на втором развороте (BEIGE)',
            '2 на втором развороте (PEARL)',
            '3 на втором развороте (CAMEO)',
            '4 на втором развороте (KHAKI)',
            '5 на втором развороте (MOONSTONE)',
            '6 на втором развороте (SAHARA)',
            '7 на втором развороте (PRINCESS)',
            '8 на втором развороте (UMBER)',
            '9 на втором развороте (DUBAI)',
            '10 на втором  развороте (BISQUE)',
            '11 на втором развороте (SAND BROWN)',
            '12 на втором  развороте (RUSTIC)',
            '13 на втором развороте (BARBIE)',
            '14 на втором  развороте (ROSE QUARTZ)',
            '15 на втором развороте (RUBY)',
            '16 на втором  развороте (POPPY)',
            '17 на втором развороте (PURPLE)',
            '18 на втором  развороте (GARNET)',
            '19 на втором развороте (PINK)',
            '20 на втором  развороте (VIOLET)',
            '21 на втором  развороте (MULBERRY)',
            '22 на втором развороте (PLUM)',
            '23 на втором  развороте (AMETHYST)',
            '24 на втором развороте (BLACK)',
            '1 на третьем развороте (DIAMOND)',
            '2 на третьем развороте (JASMINE)',
            '3 на третьем развороте (CANARY)',
            '4 на третьем развороте (MUSTARD)',
            '5 на третьем развороте (MOSS)',
            '6 на третьем развороте (APPLE GREEN)',
            '7 на третьем развороте (MEADOW)',
            '8 на третьем развороте (OLIVE)',
            '9 на третьем развороте (AQUA)',
            '10 на третьем развороте (JUNGLE)',
            '11 на третьем развороте (EMERALD)',
            '12 на третьем развороте (CHROME)',
            '13 на третьем развороте (ICE SNOW)',
            '14 на третьем развороте (OCEAN)',
            '15 на третьем развороте (SKY BLUE)',
            '16 на третьем развороте (MARINE)',
            '17 на третьем развороте (LILAC)',
            '18 на третьем развороте (AZURE)',
            '19 на третьем развороте (NAVY)',
            '20 на третьем развороте (MERMAID)',
            '21 на третьем развороте (AURORA)',
            '22 на третьем развороте (DUTCH)',
            '23 на третьем развороте (ROYAL BLUE)',
            '24 на третьем развороте (BLUE BLACK)',
        ],
        'VIVIENNE SABO harmonia':
        ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
        'HOJO':
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    }
    chosen_palette = random.choice(list(palettes.keys()))
    colors = palettes[chosen_palette]
    chosen_color = random.choice(colors)

    appeals = [
        'Красотка,', 'Принцесса,', 'Тыковка,', 'Королева,', 'Красавица,',
        '*присвистывание* Вашей маме зять не нужен? Ой, о чём это я... тут',
        'Солнце,', 'Хэй,', 'Милашкаrrr,', 'Мисс шугар мамми,',
        'Приветик! А тут', 'Прелесть,', 'Ухх какая штучка)0) Тут', 'Мисс,',
        'Юная леди,'
    ]
    chosen_appeal = random.choice(appeals)

    pharses = [
        'Ты настолько прекрасна, что тебя хочется сравнить с цветами роз!',
        ' ',
        'Хорошего дня, дорогуша!',
        ' ',
        'Вы выглядите невероятно красиво!!!',
        ' ',
        'Вам стоит попробовать себя в роли звезды, такое нужно показать всему миру! ',
        ' ',
        'Сегодня Вы всех затмили своей красотой, которая дана Вам самой природой! ',
        ' ',
        'Ты ослепляешь своей красотой словно солнце!',
        ' ',
        'Выглядишь невероятно! Наверное песня «Ах какая женщина» была написана о тебе!',
        ' ',
        'А Вам кто-нибудь говорил, что Вы само совершенство?!',
        ' ',
        ' ',
        ' ',
        'Такая женщина как Вы, достойна спать на хрустальной кровати, есть из золотой посуды, и ходить по бриллиантовым дорожкам! ',
        ' ',
        ' ',
        ' ',
        'Вы именно та женщина, за которую может сражаться весь мир! ',
        ' ',
        ' ',
        ' ',
        'Быть женщиной это великий труд, и он Вам под силу! ',
        ' ',
        'Заходит как-то улитка в бар. Бармен ей говорит: «У нас строгая политика насчёт улиток», и вышвыривает её из бара. Через неделю улитка входит в бар и говорит: «Ты нахрена это сделал?»',
        ' ',
    ]
    chosen_pharse = random.choice(pharses)

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=
        f"{chosen_appeal} для тебя выбрана палетка <b>{chosen_palette}</b> и в ней цвет теней <b>№{chosen_color}</b>!\n\n{chosen_pharse}",
        parse_mode='HTML')


def eyelash_color(update, context):
    colors = [
        'зелёный', 'синий', 'винишковый розовый', 'винишковый коричневый',
        'винишковый белый', 'винишковый чёрный', 'винишковый фиолетовый',
        'винишковый синий'
    ]
    chosen_color = random.choice(colors)
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Используй сегодня <b>{chosen_color}</b> цвет туши",
        parse_mode='HTML')


def liner_color(update, context):
    colors = [
        'жёлтую', 'синюю', 'голубую', 'красную', 'белую', 'чёрную',
        'оранжевую', 'персиковую', 'сиреневую', 'салатовую', 'розовую'
    ]
    chosen_color = random.choice(colors)

    appeals = [
        ' ', ' ', ', принцесса', ' ', ' ', ', королева', ' ', ', красотка',
        ', солнце', ' ', ' ', ' ', ', милашкаrrr', ' ', ' ', ' ', ', прелесть',
        ' ', ' ', ' ', ' ', ', мисс', ', юная леди', ' ', ' ', ' '
    ]
    chosen_appeal = random.choice(appeals)

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Используй сегодня <b>{chosen_color}</b> подводку{chosen_appeal}",
        parse_mode='HTML')


def sequins_color(update, context):
    colors = [
        'нео матрицу синь', 'розовый понос единорога',
        'белоснежную рыготню снегурочки', 'блестючку из пуговки', 'EVA MOSAIC'
    ]
    chosen_color = random.choice(colors)

    appeals = [
        ' ', ' ', ', принцесса', ' ', ' ', ', королева', ' ', ', красотка',
        ', солнце', ' ', ' ', ' ', ', милашкаrrr', ' ', ' ', ' ', ', прелесть',
        ' ', ' ', ' ', ' ', ', мисс', ', юная леди', ' ', ' ', ' '
    ]
    chosen_appeal = random.choice(appeals)

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Сегодня намазюкай <b>{chosen_color}</b>{chosen_appeal}",
        parse_mode='HTML')


updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(CommandHandler('eye_shadow', eye_shadow_color))
dispatcher.add_handler(CommandHandler('eyelash', eyelash_color))
dispatcher.add_handler(CommandHandler('liner', liner_color))
dispatcher.add_handler(CommandHandler('sequins', sequins_color))
# dispatcher.add_handler(CommandHandler('joke', send_anekdote))

keep_alive()
updater.start_polling()
updater.idle()