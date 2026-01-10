
### PARTE 2: MATRIZ DE TRAZABILIDAD TÉCNICA (ACTUALIZADA)

| ID | Prioridad | Escenario | Tipo de prueba | Resultado esperado |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Alta | Configuración integral de Origen y Destino. | Funcional / UI | El sistema gestiona orígenes y destinos en píldoras con búsqueda predictiva. |
| **TC-02** | Media | Validación de límites máximos (3) en Origen y Destino. | Borde / Negativa | Bloqueo y mensaje "Max 3" al intentar añadir una cuarta opción. |
| **TC-03** | Alta | Gestión de Fechas de Salida/Vuelta y Tipo de Viaje. | Funcional / Borde | Foco automático y restricciones de calendario (1 año / fecha actual). |
| **TC-04** | Alta | Validación de lógica de Pasajeros (Regla 18+ y límite de 11). | Funcional / Borde | Validación de mayoría de edad y bloqueo de botón [+] al llegar a 11 pasajeros. |
| **TC-05** | Media | Selección y Persistencia de Clase de Vuelo. | Funcional | Permite cambiar y persistir la clase (Económica por defecto). |
| **TC-06** | Alta | Validación de Gatillo de Búsqueda y Manejo de Errores Funcionales. | Negativa | Modal de error con lista de campos faltantes ante datos incompletos. |
| **TC-07** | Crítica | Búsqueda exitosa con campos obligatorios (Happy Path). | Funcional | La búsqueda inicia correctamente al cumplir todos los requisitos. |
| **TC-08** | Media | Manejo de Caché Predictivo en tiempo real | Técnica | Cada pulsación en Origen/Destino dispara una consulta al API en tiempo real sin usar datos cacheados. |
| **TC-09** | Baja | Persistencia de sesión sin límite de tiempo | Técnica | Los datos en la barra de búsqueda no se pierden por inactividad (sin límite de sesión). |
| **TC-10** | Alta | Generación y funcionalidad de Deep Linking | Técnica | El sistema genera una URL compartible que captura todos los parámetros de búsqueda seleccionados. |
| **TC-11** | Alta | Manejo de errores de servidor (HTTP 5xx/4xx) | Negativa / Técnica | Si el API predictivo falla, se muestra el mensaje "Servicio no disponible" en el dropdown. |
| **TC-12** | Media | Persistencia al redimensionar ventana (Responsiveness) | UI / Técnica | La información pre-diligenciada en los campos no debe perderse al cambiar el tamaño de la ventana. |



