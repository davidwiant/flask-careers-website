from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title':'Data Analyst',
    'location': 'Springfield, IL',
    'salary': '1,000,000 USD'
  },
  {
    'id': 2,
    'title':'Data Scientist',
    'location': 'Chatham, IL',
    'salary': '1,000 USD'
  },
  {
    'id': 3,
    'title':'Data Engineer',
    'location': 'Rochester, IL',
    'salary': '1 USD'
  },
  {
    'id': 4,
    'title':'Backend Engineer',
    'location': 'Springfield, IL',
    'salary': '1,000,000 USD'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='Flask')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)