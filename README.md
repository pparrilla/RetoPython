# RetoPython

## Descripcion

Proyecto realizado con FastAPI con diferentes consultas. Este contempla los siguientes endpoints (todos englobados en /api/v1):
- */jokes*, que se pueden solicitar chistes de una base de datos en SQLite, o de diferentes APIs externas
- */maths*, donde se pueden calcular el mínimo común múltiplo de una lista de números y obtención de un número + 1

### Ejecución

Lo idóneo sería crear un entorno virtual en Python e instalar los paquetes incluidos en el archivo requirements.txt.

Para su ejecución:

```python
python main.py
```

### Tests

Para lanzar los test (no engloban todos los casos), se lanza con pytest:

```python
pytest test_main.py
```

### APIs externas utilizadas

- [https://api.chucknorris.io/jokes/random](https://api.chucknorris.io/jokes/random)
- [https://icanhazdadjoke.com/](https://icanhazdadjoke.com/)