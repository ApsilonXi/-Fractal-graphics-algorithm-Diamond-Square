from random import uniform
from mayavi.mlab import *
from tkinter import messagebox, Label, Frame, Entry, Button, Tk, Checkbutton, BooleanVar
import vtk
vtk.vtkObject.GlobalWarningDisplayOff()

def diamond_step(half, mapp, chunk, mass, roughness):
    for y in range(0, mass-1, chunk):
        for x in range(0, mass-1, chunk):
            mapp[y+half][x+half] = round((mapp[y][x] + mapp[y][x+chunk] + mapp[y+chunk][x] + mapp[y+chunk][x+chunk]) / 4, 5) + round(uniform(-roughness, roughness), 5)
    return mapp

def square_step(half, mapp, chunk, mass, roughness):
    for y in range(0, mass, half):
        for x in range((y+half)%chunk, mass, chunk):
            try:
                mapp[y][x] = round((mapp[y-half][x] + mapp[y][x-half] + mapp[y][x+half] + mapp[y+half][x]) / 4, 5) + round(uniform(-roughness, roughness), 5)
            except IndexError:
                if (y > 0) and (y < mass-1):
                    mapp[y][x] = round((mapp[y-half][x] + mapp[y][x-half] + mapp[y+half][x]) / 3, 5) + round(uniform(-roughness, roughness), 5)
                elif y == mass-1:
                    mapp[y][x] = round((mapp[y-half][x] + mapp[y][x-half] + mapp[y][x+half]) / 3, 5) + round(uniform(-roughness, roughness), 5)
    return mapp

def DiamondSquare():
    n = str(input_n.get())
    roughness = str(input_roughness.get())
    d = str(input_D.get())
    if n == '' or n.find(',') != -1 or n.find('.') != -1:
        messagebox.showerror("Ошибка!", "Пожалуйста, введите корректную степень размера массива!")
        return 0
    else:
        n = int(n)
    if roughness != "" and roughness.find('-') == -1 and roughness.find('/') == -1:
        if roughness.find(",") != -1:
            roughness = float(roughness.replace(",", "."))
        else:
            roughness = float(roughness)
    else: 
        messagebox.showerror("Ошибка!", "Пожалуйста, введите корректный фактор неровности!")
        return 0
    if d == '' or d.find('.') != -1 or d.find(',') != -1 or d.find('-') != -1 or int(d[0]) < 2 or int(d[0]) > 3:
            messagebox.showerror("Ошибка!", "Пожалуйста, введите корректную размерность результата!")
            return 0

    mass = 2**n + 1
    chunk = mass-1
    iter = 0
    mapp = [[0 for j in range(mass)] for i in range(mass)]
    mapp[0][0] = round(uniform(-roughness, roughness), 5)
    mapp[0][mass-1] = round(uniform(-roughness, roughness), 5)
    mapp[mass-1][0] = round(uniform(-roughness, roughness), 5)
    mapp[mass-1][mass-1] = round(uniform(-roughness, roughness), 5)
    while chunk > 1:
        iter += 1
        r = roughness**iter
        half = chunk//2
        diamond_step(half, mapp, chunk, mass, r)
        square_step(half, mapp, chunk, mass, r)
        chunk //= 2
    for i in range(mass):
        for j in range(mass):
            mapp[i][j] = round(mapp[i][j], 5)

    figure(size=(800,800))
    if d[0] == '2':
        imshow(mapp, colormap = 'terrain')
        bar = colorbar(orientation='horizontal', nb_labels=10) 
        bar.data_range = (-0.2, 1.0)
    elif d[0] == '3':
        ch = check.get()
        if ch == 1:
            for i in range(mass):
                for j in range(mass):
                    if mapp[i][j] < 0:
                        mapp[i][j] = 0.0
        surf(mapp, colormap = 'terrain', warp_scale = 'auto')
        bar = colorbar(orientation='horizontal', nb_labels=10) 
        bar.data_range = (-0.2, 1.0)

window = Tk()
window.title("Diamond-Square")
window.geometry('600x300')
frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

n_txt = Label(frame, text="Cтепень двумерного массива: ")
n_txt.grid(row=2, column=1)
roughness_txt = Label(frame, text='Фактор неровности ландщафта: ')
roughness_txt.grid(row=3, column=1)
D_txt = Label(frame, text='Размерность результата: ')
D_txt.grid(row=4, column=1)

input_n = Entry(frame)
input_n.grid(row=2, column=2, pady=5)
input_roughness = Entry(frame)
input_roughness.grid(row=3, column=2, pady=5)
input_D = Entry(frame)
input_D.grid(row=4, column=2, pady=5)

start_btn = Button(frame, text='Построить ландшафт', command=DiamondSquare)
start_btn.grid(row=6, column=2)
exit_btn = Button(frame, text="Завершить работу", command=quit)
exit_btn.grid(row=7, column=2)
check = BooleanVar()
check.set(0)
ch_btn = Checkbutton(frame, text='Водная гладь', onvalue=1, offvalue=0, variable=check)
ch_btn.grid(row=5, column=1)
window.mainloop()



