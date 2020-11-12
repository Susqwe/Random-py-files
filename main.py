import sys
#Импорт интерфейса
from college import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QInputDialog, QLineEdit, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from database import *
from Change import *
import random
import os

Auto = Q + '\n' + P1 + '\n' + K1 
Graph = W + '\n' + P2 + '\n' + K2
Fiz = E + '\n' + P3 + '\n' + K3
Model = R + '\n' + P4 + '\n' + K4
Micro = T + '\n' + P5 + '\n' + K5
OOP = Y + '\n' + P6 + '\n' + K6
Chimical = U + '\n' + P7 + '\n' + K7
History = I + '\n' + P8 + '\n' + K8
All_history = O + '\n' + P9 + '\n' + K9
Politic = P + '\n' + P10 + '\n' + K10
Uchet = A + '\n' + P11 + '\n' + K11
Audit = S + '\n' + P12 + '\n' + K12
Culture = D + '\n' + P13 + '\n' + K13
Bio = F + '\n' + P14 + '\n' + K14
Math = G + '\n' + P15 + '\n' + K15
Picture = H + '\n' + P16 + '\n' + K16
Cherch = J + '\n' + P17 + '\n' + K17
Comp = K + '\n' + P18 + '\n' + K18
English = L + '\n' + P19 + '\n' + K19
Kazakh = Z + '\n' + P20 + '\n' + K20
Zhivopis = X + '\n' + P21 + '\n' + K21
Tip = C + '\n' + P22 + '\n' + K22
NVP = V + '\n' + P23 + '\n' + K23
Russian = B + '\n' + P24 + '\n' + K24
Phisic = N + '\n' + P25 + '\n' + K25



