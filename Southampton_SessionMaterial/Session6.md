##Flask and GET/ POST requests

By now, since we have an intermediate knowledge of the `Python` programming language. We'll be using `Flask`, a Python web application framework, to create a simple web application from scratch, with `MySQL` as a back end.

####Introduction 

The de facto framework that usually comes to our mind is the `Django` framework when we think about Python. But from a beginner's perspective, Flask is easier to start with, as compared to Django.

Flask is a framework for building lightweight web applications. In order to get up and running, we will follow the instructions as mentioned below:

Setting up Flask is pretty simple and quick. With `pip` package manager, all we need to do is:

`pip` can be installed with below command:

~~~{.python}
easy_install pip
~~~

~~~{.python}
pip install flask
~~~

Now, let's create a baseline Flask application called `hello.py` as below by importing the `flask` module and create an app using Flask:

~~~{.python}
from flask import Flask
app=Flask("HelloApp")
~~~

Now define the basic route `/` and its corresponding request handler:

~~~{.python}
@app.route("/")
def hello():
    return "Hello World!"
~~~

Next, check if the executed file is the main program and run the app:

~~~{.python}
if __name__ == "__main__":
    app.run() 
~~~

Save the changes and execute `hello.py`:

~~~{.python}
python hello.py
~~~

Point your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and you should see the welcome message.

####Flask routes and decorators

You may be wondering what `@?app.route?stands` for and why we are using it. This is what is known as a **d?ecorator**.? 

The concept of decorators exists in most programming languages; their purpose is to inject or modify code in functions. 

In simpler terms, imagine you would like to do something at the entry and/ or exit points of a function. 
This is what is happening here ? `@app.route`, ?which is part of Flask, is doing some things internally for us so that we can accept a request coming from the user's browser into the Python. 

A *decorator* always starts with the **@** sign and goes on the line right before a function is defined.

### Flask: Taking parameters from the URL

Let's look at the code below:

~~~{.python}
from flask import Flask

app=Flask("My App")

@app.route("/")
def hello():
      return "Hello World!"
      
@app.route("/<name>")
def hello_someone(name):
      return "Hello {0}!".format(name.title())
      
app.run()
~~~

