import random
from sys import exit

class Kaartenstapel (object):
    
    naam_en_waarde = {"joker": 1, "boer": 11, "vrouw": 12, "koning": 13, "aas": 14}

    kaartenpak = [
    {"kleur": "harten", "waarde": 2},
    {"kleur": "harten", "waarde": 3},
    {"kleur": "harten", "waarde": 4},
    {"kleur": "harten", "waarde": 5},
    {"kleur": "harten", "waarde": 6},
    {"kleur": "harten", "waarde": 7},
    {"kleur": "harten", "waarde": 8},
    {"kleur": "harten", "waarde": 9},
    {"kleur": "harten", "waarde": 10},
    {"kleur": "harten", "waarde": "boer"},
    {"kleur": "harten", "waarde": "vrouw"},
    {"kleur": "harten", "waarde": "koning"},
    {"kleur": "harten", "waarde": "aas"},
    {"kleur": "ruiten", "waarde": 2},
    {"kleur": "ruiten", "waarde": 3},
    {"kleur": "ruiten", "waarde": 4},
    {"kleur": "ruiten", "waarde": 5},
    {"kleur": "ruiten", "waarde": 6},
    {"kleur": "ruiten", "waarde": 7},
    {"kleur": "ruiten", "waarde": 8},
    {"kleur": "ruiten", "waarde": 9},
    {"kleur": "ruiten", "waarde": 10},
    {"kleur": "ruiten", "waarde": "boer"},
    {"kleur": "ruiten", "waarde": "vrouw"},
    {"kleur": "ruiten", "waarde": "koning"},
    {"kleur": "ruiten", "waarde": "aas"},
    {"kleur": "klaver", "waarde": 2},
    {"kleur": "klaver", "waarde": 3},
    {"kleur": "klaver", "waarde": 4},
    {"kleur": "klaver", "waarde": 5},
    {"kleur": "klaver", "waarde": 6},
    {"kleur": "klaver", "waarde": 7},
    {"kleur": "klaver", "waarde": 8},
    {"kleur": "klaver", "waarde": 9},
    {"kleur": "klaver", "waarde": 10},
    {"kleur": "klaver", "waarde": "boer"},
    {"kleur": "klaver", "waarde": "vrouw"},
    {"kleur": "klaver", "waarde": "koning"},
    {"kleur": "klaver", "waarde": "aas"},
    {"kleur": "schoppen", "waarde": 2},
    {"kleur": "schoppen", "waarde": 3},
    {"kleur": "schoppen", "waarde": 4},
    {"kleur": "schoppen", "waarde": 5},
    {"kleur": "schoppen", "waarde": 6},
    {"kleur": "schoppen", "waarde": 7},
    {"kleur": "schoppen", "waarde": 8},
    {"kleur": "schoppen", "waarde": 9},
    {"kleur": "schoppen", "waarde": 10},
    {"kleur": "schoppen", "waarde": "boer"},
    {"kleur": "schoppen", "waarde": "vrouw"},
    {"kleur": "schoppen", "waarde": "koning"},
    {"kleur": "schoppen", "waarde": "aas"},
    {"kleur": "rode", "waarde": "joker"},
    {"kleur": "zwarte", "waarde": "joker"}]


class Trekstapel (Kaartenstapel):

    trekkaartenstapel = []


class Aflegstapel (Kaartenstapel):

    aflegkaartenstapel = []


class Speler (object):

    def __init__(self, speler_nummer):
        self.naam = input(f"\nHoe heet speler {speler_nummer}?\n> ")
        self.kaarten_in_hand = []
    

class Spelsessie (object):
   
    def __init__(self):
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

    def speel_pesten(self):
        print("\n---------------------------------------------------\nLaten we beginnen!")
        klaar_met_spelen = False
        speler = self.spelers[0]
        while klaar_met_spelen is False:
            self.spelerronde.spelerronde(self, speler)
            doorgaan = input("\nVoer een willekeurige toets in om door te gaan naar de volgende speler.")
            print("---------------------------------------------------")
            if self.spelers.index(speler) < len(self.spelers) -1:
                speler = self.spelers[self.spelers.index(speler)+1]
            else:
                speler = self.spelers[0]
                # klaar_met_spelen = True

    
