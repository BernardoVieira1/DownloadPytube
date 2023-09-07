from PySimpleGUI import PySimpleGUI as sg
from pytube import Playlist, YouTube

#layout
sg.theme("DarkGreen4")
layout = [
    [sg.Text("Link do video")],
    [sg.Input(key="linkDownload"), sg.Combo(["Video", "Playlist"], default_value="Video", key="type")],
    [sg.Radio("Somente Áudio","RADIO1",default=True, key="typeMidia")],
    [sg.Radio("Somente Vídeo","RADIO1",default=False)],
    [sg.Text("Onde deseja baixar?")],
    [sg.InputText(key='DirPasta'), sg.FolderBrowse()],
    [sg.Button("Baixar")],
]

#janela no wundows
janela = sg.Window("Baixar videos do YouTube", layout)

#eventos do programa
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Baixar":
        linkDoVideo = valores["linkDownload"]
        typeLink = valores["type"]
        typeMidia = valores["typeMidia"]
        dirPasta = valores["DirPasta"]
        
        if typeLink == "Video":
            if typeMidia:
                YouTube(linkDoVideo).streams.filter(only_audio=True)[0].download(dirPasta)
            else:
                YouTube(linkDoVideo).streams.get_highest_resolution().download(dirPasta)
        else:
            playlist = Playlist(linkDoVideo)
            if typeMidia:
                for url in playlist:
                    YouTube(url).streams.filter(only_audio=True)[0].download(dirPasta)
            else:
                for url in playlist:
                    YouTube(url).streams.get_highest_resolution().download(dirPasta)



