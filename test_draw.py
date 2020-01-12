import unittest
import draw


class TestCanvas(unittest.TestCase):
    def setUp(self):
        self.canvas_txt = []

    def test_canvas_creation_where_horizontal_is_longer(self):
        """
        Test of creation of canvas where horizontal line is longer than vertical
        """
        self.canvas_txt = []
        self.canvas_txt.append('-' * 12)
        for x in range(5):
            self.canvas_txt.append('|' + ' ' * 10 + '|')
        self.canvas_txt.append('-' * 12 + '')
        draw.create_canvas(10, 5)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        for row in range(len(self.canvas_txt)):
            with self.subTest(row=row):
                self.assertEqual(output_read[row].rstrip(), self.canvas_txt[row], '{0} must be equal {1}'.format(
                    output_read[row], self.canvas_txt[row]))

    def test_canvas_creation_where_vertical_is_longer(self):
        """
        Test of creation of canvas where vertical line is longer than horizontal
        """
        self.canvas_txt = []
        self.canvas_txt.append('-' * 7)
        for x in range(10):
            self.canvas_txt.append('|' + ' ' * 5 + '|')
        self.canvas_txt.append('-' * 7 + '')
        draw.create_canvas(5, 10)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        for row in range(len(self.canvas_txt)):
            with self.subTest(row=row):
                self.assertEqual(output_read[row].rstrip(), self.canvas_txt[row], '{0} must be equal {1}'.format(
                    output_read[row], self.canvas_txt[row]))

    def test_canvas_creation_with_equal_sides(self):
        """
        Test of creation of canvas where with equal sides
        """
        self.canvas_txt = []
        self.canvas_txt.append('-' * 7)
        for x in range(5):
            self.canvas_txt.append('|' + ' ' * 5 + '|')
        self.canvas_txt.append('-' * 7 + '')
        draw.create_canvas(5, 5)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        for row in range(len(self.canvas_txt)):
            with self.subTest(row=row):
                self.assertEqual(output_read[row].rstrip(), self.canvas_txt[row], '{0} must be equal {1}'.format(
                    output_read[row], self.canvas_txt[row]))

    def test_canvas_creation_with_negative_horizontal_line(self):
        """
        Test of creation of canvas where horizontal line is negative
        """
        with self.assertRaises(IndexError):
            draw.create_canvas(-5, 10)

    def test_canvas_creation_with_negative_vertical_line(self):
        """
        Test of creation of canvas where vertical line is negative
        """
        with self.assertRaises(IndexError):
            draw.create_canvas(10, -5)

    def test_canvas_creation_with_both_lines_negative(self):
        """
        Test of creation of canvas where both lines are negative
        """
        with self.assertRaises(IndexError):
            draw.create_canvas(-5, -5)

    def test_canvas_creation_zero_by_zero(self):
        """
        Test of creation of canvas where both lines are 0
        """
        draw.create_canvas(0, 0)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        for row in range(2):
            with self.subTest(row=row):
                self.assertEqual(output_read[row].rstrip(), '--', 'canvas 0 by 0 should look  like\n--\n--')


