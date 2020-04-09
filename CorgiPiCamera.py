#Created by Cachat
from tkinter import * #Импорт библиотек
from picamera import PiCamera
from time import sleep
from tkinter.ttk import Combobox

camera = PiCamera() #инициализация камеры

def clicked(): #При клике на кнопку (см. ниже этой функции)
    ttextt = (format(txtt.get())) #Задаём переменные
    lig=int(format(co.get()))
    res=int(format(txt.get()))
    camera.brightness = lig
    
    #эффекты
    alias_to_value = {"Негатив":'negative', "Автоулучшение":'colorbalance',"Рисунок":'cartoon',"Гравюра":'emboss'}
    camera.image_effect = alias_to_value[com.get()]
    
    #баланс белого
    alias_to_value = {"Выключено":'off', "Авто":'auto',"Ночной режим":'night',"Снег":'snow'}
    camera.exposure_mode = alias_to_value[c.get()]


    if combo.get() == "Видео": #Съёмка видео
        camera.annotate_text = ttextt
        camera.start_preview()
        camera.start_recording('/home/pi/Desktop/Video.h264')
        sleep(res)
        camera.stop_recording()
        camera.stop_preview()
        res=0

    if combo.get() == "Фото": #Съёмка фото
        camera.annotate_text = ttextt
        camera.start_preview()
        sleep(res)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
        res=0 

    if combo.get() == "Превью":
        camera.annotate_text = ttextt
        camera.start_preview()
        sleep(res)
        camera.stop_preview()
        res=0 #Показ превью


window = Tk()  #Создание графического окна
window.title("CorgiPiCamera")
window.geometry('380x150')


lbl = Label(window, text="Кол-во секунд") #Отрисовка виджетов
lbl.grid(column=0, row=0)

txt = Entry(window,width=21)  #текстовое поле для секунд
txt.grid(column=1, row=0)

btn = Button(window, text="Старт", command=clicked)  
btn.grid(column=2, row=0) #Кнопка

lbl = Label(window, text="Действие")  
lbl.grid(column=0, row=3)

combo = Combobox(window) #комбобокс режимов
combo['values'] = ("Видео", "Фото", "Превью")
combo.current(0) 
combo.grid(column=1, row=3)

lbl = Label(window, text="Доп. текст") #текстовое поле для ввода верхнего текста
lbl.grid(column=0, row=7)

txtt = Entry(window,width=21)  
txtt.grid(column=1, row=7)

lbl = Label(window, text="Эффекты")  
lbl.grid(column=0, row=10)

com = Combobox(window) #комбобокс эффектов
com['values'] = ("Ничего", "Автоулучшение", "Негатив", "Рисунок", "Гравюра")  
com.current(0) 
com.grid(column=1, row=10)

lbl = Label(window, text="Яркость")  
lbl.grid(column=0, row=13)

co = Combobox(window) #комбобокс яркости
co['values'] = ("0", "25", "50", "75", "100")  
co.current(2) 
co.grid(column=1, row=13)

lbl = Label(window, text="Баланс белого")  
lbl.grid(column=0, row=16)

c = Combobox(window) #комбобокс баланса белого
c['values'] = ("Выключено","Авто","Ночной режим","Снег")  
c.current(0) 
c.grid(column=1, row=16)

window.mainloop()
#конец кода
