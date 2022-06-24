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
>>> 'Falten set minuts per les set'
```
4. Per actualitzar la hora:
```py
>>> hc.tic()
```

5. Podem inicialitzar HoraCatalana amb un objecte ```datetime```

```py
>>> from datetime import time
>>> t = time(12,34)
>>> HoraCatalana(t)
>>> 'Són dos quarts i quatre d'una'
```
## +info:
 [geiec.iec.cat](https://geiec.iec.cat/capitol_veure.asp?id_gelc=337&capitol=28)

 [ca.wikipedia.org/wiki/Sistema_horari_català](https://ca.wikipedia.org/wiki/Sistema_horari_catal%C3%A0)
