## Some more of Web Scraping

## Scraping United States National Weather Service website

### Submitting a form

The site of the United States National Weather Service is present at [www.weather.gov](http://www.weather.gov/).
United States Government has long ago decreed that all publications produced by their agencies are public domain. This means that, we can pull all sorts of data from their website. 

When using the `urllib` module from the Standard Library, we will have to read the web page HTML manually to find the form.  We can either use `Inspect element` or `View Source` command in our browser, search for 
the words `Local Forecast`, and find the following form in the middle of HTML tree:

~~~{.python}
<form method="post" action="http://forecast.weather.gov/zipcity.php" ...>
  ...
  <input type="text" id="zipcity" name="inputstring" size="9"
    value="City, St" onfocus="this.value='';" />
  <input type="submit" name="Go2" value="Go" />
</form>
~~~

The only important elements here are `form` and `input` fields inside. 
This form does a `POST` to a particular URL with, it appears, just one parameter: an  `inputstring` giving the city name and state. 

### Challenge 1: Write a python script that uses Python Standard `urllib` library to perform above interaction  and save the result to `<placename>.html`.

**NOTE: ** Python 3 libraries require bytes instead of good old strings.

~~~{.python}
#!/usr/bin/env python
# Submitting a form and retrieving a page with urllib

import urllib
import urllib.request
import urllib.parse
data = urllib.urlencode({'inputstring': 'Austin, TX'})
data = data.encode('utf-8') 
info = urllib.request.urlopen('http://forecast.weather.gov/zipcity.php', data)
content = info.read()
open('austin.html', 'w').write(content)
~~~

As you can see above, `urllib` library makes this interaction very convenient, we are able to download a forecast page using only a few lines of code. But, we had to read and understand the form ourselves instead of relying on an 
actual HTML parser to read it. 

### Scraping with `RoboBrowser`

The approach encouraged by `mechanize` is quite different: We only need the web page address of the opening page to get started, and the library itself will take the responsibility for exploring the HTML and letting us know what forms are present. It itself finds the forms on a particular web page. However, this library doesn't work on Python 3. 

In order to help us avoid reading any HTML at all, Python 3 versions >= 3.3 and Python 2 versions >= 2.6 has a library called `RoboBrowser`, a simple pythonic library for browsing web without standalone web browser. It can fetch a page, click on links and buttons, fill and submit forms. RoboBrowser can be used or of help if we need to interact with web services that don't have APIs. 

It combines the best of 2 excellent Python libraries: Requests and BeautifulSoup. It's like `Mechanize` in Python 3.

You can install RoboBrowser with command as below:

~~~{.python}
easy_install robobrowser
~~~

OR

if you have virtualenvwrapper installed:

~~~{.python}
mkvirtualenv robobrowser
pip install robobrowser
~~~

It's a Robotic web browser. Represents HTTP requests and responses using the `requests` library and parsed HTML using `BeautifulSoup`. 

Let's try working on **Challenge 1** above using **RoboBrowser**.

###Challenge 2: Submitting a form with `RoboBrowser` Pythonic library

~~~{.python}
from robobrowser import RoboBrowser

#Browse to USA National Weather site
browser=RoboBrowser(history=True)
browser.open('http://www.weather.gov/')

#Search for getForecast id
form = browser.get_form(id='getForecast')
form 
form.parsed

#Set the value to input string for the place's data you want to search
form['inputstring'].value='Austin, TX'
dir(form)                                       #Listing the methods and attributes that can be used with form
browser.submit_form(form)
browser
dir(browser)   				#Listing the methods and attributes that can be used with browser

#Checking the URL for the input string data
browser.url
type(browser.url)
~~~

We will now be opening the URL for the data based on the City, State entered in `Search` section of the website and store the data in an HTML file like before.

~~~{.python}
import urllib
import urllib.request

info=urllib.request.urlopen(browser.url)
content=info.read()

#Type below command. It will throw error based on the content's data type. But need to show error for explanation and flow of the program.
 open('austin2.html', 'w').write(content)
 
 #Based on the error, content needs to be converted to String as below. 
 content
 type(content)
 
 open('austin2.html', 'w').write(str(content))
 
 #Check the file and the format and then run below commands.
 content=content.decode()
 
 open('austin2.html', 'w').write(content)
~~~ 

### Challenge 3: Write a python script to find the total number of clinical trials as recorded by the [National Institutes of Health](https://clinicaltrials.gov/).

**Solution: **

~~~{.python}
import requests
from lxml import html
url = 'https://clinicaltrials.gov/'
document = html.fromstring(requests.get(url).text)
element = document.cssselect('#trial-count > p > .highlight')[0]
print(element.text_content())
~~~

### Challenge 4: Write a python script to find the [total number of visitors to the White House](https://www.whitehouse.gov/briefing-room/disclosures/visitor-records) in 2015.


