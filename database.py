from sqlalchemy import create_engine, text
import os

DB_DATABASE = os.environ['DB_DATABASE']
DB_USERNAME = os.environ['DB_USERNAME']
DB_HOST = os.environ['DB_HOST']
DB_PASSWORD = os.environ['DB_PASSWORD']

db_connection_string = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs
  