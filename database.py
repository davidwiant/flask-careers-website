from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://r1601cb4k2p0766moldr:pscale_pw_6KEqtMH4Oxc0qhYNCDcX0W7p77nqhr9mQiN3JYuOMEd@aws.connect.psdb.cloud/flaskcareers?charset=utf8mb4"

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
  
