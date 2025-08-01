# Análisis de Datos de Manufactura - Proyecto Hackathon

## Descripción General

Este proyecto contiene un análisis completo de datos de manufactura enfocado en la limpieza, exploración y análisis de correlaciones de variables industriales. El objetivo principal es identificar patrones y relaciones entre diferentes variables operacionales que puedan influir en la eficiencia y calidad de la producción.

## Estructura del Proyecto

```
📁 documentation/
├── 📊 Dataset_Talento.csv          # Dataset original sin procesar
├── 📊 cleaned_dataset.csv          # Dataset limpio y procesado
├── 📓 cleaning data.ipynb          # Notebook de limpieza de datos
├── 📓 exploration_cleannedDS.ipynb # Notebook de análisis de correlaciones
└── 📄 README.md                    # Documentación del proyecto
```

## Notebooks Incluidos

### 1. cleaning data.ipynb - Limpieza y Preprocesamiento de Datos (19 celdas con documentación completa)

**Propósito**: Proceso sistemático de limpieza y preparación del dataset original con documentación técnica detallada en cada etapa.

Este notebook ha sido completamente documentado con celdas de markdown que explican cada función, metodología y resultado esperado. La documentación profesional incluye descripciones técnicas de cada proceso de limpieza y análisis.

**Funcionalidades principales**:

- **Carga de datos**: Importación del dataset original `Dataset_Talento.csv`
- **Identificación de valores críticos**: Definición de columnas que no pueden contener valores nulos
- **Limpieza sistemática**: Eliminación de filas con valores faltantes en variables críticas
- **Análisis temporal**: Extracción de características temporales (hora, día de la semana, mes)
- **Análisis de correlaciones temporales**: Estudio de relaciones entre variables temporales y operacionales
- **Validación de calidad**: Verificación de la integridad de los datos después del procesamiento

**Variables críticas analizadas**:
- `temperatura`: Temperatura del proceso
- `vibración`: Niveles de vibración del equipo
- `humedad`: Condiciones de humedad ambiental
- `tiempo_ciclo`: Duración de los ciclos de producción
- `eficiencia_porcentual`: Eficiencia operacional
- `consumo_energia`: Consumo energético del proceso

**Output**: Genera el archivo `cleaned_dataset.csv` con datos procesados y listos para análisis.

### 2. exploration_cleannedDS.ipynb - Análisis Exploratorio y Correlaciones (11 celdas completamente documentadas)

**Propósito**: Análisis avanzado de correlaciones con documentación técnica profesional que explica cada función, metodología y aplicación práctica.

Este notebook incluye documentación completa en markdown para cada función de análisis, proporcionando explicaciones detalladas sobre propósitos, parámetros, implementación y casos de uso. Cada celda de código está precedida por documentación técnica que facilita la comprensión y reutilización del código.

**Funcionalidades principales**:

- **Carga de datos limpios**: Importación del dataset procesado
- **Inspección estructural**: Análisis de tipos de datos, dimensiones y completitud
- **Análisis de correlación simple**: Estudio específico entre vibración y consumo energético
- **Toolkit de análisis avanzado**: Conjunto de funciones especializadas para análisis de correlaciones

**Funciones implementadas**:

1. **`analyze_correlations()`**: 
   - Análisis completo de correlaciones entre variables numéricas
   - Capacidad de enfoque en variable objetivo específica
   - Filtrado por umbral de significancia personalizable

2. **`interpret_correlation()`**: 
   - Interpretación cualitativa de coeficientes de correlación
   - Clasificación de fuerza y dirección de relaciones

3. **`plot_correlation_heatmap()`**: 
   - Generación de mapas de calor visuales
   - Representación gráfica de matrices de correlación

4. **`find_best_predictors()`**: 
   - Identificación de mejores variables predictivas
   - Ranking de variables por poder predictivo

**Análisis específicos realizados**:
- Correlaciones con `paradas_imprevistas` (umbral 0.3)
- Identificación de top 5 predictores más relevantes
- Análisis general de correlaciones fuertes (umbral 0.4)

## Metodología de Análisis (Con Documentación Técnica Completa)

Ambos notebooks han sido completamente documentados con celdas de markdown que explican cada proceso, función y metodología utilizada. Esta documentación técnica profesional facilita la comprensión, reproducibilidad y mantenimiento del código.

### Fase 1: Limpieza de Datos (cleaning data.ipynb)
1. **Evaluación inicial**: Inspección documentada de estructura y calidad de datos
2. **Definición de criterios**: Establecimiento documentado de variables críticas sin valores faltantes
3. **Limpieza sistemática**: Proceso documentado de eliminación de registros con datos incompletos
4. **Enriquecimiento temporal**: Extracción documentada de características temporales relevantes
5. **Validación**: Verificación documentada de integridad post-procesamiento

### Fase 2: Análisis Exploratorio (exploration_cleannedDS.ipynb)
1. **Carga y verificación**: Importación documentada de datos limpios
2. **Análisis descriptivo**: Exploración documentada de distribuciones y características
3. **Correlaciones simples**: Análisis documentado de relaciones bivariadas específicas
4. **Análisis multivariado**: Estudio documentado completo de correlaciones entre todas las variables
5. **Identificación de patrones**: Detección documentada de variables predictivas clave

