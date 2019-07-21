#!/usr/bin/python3

import glob
import subprocess


def execConvertSwf(img_velha, img):
    subprocess.call(
        "swfrender "+img_velha+" -r 200 -o convertidas/"+img+".png", shell=True
    )

    msg = img_velha + " => " + img
    print(msg)

def execConvert(img_velha, img):
    subprocess.call(
        "convert -quality 100 -density 300 "+img_velha+" convertidas/"+img, shell=True
    )

    msg = img_velha + " => " + img
    print(msg)

def convertFormatoSwf():

    arquivos_encontrados = glob.glob("*.swf")

    if arquivos_encontrados:
        print("###### Iniciando processo ######")

        for arquivos in arquivos_encontrados:
            novo_formato = arquivos.replace(".swf", ".png")
            nova_img     = novo_formato

            execConvertSwf(arquivos, nova_img)

        print("###### Processo finalizado ######")

    else:
        print("Não encontrei arquivos .swf")


def convertFormato():
    formato_original = input("Qual o formato original?\n")
    formato_final    = input("Qual o novo formato?\n")
    define_prefixo   = input("Deseja inserir um prefixo?\n")

    print("###### Iniciando processo ######")

    if formato_original and formato_final:
        arquivos_encontrados = glob.glob("*." + formato_original)

        for arquivos in arquivos_encontrados:
            novo_formato = arquivos.replace("."+formato_original, "."+formato_final)
            nova_img     = define_prefixo+novo_formato
            
            execConvert(arquivos, nova_img)
            
        print("###### Processo finalizado ######")

def escolheTipo():
    print("Tipo: 1 para [.swf]; 2 para [outros]; 0 para [sair]")
    escolha = input("Qual o tipo de arquivo?\n")

    if len(escolha) > 0:
        if int(escolha) == 1:
            convertFormatoSwf()
        elif int(escolha) == 2:
            convertFormato()
        else:
            print("Nenhum tipo válido foi definido")
    else:
        print("Sem definição.")



if __name__ == "__main__":
    escolheTipo()