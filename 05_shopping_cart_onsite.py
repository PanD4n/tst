kosik = {}
oddelovac = "=" * 40
potraviny = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}

# Uvitani uzivatele
print(
    "Vitejte u naseho nakupniho kosiku!".center(len(oddelovac)),
    oddelovac, sep="\n"
)

# TODO vypsat nabídku zboží (bez počtu kusů)
for potravina, info in potraviny.items():
    cena = info[0]
    print(f"| POTRAVINA: {potravina:^10} | {cena:>3}  Kc |")
print(oddelovac)
# TODO umožnit uživateli vložit zboží do košíku
while (zbozi := input("ZBOZI: ")) != "q":
    print("Pridali jste", zbozi)
    if zbozi not in potraviny:
        print(f"Zbozi --{zbozi}-- neni v nabidce!")

    elif zbozi not in kosik and potraviny[zbozi][1] > 0:
        cena = potraviny[zbozi][0]
        kosik[zbozi] = [cena, 1]  # pridavam poprve do kosiku
        potraviny[zbozi][1] = potraviny[zbozi][1] - 1  # snizit stav skladu
    # vlozit vicekrat stejnou polozku, pokud je skladem
    elif zbozi in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi][1] = kosik[zbozi][1] + 1
        potraviny[zbozi][1] = potraviny[zbozi][1] - 1
    # zamitnout pokud uz neni na sklade
    elif potraviny[zbozi][1] == 0:
        print(f"Zbozi --{zbozi}-- neni skladem!")

print("kosik", kosik)
print("potraviny", potraviny)
# TODO DOMA - vypsat hezky obsah nákupního košíku
# TODO DOMA - sečíst cenu za nákup
