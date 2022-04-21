from calendar import c
from tkinter import *
from tkinter import ttk
from PokiAPI import pokeList, retrieveMonsImage
from library import download_image_from_url, set_desktop_background_image
import os
import sys
import ctypes

def main():

    script_dir = sys.path[0]
    img_dir = os.path.join(script_dir, 'PokePics')
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)


    root = Tk()
    root.title('Pokemon Image Viewer')
    app_id = 'Pokemon.Image.Viewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join(script_dir, 'pokeball.ico'))
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.minsize(500,600)

    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0, weight=10)
    frm.rowconfigure(1, weight=0)
    frm.rowconfigure(2, weight=0)
    frm.columnconfigure(0, weight=1)

    pokeImage = PhotoImage(file=os.path.join(script_dir, 'pokeball.png'))
    imageLabel = ttk.Label(frm, image = pokeImage)
    imageLabel.grid(row=0,column=0,padx=5,pady=5)


    listOfMons = pokeList()
    listOfMons.sort()
    listOfMons = [p.capitalize() for p in listOfMons]


    cbo_pokelist = ttk.Combobox(frm, values=listOfMons, state='readonly')
    cbo_pokelist.set('Select a Pokemon')
    cbo_pokelist.grid(row=1,column=0,padx=5,pady=5)

    def pokeSelect(event):
        pokeName = cbo_pokelist.get()
        image_url = retrieveMonsImage(pokeName)
        img_path = os.path.join(img_dir, pokeName + '.png')
        download_image_from_url(image_url, img_path)
        pokeImage['file'] = img_path
        btn_dsktp.state(['!disabled'])


    cbo_pokelist.bind('<<ComboboxSelected>>',pokeSelect)

    def pokeDesktopImage(event):
        pokeName = cbo_pokelist.get()
        img_path = os.path.join(img_dir, pokeName + '.png')
        set_desktop_background_image(img_path)

    btn_dsktp = ttk.Button(frm, text='Set as Desktop Image', command=pokeDesktopImage)
    btn_dsktp.state(['disabled'])
    btn_dsktp.grid(row=2,column=0,padx=5,pady=5)



    root.mainloop()


main()