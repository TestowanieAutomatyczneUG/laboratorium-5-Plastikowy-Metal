import unittest

class Piosenka():
    def wersy(a, b = 0):
        song = ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
                 "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."]

class PiosenkaTest(unittest.TestCase):
    def test_1_line_1(self):
        self.assertEqual(Piosenka.wersy(1),
        "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")
    @unittest.skip
    def test_2_line_5(self):
        self.assertEqual(Piosenka.wersy(5),
        "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")
    @unittest.skip
    def test_3_line_12(self):
        self.assertEqual(Piosenka.wersy(5),
        "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")
    @unittest.skip
    def test_4_lines_1_to_4(self):
        self.assertEqual(Piosenka.wersy(1,4),
        ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
         "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."])
    @unittest.skip
    def test_5_lines_6_to_12(self):
        self.assertEqual(Piosenka.wersy(6,12),
                ["On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                 "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."])
    @unittest.skip
    def test_6_all_lines(self):
        self.assertEqual(Piosenka.wersy(1),
        ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
         "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
         "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."])
    @unittest.skip
    def test_7_line_is_out_of_range(self):
        with self.assertRaisesWithMessage(ValueError):
            Piosenka.wersy(15)
    @unittest.skip
    def test_8_first_range_bigger(self):
        with self.assertRaisesWithMessage(ValueError):
            Piosenka.wersy(10,2)
    @unittest.skip
    def test_9_is_int(self):
        with self.assertRaisesWithMessage(ValueError):
            Piosenka.wersy("15")
    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

if __name__ == '__main__':
    unittest.main()
    print(Piosenka.wersy(3))