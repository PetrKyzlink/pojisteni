


# Vytvoření nového pojištění 

def vytvorit_pojisteni():
    import sqlite3


    # Informace o pojištěném
    print("\nZadejte osobní údaje pojištěného")
    print(30 * "-")
    jmeno_pojisteneho = input("\nJméno: ")
    prijmeni_pojisteneho = input("Příjmení: ")
    datum_nar = input("Datum narozeni (format dd.mm.rr): ")
    telefonni_cislo = input("Telefonní číslo: ")
    vyber_pojisteni = input("Zadejte číslo pro výběr druhu pojištění: \n1 - Auto/moto - Havarijní pojištění\n2 - Auto/moto - Povinné ručení\n3 - Pojištění majetku\n4 - Pojištění odpovědnosti za škody\n5 - Životní pojištění\n6 - All risk pojištění\n")


    conn = sqlite3.connect('pojisteni.db') #spojení s databází
    c = conn.cursor() #vytvoření kurzoru

    # Zápis pojištěného do databáze
    c.execute("""INSERT INTO 'pojisteny' ('jmeno_pojisteneho', 'prijmeni_pojisteneho', 'datum_narozeni', 'tel_cislo', 'id_pojisteni')
    VALUES ('{}', '{}', '{}', '{}', '{}') """.format(jmeno_pojisteneho, prijmeni_pojisteneho, datum_nar,telefonni_cislo, vyber_pojisteni))



    conn.commit()
    print("\nData byla uložena.")
    conn.close()
    

    


    


