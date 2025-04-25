import random
from sys import exit
import time

# Speciale kaarten:
# 2 - De volgende speler moet twee kaarten pakken, tenzij die een twee of joker kan opleggen.
# 7 - Blijft kleven; de speler mag nog een kaart neerleggen.
# 8 - In de wacht; de volgende speler wordt overgeslagen.
# boer - De speler moet de kleur kiezen van de volgende kaart. (hier variabele voor nodig)
# joker - De volgende speler moet vijf kaarten pakken, tenzij die een twee of joker kan opleggen.

# to do, onder meer: 
# - !!! Zorgen dat waarden variabelen na beurt goed worden doorgegeven aan functie start_pesten
# Zorgen dat kaarten gesorteerd worden wanneer die van trekstapel gepakt worden (gebeurt nu alleen met initieel verdelen kaarten)
# Verder testen en bugfixen.


class Kaartenstapel (object):
    
    kaartenpak = [
    {"kleur": "harten", "waarde": 2, "pestkaart": True, "naam": "2"},
    {"kleur": "harten", "waarde": 3, "pestkaart": False, "naam": "3"},
    {"kleur": "harten", "waarde": 4, "pestkaart": False, "naam": "4"},
    {"kleur": "harten", "waarde": 5, "pestkaart": False, "naam": "5"},
    {"kleur": "harten", "waarde": 6, "pestkaart": False, "naam": "6"},
    {"kleur": "harten", "waarde": 7, "pestkaart": True, "naam": "7"},
    {"kleur": "harten", "waarde": 8, "pestkaart": True, "naam": "8"},
    {"kleur": "harten", "waarde": 9, "pestkaart": False, "naam": "9"},
    {"kleur": "harten", "waarde": 10, "pestkaart": False, "naam": "10"},
    {"kleur": "harten", "waarde": 11, "pestkaart": True, "naam": "boer"},
    {"kleur": "harten", "waarde": 12, "pestkaart": False, "naam": "vrouw"},
    {"kleur": "harten", "waarde": 13, "pestkaart": False, "naam": "koning"},
    {"kleur": "harten", "waarde": 14, "pestkaart": False, "naam": "aas"},
    {"kleur": "ruiten", "waarde": 2, "pestkaart": True, "naam": "2"},
    {"kleur": "ruiten", "waarde": 3, "pestkaart": False, "naam": "3"},
    {"kleur": "ruiten", "waarde": 4, "pestkaart": False, "naam": "4"},
    {"kleur": "ruiten", "waarde": 5, "pestkaart": False, "naam": "5"},
    {"kleur": "ruiten", "waarde": 6, "pestkaart": False, "naam": "6"},
    {"kleur": "ruiten", "waarde": 7, "pestkaart": True, "naam": "7"},
    {"kleur": "ruiten", "waarde": 8, "pestkaart": True, "naam": "8"},
    {"kleur": "ruiten", "waarde": 9, "pestkaart": False, "naam": "9"},
    {"kleur": "ruiten", "waarde": 10, "pestkaart": False, "naam": "10"},
    {"kleur": "ruiten", "waarde": 11, "pestkaart": True, "naam": "boer"},
    {"kleur": "ruiten", "waarde": 12, "pestkaart": False, "naam": "vrouw"},
    {"kleur": "ruiten", "waarde": 13, "pestkaart": False, "naam": "koning"},
    {"kleur": "ruiten", "waarde": 14, "pestkaart": False, "naam": "aas"},
    {"kleur": "klaver", "waarde": 2, "pestkaart": True, "naam": "2"},
    {"kleur": "klaver", "waarde": 3, "pestkaart": False, "naam": "3"},
    {"kleur": "klaver", "waarde": 4, "pestkaart": False, "naam": "4"},
    {"kleur": "klaver", "waarde": 5, "pestkaart": False, "naam": "5"},
    {"kleur": "klaver", "waarde": 6, "pestkaart": False, "naam": "6"},
    {"kleur": "klaver", "waarde": 7, "pestkaart": True, "naam": "7"},
    {"kleur": "klaver", "waarde": 8, "pestkaart": True, "naam": "8"},
    {"kleur": "klaver", "waarde": 9, "pestkaart": False, "naam": "9"},
    {"kleur": "klaver", "waarde": 10, "pestkaart": False, "naam": "10"},
    {"kleur": "klaver", "waarde": 11, "pestkaart": True, "naam": "boer"},
    {"kleur": "klaver", "waarde": 12, "pestkaart": False, "naam": "vrouw"},
    {"kleur": "klaver", "waarde": 13, "pestkaart": False, "naam": "koning"},
    {"kleur": "klaver", "waarde": 14, "pestkaart": False, "naam": "aas"},
    {"kleur": "schoppen", "waarde": 2, "pestkaart": True, "naam": "2"},
    {"kleur": "schoppen", "waarde": 3, "pestkaart": False, "naam": "3"},
    {"kleur": "schoppen", "waarde": 4, "pestkaart": False, "naam": "4"},
    {"kleur": "schoppen", "waarde": 5, "pestkaart": False, "naam": "5"},
    {"kleur": "schoppen", "waarde": 6, "pestkaart": False, "naam": "6"},
    {"kleur": "schoppen", "waarde": 7, "pestkaart": True, "naam": "7"},
    {"kleur": "schoppen", "waarde": 8, "pestkaart": True, "naam": "8"},
    {"kleur": "schoppen", "waarde": 9, "pestkaart": False, "naam": "9"},
    {"kleur": "schoppen", "waarde": 10, "pestkaart": False, "naam": "10"},
    {"kleur": "schoppen", "waarde": 11, "pestkaart": True, "naam": "boer"},
    {"kleur": "schoppen", "waarde": 12, "pestkaart": False, "naam": "vrouw"},
    {"kleur": "schoppen", "waarde": 13, "pestkaart": False, "naam": "koning"},
    {"kleur": "schoppen", "waarde": 14, "pestkaart": False, "naam": "aas"},
    {"kleur": "rode", "waarde": 15, "pestkaart": True, "naam": "joker"},
    {"kleur": "zwarte", "waarde": 15, "pestkaart": True, "naam": "joker"}]


