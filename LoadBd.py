#sera un codigo que  toma un archivo excel y lo carga en la base de datos postgresql

import os
from sqlalchemy import create_engine
import pandas as pd

#conectar a la base de datos
db = 'Clinica'
table = 'historialcorreos'
ruta_archivo = os.path.join(os.path.dirname(__file__), 'Master Correos.xlsx')

url = 'postgresql+psycopg2://doadmin:TKxDxHfzaouypznW@db-postgresql-nyc3-33543-do-user-7742399-0.b.db.ondigitalocean.com:25060/' + db
# leer el archivo excel y cargarlo en la base de datos
engine = create_engine(url, echo=False)
df = pd.read_excel(ruta_archivo)
print(df)
df.to_sql(name=table, con=engine, if_exists='replace', index=False)