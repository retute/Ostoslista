# Asennusohje

## Paikallisesti

### Asennus

Lataa ohjelma repositoriosta. L�yd�t __Clone or download__ -valikosta kohdan __Download ZIP__.
 
Kun lataus on suoritettu, pura ladattu zip-tiedosto ja mene komentorivilt� juurikansioon.

T�m�n j�lkeen luo Python-virtuaaliymp�rist� komennolla

```
$ python3 -m venv venv
```

Aktivoi virtuaaliymp�rist� komennolla

```
$ source venv/bin/activate
```

tai

```
$ venv\Scripts\activate (Windows)
```

T�m�n j�lkeen lataa sovelluksen tarvitsemat riippuvuudet komennolla 

```
$ pip install -r requirements.txt
```


### K�ynnist�minen

Kun virtuaaliymp�rist� on aktiivinen ja riippuvuudet ladattu, niin sovellus k�ynnistyy komennolla 

```
$ python run.py
```
tai

```
$ py -3 run.py (Windows)
```

Kun sovellus on k�ynnistetty onnistuneesti, siirry selaimessa osoitteeseen

```
<http://localhost:5000/>
```

### Sammuttaminen

Sovellus sammuu, kun painat komentorivilt� painikkeita **Ctrl** ja **c**. T�m�n j�lkeen voit vain sulkea v�lilehden.


## Selaimessa (asennus)

Luo Herokuun sovellukselle oma paikka komennolla 

```
heroku create [valitse_sovellukselle_nimi]
```
T�m�n j�lkeen lis�t��n versionhallintaan tieto herokusta komennolla

```
git remote add heroku https://git.heroku.com/[valittu_nimi].git
```

Lis�t��n projekti Herokuun seuraavia komentoja k�ytt�en

```
git add .
git commit -m"Initial commit"
git push heroku master
```

Lis�t��n sovellukselle tieto siit�, ett� sovellus on Herokussa komennolla 

```
heroku config:set HEROKU=1
```

Nyt voidaan tarkastaa, onko sovelluksella olemassa jo tietokanta. T�m� onnistuu kirjautumisyrityksell� Herokun PostgreSQL-tietokantaan seuraavalla komennolla

```
heroku pg:psql
```

Jos tietokantaa ei ole, niin se voidaan lis�t� komennolla

```
heroku addons:add heroku-postgresql:hobby-dev
```

T�m�n j�lkeen sovelluksen pit�isi toimia Herokussa. Sovelluksen saa auki painamalla **Open app** nappia Herokun oikeassa yl�kulmassa.

## Selaimessa (ilman asennusta)

Sivulta <https://ostoslista-tsoha.herokuapp.com/> l�ytyy sovelluksen etusivu.