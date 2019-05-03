# Puutteet, heikkoudet ja kehitysideat

## Puutteet ja heikkoudet

### Errorit
- Useista validointi-erroreista tulee ilmoitus. Olisin kuitenkin halunnut ilmoitukset punaisella tekstillä, mutta en onnistunut siinä.
- Kategorian nimen asettaminen uniikiksi ei toiminut, sillä muuten kukaan muu käyttäjä ei olisi voinut luoda itselleen saman nimistä kategoriaa.

### CRUD
- Sovelluksessa voi tällä hetkellä muokata tuotteen "ostettu" tilaa. Tässä arvoina on kuitenkin *1 tai 0* eikä *"true" tai "false"*.
- Kategorian nimen muokkaamismahdollisuus jäi toteuttamatta. Tällä lisäyksellä olisin saanut toteutettua toisen täyden *CRUD*:in: kategorian luominen, *kategorian nimen muokkaaminen*, kategorian koon päivittyminen, kategorian poistaminen.


### Monesta moneen suhde/suhteet
- [Tietokantakaavion sivulta](https://github.com/retute/Ostoslista/blob/master/documentation/tietokantakaavio.md) löytyy ideoita siitä, mitä monesta moneen suhteita olin ajatellut toteuttaa. Aika/taidot eivät kuitenkaan riittäneet tähän.


## Jatkokehitysidet

### Käyttäjä voi nähdä listan tuotteista kategoriakohtaisesti
- Kategorialistan nimillä on linkit, joita painamalla käyttäjä pääsee näkemään listan tuotteista, jotka kuuluvat kyseiseen kategoriaan

### Käyttäjä voi poistaa oman käyttäjätunnuksensa
- Kirjautuneen käyttäjän oikeaan yläkulmaan tulee linkki, josta käyttäjä voi poistaa oman käyttäjätunnuksensa
- Samalla poistuvat myös kaikki käyttäjän lisäämät tuotteet ja kategoriat

### Käyttäjä voi muokata kategorian/tuotteen nimeä
- Kategorian nimeä voi muokata ja uusi tieto tallentuu tietokantaan vanhan nimen tilalle.
- Tuotteen nimeä voi muokata.
