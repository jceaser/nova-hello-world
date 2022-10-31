import unittest

import color

#Calculate a complement color from a supplied 24bit color.
#Copyright 2022. thomas.cherry@gmail.com


class TestColor(unittest.TestCase):

    def test_limits(self):
        ta = lambda give: color.color_limits(give)
        t1 = lambda give, exp, msg: self.assertEqual(exp, ta(give), msg)

        t1(1024, 255, "max")
        t1(255, 255, "highest")
        t1(0, 0, "lowest")
        t1(-128, 0, "min")


    def test_compliment1(self):
        """
        Test that it can sum a list of integers
        """

        data = [1, 2, 3]
        expected = [254, 253, 252]
        result = color.find_compliment(data)
        self.assertEqual(result, expected, "basic")

    def test_compliment2(self):
        """
        Test that it can sum a list of integers
        """
        ta=lambda give: color.find_compliment(give)
        t1=lambda give,exp,msg: self.assertEqual(exp, ta(give), msg)

        t1([255,0,0], [0,255,255], "Just Red")
        t1([0, 255,0], [255,0,255], "Just Green")
        t1([0, 0, 255], [255,255,0], "Just Blue")
        t1([255,255,255], [0,0,0], "White to black")
        t1([128,128,128], [127,127,127], "middle")

    def test_example_line(self):
        ta = lambda give: color.example_line(give)
        t1 = lambda exp,give,msg: self.assertEqual(exp, ta(give), msg)

        c1 = lambda r,g,b: f"\x1b[38;2;{r};{g};{b}m\uee03\uee04\uee05\x1b[00m"
        c2 = lambda r,g,b: f" ({r},{g},{b}) 0x{r:02x}{g:02x}{b:02x}"
        c3 = lambda r,g,b: c1(r,g,b) + c2(r,g,b)
        result = lambda l,r: c3(l[0],l[1],l[2]) + "->" + c3(r[0],r[1],r[2])

        colors1 = [[255,0,0], [0,255,255]]
        expected1 = result(*colors1)
        t1(expected1, colors1[0], "just red")

        colors2 = [[1,1,1],[254,254,254]]
        expected2 = result(*colors2)
        t1(expected2, colors2[0], "mostly black")

if __name__ == '__main__':
    unittest.main()
