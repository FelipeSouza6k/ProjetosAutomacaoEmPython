import PyPDF2
import os

merger = PyPDF2.PdfMerger()

listaArquivos = os.listdir("MezclarPDF/arquivos")
listaArquivos.sort()
print(listaArquivos)

for arquivo in listaArquivos:
    if ".pdf" in arquivo:
        merger.append(f"MezclarPDF/arquivos/{arquivo}")

merger.write("PDF Final.pdf")        