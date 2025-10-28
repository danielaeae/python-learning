#definujes funkci ask age ktera rika jak jsi stary
def ask_age(prompt="How old are you?"):
   
   #tady delas nekonecnou smycku, while True rika ze to bude porad dokola
   #odpoved nastane v promenne answer, pokud clovek zada prompt, .strip odstrani mezery v jeho psani
    while True:
        answer = input(prompt).strip()
        
        #pokud neodpovis, tak ti to rekne at to zadas znovu, continue rika ze se to ma opakovat od znova
        if not answer:
            print("Please enter your age.")
            continue
        #try rika ze se to ma zkusit provest, pokud to nejde, tak se to presune do except casti 
        try:   
            age=int (answer)
        #tady je prvni except cast, snazi se promenit answer na cele cislo, float udela desetinne cislo z textu, int z toho udela cele cislo
        except ValueError: 
            
            try: 
                age=int(float (answer))
                # druha except cast, pokud nevyjde to predtim, tak ti to rekne at to zadas znovu a spravne (cele cislo)
            except ValueError:
                print ("Please enter a real number (e.g., 30).")
                continue 
            
            #pokud je vek zaporny, tak ti to rekne at to prestanes zadavat jak kripl a zase se to opakuje (continue)
            if age < 0: 
                print ("Stop entering negative ages!")
                continue
            #tady uz rikas, ze pokud vse probehlo v chillu, tak se vrati age
        return age
        #tady zacina hlavni funkce, kterou zname
def main():
            #zavolas funkci ask age a ulozis to do promenne age, pak uz jen das if statements podle veku a vypises printy
            age = ask_age()
            if age <13:
                print ("You are a child.")
            elif age <20:
                print ("You are a teenager.")
            elif age <65:
                print ("You are an adult.")
            else:
                print ("You are a senior.")
        #tady se rika, ze pokud je ten soubor spusten jako hlavni program, tak se zavola ta main funkce age
if __name__=="__main__":
            main()
            
  