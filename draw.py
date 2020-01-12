import inspect


class WrongInput(Exception):
    pass


def create_canvas(x, y):
    if x < 0 or y < 0:
        raise IndexError
    canvas.clear()
    output_file = open('output.txt', 'w')
    canvas.append('-' * int(x + 2) + '\n')
    for vertical_border in range(y):
        canvas.append('|' + ' ' * x + '|\n')
    canvas.append('-' * int(x + 2) + '\n')
    output_file.writelines(canvas)
    output_file.close()


def draw_line(x1, y1, x2, y2):
    input_tuple_x = (x1, x2)
    input_tuple_y = (y1, y2)
    for z in input_tuple_x:
        if z < 1 or z > len(canvas[0]) - 3:
            raise IndexError
    for z in input_tuple_y:
        if z < 1 or z > len(canvas) - 2:
            raise IndexError
    if x1 == x2 or y1 == y2:
        output_file = open('output.txt', 'a')
        if inspect.stack()[1][3] != 'draw_rectangle':
            output_file.write(canvas[0])
        for vertical_line in range(len(canvas) - 2):
            if vertical_line + 1 == min(y1, y2):
                if x1 == x2:
                    for x in range(abs(y1 - y2) + 1):
                        id_line = vertical_line + 1 + x
                        line = list(canvas[id_line])
                        line[x1] = 'x'
                        canvas[id_line] = ''.join(line)
                if y1 == y2:
                    print_list = list(canvas[vertical_line + 1])
                    print_list[min(x1, x2): max(x1, x2) + 1] = list('x' * int(abs(x1 - x2) + 1))
                    canvas[vertical_line + 1] = ''.join(print_list)
            if inspect.stack()[1][3] != 'draw_rectangle':
                output_file.write(canvas[vertical_line + 1])
        if inspect.stack()[1][3] != 'draw_rectangle':
            output_file.write(canvas[-1])
        output_file.close()
    else:
        raise IndexError


def draw_rectangle(x1, y1, x2, y2):
    first_line = [x1, y1, x2, y1]
    second_line = [x1, y1, x1, y2]
    third_line = [x2, y1, x2, y2]
    fourth_line = [x2, y2, x1, y2]
    draw_line(*first_line)
    draw_line(*second_line)
    draw_line(*third_line)
    draw_line(*fourth_line)
    output_file = open('output.txt', 'a')
    output_file.writelines(canvas)
    output_file.close()


def fill_bucket(x, y, symbol):
    if x < 1 or x > len(canvas[0]) - 3:
            raise IndexError
    if y < 1 or y > len(canvas) - 2:
            raise IndexError
    if len(symbol) > 1:
        raise IndexError
    canvas_list = []
    for row in canvas:
        canvas_list.append(list(row))
    canvas_list = fill(y, x, symbol, canvas_list)
    for row_list in range(len(canvas_list)):
        canvas[row_list] = ''.join(canvas_list[row_list])
    output_file = open('output.txt', 'a')
    output_file.writelines(canvas)
    output_file.close()


def fill(x_alt, y_alt, symbol_alt, can):
    if can[x_alt][y_alt] != symbol_alt and can[x_alt][y_alt] != 'x'\
            and can[x_alt][y_alt] != '|' and can[x_alt][y_alt] != '-':
        can[x_alt][y_alt] = symbol_alt
        can = fill(x_alt + 1, y_alt, symbol_alt, can)
        can = fill(x_alt - 1, y_alt, symbol_alt, can)
        can = fill(x_alt, y_alt + 1, symbol_alt, can)
        can = fill(x_alt, y_alt - 1, symbol_alt, can)
    return can


canvas = []
if __name__ == '__main__':
    input_file = open('input.txt', 'r')
    input_file = input_file.readlines()
    canvas_created = 0
    for lines in input_file:
        if len(lines.split()[0]) != 1:
            raise WrongInput("Can't execute command {0}".format(lines))
        if lines.startswith('C'):
            canvas_created += 1
            create_canvas(int(lines.split()[1]), int(lines.split()[2]))
        elif lines.startswith('L') and canvas_created:
            draw_line(int(lines.split()[1]), int(lines.split()[2]), int(lines.split()[3]), int(lines.split()[4]))
        elif lines.startswith('R') and canvas_created:
            draw_rectangle(int(lines.split()[1]), int(lines.split()[2]), int(lines.split()[3]), int(lines.split()[4]))
        elif lines.startswith('B') and canvas_created:
            fill_bucket(int(lines.split()[1]), int(lines.split()[2]), lines.split()[3])
        else:
            raise WrongInput("Can't execute command {0}".format(lines))
