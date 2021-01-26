'''
Created by: Omar Abdelakher Hammad
Date: 26 Jan. 2021 - 05:28 PM
Designed using Qt Designer
Edited by Omar
'''

import sys, os
import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from numpy import linspace

# Application doesn't work without adding the following lines
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

# Canvas Class
class uiCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, x_values=[], y_values=[]):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.plot(x_values, y_values, 'r-')
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

# Main UI Design using designer code
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(234, 241, 255)")
        self.instAction = QAction(MainWindow)
        self.instAction.setObjectName(u"instAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(4, 10, 791, 51))
        font = QFont()
        font.setFamily(u"Old Antic Outline")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 79);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 120, 311, 41))
        font1 = QFont()
        font1.setFamily(u"Old Antic Outline Shaded")
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(30, 30, 116);")
        fontX = QFont()
        fontX.setFamily(u"Old Antic Outline Shaded")
        fontX.setPointSize(11)
        self.formula = QLineEdit(self.centralwidget)
        self.formula.setFont(fontX)
        self.formula.setObjectName(u"formula")
        self.formula.setGeometry(QRect(370, 130, 311, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 190, 411, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(30, 30, 116);")
        self.minVal = QLineEdit(self.centralwidget)
        self.minVal.setFont(fontX)
        self.minVal.setObjectName(u"minVal")
        self.minVal.setGeometry(QRect(220, 260, 71, 31))
        self.maxVal = QLineEdit(self.centralwidget)
        self.maxVal.setFont(fontX)
        self.maxVal.setObjectName(u"maxVal")
        self.maxVal.setGeometry(QRect(570, 260, 71, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 260, 81, 31))
        font2 = QFont()
        font2.setFamily(u"Old Antic Outline Shaded")
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(30, 30, 116);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 260, 81, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(30, 30, 116);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 350, 411, 41))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(30, 30, 116);")
        self.plotBtn = QPushButton(self.centralwidget)
        self.plotBtn.setObjectName(u"plotBtn")
        self.plotBtn.setGeometry(QRect(340, 400, 93, 41))
        font3 = QFont()
        font3.setFamily(u"Old Antic Outline Shaded")
        font3.setPointSize(11)
        self.plotBtn.setFont(font3)
        self.plotBtn.setStyleSheet(u"background-color: rgb(30, 30, 116); color: rgb(239, 243, 255); border-radius: 4px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.instAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Function Plotter Program", None))
        self.instAction.setText(QCoreApplication.translate("MainWindow", u"Instructions", None))
#if QT_CONFIG(shortcut)
        self.instAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Step 1: Enter your formula", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Step 2: Enter max. and min. values for X", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Min Value", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Max Value", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Step 3: Plot the function", None))
        self.plotBtn.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


# Our main window class, inherits the Ui_MainWindow class
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)

        # Connect the button event to a slot function
        self.plotBtn.clicked.connect(self.startPlot)

        # Connect the menu item triggering to a function
        self.instAction.triggered.connect(self.instFun)

    def startPlot(self):

        # Define allowed characters
        supported = ['x', '+', '-', '*', '/', '^']

        formula = self.formula.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")

        try:
            min_ = int(self.minVal.text())
            max_ = int(self.maxVal.text())
        except ValueError:
            msg.setText("Please enter a number in the Min / Max Value!")
            msg.exec_()

        # Assume expression is valid
        validExpr = True

        # Check if there's invalid input
        for ch in formula:

            if ch == ' ':
                # Ignore spaces
                continue

            if not ch.isdigit():
                # If character is not a number, check if it's valid
                if ch not in supported:
                    # Character not supported, show error message
                    msg.setText("Invalid input: {}!".format(ch))
                    msg.exec_()
                    validExpr = False

        formula = formula.replace('^', '**')

        if validExpr:
            # Calculate plot data
            x_values = linspace(min_, max_, num=100)

            y_values = []

            for x in x_values:
                y_values.append(eval(formula))
            
            # Show the graph in a new window
            self.plot = QWidget()
            l = QVBoxLayout(self.plot)
            canv = uiCanvas(self.plot, width=5, height=4, dpi=100, x_values=x_values, y_values=y_values)
            l.addWidget(canv)

            self.plot.resize(400, 300)
            self.plot.setWindowTitle("Function Plot Graph")
            self.plot.show()
            

    def instFun(self):
        # Show a message bix showing instruction to use the program
        msg_box = QMessageBox()
        msg_box.setText(
"""This program evaluates algebric forumlas and plots them within a starting/ending value.\n\nInstructions:
1. Enter your forumla in the designated box
2. Enter the min/max values for the plot
3. Press the 'Plot' button

NOTES:
 - Please only use 'X' as the function variable. Any other alphabets will result in an error.
 - Only operators supported are:  +  -  /  *  ^   . Any other operators will result in an error.

Thank you for using this program.
"""
        )
        msg_box.setWindowTitle("Function Plotter - Instructions")
        msg_box.exec_() 

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())