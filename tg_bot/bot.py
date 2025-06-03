import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TelegramError

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # Меняем уровень на DEBUG для более подробного логирования
)
logger = logging.getLogger(__name__)

# Создаем клавиатуру с основным меню
def get_main_menu_keyboard():
    keyboard = [
        ['🏞 Что посмотреть'],
        ['🛍 Где купить сувениры'],
        ['🏨 Где остановиться на ночь']
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите интересующий вас раздел"
    )

# Создаем клавиатуру для подменю "Что посмотреть"
def get_sights_keyboard():
    keyboard = [
        ['🏰 Кижи', '⛪ Валаам'],
        ['🌊 Рускеальские водопады', '🏔️ Гора Воттоваара'],
        ['🌲 Национальный парк Паанаярви', '🏞️ Водопад Кивач'],
        ['🏛️ Петрозаводск'],
        ['🔙 Вернуться в главное меню']
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите достопримечательность"
    )

# Создаем клавиатуру для подменю "Где купить сувениры"
def get_souvenirs_keyboard():
    keyboard = [
        ['Ягоды Карелии', 'СувенировЪ'],
        ['Морошка'],
        ['🔙 Вернуться в главное меню']
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите магазин"
    )

# Создаем клавиатуру для подменю "Где остановиться на ночь"
def get_accommodation_keyboard():
    keyboard = [
        ['🏨 Отели'],
        ['🔙 Вернуться в главное меню']
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите тип размещения"
    )

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "Добро пожаловать в бот 'Путешествие по Карелии'! 🌲\n\n"
        "Я помогу вам спланировать незабываемое путешествие по Карелии. "
        "Выберите интересующий вас раздел в меню ниже:"
    )
    await update.message.reply_text(
        welcome_message,
        reply_markup=get_main_menu_keyboard()
    )

