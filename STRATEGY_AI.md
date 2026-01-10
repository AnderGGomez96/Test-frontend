
### Índice:

**1. Prompt Maestro**

> **1.1. ¿Cómo ayuda este prompt al Ingeniero de QA?**

> **1.2. Ventaja del modelo "Stepper"**
  
> **1.3. Asistente AI utilizado: NoteBook LM**

> **1.4. Prompt**

> **1.5. Funcionalidad: Búsqueda de Vuelo (KAYAK)**

**2. Análisis de Calidad**

> **2.1 Casos de prueba irrelevantes**

> **2.2 Casos de prueba corregidos y retroalimentación**

## Prompt Maestro:

## 1.1 ¿Cómo ayuda este prompt al Ingeniero de QA?

**Elimina la Alucinación por Ambigüedad:** Al aplicar la "Fase 0", el prompt obliga a la IA a detenerse y listar vacíos de información. Esto evita que el ingeniero reciba casos de prueba basados en supuestos falsos sobre cómo debería funcionar el software.

**Creación de la Base Normativa:** Dado que las descripciones funcionales suelen ser informales, el prompt genera automáticamente los **Criterios de Aceptación (AC)**. Esto le da al QA una base sólida para validar el requerimiento con los interesados (Product Owners/Desarrolladores) antes de escribir una sola línea de prueba.

**Rigor Técnico Aplicado:** No se limita a "imaginar" escenarios; el prompt exige explícitamente el uso de técnicas de diseño como **Análisis de Valores Límite de 3 valores** y **Tablas de Decisión**. Esto asegura una cobertura de pruebas de nivel senior, detectando errores en los bordes críticos del sistema.

**Trazabilidad Garantizada:** La creación de una matriz vinculando cada AC con un caso de prueba asegura que no existan funciones sin probar ni pruebas innecesarias.

---

## 1.2. Ventaja del modelo "Stepper"

Entregar todos los casos de una vez suele parecer más rápido, pero en QA la velocidad sin precisión genera retrabajo. Las ventajas de la **entrega granular (de 2 en 2)** son:

| Característica | Entrega de una vez (One-Shot) | Modelo Secuencial (Stepper) |
| --- | --- | --- |
| **Calidad del Detalle** | El modelo tiende a simplificar pasos para no exceder el límite de salida (tokens).| Garantiza el **detalle máximo** en cada paso, ya que el modelo se enfoca en solo dos casos a la vez.|
| **Complejidad Cognitiva** | El QA debe revisar un bloque masivo de texto, aumentando la probabilidad de omitir errores. | Permite una validación ágil y por etapas, asegurando que cada bloque cumpla con el estándar de calidad.|
| **Control de Errores** | Si la lógica inicial está mal, todos los casos (ej: 20) estarán mal.| Permite corregir el rumbo tras los primeros 2 casos, ahorrando tiempo de revisión.|
| **Consistencia de Formato** | Es común que el modelo "olvide" etiquetas técnicas (`[titulo]`, `[accion]`) a mitad de una respuesta larga.| Mantiene un **Markdown estricto** y consistente en cada bloque pequeño de información.|

## 1.3. Asistente AI utilizado:

El asistente de inteligencia artificial utilizado es NoteBook LM que integra Gemini 3, NoteBook funciona como un sistema RAG que permite la recuperación de datos desde archivos cargados al cuaderno de trabajo, lo que permite reducir las alucinaciones de la inteligencia artificial y facilitan la auditoria de las respuestas ya que todo el contenido generado cita directamente las fuentes que le estamos cargando.

Pasos para usar el Prompt.

1. Cree un cuaderno en notebook.
2. Carge el prompt como una fuente (Cree un archivo .md y cargue las instrucciones del prompt). Este prompt está configurado para trabajar con archivos que describan las funcionalidades, entonces debes cargar como fuente la "funcionalidad de vuelo" tambien en un archivo .md a parte.
3. Cargue la funcionalidad de vuelo como fuente.
4. Realice la petición inicial.
> " usuando como base la fuente "prompt.md" y De acuerdo al flujo "Flujo búsqueda de vuelos.md" realicemos el diseño de los casos de prueba"
5. El asistente lo guiara por el paso a paso.


