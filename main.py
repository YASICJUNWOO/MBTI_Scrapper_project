from mm import extract_mbti_overview
from flask import Flask

app = Flask("mbti-tracker")

@app.route("/")
def home():
    return "<h1>assfdsafsdaf!</h1>"


#data = extract_mbti_overview(mbti)
#if data == 404:
#   print("error")
#else:
#    print(data)

app.run("0.0.0.0")