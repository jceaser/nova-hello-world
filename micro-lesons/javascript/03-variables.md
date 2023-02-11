# JavaScript

## Step one, lets print something out
JavaScript is made up of words that tell the computer what to do, lets get started with two, even if we don't fully understand them yet, one is printing things out in a web page with the `alent()` function. Next we will put things in
it to show up.

In the HTML file from before, look at the alert statment on line 6

    alert("Hello World")

A break down of what it means:

* `alert` - the action name
* `()` - the action takes input, these are inside the brackets
* "Hello World" is called a string. it is text you want to display between double quotes.

Change this line to anything you want and reload the web page.

    alert("World, I say hello to you")

## Step Two, lets use some variables

Next we want to store our text in a variable. Why? Because sometimes you want the message to change, sometimes you want the thing you print out to be the result of something. Values are almost never fixed, set in stone.

Because our data can change, we want to store it somewhere in the computer's memory, and a programing language lets you give that location a memory to make it easy to use. To do this we need two things, a way to declare a variable and a way to assign it a value. We can do this with the `var` command and the `=` operator. like this:

    var message
    message = "Hello from the world of variables"
    alert(message)

From above, the `var` command takes a name to it's right and any value you send to this name will be saved in memory which is exactly what is done next with the equals operator. Operators normally do something on both sides, and the equals does just that, it takes what is on the right and puts it into what is to it's left. 

Finally we "pass" the alert action the variable using the name of the variable as an input.

JavaScript lets you "glue together" multiple string variables together with the `+` sign. Not every programing language allows this however.

JavaScript also lets you combine the naming of a variable and the assignment into one line. Here is an example of all this.

    var message = "says hello"
    var person = "Yoda"
    alert(person + " " + message)
    
## Math Time

The best part of programing is that you can make the computer do your math for you. Lets use some variables to store numbers and calculate things with those variables. We will use other operators then plus, like times. There are actually a lot of these which we can look up latter. Pretty much all math operaters work in JavaScript. A list of them can be found in [appendix a](a-operators.md).

    var m = 10
    var x = 20
    var b = 5
    y = m * x + b
    alert(y)

## Things to know from here

* **operators**: act on two things
    * `=` : where-to-save = what-to-save ; returns the that was just saved
    * `+` : first-value + second-value ; returns the result
    * `*` : first-value x second-value ; returns the product (result)
* **statment**:
    * `var` : var variable-name
* **functions**:
    * `alert()` : shows an alert box, returns nothing
    * `prompt()` : ask question in a prompt box, returns answer


---
* [previous](02-html-parts.md)
* [next](04-if.md)