## 1.4. Prompt

### ROL

Actuarás como un Asistente de IA experto en Ingeniería de Pruebas de Software y Quality Assurance. Tu especialidad es transformar descripciones funcionales en artefactos de prueba de alta calidad, funcionando como un facilitador metodológico bajo un modelo de interacción paso a paso ("Stepper").

### CONTEXTO

Operas en NotebookLM donde las fuentes de información son "Descripciones de Funcionalidad" (ej: funcionalidad buscar vuelo, funcionalidad rentar carros, etc.). Tu misión es extraer la lógica de negocio, definir los criterios de aceptación y diseñar pruebas exhaustivas basadas en estas descripciones.

### OBJETIVO

Conducir una sesión interactiva para extraer Criterios de Aceptación, diseñar datos de prueba mediante técnicas avanzadas, generar una matriz de trazabilidad y producir casos de prueba detallados en bloques granulares, garantizando que no existan ambigüedades en la lógica de negocio.

### PRINCIPIO DE FUNCIONAMIENTO CORE: "UN PASO A LA VEZ"

1.  SOLO PUEDES EJECUTAR UN PASO NUMERADO A LA VEZ.
2.  NUNCA agrupes dos o más fases o solicitudes de información en una sola respuesta.
3.  Cada respuesta debe finalizar con una única pregunta o solicitud de confirmación clara para el usuario.
4.  Entrega Granular: Para evitar omisiones por límites de salida, entregarás los casos de prueba en bloques pequeños (máximo 2 por turno) hasta completar la matriz.

### INSTRUCCIONES SECUENCIALES OBLIGATORIAS

FASE 0: EXTRACCIÓN Y DEFINICIÓN DE LÍMITES

1.  Presentación: Preséntate brevemente y pide al usuario que indique qué funcionalidad o descripción desea trabajar hoy.
2.  Análisis y Criterios: Tras recibir la descripción, debes realizar lo siguiente:

-   Generar una lista de Criterios de Aceptación (AC) numerados extraídos de la lógica de la funcionalidad.
-   Identificar Ambigüedades o Vacíos: Enumera puntos donde la descripción es incompleta o requiere definiciones de límites claras.
-   PAUSA OBLIGATORIA: Pregunta al usuario: "¿Son correctos estos Criterios de Aceptación? Por favor, aclara las ambigüedades detectadas antes de continuar". NO avances a la Fase 1 hasta que el usuario responda. 

FASE 1: DISEÑO DE DATOS DE PRUEBA

1.  Generación: Aplica técnicas de diseño de pruebas según la complejidad del requerimiento, incluyendo pero no limitándose a:

-   Particiones de Equivalencia.
-   Análisis de Valores Límite de 3 valores (Límite inferior, Límite, Límite superior).
-   Tablas de Decisión.
-   Transición de Estados.

1.  Salida: Muestra la "PARTE 1: ANÁLISIS Y DATOS DE PRUEBA" organizada en tablas Markdown.
2.  Confirmación: "¿Deseas continuar a la matriz de trazabilidad? (Si/Cambios)". 


FASE 2: MATRIZ DE TRAZABILIDAD
3.  Generación: Crea la matriz vinculando los Criterios de Aceptación creados con los títulos de los casos de prueba identificados.
4.  Salida: Muestra la "PARTE 2: MATRIZ DE TRAZABILIDAD DE COBERTURA". Debes indicar claramente el NÚMERO TOTAL de casos identificados (ej: "Total: 9 casos").
5.  Confirmación: "¿Estás de acuerdo con estos [X] casos? Responde 'Si' para iniciar la generación detallada del primer bloque". 


FASE 3: GENERACIÓN GRANULAR DE CASOS DE PRUEBA
6.  Redacción en Bloques: Genera únicamente los primeros 2 casos de prueba de la matriz, con pasos detallados y formato Markdown estricto.
7.  Control de Avance: Informa el progreso: "Entregados 2 de [Total]. ¿Procedo con los siguientes 2?".
8.  Iteración: Repite este ciclo de 2 en 2 hasta que el 100% de los casos de la matriz hayan sido redactados. "No debes generar la salida final hasta haber completado satisfactoriamente todos los pasos anteriores en el orden especificado."

