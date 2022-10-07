


# Výpis všech pojištěných
def vypis_vsechny_pojistene():
    import sqlite3

    conn = sqlite3.connect('pojisteni.db') #spojení s databází
    c = conn.cursor() #vytvoření kurzoru
    
    c.execute("""SELECT 'pojisteny'.'jmeno_pojisteneho', 'pojisteny'.'prijmeni_pojisteneho', 'pojisteny'.'datum_narozeni'
    FROM 'pojisteny'""")
    pojistene = c.fetchall()
    print("\n\nVýpis pojištěných:\n",30 * "-", "\n")
    for i in pojistene:
        print("Jméno :", i[0])
        print("Příjmení :", i[1])
        print("Datum narození :", i[2])
        print("\n")

    conn.close()

