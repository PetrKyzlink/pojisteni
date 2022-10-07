

# Výpis detailu pojištěného včetně detailu pojistníka

def vypis_detailu():
    import sqlite3
    
    print("\nZadejte osobní údaje pojištěného pro vyhledávání")
    print(50 * "-")

    jmeno = input("\nJméno: ")
    prijmeni = input("Přijmení: ")
    jmeno_prijmeni = (jmeno, prijmeni, ) # proména pro sql příkaz se zástupnými znaky

    conn = sqlite3.connect('pojisteni.db') #spojení s databází
    c = conn.cursor() #vytvoření kurzoru


    hledat_detail = """SELECT 'pojisteny'.'jmeno_pojisteneho', 'pojisteny'.'prijmeni_pojisteneho', 'pojisteny'.'datum_narozeni', 'pojisteny'.'tel_cislo', 'pojisteni'.'druh_pojisteni'
    FROM 'pojisteny'
    JOIN 'pojisteni' ON 'pojisteny'.'id_pojisteni' = 'pojisteni'.'id_pojisteni'
    WHERE 'pojisteny'.'jmeno_pojisteneho'=? AND 'pojisteny'.'prijmeni_pojisteneho'=?
    LIMIT 1"""
    c.execute(hledat_detail, jmeno_prijmeni)
    v_d = c.fetchone()

    print("\nVýpis detailu pojištěného:\n", 80 * "-")

    print("Jméno: ", v_d[0])
    print("Příjmení: ", v_d[1])
    print("Datum narození: ", v_d[2])
    print("Telefonní číslo: ", v_d[3])
    print("Druh pojištění: ", v_d[4])


    conn.close()




