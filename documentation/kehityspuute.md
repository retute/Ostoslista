# Puutteet, heikkoudet ja kehitysideat

## Puutteet ja heikkoudet

### Errorit
- Useista validointi-erroreista tulee ilmoitus. Olisin kuitenkin halunnut ilmoitukset punaisella tekstill�, mutta en onnistunut siin�.
- Kategorian nimen asettaminen uniikiksi ei toiminut, sill� muuten kukaan muu k�ytt�j� ei olisi voinut luoda itselleen saman nimist� kategoriaa.

### CRUD
- Sovelluksessa voi t�ll� hetkell� muokata tuotteen "ostettu" tilaa. T�ss� arvoina on kuitenkin *1 tai 0* eik� *"true" tai "false"*.
- Kategorian nimen muokkaamismahdollisuus j�i toteuttamatta. T�ll� lis�yksell� olisin saanut toteutettua toisen t�yden *CRUD*:in: kategorian luominen, *kategorian nimen muokkaaminen*, kategorian koon p�ivittyminen, kategorian poistaminen.


### Monesta moneen suhde/suhteet
- [Tietokantakaavion sivulta](https://github.com/retute/Ostoslista/blob/master/documentation/tietokantakaavio.md) l�ytyy ideoita siit�, mit� monesta moneen suhteita olin ajatellut toteuttaa. Aika/taidot eiv�t kuitenkaan riitt�neet t�h�n.


## Jatkokehitysidet

### K�ytt�j� voi n�hd� listan tuotteista kategoriakohtaisesti
- Kategorialistan nimill� on linkit, joita painamalla k�ytt�j� p��see n�kem��n listan tuotteista, jotka kuuluvat kyseiseen kategoriaan

### K�ytt�j� voi poistaa oman k�ytt�j�tunnuksensa
- Kirjautuneen k�ytt�j�n oikeaan yl�kulmaan tulee linkki, josta k�ytt�j� voi poistaa oman k�ytt�j�tunnuksensa
- Samalla poistuvat my�s kaikki k�ytt�j�n lis��m�t tuotteet ja kategoriat

### K�ytt�j� voi muokata kategorian/tuotteen nime�
- Kategorian nime� voi muokata ja uusi tieto tallentuu tietokantaan vanhan nimen tilalle.
- Tuotteen nime� voi muokata.
