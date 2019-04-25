# Käyttöönotto

## Asennusohje

Lataa ohjelma repositoriosta. Löydät __Clone or download__ -valikosta kohdan __Download ZIP__.
 
Kun lataus on suoritettu, pura ladattu zip-tiedosto ja mene komentoriviltä juurikansioon.

Tämän jälkeen luo Python-virtuaaliympäristö komennolla

'''
$ python3 -m venv venv
'''

Aktivoi virtuaaliympäristö komennolla

'''
$ source venv/bin/activate
$ venv\Scripts\activate (Windows)
'''

Tämän jälkeen lataa sovelluksen tarvitsemat riippuvuudet komennolla 

'''
$ pip install -r requirements.txt
'''




python run-py tai py -3 run.py

(Komento riippuu koneesta. Itse käytän Windowsia ja *py -3 run.py* on toimiva)

### Käynnistäminen

Kun virtuaaliympäristö on aktiivinen ja riippuvuudet ladattu, niin sovellus käynnistyy komennolla 

'''
$ python run.py
$ py -3 run.py (Windows)
'''

Kun sovellus on käynnistetty onnistuneesti, siirry selaimessa osoitteeseen

'''
<http://localhost:5000/>
'''



