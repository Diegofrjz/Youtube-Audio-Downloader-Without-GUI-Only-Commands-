import os
from pytube import YouTube

# Ingresa la URL del video de YouTube
video_url = input('Ingresa el enlace del video de YouTube: ')

# Ingresa la ubicación donde quiere guardar el archivo de audio
audio_path = input('Ingresa la ubicación donde quieres guardar el archivo de audio (incluyendo el nombre de archivo): ')

# Descarga el video y extrae el audio en formato mp3
yt = YouTube(video_url)
audio = yt.streams \
    .filter(only_audio=True, file_extension='mp4') \
    .order_by('abr') \
    .desc() \
    .first()

if audio:
    output_file = audio.download(output_path='/tmp')
    base, ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file, new_file)
    os.replace(new_file, audio_path)
    print('Audio descargado en', audio_path)
else:
    print('No se encontró ningún audio en formato mp3 en el video.')
