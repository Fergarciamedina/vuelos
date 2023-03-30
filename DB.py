from sqlalchemy import create_engine, text

MYSQL_USER = ""
MYSQL_PASSWORD = ""
MYSQL_HOST = "mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com"
MYSQL_DATABASE = "airline"

DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"

engine = create_engine(DATABASE_URL)

# crear una conexión a la base de datos
conn = engine.connect()


