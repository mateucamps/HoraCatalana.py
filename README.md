# HoraCatalana.py
 Mòdul que retorna l'hora en català

# Ús:
1. Importar al projecte
```python
>>> from HoraCatalana import HoraCatalana
```
2. Crea un objecte ```HoraCatalana()```
```python
>>> hc = HoraCatalana()
```
3. L'objecte retorna un ```String``` amb l'hora actual
```python
>>> print(hc)
>>> 'Falten set minuts per les set'
```
4. Per actualitzar la hora:
```python
>>> hc.tic()
```

5. Podem inicialitzar HoraCatalana amb un objecte ```datetime```

```python
>>> from datetime import time
>>> t = time(12,34,56)
>>> HoraCatalana(t)
>>> 'Són dos quarts i quatre de dotze'
```
