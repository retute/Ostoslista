# Tietokantakaavio

![alt text](https://github.com/retute/Ostoslista/blob/master/documentation/Ostoslista.ui.png "Tietokantakaavio")

[Tietokantataulut](https://github.com/retute/Ostoslista/blob/master/documentation/tietokantataulut.md)


## Suhteet

- K�ytt�j� - Kategoria: yhden suhde moneen
- K�ytt�j� - Tuote: yhden suhde moneen
- Kategoria - Tuote: yhden suhde moneen


### Monen suhde moneen taulu puuttuu
Valitettavasti en onnistunut saamaan ty�h�ni monen suhde moneen yhteyksi� ja liitostauluja. Olin kuitenkin ajatellut seuraavia vaihtoehtoja t�h�n osioon:

#### Kategoria - K�ytt�j�
Jokaisella k�ytt�j�ll� voisi olla useita kategorioita ja kategorialla voisi olla useita k�ytt�ji�.
	T�ss� hieman ongelmallista olisi toteuttaa se, miten kategorialla voi olla useita k�ytt�ji�. K�ytt�j�t voisivat kenties liitty� johonkin kategoriaan.

#### Ryhm�lista
Er�s idea oli luoda ryhm�lista-luokka, jolla olisi *monen suhde moneen* suhde k�ytt�j�n kanssa. T�ss� k�ytt�j� voisi luoda ryhm�n usealle k�ytt�j�lle ja yksitt�inen k�ytt�j� voisi kuulua useaan ryhm��n. Jokaisella ryhm�ll� olisi lista asioita, joita he yhdess� ostavat. Esimerkiksi perheen kesken teht�v�t ruoka ostokset.
	T�m�n lis�ksi olisi kuitenkin pit�nyt toteuttaa kullekkin k�ytt�j�lle henkil�kohtainen ostoslista tuotelistan lis�ksi. My�s tuotelistaa olisi t�ytynyt muokata niin, ett� listassa n�kyisiv�t kaikkien lis��m�t tuotteet ja tuotteilla ei olisi k�ytt�j��.