class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super().__init__()
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#Событие нажатие кнопки генерации
		self.ui.pushButton.clicked.connect(self.start)
		self.ui.action_3.triggered.connect(self.re)
		self.ui.action_2.triggered.connect(self.exit)
		self.ui.action_4.triggered.connect(self.change)

	@pyqtSlot()


	def change(self):
		self.ui = Ui_MainWindowChange()
		self.ui.setupUiChange(self)
		self.ui.pushButton_2.clicked.connect(self.probitie)
		self.ui.pushButton_2.clicked.connect(self.refresh)
		self.ui.action_3.triggered.connect(self.re)
		self.ui.action_2.triggered.connect(self.exit)
		self.ui.action_4.triggered.connect(self.change)

	def re(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.start)
		self.ui.action_3.triggered.connect(self.re)
		self.ui.action_2.triggered.connect(self.exit)
		self.ui.action_4.triggered.connect(self.change)



	def probitie(self):
		myfile = open('database.py', mode = 'w', encoding='utf8')
		myfile.write('Q = ' + '"' + self.ui.lineEdit.text() + '"' +'\n'
			'W = ' + '"' + self.ui.lineEdit_2.text() + '"' +'\n'
			'E = ' + '"' + self.ui.lineEdit_3.text() + '"' +'\n'
			'R = ' + '"' + self.ui.lineEdit_4.text() + '"' +'\n'
			'T = ' + '"' + self.ui.lineEdit_5.text() + '"' +'\n'
			'Y = ' + '"' + self.ui.lineEdit_6.text() + '"' +'\n'
			'U = ' + '"' + self.ui.lineEdit_7.text() + '"' +'\n'
			'I = ' + '"' + self.ui.lineEdit_8.text() + '"' +'\n'
			'O = ' + '"' + self.ui.lineEdit_9.text() + '"' +'\n'
			'P = ' + '"' + self.ui.lineEdit_10.text() + '"' +'\n'
			'A = ' + '"' + self.ui.lineEdit_11.text() + '"' +'\n'
			'S = ' + '"' + self.ui.lineEdit_12.text() + '"' +'\n'
			'D = ' + '"' + self.ui.lineEdit_13.text() + '"' +'\n'
			'F = ' + '"' + self.ui.lineEdit_14.text() + '"' +'\n'
			'G = ' + '"' + self.ui.lineEdit_15.text() + '"' +'\n'
			'H = ' + '"' + self.ui.lineEdit_16.text() + '"' +'\n'
			'J = ' + '"' + self.ui.lineEdit_17.text() + '"' +'\n'
			'K = ' + '"' + self.ui.lineEdit_18.text() + '"' +'\n'
			'L = ' + '"' + self.ui.lineEdit_19.text() + '"' +'\n'
			'Z = ' + '"' + self.ui.lineEdit_20.text() + '"' +'\n'
			'X = ' + '"' + self.ui.lineEdit_21.text() + '"' +'\n'
			'C = ' + '"' + self.ui.lineEdit_22.text() + '"' +'\n'
			'V = ' + '"' + self.ui.lineEdit_23.text() + '"' +'\n'
			'B = ' + '"' + self.ui.lineEdit_24.text() + '"' +'\n'
			'N = ' + '"' + self.ui.lineEdit_25.text() + '"' +'\n'

			'\n'

			'K1 = ' + '"' + self.ui.lineEdit_26.text() + '"' +'\n'
			'K2 = ' + '"' + self.ui.lineEdit_27.text() + '"' +'\n'
			'K3 = ' + '"' + self.ui.lineEdit_28.text() + '"' +'\n'
			'K4 = ' + '"' + self.ui.lineEdit_29.text() + '"' +'\n'
			'K5 = ' + '"' + self.ui.lineEdit_30.text() + '"' +'\n'
			'K6 = ' + '"' + self.ui.lineEdit_31.text() + '"' +'\n'
			'K7 = ' + '"' + self.ui.lineEdit_32.text() + '"' +'\n'
			'K8 = ' + '"' + self.ui.lineEdit_33.text() + '"' +'\n'
			'K9 = ' + '"' + self.ui.lineEdit_34.text() + '"' +'\n'
			'K10 = ' + '"' + self.ui.lineEdit_35.text() + '"' +'\n'
			'K11 = ' + '"' + self.ui.lineEdit_36.text() + '"' +'\n'
			'K12 = ' + '"' + self.ui.lineEdit_37.text() + '"' +'\n'
			'K13 = ' + '"' + self.ui.lineEdit_38.text() + '"' +'\n'
			'K14 = ' + '"' + self.ui.lineEdit_39.text() + '"' +'\n'
			'K15 = ' + '"' + self.ui.lineEdit_40.text() + '"' +'\n'
			'K16 = ' + '"' + self.ui.lineEdit_41.text() + '"' +'\n'
			'K17 = ' + '"' + self.ui.lineEdit_42.text() + '"' +'\n'
			'K18 = ' + '"' + self.ui.lineEdit_43.text() + '"' +'\n'
			'K19 = ' + '"' + self.ui.lineEdit_44.text() + '"' +'\n'
			'K20 = ' + '"' + self.ui.lineEdit_45.text() + '"' +'\n'
			'K21 = ' + '"' + self.ui.lineEdit_46.text() + '"' +'\n'
			'K22 = ' + '"' + self.ui.lineEdit_47.text() + '"' +'\n'
			'K23 = ' + '"' + self.ui.lineEdit_48.text() + '"' +'\n'
			'K24 = ' + '"' + self.ui.lineEdit_49.text() + '"' +'\n'
			'K25 = ' + '"' + self.ui.lineEdit_50.text() + '"' +'\n'

			'\n'

			'P1 = ' + '"' + self.ui.lineEdit_51.text() + '"' +'\n'
			'P2 = ' + '"' + self.ui.lineEdit_52.text() + '"' +'\n'
			'P3 = ' + '"' + self.ui.lineEdit_53.text() + '"' +'\n'
			'P4 = ' + '"' + self.ui.lineEdit_54.text() + '"' +'\n'
			'P5 = ' + '"' + self.ui.lineEdit_55.text() + '"' +'\n'
			'P6 = ' + '"' + self.ui.lineEdit_56.text() + '"' +'\n'
			'P7 = ' + '"' + self.ui.lineEdit_57.text() + '"' +'\n'
			'P8 = ' + '"' + self.ui.lineEdit_58.text() + '"' +'\n'
			'P9 = ' + '"' + self.ui.lineEdit_59.text() + '"' +'\n'
			'P10 = ' + '"' + self.ui.lineEdit_60.text() + '"' +'\n'
			'P11 = ' + '"' + self.ui.lineEdit_61.text() + '"' +'\n'
			'P12 = ' + '"' + self.ui.lineEdit_62.text() + '"' +'\n'
			'P13 = ' + '"' + self.ui.lineEdit_63.text() + '"' +'\n'
			'P14 = ' + '"' + self.ui.lineEdit_64.text() + '"' +'\n'
			'P15 = ' + '"' + self.ui.lineEdit_65.text() + '"' +'\n'
			'P16 = ' + '"' + self.ui.lineEdit_66.text() + '"' +'\n'
			'P17 = ' + '"' + self.ui.lineEdit_67.text() + '"' +'\n'
			'P18 = ' + '"' + self.ui.lineEdit_68.text() + '"' +'\n'
			'P19 = ' + '"' + self.ui.lineEdit_69.text() + '"' +'\n'
			'P20 = ' + '"' + self.ui.lineEdit_70.text() + '"' +'\n'
			'P21 = ' + '"' + self.ui.lineEdit_71.text() + '"' +'\n'
			'P22 = ' + '"' + self.ui.lineEdit_72.text() + '"' +'\n'
			'P23 = ' + '"' + self.ui.lineEdit_73.text() + '"' +'\n'
			'P24 = ' + '"' + self.ui.lineEdit_74.text() + '"' +'\n'
			'P25 = ' + '"' + self.ui.lineEdit_75.text() + '"' +'\n')
	

	def refresh(self):
		os.execl(sys.executable, sys.executable, *sys.argv)


		
