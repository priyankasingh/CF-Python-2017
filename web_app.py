from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def hello():
    author="MyName"
    name="Robot"
    return render_template('index.html',author=author,name=name)

@app.route("/signup",methods=['POST'])
def sign_up():
    form_data=request.form
    print("Inside submit")
    print(form_data['name'])
    print(form_data['email'])
    return "ALL GOOD!"

if __name__=="__main__":
    app.run()
