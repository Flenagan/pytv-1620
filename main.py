#Main lol

import sys
from PyQt6 import QtWidgets
from tvgui import Ui_main_tv

#do I say more
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_main_tv()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()