#Функция выхода из приложения
	def exit(self):
		sys.exit()

#Функция создания таблицы
	def start(self):


		#создание массива с дисциплинами
		def dildo_pari(auto, graph, fiz, model, micro, oop, chimical, history, all_history, politic, uchet, audit, culture, bio, math, picture, cherch, comp, english, kazakh, zhivopis, tip, nVP, russian, phisic):
			all_mass = []
			if auto != 0:
				for i in range(auto):
					all_mass.append(Auto)
			else: pass
			if graph != 0:
				for i in range(graph):
					all_mass.append(Graph)
			else: pass
			if fiz != 0:
				for i in range(fiz):
					all_mass.append(Fiz)
			else: pass
			if model != 0:
				for i in range(model):
					all_mass.append(Model)
			else: pass
			if micro != 0:
				for i in range(micro):
					all_mass.append(Micro)
			else: pass
			if oop != 0:
				for i in range(oop):
					all_mass.append(OOP)
			else: pass
			if chimical != 0:
				for i in range(chimical):
					all_mass.append(Chimical)
			else: pass
			if history != 0:
				for i in range(history):
					all_mass.append(History)
			else: pass
			if all_history != 0:
				for i in range(all_history):
					all_mass.append(All_history)
			else: pass
			if politic != 0:
				for i in range(politic):
					all_mass.append(Politic)
			else: pass	
			if uchet != 0:
				for i in range(uchet):
					all_mass.append(Uchet)
			else: pass
			if audit != 0:
				for i in range(audit):
					all_mass.append(Audit)
			else: pass
			if culture != 0:
				for i in range(culture):
					all_mass.append(Culture)
			else: pass
			if bio != 0:
				for i in range(bio):
					all_mass.append(Bio)
			else: pass
			if math != 0:
				for i in range(math):
					all_mass.append(Math)
			else: pass
			if picture != 0:
				for i in range(picture):
					all_mass.append(Picture)
			else: pass
			if cherch != 0:
				for i in range(cherch):
					all_mass.append(Cherch)
			else: pass
			if comp != 0:
				for i in range(comp):
					all_mass.append(Comp)
			else: pass
			if english != 0:
				for i in range(english):
					all_mass.append(English)
			else: pass
			if kazakh != 0:
				for i in range(kazakh):
					all_mass.append(Kazakh)
			else: pass
			if zhivopis != 0:
				for i in range(zhivopis):
					all_mass.append(Zhivopis)
			else: pass
			if tip != 0:
				for i in range(tip):
					all_mass.append(Tip)
			else: pass
			if nVP != 0:
				for i in range(nVP):
					all_mass.append(NVP)
			else: pass
			if russian != 0:
				for i in range(russian):
					all_mass.append(Russian)
			else: pass
			if phisic != 0:
				for i in range(phisic):
					all_mass.append(Phisic)
			else: pass
			# random_mass = random.shuffle(all_mass)
			return all_mass


		#перемешиваем массив
		def my_shuffle(array):
		        random.shuffle(array)
		        return array


		def split_list(alist, wanted_parts=1):
		    length = len(alist)
		    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
		             for i in range(wanted_parts) ]




		all_in_one18101 = split_list(my_shuffle(dildo_pari(int(self.ui.lineEdit.text()), int(self.ui.lineEdit_2.text()), int(self.ui.lineEdit_3.text()), 
			int(self.ui.lineEdit_4.text()), int(self.ui.lineEdit_5.text()), int(self.ui.lineEdit_6.text()), int(self.ui.lineEdit_7.text()), int(self.ui.lineEdit_8.text()), 
			int(self.ui.lineEdit_9.text()), int(self.ui.lineEdit_10.text()), int(self.ui.lineEdit_11.text()), int(self.ui.lineEdit_12.text()), int(self.ui.lineEdit_13.text()), 
			int(self.ui.lineEdit_14.text()), int(self.ui.lineEdit_15.text()), int(self.ui.lineEdit_16.text()), int(self.ui.lineEdit_17.text()), int(self.ui.lineEdit_18.text()), 
			int(self.ui.lineEdit_19.text()), int(self.ui.lineEdit_20.text()), int(self.ui.lineEdit_21.text()), int(self.ui.lineEdit_22.text()), int(self.ui.lineEdit_23.text()), 
			int(self.ui.lineEdit_24.text()), int(self.ui.lineEdit_25.text()))), wanted_parts=5)
		ponedelnik18101 = all_in_one18101[0]
		vtornik18101 = all_in_one18101[1]
		sreda18101 = all_in_one18101[2]
		chetverg18101 = all_in_one18101[3]
		pyatnica18101 = all_in_one18101[4]	

		all_in_one18102 = split_list(my_shuffle(dildo_pari(int(self.ui.lineEdit_26.text()), int(self.ui.lineEdit_27.text()), int(self.ui.lineEdit_28.text()), 
			int(self.ui.lineEdit_29.text()), int(self.ui.lineEdit_30.text()), int(self.ui.lineEdit_31.text()), int(self.ui.lineEdit_32.text()), int(self.ui.lineEdit_33.text()), 
			int(self.ui.lineEdit_34.text()), int(self.ui.lineEdit_35.text()), int(self.ui.lineEdit_36.text()), int(self.ui.lineEdit_37.text()), int(self.ui.lineEdit_38.text()), 
			int(self.ui.lineEdit_39.text()), int(self.ui.lineEdit_40.text()), int(self.ui.lineEdit_41.text()), int(self.ui.lineEdit_42.text()), int(self.ui.lineEdit_43.text()), 
			int(self.ui.lineEdit_44.text()), int(self.ui.lineEdit_45.text()), int(self.ui.lineEdit_46.text()), int(self.ui.lineEdit_47.text()), int(self.ui.lineEdit_48.text()), 
			int(self.ui.lineEdit_49.text()), int(self.ui.lineEdit_50.text()))), wanted_parts=5)
		ponedelnik18102 = all_in_one18102[0]
		vtornik18102 = all_in_one18102[1]
		sreda18102 = all_in_one18102[2]
		chetverg18102 = all_in_one18102[3]
		pyatnica18102 = all_in_one18102[4]

		all_in_one18201 = split_list(my_shuffle(dildo_pari(int(self.ui.lineEdit_51.text()), int(self.ui.lineEdit_52.text()), int(self.ui.lineEdit_53.text()), 
			int(self.ui.lineEdit_54.text()), int(self.ui.lineEdit_55.text()), int(self.ui.lineEdit_56.text()), int(self.ui.lineEdit_57.text()), int(self.ui.lineEdit_58.text()), 
			int(self.ui.lineEdit_59.text()), int(self.ui.lineEdit_60.text()), int(self.ui.lineEdit_61.text()), int(self.ui.lineEdit_62.text()), int(self.ui.lineEdit_63.text()), 
			int(self.ui.lineEdit_64.text()), int(self.ui.lineEdit_65.text()), int(self.ui.lineEdit_66.text()), int(self.ui.lineEdit_67.text()), int(self.ui.lineEdit_68.text()), 
			int(self.ui.lineEdit_69.text()), int(self.ui.lineEdit_70.text()), int(self.ui.lineEdit_71.text()), int(self.ui.lineEdit_72.text()), int(self.ui.lineEdit_73.text()), 
			int(self.ui.lineEdit_74.text()), int(self.ui.lineEdit_75.text()))), wanted_parts=5)
		ponedelnik18201 = all_in_one18201[0]
		vtornik18201 = all_in_one18201[1]
		sreda18201 = all_in_one18201[2]
		chetverg18201 = all_in_one18201[3]
		pyatnica18201 = all_in_one18201[4]

		all_in_one18202 = split_list(my_shuffle(dildo_pari(int(self.ui.lineEdit_76.text()), int(self.ui.lineEdit_77.text()), int(self.ui.lineEdit_78.text()), 
			int(self.ui.lineEdit_79.text()), int(self.ui.lineEdit_80.text()), int(self.ui.lineEdit_81.text()), int(self.ui.lineEdit_82.text()), int(self.ui.lineEdit_83.text()), 
			int(self.ui.lineEdit_84.text()), int(self.ui.lineEdit_85.text()), int(self.ui.lineEdit_86.text()), int(self.ui.lineEdit_87.text()), int(self.ui.lineEdit_88.text()), 
			int(self.ui.lineEdit_89.text()), int(self.ui.lineEdit_90.text()), int(self.ui.lineEdit_91.text()), int(self.ui.lineEdit_92.text()), int(self.ui.lineEdit_93.text()), 
			int(self.ui.lineEdit_94.text()), int(self.ui.lineEdit_95.text()), int(self.ui.lineEdit_96.text()), int(self.ui.lineEdit_97.text()), int(self.ui.lineEdit_98.text()), 
			int(self.ui.lineEdit_99.text()), int(self.ui.lineEdit_100.text()))), wanted_parts=5)
		ponedelnik18202 = all_in_one18202[0]
		vtornik18202 = all_in_one18202[1]
		sreda18202 = all_in_one18202[2]
		chetverg18202 = all_in_one18202[3]
		pyatnica18202 = all_in_one18202[4]

		self.setMinimumSize(QtCore.QSize(480, 80))      # Устанавливаем размеры
		self.setWindowTitle("Работа с QTableWidget")    # Устанавливаем заголовок окна
		central_widget = QWidget(self)                  # Создаём центральный виджет
		self.setCentralWidget(central_widget)           # Устанавливаем центральный виджет

		grid_layout = QGridLayout()                     # Создаём QGridLayout
		central_widget.setLayout(grid_layout)           # Устанавливаем данное размещение в центральный виджет

		table = QTableWidget(self)  					# Создаём таблицу
		table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		table.NoEditTriggers
		table.setColumnCount(9)     # Устанавливаем колонки
		table.setRowCount(24)        # и строки в таблице



        # Устанавливаем заголовки таблицы
		table.setHorizontalHeaderLabels([" ", "Время", "18-101-Д", "Время", "18-102-ВТПО", "Время", "17-201-Д", "Время" ,"17-202-ВТПО"])

        # Устанавливаем выравнивание на заголовки
		table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
		table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
		table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)


		# объединение ячеек
		table.setSpan(0, 0, 4, 1)
		table.setSpan(5, 0, 4, 1)
		table.setSpan(10, 0, 4, 1)
		table.setSpan(15, 0, 4, 1)
		table.setSpan(20, 0, 4, 1)

        # заполняем строки
		table.setItem(0, 0, QTableWidgetItem("ПОНЕДЕЛЬНИК"))
		table.setItem(5, 0, QTableWidgetItem("ВТОРНИК"))
		table.setItem(10, 0, QTableWidgetItem("СРЕДА"))
		table.setItem(15, 0, QTableWidgetItem("ЧЕТВЕРГ"))
		table.setItem(20, 0, QTableWidgetItem("ПЯТНИЦА"))


		#18101
		table.setItem(0, 1, QTableWidgetItem("8.30 - 9.50"))
		try:		
			table.setItem(0, 2, QTableWidgetItem(ponedelnik18101[0]))
		except:
			IndexError		

		table.setItem(1, 1, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(1, 2, QTableWidgetItem(ponedelnik18101[1]))
		except:
			IndexError	
		table.setItem(2, 1, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(2, 2, QTableWidgetItem(ponedelnik18101[2]))
		except:
			IndexError		
		table.setItem(3, 1, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(3, 2, QTableWidgetItem(ponedelnik18101[3]))
		except:
			IndexError

		table.setItem(5, 1, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(5, 2, QTableWidgetItem(vtornik18101[0]))
		except:
			IndexError		
		table.setItem(6, 1, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(6, 2, QTableWidgetItem(vtornik18101[1]))
		except:
			IndexError		
		table.setItem(7, 1, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(7, 2, QTableWidgetItem(vtornik18101[2]))
		except:
			IndexError		
		table.setItem(8, 1, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(8, 2, QTableWidgetItem(vtornik18101[3]))
		except:
			IndexError

		table.setItem(10, 1, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(10, 2, QTableWidgetItem(sreda18101[0]))
		except:
			IndexError	
				
		table.setItem(11, 1, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(11, 2, QTableWidgetItem(sreda18101[1]))
		except:
			IndexError	
				
		table.setItem(12, 1, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(12, 2, QTableWidgetItem(sreda18101[2]))
		except:
			IndexError	

		table.setItem(13, 1, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(13, 2, QTableWidgetItem(sreda18101[3]))
		except:
			IndexError		

		table.setItem(15, 1, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(15, 2, QTableWidgetItem(chetverg18101[0]))
		except:
			IndexError	

		table.setItem(16, 1, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(16, 2, QTableWidgetItem(chetverg18101[1]))
		except:
			IndexError		
		table.setItem(17, 1, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(17, 2, QTableWidgetItem(chetverg18101[2]))
		except:
			IndexError		
		table.setItem(18, 1, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(18, 2, QTableWidgetItem(chetverg18101[3]))
		except:
			IndexError	

		table.setItem(20, 1, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(20, 2, QTableWidgetItem(pyatnica18101[0]))
		except:
			IndexError		
		table.setItem(21, 1, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(21, 2, QTableWidgetItem(pyatnica18101[1]))
		except:
			IndexError		
		table.setItem(22, 1, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(22, 2, QTableWidgetItem(pyatnica18101[3]))
		except:
			IndexError	

		table.setItem(23, 1, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(23, 2, QTableWidgetItem(pyatnica18101[3]))
		except:
			IndexError	
		#18102

		table.setItem(0, 3, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(0, 4, QTableWidgetItem(ponedelnik18102[0]))
		except:
			IndexError		
		table.setItem(1, 3, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(1, 4, QTableWidgetItem(ponedelnik18102[1]))
		except:
			IndexError		
		table.setItem(2, 3, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(2, 4, QTableWidgetItem(ponedelnik18102[2]))
		except:
			IndexError		
		table.setItem(3, 3, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(3, 4, QTableWidgetItem(ponedelnik18102[3]))
		except:
			IndexError		
		table.setItem(5, 3, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(5, 4, QTableWidgetItem(vtornik18102[0]))
		except:
			IndexError		
		table.setItem(6, 3, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(6, 4, QTableWidgetItem(vtornik18102[1]))
		except:
			IndexError		
		table.setItem(7, 3, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(7, 4, QTableWidgetItem(vtornik18102[2]))
		except:
			IndexError		
		table.setItem(8, 3, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(8, 4, QTableWidgetItem(vtornik18102[3]))
		except:
			IndexError		
		table.setItem(10, 3, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(10, 4, QTableWidgetItem(sreda18102[0]))
		except:
			IndexError		
		table.setItem(11, 3, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(11, 4, QTableWidgetItem(sreda18102[1]))
		except:
			IndexError		
		table.setItem(12, 3, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(12, 4, QTableWidgetItem(sreda18102[2]))
		except:
			IndexError		
		table.setItem(13, 3, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(13, 4, QTableWidgetItem(sreda18102[3]))
		except:
			IndexError		
		table.setItem(15, 3, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(15, 4, QTableWidgetItem(chetverg18102[0]))
		except:
			IndexError	
		table.setItem(16, 3, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(16, 4, QTableWidgetItem(chetverg18102[1]))
		except:
			IndexError			

		table.setItem(17, 3, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(17, 4, QTableWidgetItem(chetverg18102[2]))
		except:
			IndexError	
		table.setItem(18, 3, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(18, 4, QTableWidgetItem(chetverg18102[3]))
		except:
			IndexError	
		table.setItem(20, 3, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(20, 4, QTableWidgetItem(pyatnica18102[0]))
		except:
			IndexError	
		table.setItem(21, 3, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(21, 4, QTableWidgetItem(pyatnica18102[1]))
		except:
			IndexError	
		table.setItem(22, 3, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(22, 4, QTableWidgetItem(pyatnica18102[3]))
		except:
			IndexError	
		table.setItem(23, 3, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(23, 4, QTableWidgetItem(pyatnica18102[3]))
		except:
			IndexError	

		#17201

		table.setItem(0, 5, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(0, 6, QTableWidgetItem(ponedelnik18201[0]))
		except:
			IndexError	
		table.setItem(1, 5, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(1, 6, QTableWidgetItem(ponedelnik18201[1]))
		except:
			IndexError	
		table.setItem(2, 5, QTableWidgetItem("11.40 - 13.00"))
		try:	
			table.setItem(2, 6, QTableWidgetItem(ponedelnik18201[2]))
		except:
			IndexError	
		table.setItem(3, 5, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(3, 6, QTableWidgetItem(ponedelnik18201[3]))
		except:
			IndexError	
		table.setItem(5, 5, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(5, 6, QTableWidgetItem(vtornik18201[0]))
		except:
			IndexError	
		table.setItem(6, 5, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(6, 6, QTableWidgetItem(vtornik18201[1]))
		except:
			IndexError	
		table.setItem(7, 5, QTableWidgetItem("11.40 - 13.00"))
		try:	
			table.setItem(7, 6, QTableWidgetItem(vtornik18201[2]))
		except:
			IndexError	
		table.setItem(8, 5, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(8, 6, QTableWidgetItem(vtornik18201[3]))
		except:
			IndexError	
		table.setItem(10, 5, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(10, 6, QTableWidgetItem(sreda18201[0]))
		except:
			IndexError	
		table.setItem(11, 5, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(11, 6, QTableWidgetItem(sreda18201[1]))
		except:
			IndexError	
		table.setItem(12, 5, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(12, 6, QTableWidgetItem(sreda18201[2]))
		except:
			IndexError	
		table.setItem(13, 5, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(13, 6, QTableWidgetItem(sreda18201[3]))
		except:
			IndexError	
		table.setItem(15, 5, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(15, 6, QTableWidgetItem(chetverg18201[0]))
		except:
			IndexError	
		table.setItem(16, 5, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(16, 6, QTableWidgetItem(chetverg18201[1]))
		except:
			IndexError	
		table.setItem(17, 5, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(17, 6, QTableWidgetItem(chetverg18201[2]))
		except:
			IndexError	
		table.setItem(18, 5, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(18, 6, QTableWidgetItem(chetverg18201[3]))
		except:
			IndexError	
		table.setItem(20, 5, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(20, 6, QTableWidgetItem(pyatnica18201[0]))
		except:
			IndexError	
		table.setItem(21, 5, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(21, 6, QTableWidgetItem(pyatnica18201[1]))
		except:
			IndexError	
		table.setItem(22, 5, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(22, 6, QTableWidgetItem(pyatnica18201[3]))
		except:
			IndexError	
		table.setItem(23, 5, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(23, 6, QTableWidgetItem(pyatnica18201[3]))
		except:
			IndexError	
		#17202

		table.setItem(0, 7, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(0, 8, QTableWidgetItem(ponedelnik18202[0]))
		except:
			IndexError	
		table.setItem(1, 7, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(1, 8, QTableWidgetItem(ponedelnik18202[1]))
		except:
			IndexError	
		table.setItem(2, 7, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(2, 8, QTableWidgetItem(ponedelnik18202[2]))
		except:
			IndexError	
		table.setItem(3, 7, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(3, 8, QTableWidgetItem(ponedelnik18202[3]))
		except:
			IndexError	
		table.setItem(5, 7, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(5, 8, QTableWidgetItem(vtornik18202[0]))
		except:
			IndexError	
		table.setItem(6, 7, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(6, 8, QTableWidgetItem(vtornik18202[1]))
		except:
			IndexError	
		table.setItem(7, 7, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(7, 8, QTableWidgetItem(vtornik18202[2]))
		except:
			IndexError	
		table.setItem(8, 7, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(8, 8, QTableWidgetItem(vtornik18202[3]))
		except:
			IndexError	
		table.setItem(10, 7, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(10, 8, QTableWidgetItem(sreda18202[0]))
		except:
			IndexError	
		table.setItem(11, 7, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(11, 8, QTableWidgetItem(sreda18202[1]))
		except:
			IndexError	
		table.setItem(12, 7, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(12, 8, QTableWidgetItem(sreda18202[2]))
		except:
			IndexError	
		table.setItem(13, 7, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(13, 8, QTableWidgetItem(sreda18202[3]))
		except:
			IndexError	
		table.setItem(15, 7, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(15, 8, QTableWidgetItem(chetverg18202[0]))
		except:
			IndexError	
		table.setItem(16, 7, QTableWidgetItem("9.55 - 11.15"))
		try:
			table.setItem(16, 8, QTableWidgetItem(chetverg18202[1]))
		except:
			IndexError	
		table.setItem(17, 7, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(17, 8, QTableWidgetItem(chetverg18202[2]))
		except:
			IndexError	
		table.setItem(18, 7, QTableWidgetItem("13.05 - 14.25"))
		try:
			table.setItem(18, 8, QTableWidgetItem(chetverg18202[3]))
		except:
			IndexError	
		table.setItem(20, 7, QTableWidgetItem("8.30 - 9.50"))
		try:
			table.setItem(20, 8, QTableWidgetItem(pyatnica18202[0]))
		except:
			IndexError	
		table.setItem(21, 7, QTableWidgetItem("9.55 - 11.15"))
		try:	
			table.setItem(21, 8, QTableWidgetItem(pyatnica18202[1]))
		except:
			IndexError	
		table.setItem(22, 7, QTableWidgetItem("11.40 - 13.00"))
		try:
			table.setItem(22, 8, QTableWidgetItem(pyatnica18202[3]))
		except:
			IndexError	
		table.setItem(23, 7, QTableWidgetItem("13.05 - 14.25"))
		try:	
			table.setItem(23, 8, QTableWidgetItem(pyatnica18202[3]))
		except:
			IndexError	

        # делаем ресайз колонок по содержимому
		table.resizeColumnsToContents()
		table.resizeRowsToContents()

		grid_layout.addWidget(table, 0, 0)   # Добавляем таблицу в сетку




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())