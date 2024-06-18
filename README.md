# **Mercado Pago Data Management**
Este proyecto es un script de Python diseñado para procesar y gestionar datos de correos electrónicos asociados con bases de datos de Mercado Pago. 
Utiliza un archivo JSON como entrada y genera un archivo CSV con la información procesada.
El script realiza las siguientes acciones:
- Lee datos desde un archivo JSON que contiene información sobre bases de datos y sus propietarios.
- Procesa los datos para organizar y filtrar la información.
- Genera un archivo CSV con los datos procesados.
- Envía correos electrónicos a los propietarios de las bases de datos según su clasificación.

# **Requisitos Previos**
- Python 3.x
- Librerías de Python:
  - `pandas`
-   - `smtplib` (incluido en la biblioteca estándar de Python)
- Además, asegúrate de tener acceso a un servidor SMTP para enviar correos electrónicos. Se recomienda configurar un servidor SMTP de prueba para desarrollo y pruebas.
# **Instalación**
1. **Clona este repositorio**:
   git clone https://github.com/tu_usuario/mercado-pago-data-management.git
- Navega al directorio del proyecto:
cd mercado-pago-data-management
- Instala las dependencias:
pip install -r requirements.txt
**Configuración**
Archivo JSON:
Asegúrate de tener el archivo correos.json en el mismo directorio que el script. Este archivo debe contener la información estructurada en formato JSON.
Configuración del Servidor SMTP:
Edita el script prueba_meli_final.py para incluir la configuración de tu servidor SMTP:
Host del servidor SMTP
Puerto del servidor SMTP
Credenciales de autenticación (si es necesario)
- **Uso**
Ejecuta el script:
python3 prueba_meli_final.py
- **Resultado:**
   -El script generará un archivo archivo.csv con la información procesada del archivo JSON.
   -Enviará correos electrónicos a los propietarios de las bases de datos según su clasificación.
- **Detalles del Script**
leer_json(ruta): Lee datos de un archivo JSON.
procesar_datos(data): Procesa los datos y los organiza en un DataFrame de pandas.
guardar_csv(df, ruta): Guarda el DataFrame en un archivo CSV.
enviar_correo(destinatario, asunto, cuerpo): Envía un correo electrónico al destinatario especificado.
- **Ejemplo de Uso**
Al ejecutar el script, deberías ver un archivo archivo.csv con contenido similar a:
db_name	owner_email	classification
Mercado_pago_server_1	juan.perez@mercadopago.com	high
Mercado_pago_clientes_vip_2	maria.gomez@mercadopago.com	high
Mercado_pago_test_1	carlos.ruiz@mercadopago.com	low
Mercado_pago_qa_2	juan.perez@mercadopago.com	low
Mercado_pago_tarjetas	maria.gomez@mercadopago.com	high
Mercado_pago_tarjetas_qa	carlos.ruiz@mercadopago.com	low
Además, se enviarán correos electrónicos a los propietarios de las bases de datos.

**Contribución**
¡Contribuciones son bienvenidas! Puedes ayudar de las siguientes maneras:
-Reportando errores
-Añadiendo nuevas funciones
-Mejorando la documentación
-Para contribuir, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama nueva para tu función (git checkout -b feature/tu-nueva-funcion).
Haz un commit con tus cambios (git commit -m 'Añadir nueva función').
Sube la rama (git push origin feature/tu-nueva-funcion).
Abre un Pull Request.
Licencia
Este proyecto está bajo la Licencia MIT.
