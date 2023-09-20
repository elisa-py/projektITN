class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}"


class EvidencniSystem:
    def __init__(self):
        self.seznam_pojisteny = []

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon):#není určen formát tel.čísla a pozor na diakritiku/šlo by upravit
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.seznam_pojisteny.append(pojisteny)

    def zobraz_seznam_pojisteny(self):
        for pojisteny in self.seznam_pojisteny:
            print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):#neřeším diakritiku
        for pojisteny in self.seznam_pojisteny:
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                return pojisteny
        return None


def main():
    evidencni_system = EvidencniSystem()

    while True:
        print("\nVyberte akci:")
        print("1. Vytvořit nového pojištěného")
        print("2. Zobrazit seznam pojištěných")
        print("3. Vyhledat pojištěného podle jména a příjmení")
        print("4. Konec")

        volba = input("Zadejte číslo akce 1-4: ")#nutná volba pouze v rozmezí 1-4

        if volba == "1":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = int(input("Zadejte věk: "))
            telefon = input("Zadejte telefonní číslo: ")#str...telefonní číslo

            evidencni_system.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
            print("Pojištěný byl úspěšně vytvořen.")
        elif volba == "2":
            print("Seznam pojištěných:")
            evidencni_system.zobraz_seznam_pojisteny()
        elif volba == "3":
            jmeno = input("Zadejte jméno hledaného pojištěného: ")
            prijmeni = input("Zadejte příjmení hledaného pojištěného: ")

            nalezeny_pojisteny = evidencni_system.najdi_pojisteneho(jmeno, prijmeni)
            if nalezeny_pojisteny:
                print("Nalezený pojištěný:", nalezeny_pojisteny)
            else:
                print("Pojištěný nebyl nalezen.")
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba. Zadejte číslo od 1 do 4.")


if __name__ == "__main__":
    main()
