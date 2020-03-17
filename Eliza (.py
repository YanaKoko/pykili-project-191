import re, random, tkinter, os

def your_name(ask): # спрашивает имя, которое затем использунт в обращениях
    name=re.match("(['my name is ''my name\'s ']?)(\S*)", ask.lower())
    if name:
        name=name.group(2)
        name = name.capitalize()
    else:
        name = ''
    return name

def your_replic(replic):
    your_replic=replic.lower()
    return your_replic

def start(name):
    if name:
        say_one = 'Nice to meet you, '+name+'! '
    else:
        say_one = 'Nice to meet you! '
    ask = random.choice(['How are you?','How do you do?'])
    say = say_one+ask
    return say

def answer(replic):
    if replic == '':
        say = random.choice(["I can't understand. Repeat please.", "Could you repeat, please?"])
    else:
        answ=re.match("(^i.*m )(\w+\s*\w*)", replic)
        if answ:
            say = 'Why are you '+answ.group(2)+'?'
        elif 'because' in replic:
            say = 'What an interesting reason!'
        elif (replic.startswith('i')) and ('love' in replic or 'like' in replic):
            if 'not' in replic or "don't" in replic:
                say ='Why not?'
            else:
                say = random.choice(["Me too...",'So nice!'])
        elif (replic.startswith('i')) and ('hate' in replic):
            say = 'Keep calm!'
        elif 'bye' in replic:
            say = random.choice(['Bye!','Goodbye!','See you!','Bye-Bye!'])
        else:
            say = random.choice(['Bla-bla-bla!','Hihi-haha!', 'Would you like to see a cat or a dog?'])
                
    return(say)

def random_picture(photos_papka):
    files_list = os.listdir(photos_papka)
    choice = random.choice(files_list)
    photo = photos_papka + '\\' + choice
    return os.system(photo)
    
def main():
    root = tkinter.Tk()
    root.title('Eliza Doolittle')
    eliza_say = tkinter.Label(root, text = 'Hello! My name is Eliza. What is your name?', width = 50, bg = 'pink')
    eliza_say.grid(column = 0, row = 0)
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
            random_picture(r'C:\НИУ ВШЭ\Программирование\Project\cat')
            print('cat')
        elif 'dog' in replic:
            random_picture(r'C:\НИУ ВШЭ\Программирование\Project\dog')
            print('dog')
        eliza_say.configure(text=random.choice(['Bla-bla-bla!','Hihi-haha!']))
        you_say_two.bind('<Return>', say)
        
    def say(event):
        replic = you_say_two.get()
        you_say_two.delete('0', 'end')
        eliza_text = answer(replic.lower())
        eliza_say.configure(text=eliza_text)
        if eliza_text == 'Would you like to see a cat or a dog?':
            you_say_two.bind('<Return>', picture)
    you_say_two.bind('<Return>', say)
    root.mainloop()
    
if __name__ == "__main__":
    main()
