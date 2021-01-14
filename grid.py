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
        frame.grid(row=grid[0], column=grid[1])
        label = tk.Label(master=frame, text=f"row={grid[0]}\ncolumn={grid[1]}")
        label.pack()
        inner_frame = tk.Frame(master=frame)
        inner_frame.pack()
        self.check_vars = {}
        for i in range(6):
            for j in range(6):
                self.check_vars[(i, j)] = tk.IntVar()
                tk.Checkbutton(master=inner_frame, variable=self.check_vars[(i, j)]).grid(row=i, column=j)

    def return_list(self):
        checked_spots = filter(lambda box: self.check_vars[box].get() == 1, self.check_vars.keys())
        return list(checked_spots)

fretboxes = []
for i in range(3):
    for j in range(3):
        fretboxes.append(FretboxBuilder((i, j)))

def print_boxes():
    window.destroy()
    import draw_diagram
    chord_fing_pairs = [fretbox.return_list() for fretbox in fretboxes]
    title_str = title.get()
    for fretbox in fretboxes:
        print(fretbox.return_list())
    draw_diagram.main(title_str, chord_fing_pairs)
    exit()

window.pack()
button = tk.Button(master=main_window, command=print_boxes).pack()
main_window.mainloop()
