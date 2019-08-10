import sys
import impl
from impl.main_window import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    # Создание класса приложения из бибилиотеки PyQt5
    app = QApplication(sys.argv)
    # Создание класса диалогового окна меню
    main_window = MainWindow()
    # Вызов функции отображения диалога меню
    main_window.show()
    # После завершения работы всех диалогов закрытие приложения PyQt5
    sys.exit(app.exec_())
