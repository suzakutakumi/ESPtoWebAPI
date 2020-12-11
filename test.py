from flask import Flask
app = Flask(__name__)

@app.route("/a=<x>,b=<y>")
def Sum(x,y):
    return str(int(x)+int(y))

if __name__ == "__main__":
    app.run(debug=True, port=80)
#    app.run(debug=False,host='0.0.0.0',port=8080)
