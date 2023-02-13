# Repeating yourself with loops

Sometimes a program needs to run code over and over again, this is done with a "loop". There are three kinds of loops in JavaScript, while, do/while, and for loops. Each will be explored below.

## while

While loops perform a test and then run a code block if that test is true. This is not like an `if` statment in that the while loop will return to the test over and over till the test equals false. Consider this:

    var num = 0
    while (num=prompt("enter in the number 10"), num<0 || num>10)
    {
        alert("wrong, try again")
    }
    alert("A number between 0 and 10: " + num)

Before the "wrong" alert is shown, the while loop runs a test. This test is actually pretty advanced stuff, it uses a `,` to run two commands. The first one on the right asks the user a question and sets that value into a variable which is then used by the second statment on the right side of the `,`. If the number is not what we are looking for, the user is prompted to enter the correct value and the loop runs again. Only when the user gives the correct value does the loop end and the rest of the program continues.

## do/while

A do/while loop is almost exactly like a while, but it does the check after a loop runs, and is sometimes a better way of writing things. Lets rewrite the example above as a do/while loop.

    var num = 0
    do
    {
        num=prompt("enter in the number 10")
    }
    while (num<0 || num>10)
    alert("A number between 0 and 10: " + num)

In this case we just keep asking the question over and over till it is correct, and it may be more readable to some.

You decided which form of do/while vs while to use depending on when you will know if the loop is to stop. Most of the time you already have a value you want to test, and you want to not run code to make things run faster, but sometimes you have to start a process first. For example, you may write a program that needs to download a list of files from the web, but you will not know how many files exist till after you make the first call to the web site.

## for

the for loop may be the most common form of looping there is. You use this from to execute a loop a set number of times. It actually can be used in many different ways and is quite powerfull.

The basic idea of a for loop is that you will run through a list of items begning with a number and ending with another. The for loop has 3 sections to the test

1. initialization - runs once
2. test
3. post test action

Here is how it looks:

    for (var a=1 ; a<=10 ; a++)
    {
        alert("this is the run number " + a)
    }

The value you create in the initialization section is only valid inside the for loop. If you need the value outside the for loop then you will need to define a variable to hold it before the loop:

    var a
    for (a=1 ; a<=10 ; a++)
    {
        a = a * a
    }
    alert(a)

Loops are very powerfull but to really show them off we need to learn about arrays in the next section.

## Thinks to know from here
* three kinds of loops, do, do/while, and for
* do tests first, then runs
* do/while runs first, then tests if it should go again
* for is for a set number of loops

---
* [previous](04-if.md)
* [next](06-arrays.md)