The **<name>** is a URL matcher - It will match **/** followed by any word, for example /andreas, /rachel etc. Flask will make this value available as a parameter to **hello_someone**. We then use the **name** variable to say hello to a particular user. 

We will edit the previous file and add the function **hello_someone**. And then check if that works by visiting URL [http://127.0.0.1:5000/andreas](http://127.0.0.1:5000/andreas) or your name if you prefer.

#####Challenge 1

Try and make the above program so that visiting **localhost:5000/bye/andreas** returns `Goodbye Andreas` or `Goodbye` for any other name given.

###Serving HTML using Flask

Flask lets us serve our HTML - This is possible using the **render_template** function. All we have to do is provide the name of the template and the variables we want to pass to the template engine as keyword arguments. 

Below is an example of how to render a template:

~~~{.python}
from flask import Flask
from flask import render_template

app=Flask("HelloApp")

@app.route("/")
def hello():
      return render_template("hello.html")
      
@app.route("/<name>")
def hello_someone(name):
      return render_template("hello.html", name=name.title())
      
app.run()      
~~~

**Note: Flask will look for templates in the templates folder.**
Flask uses another library called [Jinja2](http://jinja.pocoo.org/docs/dev/), which is a templating language for Python. It's extremely powerful. Here's what an example **html file hello.html** would look like, inside a templates folder, that uses Jinja2:

~~~{.html}
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
    <h1>Hello {{ name }}! </h1>
{% else %}
    <h1>Hello World! </h1>
{% endif %}
~~~

#####Challenge 2

Extend the above code so that you can say goodbye to someone if you visit **localhost:5000/goodbye/<username>**.

Also, try to add some more parameters to the URL and pass those onto your `hello.html` template. May be something like "Hello <username>! Have a nice day!" and "Hello <username>! Have a good night!" corresponding to localhost URLs.

###Files

So far, we've seen how to send out some basic text with a simple Flask application, and the languages that are used to build the web: HTML, CSS and Javascript (as a part of previous CodeFirst course). Showing and serving text is not enough when we want to serve some actual files.

Flask has the facility to **create a folder** in the same directory as `hello.py` with the special name of `static`. Any file you put in that folder will be served by Flask automatically. 

Directory can be created using `mkdir static` command. You can save an image file in this static folder, and we'd normally access our application by visiting the URL [http://127.0.0.1:5000](http://127.0.0.1:5000), then  we can view that file by going to [http://127.0.0.1:5000/static/<image>](http://127.0.0.1:5000/static/<image>).

The `static` folder is a great place to put CSS stylesheets, Javascript script files, and images. Those files don't usually change much when a website is running, hence the folder name. A common practice is that web developers will organise these files in sub-directories called, for instance, `css`, `js`, and `ing` respectively.

###HTML Templates

The *content* of our application is put in **THE HTML** file. Flask makes use of HTML templating that allows it to put dynamic application data (like a list of email addresses that changes over time) into HTML easily, so that any web browser can view it easily, and it looks good as well. 

Flask uses another special directory to store templates, called `templates`. Let's go ahead and create it, like we did for `static` using `mkdir templates`. 

In this directory, we **create a file** called `index.html` and put some HTML: 

~~~{.html}
<!DOCTYPE html>
<html>
  <head>
    <title>{{ author }}'s first Python Web App</title>
  </head>

  <body>
    <h2>Hello {{ name }}!</h2>
  </body>
</html>
~~~

The above one is a simple HTML page, but it includes 2 simple bits of Flask's templating language. When Flask shows this template in our browser, it will replace `{{author}} and {{name}}` with what we assign those 2 variables in our application. If author was assigned to be **Jack**, then the title of the page will be **Jack's first Python Web  App**. 

A template separates what the content of the page should be, from the actual data that will be used as that content which makes things easier if we have to write a lot of dynamic web pages. They can do more than just display variables. Let's now modify the web app based on the above template now:

~~~{.python}
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
      author = "Devasena"
      name = "Robot"
      return render_template('index.html', author=author, name=name)

if __name__ == "__main__":
     app.run()
~~~

From the above script, instead of returning some text, we returned the result of calling `render_template`. First, we give it the file name of the template we wish to process. Then, we pass in the variable names that the template should know about (`author` and `name`) and what their values should be (..coincidentally, `author` and `name`). This function loads up the template, do the processing with the values entered, and return the full HTML text. 

You can now run and view your app.

###Creating a home page

When the application runs for the first time, we should show a home page with the introduction and main content. Let's make our home page a bit more prettier. Let's put some fancy fonts, large bold types, huge banner images and nice round corners and things. We need some more interesting html and some of CSS to get it look more pretty. 

Let's prepare a self-contained template that we can use for our home page. You can download it from [here](index.html) and save it in your **templates** folder. 

We can now modify our Flask app or use the same script to serve above created template.

###GET & POST requests

In the world of HTTP, there are a number of types of requests; we will be concentrating on two of them: 

- **GET** - When you want to retrieve data
- **POST** - When you want to send data

Everything we have been doing so far has been using a **GET request** - let's see how we can use a simple **POST request**. Let's add a form to [**index.html**](index.html):

~~~{.html}
<div id="contact-form">
      <h1>Get In Touch!</h1>
      <form method="post" action="/signup">
              <label for="name">Name: </label>
               <input type="text" id="name" name="name" value="" placeholder="Devasena Inupakutika" required="required" autofocus="autofocus"/>
               <label for="email">Email Address:</label>
               <input type="email" id="email" name="email" value="" placeholder="devasena.prasad@gmail.com" required="required" />
               <input type="submit" value="Submit" id="submit-button" />
       </form>
</div>
~~~

Pay attention to the **form** element which has an action equal to **/signup** - that's the URL which the form will be submitted to, relevant to the absolute URL you are at (in this case **localhost:5000**)- so we need to create an entry in our **hello.py** file:

~~~{.python}
@app.route("/signup", methods=['POST'])
def sign_up():
      form_data=request.form
      print(form_data['name'])
      print(form_data['email'])
      return "All OK!"
~~~

There is one thing that we need to do! You might have noticed that we are now accessing a variable called **request**; where did this come from? This is actually part of Flask and we need to import it - so at the very top of our `hello.py` file, let's insert:

~~~{.python}
from flask import request
~~~

Now if you navigate to [localhost:5000/hello/<username>](localhost:5000/hello/<username>).

###Flask Project Directory Structure

Below is the recommended structure for any Flask project/ application:

~~~{.python}

