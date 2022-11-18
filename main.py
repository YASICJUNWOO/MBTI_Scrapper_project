from extract_mbit import extract_mbti_overview
from flask import Flask,render_template,request,send_file

app = Flask("mbti-tracker")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result")
def result():
    mbti = request.args.get("mbti")
    if mbti in db:
        mbti_data = db[mbti]
    else:
        mbti_data = extract_mbti_overview(mbti)
        db[mbti] = mbti_data
    print(mbti_data)
    return render_template("result.html", mbti_data=mbti_data)


#data = extract_mbti_overview(mbti)
#if data == 404:
#   print("error")
#else:
#    print(data)

app.run("0.0.0.0")