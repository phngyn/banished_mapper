from tkinter import Variable


v_name = '1'
p_name = 1
vnames = [name for name in globals() if globals()[name] is p_name]
print(vnames)