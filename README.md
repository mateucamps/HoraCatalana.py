# HoraCatalana.py
 Mòdul que retorna l'hora en català en sistema de campanar.

## Ús:
1. Importar al projecte
```py
>>> from HoraCatalana import HoraCatalana
```
2. Crea un objecte ```HoraCatalana()```
```py
>>> hc = HoraCatalana()
```
3. L'objecte retorna un ```String``` amb l'hora actual
```py
>>> print(hc)
>>> "Falten set minuts per les set"
```
4. Per actualitzar l'hora:
```py
>>> hc.tic()
```

5. Podem inicialitzar HoraCatalana amb un objecte ```datetime```

```py
>>> from datetime import time
>>> t = time(12,34)
>>> HoraCatalana(t)
>>> "Són dos quarts i quatre d'una"
```

6. També podem indicar quina franja horària volem

```py
>>> HoraCatalana(franja='hivern')
>>> "Són tres quarts de set del vespre"
>>> HoraCatalana(franja='estiu')
>>> "Són tres quarts de set de la tarda"
>>> HoraCatalana(franja='auto') # Detecta en funció de data actual
```

7. També podem indicar quin prefix volem utilitzar

```py            
>>> HoraCatalana( time(18,45), prefixFrase='son-passen-falten' )
"Són tres quarts de set de la tarda"

>>> HoraCatalana( time(18,45), prefixFrase='a' )
"A tres quarts de set de la tarda"

>>> HoraCatalana( time(18,45), prefixFrase='' )
"Tres quarts de set de la tarda"
```

## +info:
 [geiec.iec.cat](https://geiec.iec.cat/text/28.2.2)

 [ca.wikipedia.org/wiki/Sistema_horari_català](https://ca.wikipedia.org/wiki/Sistema_horari_catal%C3%A0)
