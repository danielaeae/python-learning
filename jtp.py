import time #importujes modul time, proto python zna time.sleep
import string # =importujes modul string, proto python zna string.printable
text = 'Hello World' #text, co chces aby se vypsal
temp= ' ' #docasny retezec, ktery se bude vypisovat, mezera jen tak, estetika
for ch in text: #pro kazdy character v textu, ch znaci spravny znak
    for i in string.printable:  #pro kazdy znak, ktery existuje v string.printable
        if ch == i or i == ch: #pokud je spravny znak roven znaku z string.printable
            time.sleep(0.01) #program pocka 0.01 sekundy (efekt psani na stroji)
            print (temp +i) #vypisovani docasneho retezce + spravny znak
            temp +=ch  #novy docasny retezec je roven starymu retezci + ten spravny znak
            break #kdyz najdes, tak prestanes uz hledat
        else: #jinak, pokud to neni ten spravny znak
            time.sleep(0.01) #zase program pocka
            print (temp +i) #vypise to stejne se spatnym znakem, ale docasny retezec zustava
               