import re, random, collections, datetime

def read(file):
    with open (file, encoding = 'utf-8') as f:
        text = f.read()
    text = text.replace('\n',' ').replace('  ',' ').replace('—',' ')
    for symbol in [',','"', ';',]:
        text = text.replace(symbol, '')
    text = text.split(' ')
    for word in text:
        if word == '':
            text.remove(word)
    return text


def tri(text): #Делает триграммы
    trigrammas = {}
    for i in range (len(text)-2):
        tri = text[i]+' '+text[i+1]+' '+text[i+2]
        if text[i] in trigrammas.keys():
            trigrammas[text[i]].append(tri)
        else:
            trigrammas[text[i]] = [tri]
    return trigrammas

def last_word(string): #Ищет последнее слово в строке
    last_word = re.search(r' (\S+$)', string)
    if last_word:
        return last_word.group(1)
    else:
        return ''

def two_last_words(string): #Ищет 2 последних слова в строке
    two_last_words = re.search(r' (\S+ \S+$)', string)
    if two_last_words:
        return two_last_words.group(1)
    else:
        return ''

def rand_replic(word, trigrammas): # делает рандомную фразу
    my_answ = word
    for x in range(40): #Делает текст из 40 слов
        if word[-1] not in '!?.': #Если текст - не квазипредложение
                if word in trigrammas.keys():
                    answ = collections.Counter(trigrammas[word]) #Выбирает самые частотные триграммы
                    if len(answ) >= 10:
                        i = random.randint(1, 9)
                    elif len(answ) >= 5:
                        i = random.randint(1, 4)
                    else:
                        i =1
                    answ = answ.most_common(i)
                    word = answ[i-1][0]
                    if answ[i-1] != 0: 
                        word = last_word(answ[i-1][0])
                        two_words = two_last_words(answ[i-1][0])
                        if two_words != '':
                            if two_words.split(' ')[0][-1] not in '!?.':
                                my_answ += ' '+two_words
                        else:
                            my_answ += ' '+two_words.split(' ')[0]
                            break
    my_answ += '.'
    my_answ = my_answ.replace('?.','?').replace('!.','!').replace(':.','.')
    my_answ = re.sub(r'\.+', '.', my_answ)
    return my_answ

text = read('alisa.txt') #Сюда надо вставить название файла с текстом
trigrammas = tri(text)
def random_phrase(ask, trigrammas):    
    for symbol in [',','"', ';']:
        ask = ask.replace(symbol, '')
    for symbol in ['!','?', '.']:
        ask = ask.replace(symbol, '')
    ask = ask.split(' ')
    possible_answ = ['!']
    for n in range(30):
        word = random.choice(ask)
        my_answ = rand_replic(word, trigrammas)
        if len(my_answ.split(' ')) <= 15 and len(my_answ.split(' '))>3: #выбирает более короткие тексты
            possible_answ.append(my_answ)
    if len(possible_answ) > 1:
        possible_answ.remove('!')
    answer = random.choice(possible_answ)
    let_one = answer[0]
    my_answer = let_one.capitalize()+answer[1:]
    return my_answer


def dict_answ(words, dict_of_words):#выбирает ответ в словаре
    dict_answer = ''
    words = words.replace('?', '')
    for key in dict_of_words.keys():
        if key in words:
            dict_answer = dict_of_words[key]
            break
            dict_answer = ''
    return dict_answer
            
def qu_answ(words, dict_of_words):#ответ на вопрос
    qu_answ = dict_answ(words, dict_of_words)
    if qu_answ == '':
        qu_answ = random.choice(['Да!','Нет!'])
    return qu_answ
        
def reaction(words, list_of_words, list_of_words_two):#погода и бранные слова
    for word in words.split(' '):
        if word in list_of_words:
            reaction_answer = random.choice(list_of_words_two)
            break
        else:
            reaction_answer = ''
    return reaction_answer

#def books(words): не работает, но можно подумать
    #if

def love(words):#ответ на фразы со словом люблю 
    if ' не' in words:
        love_answer ='Почему нет?'
    else:
        if ('люблю') in words:
            topic = re.match(r'(.*?)(люблю)(.*)', words)
            love_answer = 'Я просто обожаю' + topic.group(3) + '!'#это вместо хобби, но вроде работает
        else:
            love_answer = random.choice(['Мне тоже :)','Как здорово!'])
    return love_answer 

def hello(): #здоровается
    my_dt = datetime.datetime.now()#определяет текущее время
    h = my_dt.hour
    if 4<h<=10:#выбирает ответ
        hello_answer = 'Доброе утро!'
    elif 10<h<=15:
        hello_answer = 'Добрый день!'
    elif 15<h<=18:
        hello_answer = 'Добрый вечер!'
    else:
        hello_answer = 'Здравствуйте!'
    return hello_answer

def answer(replic):#делает ответ
    recepie = {'яблоки':'шарлотку','груши':'варенье','грибы':'соленье'} #это еда и блюда, можно дописать
    qu = {'почему':'По кочану.', 'когда':'После дождичка в четверг.', 'зачем':'Затем.',
          'сколько':'Столько.', 'где':'В Караганде.', 'откуда':'От верблюда.',
          'кто':'Конь в пальто.', 'дела':'Как сажа бела.', 'как':'Как-то так.'} #это ответы на вопросы с вопрос. словами
    sad = ('дождь', 'слякоть', 'ливень', 'сыро', 'жара') #это неприятности
    bad = ('Пакость!', 'Мерзость!', 'Какая жалость!', 'Фи!', 'Ох-ох', 'Ох!', 'Гадость!')#это "бранные слова"
    happy = ('солнечно', 'тепло', 'ясно')
    good = ('Прелесть!', 'Чудо!', 'Ах!', 'Это так мило!', 'Ах-ах!', 'Чудесно!', 'Прелестно!')#это приятные слова
    replic=replic.lower().replace('!', '')
    if replic == '':
        say = random.choice(["Не расслышала, повторите, пожалуйста!", "Не могли бы вы ответить понятнее?"])
        say += '\U0001f644'
    elif 'привет' in replic or 'здравствуй' in replic:
        say = hello()
    elif 'спасибо' in replic:
        say = 'Всегда пожалуйста!'
    elif 'потому что' in replic:
        say = 'Спасибо, что поделились этим со мной! Доверие - это важно.'
    elif ('нравится' in replic or 'люблю' in replic):
        say = ''
        if not 'не' in replic:
            if dict_answ(replic, recepie) != '':
                say = 'Можно приготовить '+dict_answ(replic, recepie)+'!'
            else: say = ''
        if say == '':
            say = love(replic)
    elif (replic.startswith('я')) and ('ненавижу' in replic):
        say = 'Поверьте, всё будет хорошо!'
    elif 'пока' in replic or 'до свидания' in replic or 'до встречи' in replic:
        say = random.choice(['Пока!','До свидания!','До встречи!','Возвращайтесь, я буду скучать!'])
    elif '?' in replic:
        say = qu_answ(replic, qu)
    elif 'прелесть' in replic:
        say = '\U0001F60A'
    else:
        say = reaction(replic, sad, bad)
        if say == '':
            say = reaction(replic, happy, good)
            if say == '':
                say = random_phrase(replic, trigrammas)
                if say == '!':
                    say = 'Вы любите котиков?'+'\U0001F638'
    if replic.endswith(')'):
        say += '\U0001f604'
    return(say)

