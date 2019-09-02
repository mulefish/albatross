
from flask import Flask, jsonify, request 
from flask_cors import CORS



app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/')
def root():
    print("This is main.html")
    return app.send_static_file('main.html')

"""
@app.route("/")
def helloWorld():
    print("This is /")
    return "This path is merely a heartbeat check."
"""    
@app.route("/about/")
def about():
        print("This is /about/ path ")
        html = "<html><body>Paths:<hr>"
        html += "<a href='localhost:5000/'>/</a></p>"
        html += "<a href='localhost:5000/about/'>about</a></p>"
        html += "<a href='localhost:5000/data/'>data</a></p>"
        html += "<a href='localhost:5000/test/'>test</a></p>"
        return html 

@app.route("/test/")
def get_test():
        print("This is /test/")
        data = {"claimlines":[907,328],"patient_paid":[19,22],"ingredient_cost":[126,84],"days_supply":[28,29],"complexity":[13,9],"pain":[30,9],"velocity":[24,17],"total_patient_paid":[436020,144410],"total_ingredient_cost":[2633490,698360],"total_days_supply":[739040,191940],"total_complexity":[0,0],"total_velocity":[21845,5834]}
        return jsonify(data)


@app.route("/data/")
def get_data():
        print("This is /data/")

        data = {"claimlines":[907,328,4832,1326,5870,836,1841,472,2402,336,3129,2084,918,6593,1561,662,2640,3478,1182,3345,2564,2217,818],"patient_paid":[19,22,17,16,17,19,19,36,19,19,18,18,16,18,15,29,18,18,22,16,17,18,17],"ingredient_cost":[126,84,67,55,76,79,66,82,90,90,72,66,62,73,53,128,69,66,84,54,67,63,76],"days_supply":[28,29,33,35,35,34,29,36,30,38,36,38,30,39,30,32,38,36,40,35,39,41,33],"complexity":[13,9,4,4,3,7,6,3,8,11,5,14,12,11,8,2,4,2,7,6,17,16,6],"pain":[30,9,1,8,19,14,19,7,6,8,11,12,14,8,1,2,3,4,8,10,1,13,21],"velocity":[24,17,63,37,62,23,33,37,47,23,91,91,23,96,37,24,70,73,42,56,61,84,54],"total_patient_paid":[436020,144410,5452570,859900,6262800,375860,1145780,301940,2101280,121430,5141490,3340180,378930,10978370,967840,347410,3372530,4513790,863480,3066740,2624500,3263810,790350],"total_ingredient_cost":[2633490,698360,23246110,3203490,28642070,1736480,5004820,1175290,10973520,502930,21445500,12705460,1394260,45600670,3722540,2209800,13922500,16338300,3116430,11637160,10217240,12378710,3863510],"total_days_supply":[739040,191940,10823850,1767090,13028100,670930,2056280,644900,3873270,288700,10256670,7064300,756380,23748220,2025120,577870,6870240,9418500,2004960,6993340,6002780,7316400,1572050],"total_complexity":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"total_velocity":[21845,5834,307637,49807,367175,19420,62454,17730,115147,7833,287698,189875,21953,638832,59315,16273,187404,254412,50463,189918,157673,188225,44910]}

        return jsonify(data)


if __name__ == '__main__':
    app.run()

