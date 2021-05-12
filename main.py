import telebot
from telebot import types
from config import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Начать')
    markup.add(button)
    message = bot.send_message(message.chat.id,
                               'Привет, ' + message.from_user.first_name + '!\nДавайте найдем для вас работу.\nЖмите начать.',
                               reply_markup=markup)
    bot.register_next_step_handler(message, type_of_work)


@bot.message_handler(content_types=['text'])
def type_of_work(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Работа из дома')
    button2 = types.KeyboardButton('Разъездная работа')
    button3 = types.KeyboardButton('Работа в офисе')
    markup.add(button1, button2, button3)
    message = bot.send_message(message.chat.id,
                               'Выберите желаемый тип работы.',
                               reply_markup=markup)
    bot.register_next_step_handler(message, vacancies)


@bot.message_handler(content_types=['text'])
def vacancies(message):
    if message.text == 'Работа из дома':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Оператор по продаже услуг бизнесу по входящим заявкам.')
        btn2 = types.KeyboardButton('Оператор по продаже услуг бизнесу.')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        message = bot.send_message(message.chat.id,
                                   'Найдено 2 вакансии. Выберите подходящую:',
                                   reply_markup=markup)

    elif message.text == 'Разъездная работа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Продавец-консультант в городе Москва')
        btn2 = types.KeyboardButton('Представитель в городе Москва')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        message = bot.send_message(message.chat.id,
                                   'Найдено 2 вакансии. Выберите подходящую:',
                                   reply_markup=markup)

    elif message.text == 'Работа в офисе':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Консультант Тинькофф Бизнес в городе Москва. С опытом от 6 месяцев')
        btn2 = types.KeyboardButton('Консультант Тинькофф Банк (офис)')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        message = bot.send_message(message.chat.id,
                                   'Найдено 2 вакансии. Выберите подходящую:',
                                   reply_markup=markup)
    elif message.text == '/start':
        start(message)
    else:
        message = bot.send_message(message.chat.id,
                                   'Выберите вакансию')
    bot.register_next_step_handler(message, descriptions)


