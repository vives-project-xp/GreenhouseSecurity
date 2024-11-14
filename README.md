
# Greenhouse Security

Op de site campus Brugge Xavarianenstraat komt een serre van 3x6m. Daarbij komt later ook nog een Tiny-house. Dit alles als IoT incubator voor project experience. Ons project zal zorgen voor de security en beveiliging van de serre. We maken hiervoor gebruik van bewakings camera's en een toegangs controle systeem.




## Inhoud
- [GreenhouseSecurity](#greenhousesecurity)
  - [Inhoud](#inhoud)
  - [Team](#team)
  - [Installatie](#installatie)
  - [Documentatie](#documentatie)
  - [Erkenningen](#erkenningen)
  - [BOM-Lijst](#bom-lijst)
  - [Research](#research)
## Team

- [Luca De Clerck](https://github.com/LucaClrk)  
- [Xander Claessens](https://github.com/xanderClaessens)   
- [Domien Verstraete](https://github.com/Belgianwafflecorp)  

## Installatie
### Axis Camera Station
Ga naar de [Axis Camera station 5](https://www.axis.com/products/axis-camera-station/download) pagina om de nieuwste versie te downloaden. Hiermee ben je in staat de Axis camera's te beheren.
### Python
Python kan je programmeren via [Visual Studio Code](https://code.visualstudio.com/download) of een andere IDE naar keuze. Bij gebruik van Visual Studio Code kan je de Python extensie installeren om zo te beginnen aan je Python programma.
### Raspberry Pi
Eerst en vooral moet je een [Raspberry Pi](https://www.raspberrypi.com/software/) aankopen. Als het mogelijk is een model 3 of hoger. Hierna kan je via een SD kaart de [Raspberry Pi OS](https://www.raspberrypi.com/software/) installeren op je bordje. Hierna kan je dan via HDMI of DP, te zien welk bordje je hebt, verbinden met de Raspberry Pi. 

## Documentatie
### Research
  - Toegangssystemen:
    - NFC
        NFC staat voor Near-Field Communication. Zoals de naam zelf verklapt is dit een manier om communicatie in te schakelen over een kleine afstand. Een set van communicatie protocollen maken het mogelijk om communicatie tussen elektronische apparaten in staat te stellen over een afstand van max 4cm.  
        Dit werkt met enerzijds een zend-/ontvangapparaat met een voeding en anderzijds een object met een chip en antenne, zoals een kaart, die gezamenlijk een NFC-tag hebben. De tag heeft geen voeding nodig omdat hij inductie energie ontvangt van het apparaat.  
        NFC wordt in veel toepassingen gebruikt. Denk aan betalingtransacties,sleutelhanger voor toegangscontrole...  

        NFC is dus een mogelijke optie voor toegangscontrole tot de serre. Je kan dan met een NFC-tag de serre openen. Bijvoorbeeld aan de hand van je GSM en een simpele RFID-chip.  
    - Authenticator
        Een authenticator is ook een manier om toegangscontrole toe te passen. Denk aan de google authenticator die je constant codes geeft die veranderen. Dit zorgt voor een veilige manier van toegangscontrole omdat je "wachtwoord" tot de serre voor iedereen anders is en constant verandert. Ook is er geen nood aan een kaart of dergelijke, die je mogelijks kan verliezen.  
    - Biometrisch
        Biometrie betekent letterlijk "meten van de levenden" en verwijst in een hele brede zin naar de studie van levende wezens. Wij zullen deze studies toepassen om een biometrisch toegangscontrole systeem te maken.  
        Biometrie kan je "meten", denk aan je vingerafdruk, irispatroon, gelaatstrekken of DNA. Wij zullen niet zo ver gaan als DNA, maar iets zoals je vingerafdruk kan zeker zorgen voor een goeie beveiliging.
        Een toegangskaart of tag zoals bij NFC kan je verliezen, je vinger zal je niet zo rap verliezen.
        Jammer genoeg zullen zij niet aan biometrie doen omdat deze gegevens moeten opgeslaan worden. Door de privacy wet mogen wij dit soort gegevens niet opslaan.

- Camera's
    - Stappenplan

- Melding wanneer iemand het gebied betreed of inlogt
    - SMS
    - Mail

### Project Affiche
Voor het project werden wij gevraagd om een affiche te maken. Deze affiche bevat de titel van het project, een korte beschrijving, de vaardigheden die werden gebruikt voor het project te realiseren en een paar foto's. 
Met dit affiche is het de bedoeling om ons project zo aantrekkelijk mogelijk te maken en gemakkelijk uit te leggen over wat dit gaat.

<img src="images/affiche.png" alt="affiche" width="400" length="800"/>

## Code
### Authenticatie op Raspberry Pi
In de [Setup](./Documenten/setup.md) file Kan je lezen hoe we de authenticatie zullen opzetten op de Raspberry Pi.

## Pictogram:
Verplicht pictogram met aanduiding dat er camera bewaking aanwezig is.
Dit staat in het Koninklijk besluit dat dit zo moet (zie links voor meer info). 

<img src="images/camerawarning.png" alt="camera sticker" width="200" length="400"/>

## Installatie



## Links
- [Info](https://acd.eu/producten/r308-xh-blackline/)
- [Koninklijk Besluit](https://www.besafe.be/sites/default/files/2022-08/ar_pictogramme_-_version_coordonnee_avec_modif_2020.pdf) 
- [Info](https://www.besafe.be/nl/bewakingscamera/pictogram)
- [Klein pin slot](https://www.credexalarmsystems.eu/nl/eb-004-conas-electric-bolt-lockfor-automatic-doors-failsafe.html)
- [2-kanaals 3V relais module](https://www.kiwi-electronics.com/nl/2-kanaals-3v-relais-module-20106?search=relais)
- [Koninklijk Besluit](https://www.besafe.be/sites/default/files/2022-08/ar_pictogramme_-_version_coordonnee_avec_modif_2020.pdf) 
- [Info](https://www.besafe.be/nl/bewakingscamera/pictogram)
- [Klein pin slot](https://www.credexalarmsystems.eu/nl/eb-004-conas-electric-bolt-lockfor-automatic-doors-failsafe.html)
- [Keypad info](https://learn.adafruit.com/matrix-keypad?view=all)
- [Axis OS](https://www.axis.com/products/axis-camera-station/download) 

## Erkenningen

- [Info](https://acd.eu/producten/r308-xh-blackline/)
- [Koninklijk Besluit](https://www.besafe.be/sites/default/files/2022-08/ar_pictogramme_-_version_coordonnee_avec_modif_2020.pdf) 
- [Pictogram](https://www.besafe.be/nl/bewakingscamera/pictogram)
- [Klein Pin Slot](https://www.credexalarmsystems.eu/nl/eb-004-conas-electric-bolt-lockfor-automatic-doors-failsafe.html)

## BOM 

## BOM-Lijst

| Beschrijving | Hoeveelheid | Prijs (€) |
|--------------|-------------|-------|
| Raspberry pi | 1 | 61,95 |
| Nummeriek | 1 | 7,34 |
| Pictogram | 1 | 2,39 |
| Push-pull solenoids | 4 | 47,80 |
| Montage stukken  | 4 | 9,16 |
| Kables | 7 | 12.39 |
| Aftakdoos | 1 | 12.79 |
| Relais module | 1 | 11.90 |
| **Total Price** | - |  |


