# Proyecto HBNB - README

## 🔍 Visión General

Este proyecto tiene como objetivo sentar las bases para el desarrollo futuro de una aplicación web inspirada en la plataforma Airbnb.

La documentación incluye varios diagramas que representan visualmente la estructura y la lógica del sistema:

* **Diagrama de Paquetes de Alto Nivel**
* **Diagrama de Clases**
* **Diagrama de Secuencia**

También se presentan conceptos y herramientas clave para construir un sistema escalable y modular.

---

## 🛠 Arquitectura del Sistema: Diseño en Capas

### Diagrama de Paquetes de Alto Nivel

Este diagrama representa una arquitectura en capas compuesta por:

### 1. Capa de Presentación

* Interfaz con el usuario (UI o API).
* Recibe solicitudes, realiza validaciones básicas y las reenvía a la capa de lógica de negocio.
* Devuelve respuestas en formatos apropiados (JSON, HTML, etc.).

### 2. Capa de Lógica de Negocio (BLL)

* Núcleo de las reglas y validaciones de la aplicación.
* Procesa las solicitudes entrantes.
* Se comunica con la capa de datos/persistencia.

### 3. Capa de Persistencia (también llamada Capa Review/Base)

* Gestiona operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
* Interactúa directamente con la base de datos.
* Puede utilizar un ORM (Mapeador Objeto-Relacional) para manejar los datos.

#### ✅ Ejemplo de Flujo Típico:

1. Un usuario envía una solicitud para ver reseñas.
2. La capa de presentación la valida y la reenvía.
3. La capa de lógica de negocio la procesa y consulta los datos.
4. La capa de datos recupera y devuelve la información.
5. La lógica procesa la respuesta.
6. La presentación la entrega al usuario.

---

## 📦 Diagrama de Clases

Este diagrama define las entidades esenciales y sus relaciones, enfocándose en el diseño orientado a objetos y la abstracción.

### 🔷 Clase Base

* Contiene atributos compartidos como `id`, `created_at` y `updated_at`.
* Todas las demás clases heredan de ella.

### 🔷 Usuario (User)

* Atributos: `id` único, `is_admin` (booleano).
* Puede crear/modificar `Places`, escribir `Reviews` y añadir `Amenities`.
* Los administradores pueden eliminar entidades.

### 🔷 Lugar (Place)

* Representa una publicación creada por un `User`.
* Incluye su propio `id` y una referencia al `id` del propietario.
* Puede contener `Amenities` y `Reviews` opcionales.

### 🔷 Reseña (Review)

* Depende de un `User` y un `Place` existentes.
* Incluye `id` del usuario, `id` del lugar, comentario y puntuación.

### 🔷 Comodidades (Amenities)

* Características opcionales que mejoran un `Place` (Wi-Fi, TV, etc.).
* Añadidas/modificadas por el `User` propietario.
* Solo los administradores pueden editarlas globalmente.

---

## ⏳ Diagramas de Secuencia

Estos diagramas ilustran paso a paso la interacción entre capas durante acciones específicas.

### Ejemplo 1: Registro de Usuario

1. El usuario envía un formulario de registro.
2. La API valida los datos.
3. La lógica de negocio verifica formato de correo y reglas de contraseña.
4. Si es válido y el usuario no existe, se guarda en la base de datos.
5. Se devuelve un mensaje de éxito o error según corresponda.

### Ejemplo 2: Creación de un Lugar

1. El propietario envía los detalles del lugar.
2. Se validan los datos.
3. Se verifica si ya existe el lugar.
4. Si no existe, se guarda en la base y se devuelve éxito.

### Ejemplo 3: Envío de una Reseña

1. La solicitud se envía al endpoint `/review`.
2. Se validan los datos.
3. Si son válidos, se guardan en la base de datos.
4. Se devuelve un mensaje de éxito.

### Ejemplo 4: Listado de Lugares

1. La solicitud se envía al endpoint `/places`.
2. La lógica de negocio consulta y formatea los datos.
3. La API devuelve la lista al usuario.

---

## 🧠 Conceptos y Herramientas Clave

* **Diseño Modular**: Separación clara de responsabilidades.
* **Patrón Facade**: Simplifica la interacción entre capas.
* **ORM**: Mapea clases a tablas de base de datos.
* **Herramientas de Diagramación**: LucidApp para el diseño, Figma para edición visual.
* **Organización**: Documentado y gestionado con Notion.

---

## ✅ Conclusión

Este README sirve como hoja de ruta para entender la estructura y la lógica del sistema HBNB. Garantiza que, antes de escribir código, la arquitectura esté diseñada con claridad para promover mantenibilidad, escalabilidad y orden.
