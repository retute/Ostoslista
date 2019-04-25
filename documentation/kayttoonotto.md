# K�ytt��notto

## Asennusohje

Lataa ohjelma repositoriosta. L�yd�t __Clone or download__ -valikosta kohdan __Download ZIP__.
 
Kun lataus on suoritettu, pura ladattu zip-tiedosto ja mene komentorivilt� juurikansioon.

T�m�n j�lkeen luo Python-virtuaaliymp�rist� komennolla

'''
$ python3 -m venv venv
'''

Aktivoi virtuaaliymp�rist� komennolla

'''
$ source venv/bin/activate
$ venv\Scripts\activate (Windows)
'''

T�m�n j�lkeen lataa sovelluksen tarvitsemat riippuvuudet komennolla 

'''
$ pip install -r requirements.txt
'''




python run-py tai py -3 run.py

(Komento riippuu koneesta. Itse k�yt�n Windowsia ja *py -3 run.py* on toimiva)

### K�ynnist�minen

Kun virtuaaliymp�rist� on aktiivinen ja riippuvuudet ladattu, niin sovellus k�ynnistyy komennolla 

'''
$ python run.py
$ py -3 run.py (Windows)
'''

Kun sovellus on k�ynnistetty onnistuneesti, siirry selaimessa osoitteeseen

'''
<http://localhost:5000/>
'''



