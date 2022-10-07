from vypis_pojistenych import vypis_vsechny_pojistene
from pridani_pojisteneho import vytvorit_pojisteni
from detail_pojisteni import vypis_detailu


print(30 * "-", "\nEvidence pojištěných")
print(30 * "-")

# Uživatel volí akci
volba_akce = True
while volba_akce:
    print("Vyberte požadovanou akci: ")
    print("1 - Vložit nové pojištění")
    print("2 - Výpis všech pojištěných")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec\n")

    cislo_akce = input()
    if cislo_akce == "1":
        vytvorit_pojisteni()
        volba_akce = True
        input("\nPro pokračování stiskněte klávesu Enter...\n")

    elif cislo_akce == "2":
        vypis_vsechny_pojistene()
        volba_akce = True
        input("\nPro pokračování stiskněte klávesu Enter...\n")

    elif cislo_akce == "3":
        vypis_detailu()
        volba_akce = True
        input("\nPro pokračování stiskněte klávesu Enter...\n")

    elif cislo_akce == "4":
        volba_akce = False
    
    else:
        volba_akce = True
        print("Neplatná volba! Při výběru zadejte pouze číslo 1, 2, 3, 4.")
        input("\nPro pokračování stiskněte klávesu Enter...\n")





