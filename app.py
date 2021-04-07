from flask import Flask
app = Flask(__name__)

@app.route("/")
def Home():
  return "Hello Saitarn Ounprasert 6006021611054 from Server"


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=80)