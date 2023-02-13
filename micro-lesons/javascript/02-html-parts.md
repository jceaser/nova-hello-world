# Parts of an HTML page

Before we go to far it might help to explain all the parts of the HTML file from the previous page. On that page we loaded the following into a text editor and a web browser:

    1. <!-- This is an HTML Comment, it is ignored by browsers -->
    2. <!DOCTYPE html>                      <!-- Says the document is HTML 5 -->
    3. <html>                                  <!-- Starts the HTML document -->
    4.    <head>                           <!-- Starts the non-display stuff -->
    5.        <title>Page Title</title>    <!-- Page Title, shows in browser -->
    6.        <script>                    <!-- Starts the JavaScript section -->
    7.            alert("Hello World")
    8.        </script>                             <!-- Ends the Script tag -->
    9.    </head>                                   <!-- Ends the Header tag -->
    10.    <body>                            <!-- Starts the display section -->
    11.        Web page content here
    12.    </body>                                        <!-- Ends the body -->
    13.</html>                                   <!-- ends the html document -->

Each line has a unique effect in creating a web page and most of these lines contain "tags". HTML tags are made up of starting tags and ending tags. Each of these tags have a name wrapped inside of &lt; and &gt; signs. Ending tags have a slash in them to set them appart from starting tags. The text between the start and the ending tag is considered the "tag content".

For example, here is a title tag:

    <title>Text goes here</title>

From section above, the key take aways are:

* head tags contain information for the page and about the page, like title or scripts. Head tag does not display anything in the document window
* script tag contains JavaScript, this is where we will be putting our program code.
* body tag contains everything you see in the web page


## Thinks to know

* HTML tags with content have a start and end tag.
* head tag is where control stuff goes on a web page.
* the body tag is where page stuff happens.

---
* [previous](01-basics.md)
* [next](03-variables.md)

