from flask import Flask
from flask import render_template

app=Flask("HelloApp1")

@app.route("/")
def hello():
#    return "Hello Everyone!"
    return render_template("hello.html")

@app.route("/<name>")
def hello_name(name):
#    return "Hello {0}!".format(name.title())
    return render_template("hello.html",name=name.title())

if __name__=="__main__":
    app.run()

