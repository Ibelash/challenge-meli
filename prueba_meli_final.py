import pandas as pd
import sqlite3
import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#credenciales del correo (están en variables de entorno, esto lo hice para que no estuvieran las credenciales en texto plano).
name_account = "ChallengeMeli"
email_account = os.getenv('email_account')
password_account = os.getenv('password_account')

#verifica que las variables de entorno se cargaron.
if not email_account or not password_account:
    raise ValueError("No se pudieron cargar las credenciales desde las variables de entorno. Asegúrate de que estén bien configuradas.")

#configuración del servidor smtp.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(email_account, password_account)

#conecta a la base de datos de SQLite (se creará si no existe).
conn = sqlite3.connect('bases_de_datos.db')
cursor = conn.cursor()

#crea una tabla (si no existe).
cursor.execute('''
CREATE TABLE IF NOT EXISTS bases_de_datos (
    db_name TEXT,
    owner_email TEXT,
    manager_email TEXT,
    classification TEXT
)
''')

#lee el archivo json.
json_path = r'C:\Users\joels\Downloads\challenge-meli\correos.json'
with open(json_path, 'r') as file:
    db_classifications = json.load(file)

#lee el archivo csv.
csv_path = r'C:\Users\joels\Downloads\challenge-meli\archivo.csv'
usuarios_df = pd.read_csv(csv_path)

#procesa los datos y los guarda en la DB.
for db in db_classifications:
    db_name = db.get('db_name', 'Unknown')
    owner_email = db.get('owner_email', 'Unknown')
    classification = db.get('classification', 'Unknown')

    #encuentra al manager para el owner.
    manager_row = usuarios_df[usuarios_df['user_id'] == owner_email]
    if not manager_row.empty:
        manager_email = manager_row.iloc[0]['user_manager']
    else:
        manager_email = 'Unknown'

    #guarda en la base de datos.
    cursor.execute('''
    INSERT INTO bases_de_datos (db_name, owner_email, manager_email, classification)
    VALUES (?, ?, ?, ?)
    ''', (db_name, owner_email, manager_email, classification))

    #envia correos si la clasificación es alta o high.
    if classification.lower() == 'high' and manager_email != 'Unknown':
        subject = f"Revisión de Clasificación Alta: {db_name}"
        message = f"Hola,\n\nLa base de datos {db_name} tiene una clasificación alta. Por favor, revisa y aprueba esta clasificación.\n\nSaludos,\n{name_account}"

        msg = MIMEMultipart()
        msg['From'] = f"{name_account} <{email_account}>"
        msg['To'] = manager_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server.sendmail(email_account, manager_email, msg.as_string())
            print(f"Correo enviado a {manager_email} para la base de datos {db_name}.")
        except Exception as e:
            print(f"No se pudo enviar el correo a {manager_email}. Error: {str(e)}")

#hace los cambios en la base de datos y cierra la conexión.
conn.commit()
conn.close()
server.close()