# K�ytt�ohje

T�lt� sivulta l�yd�t sovelluksen k�ytt�ohjeen. Ohjeet on jaoteltu kategorioittain seuraavasti

- Kirjautuminen
- Kategoriat
- Tuotteet


## Kirjautuminen

### Jos tunnusta ei ole...

- Sovelluksen oikeassa yl�kulmassa on nappi *"Sign up"*. Paina sit�.
- Valitse tunnus, joka on v�hint��n 4 merkki� pitk�.
- Valitse salasana, joka on v�hint��n 4 merkki� pitk�.
- Et voi k�ytt�� jo olemassa olevaa salasanaa.
- Paina nappia *"Create"*, jolloin sovellus ohjaa sinut kirjautumissivulle.
- Kirjaudu sovellukseen vastaluomasi tunnuksen ja salasanan avulla.

### Jos tunnus l�ytyy...

- Oikeasta yl�kulmasta l�ytyy nappi *"Login"*. Paina siit�.
- Sy�t� k�ytt�j�tunnuksesi ja salasanasi oikeisiin kenttiin.
- T�m�n j�lkeen paina nappia *"Login"*.
- Jos salasana ei vastaa k�ytt�j�tunnusta, niin sovellus valittaa virheviestill�: "Username or password didn't match. Try again!".
- Kun tunnus ja salasana ovat oikein, niin sovellus ohjaa sinut etusivulle.

### Kirjauduttua
- Sivun yl�palkkiin ilmestyy linkit, joilla voi selata ostoslistaa, lis�t� tuotteita listaan ja selata kategorioita
- Sivun oikeassa yl�laidassa on nappi "Logged in as [username] -- Logout". Nappia painamalla k�ytt�j� voi kirjautua ulos.


## Kategoriat

### Selaa kategorioita

- Kategoriat l�ytyv�t kirjauduttua sivun yl�palkista linkist� "Categories".
- Listasta voi n�hd� kategorian id:n, nimen, koon ja napin kategorian poistamiselle.
- Kategoriat ovat listattuna sivulla niiden suuruusj�rjestyksess� eli eniten tuotteita omaava kategoria ensimm�isen�.
- Kategorian poistaminen onnistuu, jos kategorian koko on nolla, painamalla *"Delete"*-nappia.

### Luo uusi

- Kategorialistan yl�puolella on vihre� *"Add new"* -nappi, joka ohjaa sivulle, jossa voi luoda uuden kategorian.
- Uutta kategoriaa luodessa t�ytyy keksi� kategorialle nimi, joka on v�hint��n 2 merkki� pitk� ja enint��n 100 merkki�.
- Jos tuotteen nimi on virheellinen, niin ohjelma valittaa t�st� ja ohjaa uudestaan kategorian luomissivulle.


## Tuotteet

### Lis��minen
- Ennen tuotteen lis��mist� t�ytyy tarkistaa, ett� haluttu kategoria on olemassa. Jos ei ole, niin t�ytyy se luoda ensin kategoriasivulla.
- Sovelluksen yl�palkissa on linkki *"Add a new item"*, joka ohjaa tuotteen lis��missivulle.
- Sivulla on tekstikentt�, johon kirjotetaan tuotteen nimi ja valitaan sen alapuolelta haluttu kategoria.
- Tuotteen voi merkit� jo alussa ostetuksi rastittamalla kohta *"Bought"*.

### Selaaminen
- Tuotteita p��see selaamaan yl�palkin kohdasta *"Show the list".
- Tuotteet on j�rjestetty niiden id:n mukaan eli pisimp��n listalla ollut tuote on ensimm�isen�.
- Kun tuotteen "bought"-tila on 0 (Herokussa *False*), niin tuotetta ei ole ostettu. Kun tila on 1 (Herokussa *True*), niin tuote on ostettu.
- Napilla *"Buy"* voi muuttaa tuotteen tilaa siit� onko sit� ostettu (=1/True) vai ei (=0/False).
- Yksitt�isen tuotteen voi poistaa napista *"Delete"*, jolloin samalla pienenee kyseisen tuotteen kategorian koko.