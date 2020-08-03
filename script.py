import json,os
from PIL import Image
from moviepy.editor import VideoFileClip, TextClip,CompositeVideoClip
from django.utils.crypto import *


def proccess():
    # ON OBTIENS LA VIDEO DE CETTE FAÇON
    video_brute = VIDEO PATH
    # ON RECUPERE DE LE NOM ORIGINAL DE LA VIDEO
    nom_brute = video_brute.name
    # ON RECUPERE L'EXTENSION DE LA VIDEO (mp4, mov...)
    extension = nom_brute.split(".")[-1]
    # ON GENERE UN NOM ALEATOIRE POUR NOTRE VIDEO AVEC LA FONCTION GET_RANDOM_STRING
    nom1 = get_random_string(10, 'abcd012opqrs3456jklmn789efghi')
    # ON TRAITE LA VIDEO AVEC LA BIBLIOTHEQUE MOVIEPY
    video_traitee = VideoFileClip(video_a_traiter.video.path)
    # ON GENERE UNE MINIATURE POUR NOTRE VIDEO    
    miniature = video_traitee.save_frame('NOM DU FICHIER' +".png", t=5)
    # ON OBTIENS LA LARGEUR, LA HAUTEUR ET LA DUREE DE NOTRE FICHIER VIDEO
    largeur = video_traitee.w
    hauteur = video_traitee.h
    duree = video_traitee.duration
    # ON PREPARE DU TEXTE A AJOUTER SUR NOTRE VIDEO, ON SPECIFIE LA POSITION ET LA DUREE D'APPARITION DU TEXTE
    texte = TextClip("HYACINTHE KOUADIO",fontsize=20,color='white')
    texte = texte.set_pos('top').set_duration(7)
    # ON FAIS LA COMPOSITION DE NOTRE TEXTE AVEC LA VIDEO 
    video_compressee = CompositeVideoClip([video_traitee, texte])
    # ENFIN ON COMPRESSE LA VIDEO EN UN AUTRE FORMAT (webm)
    video_compressee.write_videofile("compress.webm")





