# spygrapher
A spyware that takes screenshots when it finds a given image. Software built for educational purpouses.

DISCLAIMER:
I don't encourge the use of this software as a privacy violation tool. As I already mentionate this is an educational proyect that im creating with the intention of learning how to interact with the OS and automate tasks using Python.

This script was built using Python3 and requires the following modules to work: time, os, pyautogui, pyscreeze, zipfile, opencv-python

When the script is executed 3 folders will be created, to store the screenshots, compressed screenshots and the images to be found.
On the find folder you need to put the images that the program will search on screen, this images needs to be in .png format and their names should not contain spaces or special characters. Example names: my_image_1.png, another-image231.png

Keep in mind that the resolution of the images affects the confidence of the search.
