import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *



# Creates the GUI for the entire program
class MainWindow(QWidget):

    #initialize parent and populate window
    def  __init__(self):
        super().__init__()
        view = self.createView()

        self.setWindowTitle("Calculator")
        self.setLayout(view)
        self.show()
    
    #creates the layout for the calculator and returns the QGridLayout
    #with the buttons
    def createView(self):
        calculator_layout = QGridLayout()
        
        #Create list of buttons 
        btns = ["AC", "C", "CE", "/", "7", "8", "9", "*","4", "5", "6", "-","1", "2", "3", "+","+/-", "0", ".", "="]
        row = 1
        col = 0
        output = QLineEdit()
        output.setReadOnly(True)
        output.setAlignment(Qt.AlignRight)
        
        # Create QlineEdit
        calculator_layout.addWidget(output, 0, 0, 1, 4)

        # Create buttons and attached event handler to them
        for btn in btns:
            btn_object = Button(btn, output)
            if col > 3:
                row += 1
                col = 0
            calculator_layout.addWidget(btn_object.btn, row, col)
            col += 1
    
        return calculator_layout


# Controls button pushes and output on GUI
class Button:

    def __init__(self, text, output):
        self.btn = QPushButton(text)
        self.btn.clicked.connect(lambda: self.pressed(text, output))

    def pressed(self, text, output):
        if text == "=":
            output.setText(str(eval(output.text())))
        else:
            output.setText(output.text() + text)


#start window when application is run
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec_())