## Calidad de Documentación

### Estándares de Documentación Implementados

**Documentación Técnica Completa**: Ambos notebooks incluyen celdas de markdown que preceden cada función o proceso, explicando:
- **Propósito y objetivo** de cada función
- **Parámetros de entrada** y sus tipos
- **Metodología utilizada** en el procesamiento
- **Resultados esperados** y su interpretación
- **Casos de uso prácticos** y aplicaciones

**Formateo Profesional**: 
- Eliminación de elementos decorativos (emojis) para mantener estándares profesionales
- Estructura consistente en todas las explicaciones
- Lenguaje técnico preciso y claro
- Ejemplos prácticos de uso

**Beneficios de la Documentación**:
- **Reproducibilidad**: Cualquier usuario puede entender y replicar el análisis
- **Mantenibilidad**: Facilita futuras modificaciones y extensiones
- **Transferencia de conocimiento**: Permite que otros desarrolladores comprendan el código
- **Estándares profesionales**: Cumple con buenas prácticas de documentación técnica

## Variables del Dataset

### Variables Operacionales
- **temperatura**: Temperatura del proceso de manufactura
- **vibración**: Niveles de vibración del equipo
- **humedad**: Condiciones de humedad del ambiente
- **tiempo_ciclo**: Duración de cada ciclo productivo

### Variables de Producción
- **cantidad_producida**: Unidades producidas por período
- **unidades_defectuosas**: Cantidad de productos defectuosos
- **eficiencia_porcentual**: Porcentaje de eficiencia operacional

### Variables de Recursos
- **consumo_energia**: Consumo energético del proceso
- **paradas_programadas**: Paradas planificadas de mantenimiento
- **paradas_imprevistas**: Interrupciones no planificadas (variable objetivo principal)

### Variables Temporales (generadas)
- **hour**: Hora del día
- **day_of_week**: Día de la semana
- **day_of_month**: Día del mes
- **month**: Mes del año
- **minute**: Minuto de la hora

## Resultados Clave

### Hallazgos del Análisis de Correlaciones
- Identificación de variables más correlacionadas con paradas imprevistas
- Detección de patrones temporales en la eficiencia operacional
- Mapeo de relaciones entre consumo energético y variables operacionales
- Ranking de variables predictivas para diferentes objetivos de análisis

### Métricas de Calidad de Datos
- Porcentaje de completitud después de la limpieza
- Número de registros válidos para análisis
- Distribución temporal de los datos procesados

## Herramientas y Tecnologías

- **Python 3.x**: Lenguaje de programación principal
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones numéricas y arrays
- **Matplotlib**: Visualización básica de datos
- **Seaborn**: Visualizaciones estadísticas avanzadas
- **SciPy**: Análisis estadístico y correlaciones

## Uso de los Notebooks

### Prerrequisitos
```bash
pip install pandas matplotlib seaborn scipy numpy
```

### Orden de Ejecución Recomendado
1. **Primero**: Ejecutar `cleaning data.ipynb` para generar el dataset limpio
   - Cada celda incluye documentación que explica el proceso
   - La documentación técnica facilita la comprensión de cada paso
2. **Segundo**: Ejecutar `exploration_cleannedDS.ipynb` para realizar el análisis de correlaciones
   - Documentación completa de cada función de análisis
   - Explicaciones detalladas de metodologías estadísticas utilizadas

### Navegación de la Documentación
- **Celdas de markdown**: Preceden cada función con explicaciones técnicas completas
- **Estructura consistente**: Formato uniforme en todas las explicaciones
- **Ejemplos prácticos**: Casos de uso y aplicaciones de cada función
- **Interpretación de resultados**: Guías para entender los outputs generados

### Variables Resultantes
Después de ejecutar ambos notebooks, estarán disponibles:
- `testing_clean`: DataFrame con datos limpios y características temporales
- `results`: Análisis de correlaciones con variable objetivo
- `best_predictors`: Top 5 predictores identificados
- `all_correlations`: Todas las correlaciones significativas del dataset

## Aplicaciones Potenciales

- **Mantenimiento predictivo**: Identificación de variables que predicen paradas imprevistas
- **Optimización energética**: Análisis de factores que afectan el consumo de energía
- **Control de calidad**: Detección de variables que influyen en defectos de producción
- **Planificación operacional**: Identificación de patrones temporales para optimizar horarios
- **Análisis de eficiencia**: Comprensión de factores que afectan la productividad

## Contribuciones y Desarrollo Futuro

Este proyecto establece las bases para:
- Modelos de machine learning predictivos
- Sistemas de monitoreo en tiempo real
- Dashboards de análisis operacional
- Algoritmos de optimización de procesos
- Herramientas de soporte a la toma de decisiones

---

**Nota**: Este proyecto fue desarrollado como parte de un hackathon enfocado en análisis de datos industriales y manufactura inteligente.
