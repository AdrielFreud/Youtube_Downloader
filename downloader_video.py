# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8

from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
ydl_opts = {}
from Tkinter import *
import os
from PIL import ImageTk,Image

root = Tk()
root.title('Youtube Video Downloader - Adriel')
os.system('color a')
os.system('cls')

main = '''
# Desenvolvido por Adriel Freud / Elder!
# Contato: usuariocargo2016@gmail.com 
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
'''


image3 = Image.open('inforge2.jpg')
image4 = ImageTk.PhotoImage(image3)
label4 = Label(root, image=image4)
label4.pack()
root.iconbitmap('icone.ico')

title = Label(root, text='Youtube Downloader', fg='black', font=('Arial', 21))
title.place(x=170,y=10)

def banner():
	try:
		os.system('cls')
		print(main)
	except:
		pass

def download_video():
	url = entry_url.get()
	if url:
		banner()
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
			print('[=>] Download Terminated!\n')
	else:
		os.system('cls')
		print(main+'\n\n'+'Entre com uma url valida!')

entry_url = Entry(root, width=60, justify='center')
entry_url.insert(0, 'Url do Video!')
entry_url.place(x=120, y=80)
entry_url.focus_set()

button = Button(root, width=40, justify='center', command=download_video, text='Baixar/Download')
button.place(x=160, y=130)

root.geometry('600x250+100+100')
root.mainloop()

