# Appendix B - Binary Numbers

All modern computers use binary numbers to store information, primary because binary numbers can be represented with transisters that are either "ON" (1) or "OFF" (0).

| Name        | Base    | Symbols | Code | Notes
| ----------- | ------- | ------- | ---- | ----------------------------------
| Binary      | Base 2  | 0-1     | 0b10 | How all computers store numbers
| Octal       | Base 8  | 0-7     | 007  | Not used anymore
| Decimal     | Base 10 | 0-9     | 42   | Our system
| Hexadecimal | Base 16 | 0-9,A-Z | 0xF  | A shorthand for Binary
| Bin 64      | Base 64 | A-Z,a-z,0-9,/+,= | Used to encode binary data


| Normal | Binary    | Hex | Octal | Bin 64
| ------ | --------- | --- | ----- | ------
|  0     | 0000 0000 | 00  | 00    | A
|  1     | 0000 0001 | 01  | 01    | B
|  2     | 0000 0010 | 02  | 02    | C
|  3     | 0000 0011 | 03  | 03    | D
|  4     | 0000 0100 | 04  | 04    | E
|  5     | 0000 0101 | 05  | 05    | F
|  6     | 0000 0110 | 06  | 06    | G
|  7     | 0000 0111 | 07  | 07    | H
|  8     | 0000 1000 | 08  | 10    | I
|  9     | 0000 1001 | 09  | 11    | J
| 10     | 0000 1010 | 0A  | 12    | K
| 11     | 0000 1011 | 0B  | 13    | L
| 12     | 0000 1100 | 0C  | 14    | M
| 13     | 0000 1101 | 0D  | 15    | N
| 14     | 0000 1110 | 0E  | 16    | O
| 15     | 0000 1111 | 0F  | 17    | P
| 16     | 0001 0000 | 10  | 20    | Q
| 17     | 0001 0001 | 11  | 21    | R

You can convert one number to another using `parseInt(value, base)`, where value is either a string or a decimal number and base is a number between 1 and 36.

    var b = parseInt("11", 2)   // b == 3
    var o = parseInt("11", 8)   // o == 9
    var d = parseInt("11", 10)  // d == 11
    var h = parseInt("11", 16)  // h == 17
    var x = parseInt("11", 36)  // x == 37

## Writing Numbers

JavaScript assumes your writing numbers in base 10, however if you need to write numbers from other systems you can do so using a prefix. 0b for decimal, 0 for octal, 0x for hex. No matter how you write a number, it will be internally stored as binary and printed out as decimal.

## Binary Math

Binary math works much like normal math. You carry ones and solve the number

      0011  //3
    + 0101  //5
    ------
      1000
    
        1   //carry    1   //carry    1    //carry
      0011  //3       0011 //3        0011 //3        0011 //3
    + 0101  //5     + 0101 //5      + 0101 //5      + 0101 //5
    ------          ------          ------          ------
      ...0            ..00            .000            1000
      

### AND - &

| left  | right | Result |
| ----- | ----- | ------ |
| 0 | 0 | 0  |
| 0 | 1 | 0  |
| 1 | 0 | 0  |
| 1 | 1 | 1  |

**NOTE**: Result is only 1 if both left and right is 1, which can be used to clear values.

Another way to look at the same table is:

| Set  | Data | Result |
| ---- | ---- | ------ |
| 0 | 0 | 0  |
| 0 | 1 | 0  |
| 1 | 0 | 0  |
| 1 | 1 | 1  |

If you set the flag to 0, the result is always 0.

### OR - |

| left  | right | Result |
| ----- | ----- | ------ |
| 0 | 0 | 0  |
| 0 | 1  | 1   |
| 1  | 0 | 1   |
| 1  | 1  | 1   |

**NOTE**: Result is only true if either left and right is true, which can be used to set values.

Another way to look at the same table is:

| Set | Data | Result |
| --- | ---- | ------ |
| 0 | 0 | 0  |
| 0 | 1 | 1  |
| 1 | 0 | 1  |
| 1 | 1 | 1  |

If you set the flag, the result is always 1

### XOR - ^

| left  | right | Result |
| ----- | ----- | ------ |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**NOTE**: Result is true only if left and right is different.

## Math

In computers, all math happens at the binary level. Lets look at our new math operators and one of our old ones:

      0011 //3    0011 //3    0011 //3    0011 //3
    & 0101 //5  | 0101 //5  ^ 0101 //5  + 0101 //5
    ------      ------      ------      ------
      0001 //1    0111 //7    0110 //6    1000 //8

* `1 == 3 & 5`
* `7 == 3 | 5`
* `6 == 3 ^ 5`
* `8 == 3 + 5`*

---
* [previous](a-operators.md)
* [next]()