class TestDrawLine(unittest.TestCase):
    def setUp(self):
        """
        Creates canvas for drawing
        """
        draw.create_canvas(10, 10)

    def test_draw_horizontal_line(self):
        """
        Test drawing horizontal line
        """
        draw.draw_line(2, 2, 8, 2)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        self.assertEqual(output_read[14][2:9], 'xxxxxxx', '{0} must be | xxxxxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[14][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[14][9], ' ', 'line must end at 8')

    def test_draw_horizontal_line_from_back(self):
        """
        Test drawing horizontal line backwards
        """
        draw.draw_line(8, 2, 2, 2)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        self.assertEqual(output_read[14][2:9], 'xxxxxxx', '{0} must be | xxxxxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[14][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[14][9], ' ', 'line must end at 8')

    def test_draw_vertical_line(self):
        """
        Test drawing vertical line
        """
        draw.draw_line(2, 2, 2, 8)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        vertical_line = []
        for x in range(14, 21):
            vertical_line.append(output_read[x][2])
        vertical_line = ''.join(vertical_line)
        self.assertEqual(vertical_line, 'xxxxxxx', '{0} must be "xxxxxxx"'.format(vertical_line))
        self.assertEqual(output_read[13][2], ' ', 'line must start below')
        self.assertEqual(output_read[21][2], ' ', 'line must end above')

    def test_draw_vertical_line_from_back(self):
        """
        Test drawing vertical line backwards
        """
        draw.draw_line(2, 8, 2, 2)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        vertical_line = []
        for x in range(14, 21):
            vertical_line.append(output_read[x][2])
        vertical_line = ''.join(vertical_line)
        self.assertEqual(vertical_line, 'xxxxxxx', '{0} must be "xxxxxxx"'.format(vertical_line))
        self.assertEqual(output_read[13][2], ' ', 'line must start below')
        self.assertEqual(output_read[21][2], ' ', 'line must end above')

    def test_draw_crossing_lines(self):
        """
        Test if crossing lines draw rightly
        """
        draw.draw_line(2, 4, 8, 4)
        draw.draw_line(2, 2, 2, 8)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        self.assertEqual(output_read[28][2:9], 'xxxxxxx', '{0} must be | xxxxxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[28][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[28][9], ' ', 'line must end at 8')
        vertical_line = []
        for x in range(26, 33):
            vertical_line.append(output_read[x][2])
        vertical_line = ''.join(vertical_line)
        self.assertEqual(vertical_line, 'xxxxxxx', '{0} must be "xxxxxxx"'.format(vertical_line))
        self.assertEqual(output_read[25][2], ' ', 'line must start below')
        self.assertEqual(output_read[33][2], ' ', 'line must end above')

    def test_draw_horizontal_line_out_of_canvas(self):
        """
        Test if horizontal lines can be drawn out of canvas
        """
        with self.assertRaises(IndexError):
            draw.draw_line(0, 1, 5, 1)
            draw.draw_line(5, 1, 11, 1)

    def test_draw_vertical_line_out_of_canvas(self):
        """
        Test if vertical lines can be drawn out of canvas
        """
        with self.assertRaises(IndexError):
            draw.draw_line(5, 0, 5, 5)
            draw.draw_line(5, 5, 5, 11)

    def test_draw_line_with_different_coordinates(self):
        """
        Test if lines can be drawn when coordinates are different
        """
        with self.assertRaises(IndexError):
            draw.draw_line(5, 0, 3, 6)

    def test_draw_line_in_one_pixel(self):
        """
        Test if line can be in one pixel
        """
        draw.draw_line(2, 2, 2, 2)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        line = output_read[14][2]
        self.assertEqual(output_read[14][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[14][3], ' ', 'line must end at 2')
        self.assertEqual(line, 'x', '{0} must be "x"'.format(line))
        self.assertEqual(output_read[13][2], ' ', 'line must start below')
        self.assertEqual(output_read[15][2], ' ', 'line must end above')


class TestDrawRectangle(unittest.TestCase):
    def setUp(self):
        """
        Creates canvas for drawing
        """
        draw.create_canvas(10, 10)

    def test_draw_rectangle_where_horizontal_line_is_longer(self):
        """
        Test drawing rectangle with greater horizontal line
        """
        draw.draw_rectangle(2, 2, 8, 5)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        self.assertEqual(output_read[14][2:9], 'xxxxxxx', '{0} must be | xxxxxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[14][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[14][9], ' ', 'line must end at 8')

        self.assertEqual(output_read[17][2:9], 'xxxxxxx', '{0} must be | xxxxxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[17][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[17][9], ' ', 'line must end at 8')

        vertical_line_2 = []
        vertical_line_1 = []
        for x in range(14, 18):
            vertical_line_1.append(output_read[x][2])
            vertical_line_2.append(output_read[x][8])
        vertical_line_1 = ''.join(vertical_line_1)
        vertical_line_2 = ''.join(vertical_line_2)
        self.assertEqual(vertical_line_1, 'xxxx', '{0} must be "xxxx"'.format(vertical_line_1))
        self.assertEqual(output_read[13][2], ' ', 'line must be below')
        self.assertEqual(output_read[18][2], ' ', 'line must be above')

        self.assertEqual(vertical_line_2, 'xxxx', '{0} must be "xxxx"'.format(vertical_line_2))
        self.assertEqual(output_read[13][8], ' ', 'line must be below')
        self.assertEqual(output_read[18][8], ' ', 'line must be above')

    def test_draw_rectangle_where_vertical_line_is_longer(self):
        """
        Test drawing rectangle with greater vertical line
        """
        draw.draw_rectangle(2, 2, 5, 8)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        self.assertEqual(output_read[14][2:6], 'xxxx', '{0} must be | xxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[14][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[14][6], ' ', 'line must end at 8')

        self.assertEqual(output_read[20][2:6], 'xxxx', '{0} must be | xxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[20][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[20][6], ' ', 'line must end at 8')

        vertical_line_2 = []
        vertical_line_1 = []
        for x in range(14, 21):
            vertical_line_1.append(output_read[x][2])
            vertical_line_2.append(output_read[x][5])
        vertical_line_1 = ''.join(vertical_line_1)
        vertical_line_2 = ''.join(vertical_line_2)
        self.assertEqual(vertical_line_1, 'xxxxxxx', '{0} must be "xxxxxxx"'.format(vertical_line_1))
        self.assertEqual(output_read[13][2], ' ', 'line must be below')
        self.assertEqual(output_read[21][2], ' ', 'line must be above')

        self.assertEqual(vertical_line_2, 'xxxxxxx', '{0} must be "xxxxxxx"'.format(vertical_line_2))
        self.assertEqual(output_read[13][5], ' ', 'line must be below')
        self.assertEqual(output_read[21][5], ' ', 'line must be above')

    def test_draw_rectangle_with_both_sides_equal(self):
        """
        Test drawing square
        """
        draw.draw_rectangle(2, 2, 8, 8)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        self.assertEqual(output_read[14][2:9], 'xxxxxxx', '{0} must be | xxxxxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[14][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[14][9], ' ', 'line must end at 8')

        self.assertEqual(output_read[20][2:9], 'xxxxxxx', '{0} must be | xxxxxxx  |'.format(output_read[14]))
        self.assertEqual(output_read[20][1], ' ', 'line must start from 2')
        self.assertEqual(output_read[20][9], ' ', 'line must end at 8')

        vertical_line_2 = []
        vertical_line_1 = []
        for x in range(14, 21):
            vertical_line_1.append(output_read[x][2])
            vertical_line_2.append(output_read[x][8])
        vertical_line_1 = ''.join(vertical_line_1)
        vertical_line_2 = ''.join(vertical_line_2)
        self.assertEqual(vertical_line_1, 'xxxxxxx', '{0} must be "xxxxxxx"'.format(vertical_line_1))
        self.assertEqual(output_read[13][2], ' ', 'line must be below')
        self.assertEqual(output_read[21][2], ' ', 'line must be above')

        self.assertEqual(vertical_line_2, 'xxxxxxx', '{0} must be "xxxxxxx"'.format(vertical_line_2))
        self.assertEqual(output_read[13][8], ' ', 'line must be below')
        self.assertEqual(output_read[21][8], ' ', 'line must be above')

    def test_draw_rectangle_where_one_point_is_out_of_canvas(self):
        """
        Test drawing rectangle with one point out of canvas
        """
        with self.assertRaises(IndexError):
            draw.draw_rectangle(0, 1, 5, 5)

    def test_draw_rectangle_in_one_pixel(self):
        """
        Test if rectangle can be in one pixel
        """
        draw.draw_rectangle(2, 2, 2, 2)
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output.close()
        rectangle = output_read[14][2]
        self.assertEqual(output_read[14][1], ' ', 'pixel must be clear')
        self.assertEqual(output_read[14][3], ' ', 'pixel must be clear')
        self.assertEqual(rectangle, 'x', '{0} must be "x"'.format(rectangle))
        self.assertEqual(output_read[13][2], ' ', 'pixel must be clear')
        self.assertEqual(output_read[15][2], ' ', 'pixel must be clear')


class TestFill(unittest.TestCase):
    def setUp(self):
        """
        Creates canvas for drawing
        """
        draw.create_canvas(10, 10)

    def test_fill_empty_canvas(self):
        """
        Test filling empty canvas
        """
        draw.fill_bucket(5, 5, '*')
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output_read = output_read[13:-1]
        output.close()
        for row in range(len(output_read)):
            with self.subTest(row=row):
                self.assertEqual(output_read[row][1:-2], '*' * 10, 'Whole canvas should be in *')

    def test_fill_in_rectangle(self):
        """
        Test fill of rectangle
        """
        draw.draw_rectangle(2, 2, 5, 5)
        draw.fill_bucket(3, 3, '*')
        output = open('output.txt', 'r')
        output_read = output.readlines()
        self.assertEqual(output_read[8][8], ' ', 'The rest of field should stay unfilled')
        output_read = output_read[27:29]
        output.close()
        for row in output_read:
            with self.subTest(row=row):
                self.assertEqual(row[3:5], '*' * 2, 'Should be * after fill')
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output_read = output_read[26:30]
        output.close()
        lines_of_rectangle = [output_read[0][2:6], output_read[3][2:6]]
        vertical_line_one = []
        vertical_line_two = []
        for x in range(4):
            vertical_line_one.append(output_read[x][2])
            vertical_line_two.append(output_read[x][5])
        lines_of_rectangle.append(''.join(vertical_line_one))
        lines_of_rectangle.append(''.join(vertical_line_two))
        for x in lines_of_rectangle:
            with self.subTest(x=x):
                self.assertEqual(x, 'x' * 4, 'Lines of rectangle should stay x')

    def test_fill_outside_of_rectangle(self):
        """
        Test fill outside of rectangle
        """
        draw.draw_rectangle(2, 1, 5, 5)
        draw.fill_bucket(1, 1, '*')
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output_read = output_read[25:35]
        output.close()
        self.assertCountEqual(output_read[0][1:-2], 'xxxx******', 'Place outside rectangle should be filled with *')
        for row in range(1, 4):
            self.assertCountEqual(output_read[row][1:-2], 'xx******  ', 'Place inside rectangle should be empty')
        self.assertCountEqual(output_read[4][1:-2], 'xxxx******', 'Place outside rectangle should be filled with *')
        for row in range(5, 10):
            self.assertCountEqual(output_read[row][1:-2], '**********',
                                  'Place outside rectangle should be filled with *')

    def test_fill_outside_canvas(self):
        """
        Test fill outside of canvas
        """
        with self.assertRaises(IndexError):
            draw.fill_bucket(-1, -1, '*')

    def test_fill_where_filled_with_same_symbol(self):
        """
        Test filling the place that already filled with same symbol "*"
        """
        draw.fill_bucket(5, 5, '*')
        draw.fill_bucket(8, 8, '*')
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output_read = output_read[25:-1]
        output.close()
        for row in range(len(output_read)):
            with self.subTest(row=row):
                self.assertEqual(output_read[row][1:-2], '*' * 10, 'Whole canvas should be in *')

    def test_fill_when_filled_with_another_symbol(self):
        """
        Test filling the place that already filled with another symbol
        """
        draw.fill_bucket(5, 5, '*')
        draw.fill_bucket(8, 8, '/')
        output = open('output.txt', 'r')
        output_read = output.readlines()
        output_read = output_read[25:-1]
        output.close()
        for row in range(len(output_read)):
            with self.subTest(row=row):
                self.assertEqual(output_read[row][1:-2], '/' * 10, 'Whole canvas should be in /')


if __name__ == '__main__':
    unittest.main()
