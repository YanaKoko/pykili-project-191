import re, random, tkinter, os, collections

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

def rand_replic(word, trigrammas):
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

text = read('алиса.txt') #Сюда надо вставить название файла с текстом
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

def cat_dog(words):
        if 'cat'in words:
            picture = random_picture(r'C:\Users\mi\Desktop\конспекты\python\ПРОЕКТ\photos\cat')
            print(picture)
            show_pict(picture)
        elif 'dog' in words:
            picture = random_picture(r'C:\Users\mi\Desktop\конспекты\python\ПРОЕКТ\photos\dog')
            print(picture)


def your_name(ask): # спрашивает имя, которое затем использунт в обращениях
    my_name=re.match("(((меня зовут)|(я))(\s))?(\S+)", ask.lower())
    if my_name:
        name=my_name.group(6)
        name = name.capitalize()
    else:
        name = ''
    return(name)

def your_replic(replic):
    your_replic=replic.lower()
    return your_replic

def start(name):
    if name:
        say_one = 'Приятно познакомиться, '+name+'! '
    else:
        say_one = 'Очень рада знакомству! '
    ask = random.choice(['Жизнь прекрасна?','У вас сейчас хорошее настроение?'])
    say = say_one+ask
    return say

def answer(replic):
    replic=replic.lower().replace('!', '')
    if replic == '':
        say = random.choice(["Не расслышала, повторите, пожалуйста!", "Не могли бы вы ответить понятнее?"])
        say = random.choice([random_phrase(replic, trigrammas),'А почему?'])
    elif 'потому что' in replic:
        say = 'Спасибо, что поделились этим со мной! Доверие - это важно.'
    elif (replic.lower().startswith('я')) and ('нравится' in replic or 'люблю' in replic) and not replic.endswith('?'):
        if 'не' in replic:
            say ='Почему нет?'
        else:
            if ('люблю') in replic:
                say = random.choice(['И я :)','Как здорово!'])
            else:
                say = random.choice(['Мне тоже :)','Как здорово!'])
    elif (replic.startswith('я')) and ('ненавижу' in replic):
        say = 'Поверьте, всё будет хорошо!'
    elif 'пока' in replic or 'до свидания' in replic or 'до встречи' in replic:
        say = random.choice(['Пока!','До свидания!','До встречи!','Возвращайтесь, я буду скучать!'])
    else:
        say = random.choice([random_phrase(replic, trigrammas),'Как же могло так получиться?'])
        if say == '!':
            say = 'А почему?'
        
                
    return(say)

def random_picture(photos_papka):
    files_list = os.listdir(photos_papka)
    choice = random.choice(files_list)
    photo = photos_papka + '\\' + choice
    return photo

def show_pict(photo):
    show_window = tkinter.Toplevel()
    im = tkinter.PhotoImage(file=photo)
    picture = tkinter.Label(show_window, image = im)
    picture.pack()
    show_window.mainloop()
    
def main():
    root = tkinter.Tk()
    root.title('Eliza Doolittle')
    root.geometry('810x200')
    root["bg"] = 'pink'
    root.iconbitmap(r'icon.ico')
    eliza_say = tkinter.Label(root, text = 'Здравствуйте! Меня зовут Элиза, а вас?',
                              wraplength='300', width = '50', bg = 'pink')
    eliza_say.grid(column = 0, row = 1)
    you_say = tkinter.Entry(root, width = 50)
    you_say.grid(column = 1, row = 0)
    you_say_two = tkinter.Entry(root, width = 50)
    def hello(event):
        name = your_name(you_say.get())
        eliza_text = start(name)
        eliza_say.configure(text=eliza_text)
        you_say.destroy()
        you_say_two.grid(column = 1, row = 0)

    you_say.bind('<Return>', hello)
    
    def picture(event):
        replic = you_say_two.get()
        you_say_two.delete('0', 'end')
        if 'cat' in replic:
            photo = random_picture(r'C:\Users\mi\Desktop\конспекты\python\ПРОЕКТ\photos\cat')
            print(photo)
            show_pict(photo, root)
        elif 'dog' in replic:
            photo = random_picture(r'C:\Users\mi\Desktop\конспекты\python\ПРОЕКТ\photos\dog')
            print(photo, root)
        eliza_say.configure(text=random.choice(['Я уже говорила, что вы прекрасно выглядите? Я всё вижу ;)','Вы удивительно приятный собеседник!',
                                                'С каждой минутой я всё сильнее рада знакомству с вами!', 'Давайте общаться чаще!']))
        you_say_two.bind('<Return>', say)

    def say(event):
        replic = you_say_two.get()
        you_say_two.delete('0', 'end')
        eliza_text = answer(replic.lower())
        eliza_say.configure(text=eliza_text)
        if eliza_text == 'Вы любите котиков и пёсиков?':
            print('CAT&DOG')
            def catdog(event):
                new_replic = you_say_two.get()
                you_say_two.delete('0', 'end')
                cat_dog(new_replic)
                you_say_two.bind('<Return>', say)
            you_say_two.bind('<Return>', catdog)
        elif eliza_text in ['Пока!','До свидания!','До встречи!','Возвращайтесь, я буду скучать!']:
            you_say_two.destroy()
    you_say_two.bind('<Return>', say)
    root.mainloop()
    
if __name__ == "__main__":
    main()
