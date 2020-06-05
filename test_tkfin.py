import tkinter

def test(answers):
        mel = answers[0]
        fleg = answers[1]
        hol = answers[2]
        sang = answers[3]
        if mel == fleg == hol == sang:
            return 'Хм... Вы весьма гармоничная личность.'
        if sang is max(mel, fleg, hol, sang):
            return 'Вы преимущественно сангвиник.'
        elif fleg is max(mel, fleg, hol, sang):
            return 'Вы преимущественно флегматик.'
        elif hol is max(mel, fleg, hol, sang):
            return 'Вы преимущественно холерик.'
        else:
            return 'Вы преимущественно меланхолик.'

def test_result(answer):
        text = tkinter.Label(text=answer, font='Arial 14', bg = 'oldlace').grid()
        
        
def test_buttons():
    test_window = tkinter.Tk()
    test_window['bg'] = 'oldlace'
    ivar = tkinter.IntVar()
    test_window.title('1. Ваши сильные качества:')
    rbutton1 = tkinter.Radiobutton(test_window, bg = 'oldlace', text= 'А) Рациональность.', variable=ivar, value=1) #Это начальные кнопки
    rbutton2 = tkinter.Radiobutton(test_window, bg = 'oldlace', text= 'Б) Уравновешенность.', variable=ivar, value=2)
    rbutton3 = tkinter.Radiobutton(test_window, bg = 'oldlace', text= 'В) Активность.', variable=ivar, value=3)
    rbutton4 = tkinter.Radiobutton(test_window, bg = 'oldlace', text= 'Г) Позитивность.', variable=ivar, value=4)
    rbutton1.grid(column=0, row=0) 
    rbutton2.grid(column=1, row=0) 
    rbutton3.grid(column=2, row=0) 
    rbutton4.grid(column=3, row=0)
    but_one = tkinter.Button(test_window, bg = 'tomato', text = 'PRESS') 
    but_three = tkinter.Button(test_window, bg = 'skyblue', text = 'PRESS')
    but_four = tkinter.Button(test_window, bg = 'yellow', text = 'PRESS')
    but_five = tkinter.Button(test_window, bg = 'aquamarine', text='Закончить тест')
    A = 0
    B = 0
    C = 0
    D = 0
    
    def counter(vary):  #Теперь это не событие, а функция
        x = vary.get()
        if x == 1:
            nonlocal A
            A = A + 1
        elif x == 2:
            nonlocal B
            B = B + 1
        elif x == 3:
            nonlocal C
            C = C + 1
        else:
            nonlocal D
            D = D + 1
    but_one.grid(column=4, row=2)

    def multy_config(w_list, t_list): 
        for x in range(len(w_list)):
            w_list[x].configure(text = t_list[x])
    q_2 = ['А) Нерешительность.', 'Б) Пассивность.', 'В) Непостоянство.', 'Г) Несерьезность.']
    q_3 = ['А) В пессимистичном.', 'Б) Спокойном.', 'В) Беспокойном, переменчивом.', 'Г) В хорошем.']
    q_4 = ['А) Необщителен.', 'Б) Малообщителен.', 'В) Средне общителен.', 'Г) Очень общителен.']
    def question_2(event):
        test_window.title('2. Ваши недостатки:')
        multy_config([rbutton1, rbutton2, rbutton3, rbutton4], q_2)
        but_one.destroy()
        but_three.grid(column=4, row=2)
        counter(ivar)
    but_one.bind('<Button-1>', question_2)

    def question_3(event):
        test_window.title('3. В каком настроении вы находитесь чаще всего?')
        multy_config([rbutton1, rbutton2, rbutton3, rbutton4], q_3)
        but_three.destroy()
        but_four.grid(column=4, row=2)
        counter(ivar)
        
    but_three.bind('<Button-1>', question_3)
    
    def question_4(event):
        test_window.title('4. Насколько вы общительны?')
        multy_config([rbutton1, rbutton2, rbutton3, rbutton4], q_4)
        but_four.destroy()
        but_five.grid(column=4, row=2)
        counter(ivar)
        
    but_four.bind('<Button-1>', question_4)

    def question_5(event):
        counter(ivar)
        test_window.title('Результат')
        rbutton1.destroy()
        rbutton2.destroy()
        rbutton3.destroy()
        rbutton4.destroy()
        test_result(test((A, B, C, D)))
        but_five.destroy()

    but_five.bind('<Button-1>', question_5)

    test_window.mainloop()
    
#test_buttons()
