# Asennusohje

## Paikallisesti

### Asennus

Lataa ohjelma repositoriosta. Löydät __Clone or download__ -valikosta kohdan __Download ZIP__.
 
Kun lataus on suoritettu, pura ladattu zip-tiedosto ja mene komentoriviltä juurikansioon.

Tämän jälkeen luo Python-virtuaaliympäristö komennolla

```
$ python3 -m venv venv
```

Aktivoi virtuaaliympäristö komennolla

```
$ source venv/bin/activate
```

tai

```
$ venv\Scripts\activate (Windows)
```

Tämän jälkeen lataa sovelluksen tarvitsemat riippuvuudet komennolla 

```
$ pip install -r requirements.txt
```


### Käynnistäminen

Kun virtuaaliympäristö on aktiivinen ja riippuvuudet ladattu, niin sovellus käynnistyy komennolla 

```
$ python run.py
```
tai

```
$ py -3 run.py (Windows)
```

Kun sovellus on käynnistetty onnistuneesti, siirry selaimessa osoitteeseen

```
<http://localhost:5000/>
```

### Sammuttaminen

Sovellus sammuu, kun painat komentoriviltä painikkeita **Ctrl** ja **c**. Tämän jälkeen voit vain sulkea välilehden.


## Selaimessa (asennus)

Luo Herokuun sovellukselle oma paikka komennolla 

```
heroku create [valitse_sovellukselle_nimi]
```
Tämän jälkeen lisätään versionhallintaan tieto herokusta komennolla

```
git remote add heroku https://git.heroku.com/[valittu_nimi].git
```

Lisätään projekti Herokuun seuraavia komentoja käyttäen

```
git add .
git commit -m"Initial commit"
git push heroku master
```

Lisätään sovellukselle tieto siitä, että sovellus on Herokussa komennolla 

```
heroku config:set HEROKU=1
```

Nyt voidaan tarkastaa, onko sovelluksella olemassa jo tietokanta. Tämä onnistuu kirjautumisyrityksellä Herokun PostgreSQL-tietokantaan seuraavalla komennolla

```
heroku pg:psql
```

Jos tietokantaa ei ole, niin se voidaan lisätä komennolla

```
heroku addons:add heroku-postgresql:hobby-dev
```

Tämän jälkeen sovelluksen pitäisi toimia Herokussa. Sovelluksen saa auki painamalla **Open app** nappia Herokun oikeassa yläkulmassa.

## Selaimessa (ilman asennusta)

Sivulta <https://ostoslista-tsoha.herokuapp.com/> löytyy sovelluksen etusivu.