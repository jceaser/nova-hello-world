# Appendix A - Operators

Table of operators in order of precedence, just like in algebra, some operators are done first

| Operator | Name | Type | What it does |
| -------- | ---- | ---- | ------------ |
| ()    | Parentheses | Special | Groups math operations
| x++   | Postfix Increment | Unary | Add after using
| x--   | Postfix Decrement | Unary | Subtract after using
| !     | NOT | Unary | reverses a true/false
| ~     | Bitwise NOT | Unary | reverses every bit of a number
| ++x   | Prefix Increment | Unary | Add before using
| --x   | Prefix Decrement | Unary | Subtract before using
| **    | Power | Binary | left value to the power of the right value
| *     | Times | Binary | left value times the right value
| /     | Division | Binary | left value divided by the right value
| %     | Remainder | Binary | left value divided by the right value, but return the remainder
| +     | Plus | Binary | returns the value of two numbers added together
| -     | Minus | Binary | returns the value of two numbers subtracted
| <     | Less than | Binary | True if the left is less then the right
| <=    | Less then or equal | Binary | True if the left is less then or equal to the right
| >     | Greater then | Binary | True if the left is larger then the right
| >=    | Greater than or equal | Binary | True if the left is larger or equal to the right
| ==    | Equal Test | Binary | True if both values are the same value
| !=    | Not Equal Test | Binary | True if both values are different
| &     | AND | Binary | Numeric AND two values, return value
| ^     | XOR | Binary | Numeric XOR two values, return value
| \|    | OR | Binary | Numeric OR two values, return value
| &&    | Binary AND | Binary | AND two values and return true or false
| \|\|  | Binary OR | Binary | OR two values and return true or false
| a?b:c | inline if | Ternary | If `a` is true, then return `b`, else `c`.

    (a+b) * c ^ d

1. a+b because is first ()
2. c^d
3. times is last

## Binary Operations

Binary operations can be with the values 0 and 1 or false and true. 0==false, 1==true. These tables are used to decipher the meaning of operations like:

    var a = true
    var b = false
    var c = a && b
    //c should be false in this case because : false = true && false

### AND - &&

| left  | right | Result |
| ----- | ----- | ------ |
| false | false | false  |
| false | true  | false  |
| true  | false | false  |
| true  | true  | true   |

**NOTE**: Result is only true if both left and right is true

### OR - ||

| left  | right | Result |
| ----- | ----- | ------ |
| false | false | false  |
| false | true  | true   |
| true  | false | true   |
| true  | true  | true   |

**NOTE**: Result is only true if either left and right is true

### XOR - ^

| left  | right | Result |
| ----- | ----- | ------ |
| false | false | false  |
| false | true  | true   |
| true  | false | true   |
| true  | true  | false  |

**NOTE**: Result is true only if left and right is different.

---
* [previous](02-html-parts.md)
* [next]()