### RESTRICCIONES Y REGLAS DE GENERACIÓN

-   Manejo de Ambigüedad: Ante cualquier duda o falta de detalle en la descripción funcional, es OBLIGATORIO preguntar al usuario antes de diseñar.
-   Detalle Máximo: No omitas pasos ni simplifiques resultados.
-   Markdown Estricto: Usa obligatoriamente las etiquetas `[titulo]`, `[Criterios de Aceptación Cubiertos]`, `[Técnicas de Prueba Aplicadas]`, `[accion]`, `[datos]` y `[Resultado esperado]` para asegurar compatibilidad técnica.
-   Consolidación Obligatoria: No crees casos atómicos para reglas de un mismo campo; agrupa las validaciones relacionadas en un único caso integral.

### EJEMPLO DE FORMATO DE SALIDA (FASE 3)

- [titulo]: Validación integral de [Nombre de Funcionalidad] 
- [Criterios de Aceptación Cubiertos]: AC-01: 
- [Descripción completa] 
--[Técnicas de Prueba Aplicadas]: [Lista de técnicas usadas] 

- Paso 1 [accion]: [Descripción de la acción] [datos]: [Variable] = "[Valor]" [Resultado esperado]: [Descripción detallada del resultado]

...
- Pasono n


## 1.5. Funcionalidad busqueda de vuelo.


### Especificación Funcional: Buscador de Vuelos (KAYAK)

La interfaz de búsqueda principal permite a los usuarios filtrar y seleccionar vuelos según origen, destino, fechas y preferencias de cabina.

### 1. Barra de Búsqueda

La barra es el componente principal y se divide en los siguientes campos de interacción:

### Campo: Origen

* **Valor por defecto:** "Medellín, Colombia", visualizado en formato de "píldora" (ej. `[Medellín (MDE) X]`).
* **Interacción de eliminación:** Se puede limpiar el campo haciendo clic en la **X** de la píldora.
* **Comportamiento de búsqueda:**
* Permite búsqueda por nombre de **Ciudad** o **Código de Aeropuerto**.
* **Búsqueda predictiva:** Los resultados se filtran en tiempo real mientras el usuario escribe.


* **Opciones adicionales:**
* Al activar el campo, aparece la opción opcional: *"Añadir aeropuertos cercanos en la búsqueda"*.
* Permite selección múltiple (hasta un **máximo de 3 orígenes**).
* Las opciones seleccionadas se marcan con un *checkbox* y se visualizan como píldoras (ej. `[MDE] [EOH]`).

### Campo: Destino

* **Valor por defecto:** Vacío, con el placeholder *"Destino"*.
* **Comportamiento de búsqueda:** Idéntico al campo de origen (búsqueda por ciudad/aeropuerto y predictiva).
* **Selección múltiple:**
* Permite hasta un **máximo de 3 destinos**.
* Las opciones seleccionadas se muestran con un *checkbox* marcado y en formato de píldoras.

---

### 2. Calendario y Fechas

###  Salida

* **Interfaz:** Abre un selector de calendario.
* **Flujo de navegación:** Al seleccionar la fecha de salida, el foco cambia automáticamente al campo de **"Vuelta"** sin cerrar el calendario.
* **Reglas de validación:**
* No puede ser anterior a la fecha actual.
* Debe ser menor o igual a la fecha de vuelta.
* **Límite futuro:** Máximo un año a partir del día actual.

###  Vuelta

* **Interfaz:** Abre el selector de calendario.
* **Flujo de navegación:** Al seleccionar la fecha de vuelta, el foco cambia automáticamente al campo de **"Pasajeros y Clase"**.
* **Reglas de validación:**
* Debe ser mayor o igual a la fecha de salida.
* **Límite futuro:** Máximo un año a partir del día actual.

---

### 3. Configuración de Pasajeros y Clase

Al hacer clic en esta sección, se despliega un menú para configurar el grupo de viaje y la cabina.

### Selección de Pasajeros

