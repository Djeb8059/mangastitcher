This is for you swashbuckling eyepatchers who read manga off of mangakatana.com
I'm also a swashbuckling eyepatcher so I made this python script that "stitches" pages together (as they are all seperate images) into a pdf

How to use:
  1. pip install all of the stuff (pypdf, os, img2pdf, and PIL)
  2. Extract manga into same directory as mangastitcher python script
  3. Make sure directories are like this:
  4. whatever/mgst.py and whatever/manga/(ex. c001 for chapter 1)
  5. Run mangastitcher
  7. It'll ask you which folder to stitch (do the manga root folder (whatever/manga in my example))
  8. Then which chapters are in the folder (or which ones you want to stitch) (For example, 1,5 for chapters 1-5 in the manga folder) IMPORTANT: You have to do the actual chapter numbers, I know mangakatana lets you download chapters in groups of ten, but this program gets the absolute chapter numbers
  9. It'll then ask you how many images there are in each chapter (For example, if there are 20 images in the 1st chapter, 31 images in the second, and 19 in the third put 20,31,19)
  10. Then if it completed successfully it'll tell you (if it doesn't you screwed up on your part 💀)

too lazy to build exe version but I'll do it someday
