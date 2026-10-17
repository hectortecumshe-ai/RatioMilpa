<p align="center"><img src="logo.svg" width="96" alt="Ratio Milpa"></p>

# Ratio Milpa

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23432656.svg)](https://doi.org/10.5281/zenodo.23432656)

👉 **https://hectortecumshe-ai.github.io/RatioMilpa/**

**El conocimiento local del maíz en México como sistema complejo adaptativo.** Aplicación de **Ratio Complexus**, el ala de la suite [Ratio](https://hectortecumshe-ai.github.io/) dedicada a los sistemas complejos adaptativos: *lo que está tejido junto*. Hermana de [Ratio Telar](https://hectortecumshe-ai.github.io/RatioTelar/), pero hecha para un solo cultivo y para un **estudio nacional**: cada localidad se documenta con el mismo cuestionario y los resultados se juntan en un atlas.

Está hecha para productores y para científicos, en español y en inglés.

## Qué contiene (versión 0.1.0)

| Bloque | Contenido |
|---|---|
| 1 · Maíz | Nativo o criollo, con las 64 razas de México en siete grupos (CONABIO, 2020; Sánchez et al., 2000), o mejorado o híbrido; sistema (milpa, MIAF, monocultivo, asociado, rotación, agroforestal, traspatio, forrajero o propio) y unidad de producción |
| 2 · Región | Mapa real de México; estado, municipio y localidad (2,478 municipios y 54,357 localidades del INEGI con altitud y coordenadas) |
| 3 · Requerimientos | Las cinco reglas básicas (5B) y los requerimientos innovados en la localidad |
| 4 · Manejo | Cuestionario base de 38 pasos y 85 actividades: la localidad responde cuáles practica (sí o no), pone sus fechas y agrega sus innovaciones |
| 5 · Regeneración | Ocho perillas 0–4 con valores sugeridos que se confirman; índice de regeneración, línea base y materia orgánica |
| 6 · Riesgos | 19 amenazas con perillas de probabilidad, impacto y control; matriz 5 × 5, capacidad adaptativa e índice de riesgo |
| 7 · Elementos | 63 elementos en 10 categorías y los propios de la localidad |
| 8 · Precio y valor | Precio por unidad y por hectárea; valor económico, de uso, cultural y ecológico |
| 9 · Formulación | Modelo del sistema complejo adaptativo y formulación matemática |
| 10 · Tablero | Red ponderada, centralidades, comunidades (Louvain), correlaciones φ, calendario circular y cladograma del vecino más cercano |
| 11 · Sostenibilidad | Compartimentos, índice de Sarandón (2002), 17 ODS y huella de carbono (IPCC) |
| 12 · Prospectiva | Tres escenarios a 2, 5 y 10 años |
| 13 · Informe | Resumen redactado, tablas, CSV, PDF y el archivo de la localidad (`.milpa.json`) |
| 14 · Atlas nacional | Junta los archivos de muchas localidades: mapa, frecuencia de cada práctica a escala nacional y por región, maíces sembrados, innovaciones y red nacional del conocimiento del maíz |

Además: **Validación** (caso publicado, motor de redes frente a NetworkX, cladograma frente a SciPy, huella de carbono y agregación del atlas) y **Teoría**.

## Sin datos precargados

La aplicación arranca en blanco. Para que nadie confunda un ejemplo con sus propios datos:

- los campos vacíos muestran texto gris de ayuda;
- las sugerencias de la app (perillas de regeneración y de riesgo) se ven punteadas hasta que la persona las mueve o las acepta;
- la barra «Llenado por ti» y las marcas del menú cuentan solo lo que llenó la persona;
- el Stack publicado del maíz criollo de Calpan, Puebla (Díaz-José et al., 2026) se consulta en una ventana aparte, con marca de agua, o en un «modo ejemplo» con una franja fija que lo anuncia. Nunca se copia a los campos del usuario.

## Estudio nacional sin servidor

1. Cada encuestador llena una localidad y la guarda en el Bloque 13 con **Guardar proyecto** (`.milpa.json`).
2. Quien coordina reúne los archivos y los agrega en el **Atlas nacional**, varios a la vez.
3. El atlas se exporta como un solo archivo (`.atlas.json`) para compartirlo o seguir agregando, y en CSV de localidades y de prácticas.

Ningún dato sale a un servidor. Frecuencia de una práctica = localidades que respondieron «sí» ÷ localidades que respondieron; lo no respondido no entra al denominador.

## Instructivos

| | Español | English |
|---|---|---|
| **Productor** · paso a paso, atlas nacional, guía de entrevista y hojas de campo | [web](https://hectortecumshe-ai.github.io/RatioMilpa/instructivo-productor.html) · [PDF](instructivo/RatioMilpa-Instructivo-Productor.pdf) | [web](https://hectortecumshe-ai.github.io/RatioMilpa/instructivo-productor.html?lang=en) · [PDF](instructivo/RatioMilpa-Producer-Guide.pdf) |
| **Científico** · modelo, ecuaciones, agregación del atlas, validación y ejemplo resuelto | [web](https://hectortecumshe-ai.github.io/RatioMilpa/instructivo-cientifico.html) · [PDF](instructivo/RatioMilpa-Instructivo-Cientifico.pdf) | [web](https://hectortecumshe-ai.github.io/RatioMilpa/instructivo-cientifico.html?lang=en) · [PDF](instructivo/RatioMilpa-Scientist-Guide.pdf) |

Texto bajo licencia CC BY 4.0.

## Rigor


Cada cifra muestra su fuente. Lo que es agrupación o lectura de la app se marca como **«Lectura de Ratio Milpa»**. Lo que no está documentado aparece como **«sin dato»**: la aplicación no inventa valores.

## Uso

Abre `index.html` en cualquier navegador; funciona sin conexión. No usa cookies, rastreadores ni recursos de terceros.

```bash
python armar.py                    # arma index.html a partir de src/
python pruebas/verificar_red.py    # motor de redes frente a NetworkX
python pruebas/verificar_clado.py  # cladograma frente a SciPy
```

## Autores

Héctor Tecumshé Mojica-Zárate ([ORCID 0000-0002-9067-3983](https://orcid.org/0000-0002-9067-3983)) · Oscar Díaz-José

## Fuentes principales

- Díaz-José, O., Mojica-Zárate, H. T., Díaz-José, J., y Vilaboa-Arróniz, J. (2026). El conocimiento agrícola local: el stack del maíz criollo en Calpan, Puebla. *Agricultura, Sociedad y Desarrollo*, 23(3). https://doi.org/10.22231/asyd.v23i3.1822
- CONABIO (2020). Razas de maíz de México.
- INEGI (2020). Censo de Población y Vivienda; Catálogo Único de Claves Geoestadísticas.
- Sarandón, S. J. (2002); IPCC (2006, 2014, 2018, 2019).

## Licencia

MIT. Contornos del mapa: Natural Earth (dominio público).