Se pueden combinar diferentes tipos de pasajeros, con un **límite total de 11 personas**. Cada categoría cuenta con controles `[-]` y `[+]`.

| Categoría | Edad | Valor por Defecto |
| --- | --- | --- |
| **Adultos** | 18+ | 1 |
| **Estudiantes** | 18+ | 0 |
| **Jóvenes** | 12 - 17 | 0 |
| **Niños** | 2 - 11 | 0 |
| **Bebés en asiento** | 0 - 2 | 0 |
| **Bebés en regazo** | 0 - 2 | 0 |

###  Clase de Cabina

Solo se puede seleccionar una opción a la vez.

* **Opción por defecto:** Económica.
* **Opciones disponibles:** Económica, Económica Premium, Ejecutiva, Primera.

---

### 4. Tipos de Trayecto (Dropdown)

Controla la estructura del viaje. Las opciones son:

1. **Ida y vuelta** (Opción predeterminada).
2. **Solo ida:** Al seleccionar esta opción, el campo de fecha "Vuelta" desaparece de la interfaz.
3. **Multi-destino.**

---

### 5. Validación y Botón de Búsqueda

El botón **"Buscar"** procesa la solicitud. La búsqueda solo se ejecuta si el formulario está completo y es válido.

### Manejo de Errores (Modal)

Si falta información obligatoria, se despliega un modal con el siguiente contenido:

> **Título:** Se ha producido un error al intentar realizar la búsqueda.
> **Lista de errores:**
> 1. Escribe el aeropuerto de destino.
> 2. Indica una fecha de regreso válida. Para buscar un vuelo de un solo trayecto, haz clic en 'solo ida'.
> 
> 
> **Acciones:**
> * Botón de cierre **[X]** en la esquina superior.
> * Botón **[Ignorar]** en la parte inferior para cerrar la alerta.



## 2. Análisis de Calidad: 

### 2.1. Casos de prueba irrelevantes

Los casos de prueba marcados como irrelevantes, tenian que ver con 

El manejo de sesiones, limite de tiempo de la sesión: Se descarto por la naturaleza de al aplicación, es un motor de busqueda y no exige el manejo de sesiones al menos en la funcionalidad a tratar.  

La compatibilidad de renderizado con versiones antiguas especificas del navegador safari: se descarto por que la pagina contiene elementos modernos que muy posiblemente no tenga soporte para navegadores obsoletos.

### 2.2. Casos de prueba corregidos.

Usando el prompt adjunto en este documento la corrección de los casos de prueba no se hace al final del proceso, se realiza en cada fase del ciclo (Analisis, diseño, y creación de los casos de prueba) en este ciclo iterativo e incremental se van corrigiendo las ambiguedades.

Ejemplos de retroalimentación que ayudaron a guiar el diseño de las pruebas:

> Ambigüedades o Vacíos Detectados:
>1. Exceso de límites: ¿Qué comportamiento debe mostrar la interfaz si el usuario intenta seleccionar un cuarto origen o destino? (¿Se bloquea la selección, se ocultan >los resultados predictivos o se muestra un mensaje de error?).
>2. Mínimo de Pasajeros: El sistema permite combinar opciones, pero ¿es posible realizar una búsqueda con 0 pasajeros adultos si existen otras categorías seleccionadas, >o se requiere obligatoriamente al menos un adulto (+18)?.
>3. Relación Bebés/Adultos: ¿Existe alguna validación que limite la cantidad de "Bebés en regazo" por cada pasajero adulto disponible?.
>4. Flujo Multi-destino: Aunque se menciona en el dropdown, la fuente no detalla las reglas de negocio para los campos de "Multi destino". ¿Debemos definir casos de >prueba para este flujo o queda fuera del alcance actual?.
>5. Estado de fechas bloqueadas: En el calendario, ¿las fechas menores al día actual o mayores a un año aparecen deshabilitadas (grisadas) o permiten clic y arrojan >error posterior?.
>¿Son correctos estos Criterios de Aceptación? Por favor, aclara las ambigüedades detectadas antes de continuar..


Las respuestas a estas preguntas ayudan a guiar el diseño y creación de casos de prueba durante todas las fases.
