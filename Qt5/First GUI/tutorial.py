from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow): #klasse fenster
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,200,300,300)#xpos,ypos, width,height
        self.setWindowTitle('My first window')
        self.initUI()    #in extra function to make it more structured


    def initUI(self): #is here to make it more structured
        self.label = QtWidgets.QLabel(self) #.QLabel() tells where the label should appear in this case in the window itself--> .QLabel(self) 
        self.label.setText('my first label!')
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self) # button should be in window
        self.b1.setText('Click me!')
        self.b1.clicked.connect(self.clicked)# clicked.connect --> when button is clicked function clickedis called to clicked function


    def clicked(self):
        self.label.setText('you pressed the button')
        self.update()
        
    def update(self):
        self.label.adjustSize()
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()         #create obj QMainWindow
    win.show()  #shows the window
    sys.exit(app.exec_())  #exit program an window

window()#call the funktion to make object