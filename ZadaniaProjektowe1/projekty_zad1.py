from PyPDF2 import PdfMerger

def polacz_pliki(pdf1, pdf2, plik_laczony):
    laczenie = PdfMerger()
    
    laczenie.append(pdf1)
    laczenie.append(pdf2)

    laczenie.write(plik_laczony)
    laczenie.close()

if __name__ == "__main__":

    plik1 = 'projekty.pdf'
    plik2 = 'app-prop-pickle.pdf'
    plik1_plik2 = 'plik1_plik2.pdf'
    plik2_plik1 = 'plik2_plik1.pdf'

    polacz_pliki(plik1, plik2, plik1_plik2)
    polacz_pliki(plik2, plik1, plik2_plik1)


