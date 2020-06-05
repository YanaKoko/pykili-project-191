import vk_api #это надо установить
import vk_answers, holy #это наши функции
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import os, random

def my_token():
    # API-ключ созданный ранее
    token = "5b0dc0bf68ae8da677d546d035fea30f566065ae3265586521601bba62c03313683aec5eef95924d470d8"
    # Авторизуемся как сообщество
    vk = vk_api.VkApi(token=token)
    return vk

def write_msg(user_id, message, vk): #отправляет сообщение
    random_id=get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})


def make_attachment(photo, vk): #делает приложение
    photo=vk_api.upload.VkUpload(vk).photo_messages(photos = photo, peer_id=None)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment

def send_photo(user_id, message, attachment, vk): # отправляет фото
    random_id=get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message':message, 'attachment':attachment, 'random_id': random_id})


def random_picture(photos_papka):
    files_list = os.listdir(photos_papka)
    choice = random.choice(files_list)
    photo = photos_papka + '\\' + choice
    return photo



def animal_photo(animal, vk, user_id):
    photo = random_picture(r'C:\НИУ ВШЭ\Программирование\Project\\'+animal)
    attachment = make_attachment(photo, vk)
    send_photo(user_id, 'Смотрите, какая прелесть!', attachment, vk)


text_test = ['1. Ваши сильные качества:\nА) Рациональность.\nБ) Уравновешенность.\nВ) Активность.\nГ) Позитивность.',
             '2. Ваши недостатки:\nА) Нерешительность.\nБ) Пассивность.\nВ) Непостоянство.\nГ) Несерьезность.',
             '3. В каком настроении вы находитесь чаще всего?\nА) В пессимистичном.\nБ) Спокойном.\nВ) Беспокойном, переменчивом.\nГ) В хорошем.',
             '4. Насколько вы общительны?\nА) Необщителен.\nБ) Малообщителен.\nВ) Средне общителен.\nГ) Очень общителен.']

def counter(diction, num):
    if num in diction.keys():
        diction[num]+=1
    else:
        diction[num] = 0
    return(diction)


def gt_counter(diction, num, answer, start):
    if num in diction.keys():
        diction[num].append(answer)
    else:
        diction[num] = start
    return(diction)

def check(request, user_id, vk):
    if not request.lower() in 'абвг':
        write_msg(user_id, 'Пожалуйста, будьте внимательнее!', vk)


def res(lst): #делает результат теста
    mel = lst.count('а')
    fleg = lst.count('б')
    hol = lst.count('в')
    sang = lst.count('г')
    if mel == fleg == hol == sang:
        return 'Хм...'+'\U0001f914'+' Вы весьма гармоничная личность.'
    if sang is max(mel, fleg, hol, sang):
        return 'Вы преимущественно сангвиник.'+'\U0001f60a'
    elif fleg is max(mel, fleg, hol, sang):
        return 'Вы преимущественно флегматик.'+'\U0001f636'
    elif hol is max(mel, fleg, hol, sang):
        return 'Вы преимущественно холерик.'+'\U0001f600'
    else:
        return 'Вы преимущественно меланхолик.'+'\u2639'



def vocabulary(file): # делает из файла .txt список с названиями городов, с которым сверяется
    with open(file, encoding='utf-8') as f:
        text = f.read()
    words = text.split('\n')
    cities = []
    for i in words:
        if len(i) > 1:
            cities.append(i)
    for i in range(len(cities)):
        cities[i] = cities[i].replace('\u200e', '')
    return cities




def check_answer(programm_word, answer, all_replies, cities): # проверяет ответ пользователя по правилам игры...
    letter = programm_word[-1] # ...если всё хорошо выдаёт False
    if not answer.startswith(letter.upper()):
        return 'Я так не играю!'
    elif answer in all_replies:
        return 'Это слово уже было, я выиграла'
    elif answer not in cities:
        return 'Такого города нет!'
    else:
        return False

def reply(cities, all_replies, answer): # конструирует ответ по правилам игры, выдаёт название города
    letter = answer[-1]
    if letter == 'ь' or letter == 'ё':
        letter = answer[-2]
    for i in cities:
        if i.startswith(letter.upper()) and i not in all_replies:
            all_replies.append(i)
            return i



def mod(diction, num):
    if num not in diction.keys():
        diction[num] = 'talk'
    return(diction)


