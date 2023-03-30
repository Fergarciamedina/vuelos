from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

app = FastAPI()

# Cadena de conexión
DATABASE_URL = "mysql+pymysql://bsale_test:bsale_test@mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com/airline"

# Crear motor de base de datos
engine = create_engine(DATABASE_URL)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ejemplo de uso de la sesión para consultar todas las tablas de la base de datos
@app.get("/tables")
def get_tables():
    session = SessionLocal()
    result = session.execute("SHOW TABLES")
    tables = [row[0] for row in result]
    return tables