class Spelerronde (Spelsessie):

    def spelerronde(self, speler):
        print(f"\n{speler.naam} is nu aan de beurt.")
        mogelijkheden = self.spelerronde.noem_mogelijkheden(self, speler)
        if len(mogelijkheden) == 0:
            self.verdelen.maak_aflegstapel_tot_trekstapel(self, speler)
            # return
        elif len(mogelijkheden) == 1:
            self.spelerronde.leg_enige_mogelijke_kaart_af(self, speler, mogelijkheden[0])
            # return
        else:
            self.spelerronde.speel_ronde(self, speler, mogelijkheden)
            # return

    def noem_mogelijkheden(self, speler):
        print(f'\nDe bovenste kaart van de aflegstapel is momenteel:\n\nEen {self.aflegstapel.aflegkaartenstapel[-1]["kleur"]} {self.aflegstapel.aflegkaartenstapel[-1] ["waarde"]}.')
        
        print(f"\nEr liggen momenteel {len(self.trekstapel.trekkaartenstapel)} kaart(en) op de trekstapel.")
        for andere_speler in self.spelers:
            if andere_speler != speler:
                print(f'\nSpeler {andere_speler.naam} houdt momenteel {len(andere_speler.kaarten_in_hand)} kaart(en) vast.')
            else:
                pass

        print(f"\n{speler.naam} heeft momenteel de volgende kaarten in zijn/haar handen:\n")
        for kaart in speler.kaarten_in_hand:
            if kaart != speler.kaarten_in_hand[-1]:
                print(f'Een {kaart["kleur"]} {kaart["waarde"]};')
            else:
                print(f'Een {kaart["kleur"]} {kaart["waarde"]}')

        mogelijkheden = []
        for kaart in speler.kaarten_in_hand:
            if kaart["kleur"] == self.aflegstapel.aflegkaartenstapel[-1]["kleur"] or kaart["waarde"] == self.aflegstapel.aflegkaartenstapel[-1]["waarde"]:
                mogelijkheden.append(kaart)
            else:
                pass
        if len(mogelijkheden) > 0:
            print("\nHiervan kunnen de volgende kaarten worden afgelegd:\n")
            for kaart in mogelijkheden:
                print(f"{mogelijkheden.index(kaart) + 1}. Een {kaart['kleur']} {kaart['waarde']}")
        else:
            pass
        return mogelijkheden
    

    
    def leg_enige_mogelijke_kaart_af(self, speler, mogelijkheid):
        print(f"\nAangezien speler {speler.naam} maar een kaart neer kan leggen, legt hij/zij deze kaart neer.")
        print(f'\nDit is een: {mogelijkheid["kleur"]} {mogelijkheid["waarde"]}.')
        self.aflegstapel.aflegkaartenstapel.append(mogelijkheid)
        speler.kaarten_in_hand.remove(mogelijkheid)

    def speel_ronde(self, speler, mogelijkheden):
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
        
        print(f'\nSpeler {speler.naam} legt de volgende kaart neer: Een {kaartkeuze["kleur"]} { kaartkeuze["waarde"]}.')
        self.aflegstapel.aflegkaartenstapel.append(kaartkeuze)
        speler.kaarten_in_hand.remove(kaartkeuze)
        # Hierna controleren of iemand nog een andere kaart neer kan leggen. 

                
            

class Spelersfabriek (Spelsessie):

    mogelijke_speleraantallen = ["2", "3", "4", "5", "6", "twee", "drie", "vier", "vijf", "zes"]
    getal_woord_correspondentie = {"twee": 2, "drie": 3, "vier": 4, "vijf": 5, "zes": 6}
    
    def maak_spelers_aan (self):
        spelers = []
        aantal_spelers = self.bepaal_aantal_spelers(self)
        for i in range(1, aantal_spelers + 1):
            spelers.append(Speler(i))
        return spelers
    
    def bepaal_aantal_spelers(self):
        aantal_spelers_bepaald = False
        while aantal_spelers_bepaald is False:
            aantal_spelers = input("\nMet hoeveel spelers wil je vandaag pesten?\n\nHet minimale aantal is twee, en het maximale aantal is zes.\n> ")
            if aantal_spelers.lower() not in self.mogelijke_speleraantallen:
                print("\nDat is geen geldig aantal, helaas. Vul voortaan een getal tussen 2 en 6 in (als getal of als Nederlands woord).")
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
        kaarten_verdeeld = False
        while kaarten_verdeeld is False:
            for speler in spelers:
                if len(speler.kaarten_in_hand) < 7:
                    speler.kaarten_in_hand.append(gesorteerd_pak[0])
                    gesorteerd_pak.remove(gesorteerd_pak[0])
                else:
                    while len(gesorteerd_pak) > 0:
                        self.trekstapel.trekkaartenstapel.append(gesorteerd_pak[0])
                        gesorteerd_pak.remove(gesorteerd_pak[0])
                    kaarten_verdeeld = True
                    print(f"\nDe kaarten zijn verdeeld over de aanwezige {len(spelers)} spelers.")
                    self.verdelen.leg_beginkaart_op_aflegstapel(self)
                    break

    def leg_beginkaart_op_aflegstapel(self):

        beginkaart_aflegstapel = self.trekstapel.trekkaartenstapel[0]
        self.aflegstapel.aflegkaartenstapel.append(beginkaart_aflegstapel)
        self.trekstapel.trekkaartenstapel.remove(beginkaart_aflegstapel)

    def maak_aflegstapel_tot_trekstapel(self, speler):
        print(f"\nAangezien {speler.naam} geen kaarten neer kan leggen, pakt hij/zij een kaart van de stapel.")
        if len(self.trekstapel.trekkaartenstapel) != 0:
            gepakte_kaart = self.trekstapel.trekkaartenstapel[0]
            speler.kaarten_in_hand.append(gepakte_kaart)
            self.trekstapel.trekkaartenstapel.remove(gepakte_kaart)
        else:
            print("\nAangezien er geen kaarten meer liggen op de trekstapel, moeten de kaarten van de aflegstapel opnieuw geschud worden.")
            te_sorteren_kaarten = self.aflegstapel.aflegkaartenstapel[:len(self.aflegstapel.aflegkaartenstapel)-1:]
            self.aflegstapel.aflegkaartenstapel = self.aflegstapel.aflegkaartenstapel[-1]
            self.trekstapel.trekkaartenstapel = self.verdelen.sorteren(te_sorteren_kaarten, len(te_sorteren_kaarten))

def main():

    nieuw_spel = Spelsessie ()
    nieuw_spel.speel_pesten()

main()