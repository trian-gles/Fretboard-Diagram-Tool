import tkinter as tk

main_window = tk.Tk()
app_name = tk.Label(text="Guitar fret chart builder", width=30)
app_name.pack()
title_label = tk.Label(text="Page Title:")
title_label.pack()
title = tk.Entry()
title.pack()
window = tk.Frame(master=main_window)

class FretboxBuilder:
    def __init__(self, grid):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            height=3,
            borderwidth=1
        )
        frame.grid(column=grid[0], row=grid[1])
        self.box_title = tk.Entry(master=frame)
        self.box_title.pack()
        inner_frame = tk.Frame(master=frame)
        inner_frame.pack()
        self.check_vars = {}
        self.fret_entries = []
        for j in range(5):
            fret_label = tk.Entry(master=inner_frame, width=2)
            fret_label.grid(column=0, row=j)
            self.fret_entries.append(fret_label)
            for i in range(6):
                self.check_vars[(i, j)] = tk.IntVar()
                tk.Checkbutton(master=inner_frame, variable=self.check_vars[(i, j)]).grid(column=i + 1, row=j)

    def return_content(self):
        content_dict = {}
        checks = filter(lambda box: self.check_vars[box].get() == 1, self.check_vars.keys())
        content_dict['checked_spots'] = list(checks)
        content_dict['name'] = self.box_title.get()
        fret_nums = map(lambda fret: fret.get(), self.fret_entries)
        content_dict['fret_nums'] = list(fret_nums)
        return content_dict

fretboxes = []
for i in range(3):
    for j in range(3):
        fretboxes.append(FretboxBuilder((i, j)))

def print_boxes():
    import draw_diagram
    fretbox_details = [fretbox.return_content() for fretbox in fretboxes]
    title_str = title.get()
    #print(fretbox_details)
    window.destroy()
    draw_diagram.main(title_str, fretbox_details)
    exit()

window.pack()
button = tk.Button(master=main_window, command=print_boxes, text="Render").pack()
main_window.mainloop()