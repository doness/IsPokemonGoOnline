from flask import Flask, render_template, redirect, request
app = Flask(__name__)
import json
from flask_table import Table, Col

class ServerTable(Table):
    """
    Table Property
    """
    classes = ['table', 'table-striped']
    location = Col('Location')
    status = Col('Status')
    delay = Col('Time Elapsed')

class Item(object):
    """
    Table Property
    """
    def __init__(self, location, delay, status):
        self.location = location
        self.status = status
        self.delay = delay

def GetCONInfo():
    a = json.load(open('output.json'))
    b = []
    b.append(a['CON']['delay'])
    b.append(a['CON']['quality'])
    return b

def JSONProcessing():
    a = json.load(open('output.json'))
    b = ["AUTH","CON","US","UK","GER","NED"]
    c = []
    z = []
    for i in b:
        c.append(a[i]['quality'])
        z.append(a[i]['delay'])
    d = zip(b,c,z)

    return d

@app.route("/", methods=["GET","POST"])
def homeFunc():
    listTable = []
    for abc in JSONProcessing():
        location, status, delay = abc
        listTable.append(Item(location, status, delay))
    servers = ServerTable(listTable)
    b = GetCONInfo()
    return render_template("home.html", statusserver=b[1], ping=b[0], table=servers)

@app.route("/api/", methods=["GET","POST"])
def apiFunc():
    f = open("output.json")
    js = json.load(f)
    return json.dumps(js, indent=4, sort_keys=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
