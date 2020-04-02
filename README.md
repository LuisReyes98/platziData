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
 Es importante de considerar, ya que al accederse de forma programatica a una pagina web si no se ejecuta el javascript es posible que no hay informacion visible, ya que esta carga por medio de la ejecucion del javascript

- **Json** transferencia de datos por API (importante)
