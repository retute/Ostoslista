# Käyttöohje

Tältä sivulta löydät sovelluksen käyttöohjeen. Ohjeet on jaoteltu kategorioittain seuraavasti

- Kirjautuminen
- Kategoriat
- Tuotteet


## Kirjautuminen

### Jos tunnusta ei ole...

- Sovelluksen oikeassa yläkulmassa on nappi *"Sign up"*. Paina sitä.
- Valitse tunnus, joka on vähintään 4 merkkiä pitkä.
- Valitse salasana, joka on vähintään 4 merkkiä pitkä.
- Et voi käyttää jo olemassa olevaa salasanaa.
- Paina nappia *"Create"*, jolloin sovellus ohjaa sinut kirjautumissivulle.
- Kirjaudu sovellukseen vastaluomasi tunnuksen ja salasanan avulla.

### Jos tunnus löytyy...

- Oikeasta yläkulmasta löytyy nappi *"Login"*. Paina siitä.
- Syötä käyttäjätunnuksesi ja salasanasi oikeisiin kenttiin.
- Tämän jälkeen paina nappia *"Login"*.
- Jos salasana ei vastaa käyttäjätunnusta, niin sovellus valittaa virheviestillä: "Username or password didn't match. Try again!".
- Kun tunnus ja salasana ovat oikein, niin sovellus ohjaa sinut etusivulle.

### Kirjauduttua
- Sivun yläpalkkiin ilmestyy linkit, joilla voi selata ostoslistaa, lisätä tuotteita listaan ja selata kategorioita
- Sivun oikeassa ylälaidassa on nappi "Logged in as [username] -- Logout". Nappia painamalla käyttäjä voi kirjautua ulos.


## Kategoriat

### Selaa kategorioita

- Kategoriat löytyvät kirjauduttua sivun yläpalkista linkistä "Categories".
- Listasta voi nähdä kategorian id:n, nimen, koon ja napin kategorian poistamiselle.
- Kategoriat ovat listattuna sivulla niiden suuruusjärjestyksessä eli eniten tuotteita omaava kategoria ensimmäisenä.
- Kategorian poistaminen onnistuu, jos kategorian koko on nolla, painamalla *"Delete"*-nappia.

### Luo uusi

- Kategorialistan yläpuolella on vihreä *"Add new"* -nappi, joka ohjaa sivulle, jossa voi luoda uuden kategorian.
- Uutta kategoriaa luodessa täytyy keksiä kategorialle nimi, joka on vähintään 2 merkkiä pitkä ja enintään 100 merkkiä.
- Jos tuotteen nimi on virheellinen, niin ohjelma valittaa tästä ja ohjaa uudestaan kategorian luomissivulle.


## Tuotteet

### Lisääminen
- Ennen tuotteen lisäämistä täytyy tarkistaa, että haluttu kategoria on olemassa. Jos ei ole, niin täytyy se luoda ensin kategoriasivulla.
- Sovelluksen yläpalkissa on linkki *"Add a new item"*, joka ohjaa tuotteen lisäämissivulle.
- Sivulla on tekstikenttä, johon kirjotetaan tuotteen nimi ja valitaan sen alapuolelta haluttu kategoria.
- Tuotteen voi merkitä jo alussa ostetuksi rastittamalla kohta *"Bought"*.

### Selaaminen
- Tuotteita pääsee selaamaan yläpalkin kohdasta *"Show the list".
- Tuotteet on järjestetty niiden id:n mukaan eli pisimpään listalla ollut tuote on ensimmäisenä.
- Kun tuotteen "bought"-tila on 0 (Herokussa *False*), niin tuotetta ei ole ostettu. Kun tila on 1 (Herokussa *True*), niin tuote on ostettu.
- Napilla *"Buy"* voi muuttaa tuotteen tilaa siitä onko sitä ostettu (=1/True) vai ei (=0/False).
- Yksittäisen tuotteen voi poistaa napista *"Delete"*, jolloin samalla pienenee kyseisen tuotteen kategorian koko.