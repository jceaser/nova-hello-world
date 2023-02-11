# Parts of an HTML page

Before we go to far it might help to explain all the parts of the HTML file from the previous page. On that page we loaded the following into a text editor and a web browser:

    1. <!DOCTYPE html>
    2. <html>
    3.    <head>
    4.        <title>Page Title</title>
    5.        <script>
    6.            alert("Hello World")
    7.        </script>
    8.    </head>
    9.    <body>
    10.        Web page content here
    11.    </body>
    12.</html>

Each line has a unique effect in creating a web page and most of these lines contain "tags". HTML tags are made up of starting tags and ending tags. Each of these tags have a name wrapped inside of &lt; and &gt; signs. Ending tags have a slash in them to set them appart from starting tags. The text between the start and the ending tag is considered the "tag content".

For example, here is a title tag:

    <title>Text goes here</title>

In the web page example at the top of the page, here is a break down of all the tags:

1. doctype: tells a web browser that the file is an HTML 5 document.
2. html: starts the HTML page content
3. head: Starts the "Header" section, a place for information the web page holds that is not viewable.
4. title: The document title, shows in the Tab of the web browser or in the window.
5. script: This is what we are looking for, it is the script tag for loading javascript!
6. JavaScript Code!
7. script end tag
8. head end tag
9. Body start tag: visual part of the document
10. Page content is here, not much, just some words
11. Body end tag
12. HTML end tag

## Thinks to know

* HTML tags with content have a start and end tag.
* head tag is where control stuff goes on a web page.
* the body tag is where page stuff happens.

---
* [previous](01-basics.md)
* [next](03-variables.md)

