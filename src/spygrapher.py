import time, os
import pyautogui, pyscreeze
import zipfile

''' Thing to do in order of importance'''

#TODO implement email attachments

class Directories(object):
	__slots__ = ['current' ,'find', 'screenshots', 'compressed']
	def __init__(self):
		self.current = os.path.dirname(os.path.realpath(__file__))
		self.find = os.path.join(self.current, 'find')
		self.screenshots = os.path.join(self.current, 'screenshots')
		self.compressed = os.path.join(self.current, 'compressed')

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
	zip_name = 'images_' + date_time + '.zip'
	zip_file = zipfile.ZipFile(os.path.join(dir.compressed, zip_name), mode='w', compression=zipfile.ZIP_DEFLATED)
	for file in os.listdir(dir.screenshots):
		if file.endswith('.png'):
			zip_file.write(os.path.join(dir.screenshots, file))
	zip_file.close()

def takeScreenshots(amount, interval):
	for i in range(0, amount):
		date_time = getCurrentDateTime()
		screenshot_name = 'image' + str(i + 1) + '_' + date_time + '.png'
		pyautogui.screenshot(os.path.join(dir.screenshots, screenshot_name))
		time.sleep(interval)

def checkFindImages():
	return [file for file in os.listdir(dir.find) if file.endswith('.png')]		

def checkFolders():
	for k in range(0, 3):
		if not os.path.exists(dir.find):
			os.mkdir('find')
		elif not os.path.exists(dir.screenshots):
			os.mkdir('screenshots')
		elif not os.path.exists(dir.compressed):
			os.mkdir('compressed')

if __name__ == '__main__':

	dir = Directories()
	i = 0
	find_images = []
	amount, interval = 10, 3 # takeScreenshots arguments

	checkFolders()

	print('Searching...\n')
	while True:
		try:
			if find_images != checkFindImages():
				find_images = checkFindImages()
				print('New images have been added or substracted from the find folder.\n')
				time.sleep(1)
				print('Searching...\n')
			i = i % len(find_images)
			pyautogui.locateOnScreen(os.path.join(dir.find, find_images[i]), confidence = 0.9)
			print('Image found!')
			print('Taking screenshots, this process will take ' + str(amount*interval) + ' seconds')
			takeScreenshots(amount, interval)
			print('Creating compressed file')
			createZip()
			print('Deleting screenshots')
			deleteImages()
			print('\nSearching...\n')
		except pyscreeze.ImageNotFoundException:
			time.sleep(1)
			i += 1
		except ZeroDivisionError:
			print('The find folder does not containg any image to look for.\n')
			print('Please insert at least one .png in the find folder. The folder has been created in the same directory as this script.')
			while len(find_images) == 0:
				time.sleep(2)
				find_images = checkFindImages()
			print('\n' + str(len(checkFindImages())) + ' image/s found!\n')
			print('Searching...\n')