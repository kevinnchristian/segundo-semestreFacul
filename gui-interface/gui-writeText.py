from tkinter import Tk, Text, BOTH

def key_pressed(event):
    print('Char: {}'.format(event.keysym))

def mouse_cliked_left(event):
    print('Mouse left clicked')

def mouse_cliked_right(event):
    print('Mouse right clicked')

root = Tk()

text = Text(root, width=30, height=15)
text.bind('<KeyPress>', key_pressed)
text.bind('<Button-1>', mouse_cliked_left)
text.bind('<Button-3>', mouse_cliked_right)
text.pack(expand=True, fill=BOTH)

root.mainloop()