class Trekstapel (Kaartenstapel):

    trekkaartenstapel = []


class Aflegstapel (Kaartenstapel):

    aflegkaartenstapel = []


class Speler (object):

    gekozen_namen = []

    def __init__(self, speler_nummer):
        self.naam = self.set_naam_speler(speler_nummer)
        self.kaarten_in_hand = []

    def set_naam_speler(self, speler):
        naam = input(f"\nHoe heet speler {speler}?\n> ")
        if naam in self.gekozen_namen:
            print("\nEen andere speler heeft al die naam gekregen. Bedenk iets anders.")
            return self.set_naam_speler(speler)
        else:
            self.gekozen_namen.append(naam)
            return naam
        
    def sorteer_kaarten_per_speler(speler):
        kaarten_gesorteerd = sorted(speler.kaarten_in_hand, key=lambda d: (d['kleur'], d['waarde']))
        speler.kaarten_in_hand = kaarten_gesorteerd
        

class Spelsessie (object):
   
    def __init__(self, begin_speler, boer_verplichting, aantal_strafkaarten):
        self.kaartenpak = Kaartenstapel
        self.verdelen = Kaartverdeling
        self.speler = Speler
        self.spelersfabriek = Spelersfabriek
        self.trekstapel = Trekstapel
        self.aflegstapel = Aflegstapel
        self.spelerronde = Spelerronde

        self.spelers = self.spelersfabriek.maak_spelers_aan(self.spelersfabriek)
        self.kaartenset = self.verdelen.sorteren(self.kaartenpak.kaartenpak, 54)
        self.verdeling = self.verdelen.verdelen_over_spelers(self, self.spelers, self.kaartenset)

        self.speler_aan_de_beurt = self.spelers[begin_speler]  # Weinig elegante oplossing
        self.boer_verplichting = boer_verplichting
        self.aantal_strafkaarten = aantal_strafkaarten
        

    def speel_pesten(self):
        print("\n---------------------------------------------------\nLaten we beginnen!")
        while True:
            self.spelerronde.spelerronde(self, self.speler_aan_de_beurt, self.boer_verplichting, self.aantal_strafkaarten)
            beëindig_ronde = input("\nVoer een willekeurig teken in om je ronde te beëindingen.\n> ")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            doorgaan = input(f"\nVoer een willekeurig teken in om door te gaan naar speler {self.speler_aan_de_beurt.naam}.\n> ")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---------------------------------------------------")

    