# Обработчик текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text
        logger.info(f"Получено сообщение: {text}")
        
        if text == "🏞 Что посмотреть":
            await update.message.reply_text(
                "Выберите интересующую вас достопримечательность:",
                reply_markup=get_sights_keyboard()
            )
        elif text == "🛍 Где купить сувениры":
            await update.message.reply_text(
                "Выберите магазин для получения подробной информации:",
                reply_markup=get_souvenirs_keyboard()
            )
        elif text == "🏨 Где остановиться на ночь":
            await update.message.reply_text(
                "Выберите тип размещения:",
                reply_markup=get_accommodation_keyboard()
            )
        elif text == "🔙 Вернуться в главное меню":
            await update.message.reply_text(
                "Главное меню:",
                reply_markup=get_main_menu_keyboard()
            )
        # Обработка подменю "Что посмотреть"
        elif text == "🏰 Кижи":
            await update.message.reply_photo(
                photo="https://s2.stc.all.kpcdn.net/putevoditel/projectid_534672/images/tild3130-3266-4937-b861-376262353362__70.jpg",
                caption=(
                    "Кижи - уникальный музей-заповедник под открытым небом, известный своими деревянными церквями.\n\n"
                    "📍 Расположение: [Открыть на Яндекс Картах](https://yandex.ru/maps/-/CHGvROIJ)\n"
                    "⏰ Время работы: 8:00-20:00\n"
                    "💰 Стоимость: от 500₽\n"
                    "🚢 Как добраться: теплоходом из Петрозаводска"
                ),
                parse_mode='Markdown'
            )
        elif text == "⛪ Валаам":
            await update.message.reply_photo(
                photo="https://avatars.mds.yandex.net/i?id=50ae304209cca76e860bfa10a9d93b64_l-5262023-images-thumbs&n=13",
                caption=(
                    "Валаам - архипелаг с древним монастырем и уникальной природой.\n\n"
                    "📍 Расположение: [Открыть на Яндекс Картах](https://yandex.ru/maps/-/CHGvRHI6)\n"
                    "⏰ Время работы: 6:00-20:00\n"
                    "💰 Стоимость: от 1000₽\n"
                    "🚢 Как добраться: теплоходом из Сортавалы"
                ),
                parse_mode='Markdown'
            )
        elif text == "🌊 Рускеальские водопады":
            await update.message.reply_photo(
                photo="https://avatars.mds.yandex.net/i?id=3361424eb7720c780b8e803b62b94df0735280ad-10667780-images-thumbs&n=13",
                caption=(
                    "Рускеальские водопады - каскад из четырех водопадов на реке Тохмайоки.\n\n"
                    "📍 Расположение: [Открыть на Яндекс Картах](https://yandex.ru/maps/-/CHGvR2mi)\n"
                    "⏰ Время работы: круглосуточно\n"
                    "💰 Стоимость: бесплатно\n"
                    "🚗 Как добраться: на машине из Сортавалы"
                ),
                parse_mode='Markdown'
            )
        elif text == "🏔️ Гора Воттоваара":
            await update.message.reply_photo(
                photo="https://i.pinimg.com/originals/62/df/c1/62dfc1882fef804cca9d50ddcd7839b5.jpg",
                caption=(
                    "Воттоваара - загадочная гора с древними сейдами и уникальными пейзажами.\n\n"
                    "📍 Расположение: [Открыть на Яндекс Картах](https://yandex.ru/maps/-/CHGvVZIv)\n"
                    "⏰ Время работы: круглосуточно\n"
                    "💰 Стоимость: бесплатно\n"
                    "🚗 Как добраться: на внедорожнике из поселка Гимолы"
                ),
                parse_mode='Markdown'
            )
        elif text == "🌲 Национальный парк Паанаярви":
            await update.message.reply_photo(
                photo="https://cdn.sportmaster.ru/upload/content/mediahab/prod/0e819e1c-ae2f-4dfb-a6d3-6f37dddf312c.jpg",
                caption=(
                    "Паанаярви - заповедник с нетронутой природой и чистейшими озерами.\n\n"
                    "📍 Расположение: [Открыть на Яндекс Картах](https://yandex.ru/maps/-/CHGvV60y)\n"
                    "⏰ Время работы: 9:00-17:00\n"
                    "💰 Стоимость: от 300₽\n"
                    "🚗 Как добраться: на машине из поселка Пяозерский"
                ),
                parse_mode='Markdown'
            )
        elif text == "🏞️ Водопад Кивач":
            await update.message.reply_photo(
                photo="https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_67656e4097843f1beb4ed44d_677f17ac61de3c12dec241a9/scale_1200",
                caption=(
                    "Кивач - второй по величине равнинный водопад в Европе.\n\n"
                    "📍 Расположение: [Открыть на Яндекс Картах](https://yandex.ru/maps/-/CHGvJ88L)\n"
                    "⏰ Время работы: 8:00-20:00\n"
                    "💰 Стоимость: от 200₽\n"
                    "🚗 Как добраться: на машине из Петрозаводска"
                ),
                parse_mode='Markdown'
            )
        elif text == "🏛️ Петрозаводск":
            await update.message.reply_photo(
                photo="https://avatars.mds.yandex.net/i?id=fd5c069785b8a1f363b1a594c2953b9a_l-12614240-images-thumbs&n=13",
                caption=(
                    "Петрозаводск - столица Карелии с богатой историей и культурой.\n\n"
                    "📍 Расположение: [Открыть на Яндекс Картах](https://yandex.ru/maps/-/CHGvVPph)\n"
                    "⏰ Время работы: круглосуточно\n"
                    "💰 Стоимость: зависит от места\n"
                    "🚂 Как добраться: поездом или самолетом"
                ),
                parse_mode='Markdown'
            )
        # Обработка подменю "Где купить сувениры"
        elif text == "Ягоды Карелии":
            await update.message.reply_photo(
                photo="https://avatars.mds.yandex.net/get-altay/15413153/2a0000019666904acb8fabc7dc39d1145d88/XXXL",
                caption=(
                    "Ягоды Карелии\n\n"
                    "📍 Расположение: [Открыть на Яндекс Карты](https://yandex.ru/maps/-/CHGvbEoH)\n"
                    "📌 Адрес: г. Петрозаводск, пр. Ленина, 38\n"
                    "⏰ Время работы: 10:00-20:00 (ежедневно)\n"
                ),
                parse_mode='Markdown'
            )
        elif text == "СувенировЪ":
            await update.message.reply_photo(
                photo="https://avatars.mds.yandex.net/get-altay/13063086/2a000001945f5bff2fb50c1c8c01af5e8026/XXXL",
                caption=(
                    "СувенировЪ\n\n"
                    "📍 Расположение: [Открыть на Яндекс Карты](https://yandex.ru/maps/-/CHGvfYk2)\n"
                    "📌 Адрес: г. Петрозаводск, ул. Ленина, 36\n"
                    "⏰ Время работы: 10:00-20:00 (ежедневно)\n"
                ),
                parse_mode='Markdown'
            )
        elif text == "Морошка":
            await update.message.reply_photo(
                photo="https://avatars.mds.yandex.net/get-altay/14350490/2a000001960127c876f4c89b1f8bf4914e17/XXXL",
                caption=(
                    "Морошка\n\n"
                    "📍 Расположение: [Открыть на Яндекс Карты](https://yandex.ru/maps/-/CHGznV2T)\n"
                    "📌 Адрес: г. Петрозаводск, ул. Антикайнена, 32\n"
                    "⏰ Время работы: 10:00-19:00 (ежедневно)\n"  
                ),
                parse_mode='Markdown'
            )
        # Обработка подменю "Где остановиться на ночь"
        elif text == "🏨 Отели":
            await update.message.reply_text(
                "Выберите отель для получения подробной информации:",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ['🏨 Отель Карелия (Петрозаводск)'],
                        ['🏨 Гостиница Кондопога', '🏨 Отель Piipun Piha (Сортавала)'],
                        ['🔙 Вернуться в главное меню']
                    ],
                    resize_keyboard=True,
                    input_field_placeholder="Выберите отель"
                )
            )
        elif text == "🏨 Отель Карелия (Петрозаводск)":
            await update.message.reply_photo(
                photo="https://karelia-hotel.ru/upload/iblock/926/zhf4fm5vghp5xvex8v0x4tn08kpbcri3.webp",
                caption=(
                    "🏨 Отель Карелия\n\n"
                    "📍 Расположение: [Открыть на Яндекс Карты](https://yandex.ru/maps/-/CHGzEPnE)\n"
                    "📌 Адрес: г. Петрозаводск, наб. Гюллинга, 2\n"
                    "⏰ Заезд: с 14:00, выезд: до 12:00\n"
                    "💰 Стоимость: от 3500₽ за ночь\n"
                    "📞 Телефон: +7 (8142) 73-33-33\n"
                    "🌐 Сайт: [karelia-hotel.ru](https://karelia-hotel.ru)\n\n"
                    "Спа-отель «Карелия» — современный отель в карельском стиле с собственным спа-центром и рестораном авторской карельской кухни. "
                    "Выбирая нас, вы выбираете отдых в окружении природы в историческом центре города. "
                    "Из каждого номера открывается панорамный вид на город, реку и парк или второй по величине пресноводный водоём в Европе — Онежское озеро.\n\n"
                    "Услуги отеля:\n"
                    "• Спа-центр с бассейном, саунами и хаммамом\n"
                    "• Ресторан авторской карельской кухни\n"
                    "• Тренажёрный зал\n"
                    "• Завтрак «шведский стол»\n"
                    "• Размещение с домашними животными\n"
                    "• Круглосуточная автостоянка\n"

                ),
                parse_mode='Markdown'
            )
        elif text == "🏨 Гостиница Кондопога":
            await update.message.reply_photo(
                photo="https://media-cdn.tripadvisor.com/media/photo-s/18/c9/a3/82/caption.jpg",
                caption=(
                    "🏨 Гостиница Кондопога\n\n"
                    "📍 Расположение: [Открыть на Яндекс Карты](https://yandex.ru/maps/-/CHGzE-z2)\n"
                    "📌 Адрес: г. Кондопога, ул. Советов, 14\n"
                    "⏰ Заезд: с 14:00, выезд: до 12:00\n"
                    "💰 Стоимость: от 3100₽ за сутки\n"
                    "📞 Телефон: +7 (800) 302-41-30\n"
                    "📧 Email: hotelkondopoga@yandex.ru\n"
                    "🌐 Сайт: [otel-kondopoga.ru](https://otel-kondopoga.ru)\n\n"
                    "Гостиница расположена в культурно-спортивном центре Карелии - г. Кондопога: "
                    "от Мурманска - 890 км, от Санкт-Петербурга - 470 км, от Петрозаводска - 40 км.\n\n"
                    "Услуги гостиницы:\n"
                    "• Ресторан (45 посадочных мест)\n"
                    "• Удобная парковка на территории\n"
                ),
                parse_mode='Markdown'
            )
        elif text == "🏨 Отель Piipun Piha (Сортавала)":
            await update.message.reply_photo(
                photo="https://avatars.mds.yandex.net/get-altay/12800836/2a000001906983ebf27bcaddf709f6438cea/XXXL",
                caption=(
                    "🏨 Отель Piipun Piha\n\n"
                    "📍 Расположение: [Открыть на Яндекс Карты](https://yandex.ru/maps/-/CHGzE06Z)\n"
                    "📌 Адрес: г. Сортавала, ул. Карельская, 22\n"
                    "⏰ Заезд: с 14:00, выезд: до 12:00\n"
                    "💰 Стоимость: от 3500₽ за ночь\n"
                    "📞 Телефон: +7 (814) 304-55-55\n"
                    "🌐 Сайт: [piipunpiha.ru](https://piipunpiha.ru)\n\n"
                    "Отель Piipun Piha — уютный отель в центре Сортавалы, расположенный в историческом здании. "
                    "Из окон открывается прекрасный вид на Ладожское озеро и городскую набережную.\n\n"
                    "Услуги отеля:\n"
                    "• Ресторан с панорамным видом\n"
                    "• Парковка\n"
                    "• Трансфер от/до вокзала\n"
                    "• Экскурсионное бюро\n"
                    "• Прокат велосипедов\n\n"
                    "Рядом с отелем:\n"
                    "• Набережная Ладожского озера\n"
                    "• Музей Кронида Гоголева\n"
                    "• Парк Ваккосалми\n"
                    "• Пристань для круизов на Валаам\n"
                    "• Горный парк Рускеала"
                ),
                parse_mode='Markdown'
            )
    except TelegramError as e:
        logger.error(f"Ошибка Telegram при обработке сообщения: {e}", exc_info=True)
        await update.message.reply_text("Произошла ошибка при обработке сообщения. Пожалуйста, попробуйте позже.")
    except Exception as e:
        logger.error(f"Неожиданная ошибка при обработке сообщения: {e}", exc_info=True)
        await update.message.reply_text("Произошла непредвиденная ошибка. Пожалуйста, попробуйте позже.")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик ошибок."""
    logger.error(f"Ошибка при обработке обновления {update}: {context.error}", exc_info=True)

def main():
    try:
        # Создаем приложение
        application = Application.builder().token('7784053804:AAE6S1ZLbKJyAN8plFQjmky8nTXsgkXszNo').build()

        # Добавляем обработчики
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        # Добавляем обработчик ошибок
        application.add_error_handler(error_handler)

        logger.info("Бот запускается...")
        # Запускаем бота
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Критическая ошибка при запуске бота: {e}", exc_info=True)

if __name__ == '__main__':
    main() 