def main():
    diction = {}
    test_answers = {}
    game_answers = {}
    x = 0
    vk = my_token()
    longpoll = VkLongPoll(vk)
    message = ''
    cities = vocabulary('cities.txt')
    my_reply = 'Лондон'
    for event in longpoll.listen():
         # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            count = counter(diction, event.user_id)
            number = diction[event.user_id]
            x += 1
            request = event.text
            my_answer = event.text
            request = request.lower()
            #Отправляем сообщение
            if 0<= number < 5 or 10< number < 15 and not 100<=number<=503:
                if count[event.user_id] >= 100501:#после игры поздравляет с праздником
                    message = 'Сегодня замечательный праздник - '+holy.congrats()+'!\nЯ вас поздравляю!'
                    write_msg(event.user_id, message, vk)
                elif number != 16 and (number < 100 or number > 200):
                    message_prev = message
                    message = vk_answers.answer(request) #Ответы получаем из ранее написанной функции
                    if message_prev != message:
                        write_msg(event.user_id, message, vk)
                if 'Вы любите котиков?'+'\U0001F638' in message:
                    count[event.user_id] = 500
            elif count[event.user_id] >= 100501:#после игры поздравляет с праздником
                message = 'Сегодня замечательный праздник - '+holy.congrats()+'!\nЯ вас поздравляю!'+3*'\U0001f389'
                write_msg(event.user_id, message, vk)
                count[event.user_id] = -100500
            elif number < 0:
                message = vk_answers.answer(request)
                if message == 'Вы любите котиков?'+'\U0001F638':
                    count[event.user_id] += 100
                else:
                    write_msg(event.user_id, message, vk)
                    count[event.user_id] = 0
            elif number == 15:#на 16-ю реплику начинается игра
                message = 'Хотите поиграть в города?'                
                write_msg(event.user_id, message, vk)
            elif number == 16: #спрашивает о желании поиграть
                if 'нет' in request:
                    write_msg(event.user_id, 'Нет так нет, моё дело предложить', vk)
                    count[event.user_id] = 100500 #переходит обратно в болталку
                else:
                    write_msg(event.user_id, 'Я начинаю!\nЛондон', vk)
                    count[event.user_id] = 101
            elif count[event.user_id] == 5:#на 5-ю реплику начинается тест
                message = 'Хотите узнать ваш темперамент?'                
                write_msg(event.user_id, message, vk)
            elif count[event.user_id] == 6: #спрашивает о желании пройти тест
                if 'нет' in request:
                    write_msg(event.user_id, 'На нет и суда нет', vk)
                    count[event.user_id] = 11
                else:
                    message = text_test[0]  #начинает тест               
                    write_msg(event.user_id, message, vk)
                    count[event.user_id] = 6 #переходит обратно в болталку
            elif 7<=count[event.user_id]<=9 :
                message = text_test[count[event.user_id]-6]  #начинает тест
                check(request, event.user_id, vk)
                write_msg(event.user_id, message, vk)
                test_answers = gt_counter(test_answers, event.user_id, request, [request])
            elif count[event.user_id] == 10:
                test_answers = gt_counter(test_answers, event.user_id, request, [request])
                check(request, event.user_id, vk)
                message=res(test_answers[event.user_id])
                write_msg(event.user_id, message, vk)
            elif 100 < count[event.user_id] <= 500:
                gt_counter(game_answers, event.user_id, my_reply, ['Лондон'])
                if not check_answer(my_reply, my_answer, game_answers[event.user_id], cities):
                    my_reply = reply(cities, game_answers[event.user_id], my_answer)
                    if not my_reply == None:
                        write_msg(event.user_id, my_reply, vk)
                    else:
                        write_msg(event.user_id, 'Поздравляю с победой!'+'\U0001f3c6', vk)
                    game_answers[event.user_id].append(my_answer)
                else:
                    my_reply = check_answer(my_reply, my_answer, game_answers[event.user_id], cities)+'\U0001f61d'
                    write_msg(event.user_id, my_reply, vk)
                    count[event.user_id] = 100500
                    game_answers[event.user_id] = []
            elif count[event.user_id] == 501:
                if 'не' in request:
                    write_msg(event.user_id, 'А собачек?'+'\U0001f436', vk)
                else:
                    animal = 'cat'
                    animal_photo(animal, vk, event.user_id)
                    count[event.user_id] = 2
            elif count[event.user_id] == 502:
                if 'не' in request:
                    write_msg(event.user_id, 'Как жаль!', vk)
                else:
                    animal = 'dog'
                    animal_photo(animal, vk, event.user_id)
                count[event.user_id] = 2
            '''else:
                if message_prev != message:
                    write_msg(event.user_id, message, vk)
            #if mod == 'talk':
                #diction[event.user_id] += 1'''

if __name__ == '__main__':
    main()
