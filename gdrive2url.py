#!/usr/bin/python3

# A Simple GUI way to Convert Goggle Drive Url's to ready to Download files :) 
#code by nikkpap @ 2018 for Techmesh.gr
#https://www.facebook.com/techmesh.gr/

import sys

if sys.version_info[0] == 3:
    # for Python3
    from tkinter import * 
    from tkinter import ttk  ## notice lowercase 't' in tkinter here
else:
    # for Python2
    from Tkinter import * 
    import ttk  ## notice capitalized T in Tkinter

def converterUrl():
    try:
        get_url = oem_url.get()
        url1,url2 = get_url.split("=")
        conv_url.set("https://drive.google.com/uc?export=download&id=" + url2)
    except ValueError:
        pass


#gui
window_gdrive = Tk()
window_gdrive.title("Google Drive Direct Download URL Maker v0.2")

frame_gdrive = ttk.Frame(window_gdrive, padding="3 3 12 12")
frame_gdrive.grid(column=0, row=0, sticky=(N, W, E, S))
window_gdrive.columnconfigure(0, weight=1)
window_gdrive.rowconfigure(0, weight=1)

#vars
oem_url = StringVar()
conv_url = StringVar()

#textbox oem
oem_url_entry_gdrive = ttk.Entry(frame_gdrive, width=70, textvariable=oem_url)
oem_url_entry_gdrive.grid(column=2, row=1, sticky=(W, E))
#textbox converted
conv_url_entry = ttk.Entry(frame_gdrive, width=70, textvariable=conv_url)
conv_url_entry.grid(column=2, row=2, sticky=(W, E))
#botton convert
ttk.Button(frame_gdrive, text="Convert", command=converterUrl).grid(column=3, row=4, sticky=W)
#labels of text boxes
ttk.Label(frame_gdrive, text="Original Url").grid(column=1, row=1, sticky=E)
ttk.Label(frame_gdrive, text="Converted Url").grid(column=1, row=2, sticky=E)
ttk.Label(frame_gdrive, text="by nikkpap").grid(column=3, row=2, sticky=W)

for child in frame_gdrive.winfo_children(): child.grid_configure(padx=5, pady=5)

oem_url_entry_gdrive.focus()
window_gdrive.bind('<Return>', converterUrl)

def oem_url_entry_gdrive_mark(event):
    oem_url_entry_gdrive.selection_range(0, END)

def conv_url_entry_mark(event):
    conv_url_entry.selection_range(0, END)

oem_url_entry_gdrive.bind("<FocusIn>", oem_url_entry_gdrive_mark)
conv_url_entry.bind("<FocusIn>", conv_url_entry_mark)

window_gdrive.mainloop()