This is for you swashbuckling eyepatchers who read manga off of mangakatana.com
I'm also a swashbuckling eyepatcher so I made this python script that "stitches" pages together (as they are all seperate images) into a pdf

How to use with easygui:
  1. pip install all of the stuff (pypdf, os, img2pdf, PIL, and easygui (obviously))
  2. Extract manga into any directory
     IMPORTANT: Make sure all chapter subdirectories only have images you want to be stitched
  6. Download (if you haven't) and run mgstgui.pyw
  7. It'll ask you which folder to stitch (whichever one has the chapter subdirectories in it)
  8. Then which chapters are in the folder (or which ones you want to stitch)
     IMPORTANT: You have to do the actual chapter numbers, I know mangakatana lets you download chapters in groups of ten, but this program gets the absolute chapter numbers
  10. Then if it completed successfully it'll tell you

How to use non easygui:
  1. pip install all of the stuff (pypdf, os, img2pdf, and PIL)
  2. Extract manga into same directory as mgst.py
  3. Make sure directories are like this:
     whatever/mgst.py and whatever/manga/c001 (ex. c001 for chapter 1)
     IMPORTANT: Make sure all chapter subdirectories only have images you want to be stitched
  4. Download (if you haven't) and run mgst.py
  5. It'll ask you which folder to stitch (do the manga root folder (whatever/manga in my example))
  6. Then which chapters are in the folder (or which ones you want to stitch) (For example, 1,5 for chapters 1-5 in the manga folder)
     IMPORTANT: You have to do the actual chapter numbers, I know mangakatana lets you download chapters in groups of ten, but this program gets the absolute chapter numbers
  7. Then if it completed successfully it'll tell you
