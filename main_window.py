import csv
import numpy as np
import matplotlib.pyplot as plt
import impl
#PyQt5
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
#App
from impl.Opheim import Opheim
from impl.Line_generator import Line
from view.main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind_events()
        self.create_graphic()
    def bind_events(self):
        self.ui.about.triggered.connect(self.about)
        self.ui.developer.triggered.connect(self.developer)
        self.ui.open_file.triggered.connect(self.open_file)
        self.ui.save_file.triggered.connect(self.save_file)
        self.ui.generate_line.clicked.connect(self.generate_line)
        self.ui.simplify_opheim.clicked.connect(self.simplify_opheim)
    def create_graphic(self):
        self.fig = plt.figure(figsize=(10, 10))
        self.fig.gca().set_aspect('equal', adjustable='box')
        self.axes = self.fig.add_subplot(111)
    def update_graphic(self):
        self.axes.clear()
    def about(self):
        QMessageBox.about(self, "О программе!", "Данная программа выполняет упрощение полигональной цепи алгоритмом Опхейма.")
    def developer(self):
        QMessageBox.about(self, "О разработчике!", "Программа разработана студентом ГУАП, группы 4615. Инициалы и фамилия: П.Ю. Лаптев")
    # Открытие файла
    def open_file(self):
        # Открываем диалоговое окно загрузки файла
        fname = QFileDialog.getOpenFileName(self, 'Open file', filter ='CSV(*.csv)')[0]
        if fname != '':
            # Открываем файл на чтение
            with open(fname, newline='') as csvfile:
                # Считываем файл в словарь
                reader = csv.DictReader(csvfile)
                data = []
                for row in reader:
                    # Считываем данные
                    data.append((float(row['X']), float(row['Y'])))
                # Если данные есть загружаем наш многоугольник
                if len(data) > 0:
                    self.load_line(data)
                else:
                    QMessageBox.about(self, "Ошибка!", "Файл имеет неправильный формат!")
    # Сохранение файла
    def save_file(self):
        # Открываем диалоговое окно сохранения файла
        fname = QFileDialog.getSaveFileName(self, 'Save File', filter ='CSV(*.csv)')[0]
        if fname != '':
            # Открываем файл на запись
            outfile = open( fname, "w")
            # Запускаем csv запись словаря
            writer = csv.DictWriter(outfile, fieldnames=['X', 'Y'])
            # Записываем заголовок
            writer.writeheader()
            # Записываем данные
            for data in self.line.get_line():
                writer.writerow({ 'X' : str(data[0]), 'Y' : str(data[1]) })
            # Сохраняем файл
            outfile.close()
    def generate_line(self):
        self.update_graphic()
        self.line = Line()
        line_data = self.line.generate_random_line(int(self.ui.input_num_points.text()), int(self.ui.input_direction.text()),[int(self.ui.input_min_rnd.text()),int(self.ui.input_max_rnd.text())])
        plt.plot(line_data[:,0],line_data[:,1])
        plt.scatter(line_data[:,0],line_data[:,1])
        self.fig.canvas.draw()
        plt.show()
    def simplify_opheim(self):
        opheim = Opheim()
        data_line = self.line.get_line()
        mask,_ = opheim.simplify_opheim(float(self.ui.input_tolerance.text()),float(self.ui.input_maxdist.text()), data_line, int(self.ui.input_count_step.text()))
        simplified = data_line[mask]
        plt.plot(simplified[:,0],simplified[:,1])
        plt.scatter(simplified[:,0],simplified[:,1])
        #deleted points
        deleted = data_line[np.logical_not(mask)]
        plt.scatter(deleted[:,0],deleted[:,1],color='red',marker='x',s=50,linewidth=2.0)
        self.fig.canvas.draw()
    def load_line(self, line):
        self.update_graphic()
        data_line = np.array(line,dtype='double')
        self.line = Line()
        self.line.set_line(data_line)
        plt.plot(data_line[:,0],data_line[:,1])
        plt.scatter(data_line[:,0],data_line[:,1])
        self.fig.canvas.draw()
        plt.show()