class Spelerronde (Spelsessie):

    def spelerronde(self, speler, boer_verplichting, aantal_strafkaarten):
        print(f"\n{speler.naam} is nu aan de beurt.")
        print(f"\nEr liggen momenteel {len(self.trekstapel.trekkaartenstapel)} kaart(en) op de trekstapel.\n")
        for andere_speler in self.spelers:
            if andere_speler != speler:
                print(f'Speler {andere_speler.naam} houdt momenteel {len(andere_speler.kaarten_in_hand)} kaart(en) vast.')
            else:
                pass
        
        print(f'\n\nDe bovenste kaart van de aflegstapel is momenteel:\n\nEen {self.aflegstapel.aflegkaartenstapel[-1]["kleur"]} {self.aflegstapel.aflegkaartenstapel[-1]["naam"]}')

        time.sleep(5)
        print("\nJe hebt momenteel de volgende kaart(en) in je handen:\n")
        for kaart in speler.kaarten_in_hand:
            if kaart != speler.kaarten_in_hand[-1]:
                print(f'Een {kaart["kleur"]} {kaart["naam"]};')
            else:
                print(f'Een {kaart["kleur"]} {kaart["naam"]}')

        self.spelerronde.spelerronde_deel_2(self, speler, boer_verplichting, aantal_strafkaarten)

    def spelerronde_deel_2(self, speler, boer_verplichting, aantal_strafkaarten):

        if aantal_strafkaarten != 0:
            time.sleep(4)
            print(f"\nTenzij je een joker of twee kunt opleggen, moet je {aantal_strafkaarten} kaarten van de trekstapel pakken.")
            mogelijkheden = self.spelerronde.noem_mogelijkheden_bij_strafkaarten(self, speler)
        elif boer_verplichting != "":
            time.sleep(2)
            print(f"\nAangezien eerder een boer is neergelegd, moet je volgende kaart van deze kleur zijn: {boer_verplichting}.")
            mogelijkheden = self.spelerronde.noem_mogelijkheden_na_boer(self, speler, boer_verplichting)
        else:
            mogelijkheden = self.spelerronde.noem_mogelijkheden_geen_bijzonderheden(self, speler)

        time.sleep(5)
        if len(mogelijkheden) == 0:
            if aantal_strafkaarten == 0:
                print("\nAangezien je geen kaarten neer kunt leggen, pak je een kaart van de stapel.")
                if len(self.aflegstapel.aflegkaartenstapel) == 0:
                    self.verdelen.maak_aflegstapel_tot_trekstapel(self, speler)
                else:
                    pass
                te_pakken_kaart = self.trekstapel.trekkaartenstapel[-1]
                speler.kaarten_in_hand.append(te_pakken_kaart)
                self.trekstapel.trekkaartenstapel.remove(te_pakken_kaart)
                time.sleep(1)
                print(f'\nJe hebt de volgende kaart gepakt: een {te_pakken_kaart["kleur"]} {te_pakken_kaart["naam"]}')
            else:
                print(f"\nAangezien je geen twee of joker hebt, moet je {aantal_strafkaarten} kaarten van de stapel pakken.\n\nJe pakt:")
                if aantal_strafkaarten > len(self.trekstapel.trekkaartenstapel):
                    speler.kaarten_in_hand.append(self.trekstapel.trekkaartenstapel[::])
                    aantal_strafkaarten -= len(self.trekstapel.trekkaartenstapel)
                    for kaart in self.trekstapel.trekkaartenstapel:
                        print(f'Een {kaart["kleur"]} {kaart["naam"]};')
                    self.trekstapel.trekkaartenstapel.clear()
                    self.verdelen.maak_aflegstapel_tot_trekstapel(self, speler)
                else:
                    pass

                while aantal_strafkaarten > 0:
                    te_pakken_kaart = self.trekstapel.trekkaartenstapel[-1]
                    speler.kaarten_in_hand.append(te_pakken_kaart)
                    self.trekstapel.trekkaartenstapel.remove(te_pakken_kaart)
                    aantal_strafkaarten -= 1
                    if aantal_strafkaarten > 0:
                        print(f'Een {te_pakken_kaart["kleur"]} {te_pakken_kaart["naam"]};')
                    else:
                        print(f'Een {te_pakken_kaart["kleur"]} {te_pakken_kaart["naam"]}')

            self.speler.sorteer_kaarten_per_speler(speler)
            volgende_speler = ""
            if self.spelers.index(speler) != (len(self.spelers) -1):
                volgende_speler = self.spelers[self.spelers.index(speler) + 1]
            else:
                volgende_speler = self.spelers[0]

            self.spelerronde.set_waardes_voor_volgende_ronde (self, volgende_speler, boer_verplichting, aantal_strafkaarten)

        elif len(mogelijkheden) == 1:
            print(f'\nAangezien je maar één kaart neer kunt leggen, leg je deze kaart neer.\nDit is een: {mogelijkheden[0]["kleur"]} {mogelijkheden[0]["naam"]}.')
            boer_verplichting = ""
            self.spelerronde.afsluiting_ronde(self, speler, mogelijkheden[0], boer_verplichting, aantal_strafkaarten)

        else:
            print("\nJe kunt de volgende kaarten neerleggen:\n")
            for kaart in mogelijkheden:
                print(f"{mogelijkheden.index(kaart) + 1}. Een {kaart['kleur']} {kaart['naam']}")
            kaartkeuze = self.spelerronde.speel_ronde(self, mogelijkheden)
            print(f'\nJe legt de volgende kaart neer: Een {kaartkeuze["kleur"]} { kaartkeuze["naam"]}.')
            boer_verplichting = ""
            input_voor_volgende_speler = self.spelerronde.afsluiting_ronde(self, speler, kaartkeuze, boer_verplichting, aantal_strafkaarten)
            return input_voor_volgende_speler


    def noem_mogelijkheden_geen_bijzonderheden(self, speler):        
        mogelijkheden = []
        for kaart in speler.kaarten_in_hand:
            if (kaart["kleur"] == self.aflegstapel.aflegkaartenstapel[-1]["kleur"] or kaart["naam"] == self.aflegstapel.aflegkaartenstapel[-1]["naam"]) or kaart["naam"] == "joker" or self.aflegstapel.aflegkaartenstapel[-1]["naam"] == "joker" or (self.aflegstapel.aflegkaartenstapel[-1]["naam"] == "2" and len(self.aflegstapel.aflegkaartenstapel) > 1):
                mogelijkheden.append(kaart)
            else:
                pass
        return mogelijkheden
    
    
    def noem_mogelijkheden_na_boer(self, speler, boer_verplichting):
        mogelijkheden = []
        for kaart in speler.kaarten_in_hand:
            if kaart["kleur"] == boer_verplichting or kaart["naam"] == "joker":
                mogelijkheden.append(kaart)
            else:
                pass
        return mogelijkheden
    

    def noem_mogelijkheden_bij_strafkaarten(self, speler):
        mogelijkheden = []
        for kaart in speler.kaarten_in_hand:
            if kaart["naam"] == "2" or kaart["naam"] == "joker":
                mogelijkheden.append(kaart)
            else:
                pass
        return mogelijkheden


    def speel_ronde(self, mogelijkheden):
        kaart_gekozen = False
        kaartkeuze = ""
        while kaart_gekozen is False:
            kaartkeuze = input("\nWelke kaart wil je neerleggen?\nVoer het getal in dat je ziet staan naast de kaart die je neer wilt leggen.\n> ")
            try: kaartkeuze = int(kaartkeuze)
            except:
                print("\nSorry, je kunt alleen een enkel getal invoeren.")
            if type(kaartkeuze) == int and not kaartkeuze < 1 and kaartkeuze <= len(mogelijkheden):
                kaartkeuze = mogelijkheden[kaartkeuze-1]
                kaart_gekozen = True
            elif type(kaartkeuze) != int:
                pass
            elif  kaartkeuze <1:
                print("\nJe kunt geen getal kleiner dan één invoeren.")
            else:
                print("\nZo veel opties heb je niet!")
        return kaartkeuze

    def afsluiting_ronde(self, speler, kaartkeuze, boer_verplichting, aantal_strafkaarten):
        
        self.aflegstapel.aflegkaartenstapel.append(kaartkeuze)
        speler.kaarten_in_hand.remove(kaartkeuze)
        if speler.kaarten_in_hand == []:
            if kaartkeuze["pestkaart"] is False:
                print(f"\nAangezien je geen kaarten meer in je hand hebt, heb je het spel gewonnen!\n\nDriewerf hoera voor {speler.naam}!\n\nHoera!\n\nHoera!\n\nHoera!")
                exit(0)
            else:
                print("\nJe mag niet eindigen met een pestkaart. Je moet daarom twee kaarten van de trekstapel pakken.")
                if len(self.trekstapel.trekkaartenstapel) < 2:
                    self.verdelen.maak_aflegstapel_tot_trekstapel(self, speler)
                else:
                    pass

                te_pakken_kaarten = self.trekstapel.trekkaartenstapel[-1:-3:-1]
                speler.kaarten_in_hand.append(te_pakken_kaarten)
                self.trekstapel.trekkaartenstapel.remove(te_pakken_kaarten)

        elif len(speler.kaarten_in_hand) == 1:
            print("\nAangezien je nog maar één kaart in je hand hebt, is het tijd op tafel te kloppen.")
            kloppen = input("Voer een willekeurig teken in om op tafel te kloppen.\n> ")

        else:
            pass
        
        time.sleep(2)
        if speler != self.spelers[-1]:
            volgende_speler = self.spelers[self.spelers.index(speler) + 1]
        else:
            volgende_speler = self.spelers[0]

        if kaartkeuze["naam"] == "boer":
            kleur_gekozen = False
            kleuropties = ["harten", "ruiten", "klaver", "schoppen"]
            while kleur_gekozen is False:
                boer_verplichting = input("\nVan welke kleur moet de volgende kaart zijn?\n> ").lower()
                if boer_verplichting not in kleuropties:
                    print("\nIk heb je antwoord niet begrepen. Voer voortaan 'harten', 'ruiten', 'klaver' of 'schoppen' in.")
                else:
                    kleur_gekozen = True

        elif kaartkeuze["naam"] == "2" or kaartkeuze["naam"] == "joker":
            strafkaart = kaartkeuze
            if strafkaart["naam"] == "joker":
                strafkaart["waarde"] = 5
            else:
                pass
            aantal_strafkaarten += strafkaart["waarde"]
            print(f"\nDe volgende speler zal nu {aantal_strafkaarten} kaarten moeten pakken, of zelf een twee of joker opleggen.")

        elif kaartkeuze["naam"] == "7":
            print("\nJe mag nog een keer!")
            self.spelerronde.spelerronde_deel_2(self, speler, boer_verplichting, aantal_strafkaarten)

        elif kaartkeuze["naam"] == "8":
            if len(self.spelers) > 2:
                if self.spelers.index(speler) < (len(self.spelers) -2):
                    volgende_speler = self.spelers[self.spelers.index(speler) + 2]
                else:
                    if speler == self.spelers[-2]:
                        volgende_speler = self.spelers[0]
                    else:
                        volgende_speler = self.spelers[1]
                print(f"\nDe volgende speler wordt nu overgeslagen, zodat {volgende_speler.naam} zo aan de beurt is.")
            else:
                print("\nJe mag nog een keer!")
                self.spelerronde.spelerronde_deel_2(self, speler, boer_verplichting, aantal_strafkaarten)
        else:
            pass

        self.spelerronde.set_waardes_voor_volgende_ronde (self, volgende_speler, boer_verplichting, aantal_strafkaarten)

    def set_waardes_voor_volgende_ronde (self, volgende_speler, boer_verplichting, aantal_strafkaarten):

        self.speler_aan_de_beurt = volgende_speler
        self.boer_verplichting = boer_verplichting
        self.aantal_strafkaarten = aantal_strafkaarten