/your_app
       hello.py
       /static
              /js
                    hello.js
             /css
                    hello.css
            /images
                   hello.jpg
       /templates
            hello.html
~~~

Whatever is stored in `templates` can be automatically detected when using `render_template` function, so there isn't anything else we need to do. In order to reference our CSS, Javascript and images from within our HTML, then we need to do something like below:

~~~{.html}
<!doctype html>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/hello.css') }}">
<title>Hello from Flask</title>
{% if name %}
    <h1>Hello {{ name }}! </h1>
{% else %}
    <h1>Hello World! </h1>
{% endif %}
~~~    

###Head to [Mandrill's website](http://mandrill.com) and create an account; we will be using Mandrill to programmatically send emails.

###Head to [twitter.com](https://twitter.com/) and create yourself a **Twitter** account if you don't already have one; we will be using Twitter's API to fetch data - you will need to have an account in order to do that. 

##Using external APIs

###APIs

APIs are of vital importance to developers; they enable you to programmatically access data from various different services such as Twitter, Facebook and Spotify to name a few. APIs enable you to create applications powered by data from any service of your liking. 

###Mandrill

When building a website, for example a landing page for what is to come, one vital thing to do is capture the details of people that might be interested in what you are going to launch. 

Most importantly, you want to capture their email address so you can communicate things to them. 
In this session, we will learn how to capture a user's email address and any other details for that matter 
and programmatically send them an email to confirm that they have signed up to your website's newsletter. 

This will be an interactive session based on what we did in **Session 6**. If you look at what we did during that session under the **GET & POST** section, you will see that we already learnt how to capture a user's name and email and print it out on our terminal. Now we are going to use that data to send an email. 

We will be using [Mandrill](http://mandrill.com), an email infrastructure service - or in simpler terms, a service that enables you to programmatically send emails. Madrill has a Python library that makes it easy to send emails, so go ahead and head over to their [Python documentation](https://mandrillapp.com/api/docs/index.python.html) and follow the instructions on how to install the Python client and get started. 

Please create an account on Mandrill now. If you get an error message like `too many people are trying to create an account from the same location`, then wait a little bit. 

This is Mandrill's way to safeguard against spammers creating accounts programmatically to send spam e-mail. 

You can get the Mandrill Python API Client using below command:

~~~{.python}
sudo pip install mandrill
~~~

In order to programmatically send emails, we need to get an API key, so go ahead and click on **Get API Keys**. On the next page that you are presented with, click on **+New API Key**. 

On the form that opens up, add a description to make it easier to track your API Keys and leave the rest of boxes unchecked. 

You might wonder, why would you ever want to create multiple API keys. This is especially useful when your website grows and you start sending emails for different functions; registration emails, newsletters etc.  In those cases, you would want to use a different API Key for each function to make life easier when managing what each component does. 

After adding a description, hit **Create API Key** - you should now see a key listed. You will notice that there is a little On/ Off toggle button to the right of the key - ensure that is **On**. 

If we now go back to [Mandrill's Python Documentation](https://mandrillapp.com/api/docs/index.python.html), you can see instructions on how to use the library - to authenticate yourself with Mandrill via Python this is as simple as writing 2 lines of code:

~~~{.python}
import mandrill
mandrill_client = mandrill.Mandrill('Your_API_Key')
~~~

Next up, we want to actually send an email, so we can look at [this](https://mandrillapp.com/api/docs/messages.python.html) part of the documentation which you can access from the left hand side of the Python documentation. The most minimal to send an email would be the following:

~~~{.python}
import mandrill
mandrill_client = mandrill.Mandrill('Your_API_Key')

message={
         'from_email': 'sender email address',
         'from_name': 'sender name' ,
         'html': '<p>Thanks for signing up to our awesome newsletter!<p>',
         'subject': 'Welcome!',
         'to': [
             {
                  'email': 'recipient email address', 
                  'name': 'Recipient name goes here',
                  'type': 'to'
             }
         ]
}

mandrill_client.messages.send(
         message=message,
         async=False,
)

~~~{.python}                           

The above example is completely independent from a Flask app, so what you should do now is to figure out how to apply the above code in the context of your Flask app that we created in the last session. 

Ensure that you're sending an email to a valid email address, set your own email address as the **from_email** and use the email and name submitted via the form that we were previously printing.

Read through the documentation and figure out what other things you can do with Mandrill - Can you send an email to multiple recipients? Can you add attachments?

