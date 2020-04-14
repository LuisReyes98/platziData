# Data engineering with Python

## Entornos

[Conda](https://www.anaconda.com/distribution/) es recomendado para data science ya que ya posee agrupados todos los paquetes necesarios para esta tarea

### Comandos

crear entono virtual en conda

```sh
conda create --name platzi_data beautifulsoup4 requests numpy pandas matplotlib yaml
```

activar entorno virtual

```sh
conda activate platzi_data
```

desactivar

```sh
conda desactivate
```

borrar con todos los paquetes

```sh
conda remove --name platzi_data --all
```

## Fuentes de datos

Se pueden obtener datos de casi cualquier lugar en la web

Paginas de datos finacieros, sitios de noticias, datos de precipitacion, clima, economicos, etc...

de APIs que retornan datos

Redes sociales como Facebook o Twitter

Fuentes de user analytics

Sensores de velocidad, gasolina, temperatura (IOT)

El internet esta plagado de datos desde paginas web de noticias y paginas web en general como datos semiestructurados
hasta datasets publicos que estan disponibles para ser buscados en servicios como:

- [Goggle Data Search](https://datasetsearch.research.google.com/)

- [Kaggle](https://www.kaggle.com/#)

- [Data.world](https://data.world/search?q=covid+19)

## ETL

el dia a dia de un ingeniero de datos es:

### Extract

Se obtienen los datos de base de datos sql, archivos csv, data sets publicos, etc.., para obtener la mayor cantidad de datos posibles que sean relevantes con el problema que buscas solucionar

### Transform

Se limpian los datos , se estructuran y enriquecen para poder llevarlos a una **data warehouse**

### Load

Es el tipo de insercion de datos en la dataware house

depende mucho del tipo de solucion que se haya escogido

existen multiples tipos de data warehouse

## Tecnologias web

Un problema muy comun es no encontrar el data set correcto, y no poder encontrar los datos que te permitiran responder la pregunta que te has planteado

por eso debes ser capaz de construir tus propios datasets

### Que es?

Las teconologias web, se suele pensar que es el **internet** pero esto es erroneo ya que el internet es millones de veces mas grande y representa solamente el canal en el que existe la web.

el internet esta conformado tambien por APIs, email, http, protocolos de transferencia entre otras

esto es importante de conocer a la hora de buscar de donde es posible extraer datos

**La web** es una parte del internet donde se puede acceder a diversos documentos a traves de vinculos en forma de URL accediendo a archivos HTML que interactuan o no con un backend.

la web posee varios elementos basicos:

- **HTML** Estructura (importante)

- **CSS**. Presentacion

- **Javascript**, interactividad y computo.
 Es importante de considerar, ya que al accederse de forma programatica a una pagina web si no se ejecuta el javascript es posible que no hay informacion visible, ya que esta carga por medio de la ejecucion del javascript, bien por que sea una single page application o pida data por interaccion del usuario con el javascript

- **Json** transferencia de datos por API (importante)

### Web scraping

Utilizando librerias como `beautifulsoup4` se puede analizar la estructura html de un pagina web mediante un sistema de nodos permitiendo estraer informacion de la misma.

Del mismo modo la mayor desventaje es que para encontrar la informacion a buscar se requiere un profundo analisis y lectura del html.

### Page object Pattern

Es un patron de pruebas automatizadas

consiste en esconder los queries especificos que se utilizan para manipular un documento HTML, detras de un objeto que representa la pagina web.

si no se hace esto y se agregan los queries directamente al codigo principal, el codigo es bastante fragil y arreglarlo se vuelve muy dificil.

Ejemplo:

```python
class WebPage:

  @property
  def page_header(self):
    return soup.select('.some-query h1')
```

### Estructura

declarando las funciones del scraper es mas comodo declarar las funciones que se necesitan primero y luego la implementacion especifica

## Web Scraper

comandos

```sh
python main.py --help
```

```sh
python main.py $news_site
```

## Python syntaxis

Un piso `_variable` es una convencion de clase que da la pista que la variable es interna de en donde se declara mas no cambia la forma en la python la interpreta, esta es una convencion de PEP8.

Dos pisos `__variable` en una clase `MiClase` ocasiona que python la maneje de forma diferente, para evitar que `__variable` sea sobreescrita por una subclase. Al tratar de acceder a ella en una instacia de la clase seria de la siguiente forma `_MiClase__var`

ejemplo:

```python
class MiClase:
  def __init__(self):
    self.__var = 3

example = MiClase()

example._MiClase__var # 3
```

esto lo hace python de forma automatica para proteger el valor de la variable

## Pandas

Es una libreria de python que permite transformar, modificar, leer, editar, buscar y analizar grandes grupos de datos

las formas de datos principales de datos de pandas son

- Series

- Dataframes

Importante saber que pandas es una libreria fuertemente tipada a pesar de que python no sea fuertemente tipado

### Series

las series son similares a una columna de una tabla de una base de datos, posee comportamientos similiares a los de una lista mas no son ni se trabajan como una lista, y todos los datos dentro de una serie deben ser del mismo tipo

poseen una unica dimension

### Dataframes

son en su concepto mas sencillo una tabla donde las columnas y filas tienen etiquetas.

posee un minimo de 2 dimensiones

### Data wrangling

Se conoce como el domado de datos en español.

De las razones por la cual pandas es tan popular es porque posee las funciones del lenguage R para hacer Data wrangling y la disponibilidad de las bibliotecas de python existentes.