class Spelersfabriek (Spelsessie):

    mogelijke_speleraantallen = ["2", "3", "4", "5", "twee", "drie", "vier", "vijf"]
    getal_woord_correspondentie = {"twee": 2, "drie": 3, "vier": 4, "vijf": 5}
    
    def maak_spelers_aan (self):
        spelers = []
        aantal_spelers = self.bepaal_aantal_spelers(self)
        for i in range(1, aantal_spelers + 1):
            spelers.append(Speler(i))
        return spelers
    
    def bepaal_aantal_spelers(self):
        aantal_spelers_bepaald = False
        while aantal_spelers_bepaald is False:
            aantal_spelers = input("\nMet hoeveel spelers wil je vandaag pesten?\n\nHet minimale aantal is twee, en het maximale aantal is vijf.\n> ")
            if aantal_spelers.lower() not in self.mogelijke_speleraantallen:
                print("\nDat is geen geldig aantal, helaas. Vul voortaan een getal tussen 2 en 5 in (als getal of als Nederlands woord).")
            else:
                aantal_spelers_bepaald = True
                try: aantal_spelers = int(aantal_spelers)
                except:
                    aantal_spelers = self.getal_woord_correspondentie[aantal_spelers]
                return aantal_spelers

            
class Kaartverdeling (Spelsessie):

    def sorteren(kopie_kaartenset, aantal_te_sorteren_kaarten):
        gesorteerd_pak = []
        while len(gesorteerd_pak) < aantal_te_sorteren_kaarten:
            te_sorteren_kaart = random.randint(0, len(kopie_kaartenset) - 1)
            gesorteerd_pak.append(kopie_kaartenset[te_sorteren_kaart])
            kopie_kaartenset.remove(kopie_kaartenset[te_sorteren_kaart])
        else:
            print("\n---------------------------------------------------\nDe kaarten zijn gesorteerd.\n\nNu worden ze over de spelers verdeeld.")
            return gesorteerd_pak

    def verdelen_over_spelers (self, spelers, gesorteerd_pak):
        for speler in spelers:
            while len(speler.kaarten_in_hand) < 7:
                speler.kaarten_in_hand.append(gesorteerd_pak[0])
                gesorteerd_pak.remove(gesorteerd_pak[0])
            else:
                self.speler.sorteer_kaarten_per_speler(speler)

        for kaart in gesorteerd_pak:
            self.trekstapel.trekkaartenstapel.append(kaart)
        gesorteerd_pak.clear()
                
        print(f"\nDe kaarten zijn verdeeld over de aanwezige {len(spelers)} spelers.")
        self.verdelen.leg_beginkaart_op_aflegstapel(self)

    def leg_beginkaart_op_aflegstapel(self):

        beginkaart_aflegstapel = self.trekstapel.trekkaartenstapel[-1]
        self.aflegstapel.aflegkaartenstapel.append(beginkaart_aflegstapel)
        self.trekstapel.trekkaartenstapel.remove(beginkaart_aflegstapel)

    def maak_aflegstapel_tot_trekstapel(self, speler):

        print("\nAangezien er geen kaarten meer liggen op de trekstapel, moeten de kaarten van de aflegstapel opnieuw geschud worden.") #Zou mis kunnen gaan als er maar een kaart op de aflegstapel ligt.
        te_sorteren_kaarten = self.aflegstapel.aflegkaartenstapel[:len(self.aflegstapel.aflegkaartenstapel)-1:]
        self.aflegstapel.aflegkaartenstapel = self.aflegstapel.aflegkaartenstapel[-1]
        self.trekstapel.trekkaartenstapel = self.verdelen.sorteren(te_sorteren_kaarten, len(te_sorteren_kaarten))

def main():

    nieuw_spel = Spelsessie (0, "", 0)
    nieuw_spel.speel_pesten()

main()
