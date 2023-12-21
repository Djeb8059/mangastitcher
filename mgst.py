import pypdf, os, img2pdf
from PIL import Image

def cnvrtimg(path, fpath):
    with Image.open(path) as image:
        pdf_bytes = img2pdf.convert(image.filename)
        with open(fpath, "wb") as file:
            file.write(pdf_bytes)

def addzero(num, amount):
    nnum = str(int(num))
    zero = "0" * (amount - len(nnum))
    return zero + nnum

def wrtimgtopdf(imgto):
    with pypdf.PdfWriter as converter:
        converter.add_blank_page(pypdf.PdfReader(imgto).pages[0])
        converter.write("img")

# one inch is 72 pixels ig
inch = 72

rootdir = input("Stitch which folder? ")
chform = input("Chapter format? (ex. '11,20' would mean folders 'c011, c012, ..., c020') ").split(",")
input("Important: All files in chapter subdirectories must be image files")

# makes temporary directory to store pdfs in
os.mkdir("pdftemps")
temps = os.path.dirname(os.path.abspath(__file__)) + "\\pdftemps"

with pypdf.PdfWriter() as writer:

    for ch in range(int(chform[0]), int(chform[1]) + 1):

        for img in range(1, int(imgamount[ch - int(chform[0])]) + 1):
            # defining paths and stuff
            imgpath = os.path.dirname(os.path.abspath(__file__)) + "\\" + rootdir + "\\" + "c" + addzero(ch, 3) + "\\" + addzero(img, 3) + ".jpg"
            temppath = temps + "\\temp.pdf"

            # converting image
            cnvrtimg(imgpath, temppath)
            # appending to output
            writer.append(temppath)
            # removing temporary pdf
            os.remove(temppath)
        
    # writing to file
    with open("output.pdf", "wb") as outFile:
        writer.write(outFile)

# deleting temporary directory
os.removedirs("pdftemps")

input("Operation successfully completed")
