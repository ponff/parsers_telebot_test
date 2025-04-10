import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("8073098746:AAHCLTZACe4xIBUocKz_gmmltEZ-LQydK2g")  # Замените на ваш токен

# Функция парсинга фильмов
import requests
from bs4 import BeautifulSoup

def parse_movies():
    try:
        url = 'https://www.kinopoisk.ru/lists/movies/'  # Замените на актуальный URL
        headers = {
            'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        soup = BeautifulSoup(response.text, 'html.parser')
        
        movies = []
        # Ищем элементы с атрибутом data-test-id="movie-list-item"
        for item in soup.find_all(attrs={"data-test-id": "movie-list-item"}):  
            title_element = item.find('h3')  # Замените на правильный элемент, если нужно
            title = title_element.text.strip() if title_element else "Нет названия"
            rating_element = item.find('span', class_='rating')  # Замените на правильный элемент, если нужно
            rating = rating_element.text.strip() if rating_element else "Нет рейтинга"
            movies.append(f'Название: "{title}", Рейтинг: {rating}')
        
        return movies if movies else ["Фильмы не найдены."]
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка: {e}")
        return ["Произошла ошибка. Попробуйте позже."]
# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш помощник-бот.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Доступные команды:\n/start - приветствие\n/help - помощь\n/menu - меню")

# Обработчик команды /menu
@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Фильмы"), KeyboardButton("Курсы"), KeyboardButton("Книги"))
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

# Обработчик нажатия кнопки "Фильмы"
@bot.message_handler(func=lambda message: message.text == "Фильмы")
def handle_movies(message):
    movies = parse_movies()
    response = "\n".join(movies)
    bot.reply_to(message, response)

# Обработчик нажатия кнопки "Курсы" (пример)
@bot.message_handler(func=lambda message: message.text == "Курсы")
def handle_courses(message):
    # Здесь можно добавить логику парсинга курсов
    bot.reply_to(message, "Функция парсинга курсов еще не реализована.")

# Обработчик нажатия кнопки "Книги" (пример)
@bot.message_handler(func=lambda message: message.text == "Книги")
def handle_books(message):
    # Здесь можно добавить логику парсинга книг
    bot.reply_to(message, "Функция парсинга книг еще не реализована.")

if __name__ == '__main__':
    bot.polling()