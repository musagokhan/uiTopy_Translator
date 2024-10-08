##################################################
###### version               : 1.1.1        ######
###### first Release date    : 11.03.2024   ######
###### last Release date     : 13.03.2024   ######
###### author                : mgkorkut     ######
##################################################


#import guiQt
#from help import Ui_Form
import os
from gui import guiQt
from gui.help import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog
import subprocess
import sys


class mainClass(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = guiQt.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.handleRun) 
        self.ui.pushButton_2.clicked.connect(self.handleHelpInfo) # help button

 
    def handleRun(self):

        uiFile = self.ui.lineEdit.text()
        pyFile = self.ui.lineEdit_2.text()
        
        currentPath = os.path.dirname(os.path.abspath(__file__)) 
        print(f"currentPath    : {currentPath}")

        command = f"pyuic5 -x {uiFile} -o {pyFile}"
        try:
            subprocess.run(command, shell=True, check=True)
            self.ui.lineEdit_3.setStyleSheet("color: darkgreen")
            self.ui.lineEdit_3.setText(f"{pyFile} file successfully created")
            self.ui.pushButton.setStyleSheet("background-color: darkgreen")
        except subprocess.CalledProcessError:
            self.ui.pushButton.setStyleSheet("background-color: red")
            self.ui.lineEdit_3.setStyleSheet("color: red")
            self.ui.lineEdit_3.setText(f"Error: No such file or directory: {uiFile}")



    def handleHelpInfo(self):
        self.helpDialog = QDialog(self)  # Dialog create
        self.uiHelp = Ui_Form()  # create Ui_Form
        self.uiHelp.setupUi(self.helpDialog)  # run UI
        self.helpDialog.exec_()  # show Dialog 



def window():   
    app = QApplication(sys.argv)
    main_window = mainClass()

    # update PNG path
    currentPath = os.path.dirname(os.path.abspath(__file__)) 
    imgPath = os.path.join(currentPath,  "gui", "img")  # img folder PATH
    backwalPath = os.path.join(imgPath, "backWal.png")  # backWal PATH
    logoPath = os.path.join(imgPath, "logo.png")  # logo PATH
    # update PNG Path
    main_window.ui.label_5.setPixmap(QtGui.QPixmap(backwalPath))
    main_window.ui.label.setPixmap(QtGui.QPixmap(logoPath))

    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()