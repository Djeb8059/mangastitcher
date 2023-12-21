import pypdf, os, img2pdf, easygui
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

rootdir = easygui.diropenbox(title="Select the folder your manga's chapters are in | Mangastitcher")
if not rootdir:
    quit()
chform = easygui.multenterbox(title= "Mangastitcher", msg="Which chapters to stitch? (Every chapter in between is stitched, ending chapter included)", fields=["Chapter prefix", "Starting chapter", "Ending chapter"], values=["c", "1", "10"])
if not chform:
    quit()
easygui.msgbox(title="Mangastitcher", msg="Important: All files in each chapter subdirectory must be images")

# makes temporary directory to store pdfs in
os.mkdir("pdftemps")
temps = os.path.dirname(os.path.abspath(__file__)) + "\\pdftemps"

with pypdf.PdfWriter() as writer:

    for ch in range(int(chform[1]), int(chform[2]) + 1):
        chpath = rootdir + "\\" + chform[0] + addzero(ch, 3)
        for img in range(1, len(os.listdir(chpath))):
            # defining paths and stuff
            imgpath = chpath + "\\" + addzero(img, 3) + ".jpg"
            temppath = temps + "\\temp.pdf"

            # converting image
            cnvrtimg(imgpath, temppath)
            # appending to output
            writer.append(temppath)
            # removing temporary pdf
            os.remove(temppath)
        
    # writing to file
    with open(rootdir + "\\output.pdf", "wb") as outFile:
        writer.write(outFile)

# deleting temporary directory
os.removedirs("pdftemps")

easygui.msgbox(msg="Operation completed, written file in chosen folder", title="Mangastitcher")