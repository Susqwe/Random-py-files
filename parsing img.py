import os
import glob
import time


while True:
	try:
		for x in glob.glob("C:\\Users\\USER\\Desktop\\GraberScreens\\py2\\*.jpg"):
			statinfo = os.stat(str(x))
			if statinfo.st_size != 5082:
				pass
			else:
				os.remove(x)
				print("Файл: " + str(x) + " успешно удалён")
	except:
		print("Пустых файлов не найдено. Ждём 10 секунд.")
		time.sleep(10)