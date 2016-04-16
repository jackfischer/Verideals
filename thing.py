from flask import Flask, request
import requests, secrets
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
  code = request.args["code"]
  base="https://api.cloudapi.verizon.com/cloud/1/oauth2/token"
  payload = {
      'client_id': 'iz2EI43NkEq69NuqZPi1dHqm4O0a',
      'redirect_uri': 'http://jackfischer.me:5000/',
      'grant_type': 'authorization_code',
      'client_secret': secrets.client_secret,
      'code': code
      }

  r = requests.post(base, data=payload)
  return r.text
  

app.run(host='0.0.0.0', debug=True)


