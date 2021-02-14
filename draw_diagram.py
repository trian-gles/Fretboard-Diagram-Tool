from graphics import Point, Rectangle, Circle, Text, GraphWin, Line

INCH = 75

WIDTH = INCH * 17 / 2
HEIGHT = INCH * 11
FRET_HEIGHT = INCH / 2

ORIGIN = Point(INCH, INCH)
END_POINT = Point(WIDTH - INCH, HEIGHT - INCH)
MARGIN = Rectangle(ORIGIN, END_POINT)




class FretBox():
    def __init__(self, origin, frets):
        end_point = origin.clone()
        self.frets = frets
        self.origin = origin
        self.width = int(INCH * 1.5)
        height = int(FRET_HEIGHT * frets)
        end_point.move(self.width, height)
        self.rect = Rectangle(origin, end_point)

        #draw vertical lines
        self.lines = []
        for i in range(1, 5):
            x_val = origin.x + int(i * self.width / 5)
            line_or = Point(x_val, origin.y)
            line_end = Point(x_val, end_point.y)
            self.lines.append(Line(line_or, line_end))

        #draw horizontal lines
        for i in range(1, frets):
            y_val = origin.y + int(i * FRET_HEIGHT)
            line_or = Point(origin.x, y_val)
            line_end = Point(end_point.x, y_val)
            self.lines.append(Line(line_or, line_end))

    def draw(self, win):
        self.rect.draw(win)
        for line in self.lines:
            line.draw(win)

    def draw_finger(self, win, fret):
        fing_x = self.origin.x + int(fret[0] * self.width / 5)
        fing_y = self.origin.y + int(fret[1] * FRET_HEIGHT + FRET_HEIGHT / 2)
        finger = Circle(Point(fing_x, fing_y), 8)
        finger.draw(win)
        finger.setFill("black")

    def draw_name(self, win, name):
        name_point = Point(self.origin.x + (self.width / 2), self.origin.y - .2 * INCH)
        name_text = Text(name_point, name)
        name_text.draw(win)

    def draw_fretnums(self, win, fretnums):
        for i in range(len(fretnums)):
            point_x = self.origin.x - .2 * INCH
            point_y = self.origin.y + int(i * FRET_HEIGHT + FRET_HEIGHT / 2)
            num_point = Point(point_x, point_y)
            num_text = Text(num_point, fretnums[i])
            num_text.draw(win)


def main_box(title, content):
    win = GraphWin("Sheet", WIDTH, HEIGHT)
    title_text = Text(Point(WIDTH / 2, ORIGIN.y), title)
    title_text.draw(win)
    fretboxes = []
    chord_num = 0
    for i in range(3):
        for j in range(3):
            x_or = ORIGIN.x + int(INCH * i * 2.5)
            y_or = ORIGIN.y + INCH / 2 + int(INCH * j * 3)
            fretbox = FretBox(Point(x_or, y_or), 5)
            fretbox.draw(win)
            for finger in content[chord_num]['checked_spots']:
                print(f"Finger at {finger} in chord {chord_num}")
                fretbox.draw_finger(win, finger)
            fretbox.draw_name(win, content[chord_num]['name'])
            fretbox.draw_fretnums(win, content[chord_num]['fret_nums'])
            chord_num += 1
    #MARGIN.draw(win)
    click = win.getMouse()
    win.postscript(file=f"{title}.eps", colormode="color")
    win.close()

def main_full(title, content):
    win = GraphWin("Sheet", WIDTH, HEIGHT)
    title_text = Text(Point(WIDTH / 2, ORIGIN.y), title)
    title_text.draw(win)
    fretboxes = []
    chord_num = 0
    for i in range(3):
        x_or = ORIGIN.x + int(INCH * i * 2.5)
        y_or = ORIGIN.y + INCH / 2
        fretbox = FretBox(Point(x_or, y_or), 15)
        fretbox.draw(win)
        for finger in content[chord_num]['checked_spots']:
            fretbox.draw_finger(win, finger)
        fretbox.draw_name(win, content[chord_num]['name'])
        fret_nums = ['', '', '3', '', '5', '', '7', '', '9', '', '', '12', '', '', '15']
        fretbox.draw_fretnums(win, fret_nums)
        chord_num += 1
    #MARGIN.draw(win)
#    click = win.getMouse()
    win.postscript(file=f"{title}.eps", colormode="color")
    win.close()

if __name__ == "__main__":
    TITLE = "TEST"

    test_boxes = [{'checked_spots': [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 4)],
    'name': '(0,0)', 'fret_nums': ['1', '2', '3', '4','5']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']},
    {'checked_spots': [], 'name': '(1,2)', 'fret_nums': ['', '', '', '', '']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']}]
    #main_box(TITLE, test_boxes)
    test_full = [{'checked_spots': [(0, 0), (1, 1), (2, 2), (3, 3), (4, 10), (5, 4)],
    'name': '(0,0)', 'fret_nums': ['1', '2', '3', '4','5', '6']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']},
    {'checked_spots': [], 'name': '', 'fret_nums': ['', '', '', '', '']}]

    main_full(TITLE, test_full)