@bot.message_handler(content_types=['text'])
def descriptions(message):
    if message.text == 'Оператор по продаже услуг бизнесу по входящим заявкам.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Откликнуться')
        back = types.KeyboardButton('Назад')
        markup.add(btn)
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Условия:\n'
                         ' ✅Работа из дома. Не тратите время и деньги на дорогу в офис. Работаете там, где удобно\n'
                         ' ✅Звонки по интернету Звонки в рабочей системе компании без дополнительных затрат\n'
                         ' ✅С 9 до 21 по Москве Вы сами выбираете удобный график и согласовываете с руководителем\n'
                         ' ✅Всему научим Мы подготовили для вас много полезного материала\n'
                         '-----------------------------------------------------------------\n'
                         '💰Вознаграждение:\n'
                         'От 50 000 ₽ в месяц, если работаете 40 часов в неделю\n'
                         'Вознаграждение полностью сдельное\n'
                         'Фиксированная часть до 30 000\n'
                         'Бонус за каждого привлеченного клиента\n', reply_markup=markup)
        bot.register_next_step_handler(message, respond)

    elif message.text == 'Оператор по продаже услуг бизнесу.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Откликнуться')
        back = types.KeyboardButton('Назад')
        markup.add(btn)
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Условия:\n'
                         ' ✅Удобство и комфорт. Не тратите время и деньги на дорогу в офис. Работаете там, где удобно\n'
                         ' ✅Звонки по интернету. Звонки в рабочей системе компании без дополнительных затрат\n'
                         ' ✅С 10 до 19 по Москве. В будние дни\n'
                         ' ✅Всему научим. Мы подготовили для вас много полезного материала\n'
                         '-----------------------------------------------------------------\n'
                         '💰Вознаграждение:\n'
                         'От 60 000 ₽ в месяц, если работаете 30 часов в неделю\n'
                         'Вознаграждение полностью сдельное\n'
                         'Фиксированная часть до 40 000\n'
                         'Бонус за каждого привлеченного клиента\n', reply_markup=markup)
        bot.register_next_step_handler(message, respond)

    elif message.text == 'Продавец-консультант в городе Москва':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Откликнуться')
        back = types.KeyboardButton('Назад')
        markup.add(btn)
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Условия:\n'
                         ' ✅Гибкий график. Сможете совмещать работу с учебой и другими повседневными делами\n'
                         ' ✅Корпоративные условия по продуктам. Выгодные тарифы на всю линейку Тинькофф\n'
                         ' ✅Прозрачная система повышения. Чем выше показатели, тем больше премия и быстрее карьерный рост\n'
                         ' ✅Оплачиваемая корпоративная стажировка. Заплатим бонус за успешное прохождение стажировки\n'
                         '-----------------------------------------------------------------\n'
                         '💰Вознаграждение:\n'   
                         'От 47 000 ₽ в месяц, если работаете 40 часов в неделю\n'
                         'Фиксированный оклад после оформления в штат\n'
                         'Бонус за каждый проданный продукт\n'
                         'Бонус за перевыполнение плана продаж\n'
                         'Неограниченный доход\n', reply_markup=markup)
        bot.register_next_step_handler(message, respond)

    elif message.text == 'Представитель в городе Москва':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Откликнуться')
        back = types.KeyboardButton('Назад')
        markup.add(btn)
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Условия:\n'
                         ' ✅5/2 и 2/2. Свободные дни – плавающие\n'
                         ' ✅Выдадим смартфон и оплатим связь\n'
                         '-----------------------------------------------------------------\n'
                         '💰Вознаграждение:\n'
                         'От 54 000 ₽ в месяц, если работаете 40 часов в неделю\n'
                         'Бонус за количество проведенных встреч\n'
                         'Бонус за подключенные дополнительные услуги\n'
                         'Бонус за привлеченные заявки на оформление карт\n'
                         'Бонус за транспортные расходы\n', reply_markup=markup)
        bot.register_next_step_handler(message, respond)

    elif message.text == 'Консультант Тинькофф Бизнес в городе Москва. С опытом от 6 месяцев':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Откликнуться')
        back = types.KeyboardButton('Назад')
        markup.add(btn)
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Условия:\n'
                         ' ✅Обучение. Оформляем с первого дня обучения\n'
                         ' ✅Дополнительные бонусы. Корпоративные тарифы и скидки, возможность совмещать работу из офиса и из дома\n'
                         ' ✅График работы. 5/2 с плавающими выходными. Спустя два месяца работы можно перейти на 2/2\n'
                         ' ✅Карьерный рост. Первое повышение возможно уже спустя 6 месяцев работы\n'
                         '-----------------------------------------------------------------\n'
                         '💰Вознаграждение:\n'
                         'В среднем 65 000 ₽ в первые 3 месяца работы\n'
                         'Высокое качество обслуживания позволит вам зарабатывать намного больше\n'
                         'Бонус может составлять до 25 000 ₽\n'
                         'Разнообразие задач превратит работу в увлекательный труд\n', reply_markup=markup)
        bot.register_next_step_handler(message, respond)

    elif message.text == 'Консультант Тинькофф Банк (офис)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Откликнуться')
        back = types.KeyboardButton('Назад')
        markup.add(btn)
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Условия:\n'
                         ' ✅Удобство и комфорт. Не тратите время и деньги на дорогу в офис. Работаете там, где удобно\n'
                         ' ✅Звонки по интернету. Звонки в рабочей системе компании без дополнительных затрат\n'
                         ' ✅С 10 до 19 по Москве. В будние дни\n'
                         ' ✅Всему научим. Мы подготовили для вас много полезного материала\n'
                         '-----------------------------------------------------------------\n'
                         '💰Вознаграждение:\n'
                         'От 60 000 ₽ в месяц, если работаете 30 часов в неделю\n'
                         'Вознаграждение полностью сдельное\n'
                         'Фиксированная часть до 40 000\n'
                         'Бонус за каждого привлеченного клиента\n', reply_markup=markup)
        bot.register_next_step_handler(message, respond)

    elif message.text == 'Назад':
        type_of_work(message)


@bot.message_handler(content_types=['text'])
def respond(message):
    if message.text == 'Назад':
        type_of_work(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        message = bot.send_message(message.chat.id,
                                   'Введите ваши ФИО', reply_markup=markup)
        bot.register_next_step_handler(message, phone)


@bot.message_handler(content_types=['text'])
def phone(message):
    if message.text == 'Назад':
        type_of_work(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        message = bot.send_message(message.chat.id,
                                   'Введите номер телефона', reply_markup=markup)
        bot.register_next_step_handler(message, mail)


@bot.message_handler(content_types=['text'])
def mail(message):
    if message.text == 'Назад':
        type_of_work(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        message = bot.send_message(message.chat.id,
                                   'Введите email', reply_markup=markup)
        bot.register_next_step_handler(message, approve)


@bot.message_handler(content_types=['text'])
def approve(message):
    if message.text == 'Назад':
        type_of_work(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('В меню')
        markup.add(back)
        message = bot.send_message(message.chat.id,
                                   'Заявка принята!', reply_markup=markup)

bot.polling(none_stop=True, interval=0)
