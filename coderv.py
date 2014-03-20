'''
Created on Mar 19, 2014

@author: wilbur
'''
import sys
import os

from PyQt4 import QtGui
from PyQt4.QtGui import QApplication
from mainwindow import MainWindow

class CodeReviewer(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.pwd = ''
        self.prevFind = ''
        self.setWindowTitle('code reviewer')
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setMargin(0)
        self.setLayout(mainLayout)
        
        hbox = QtGui.QHBoxLayout()
        hbox.setContentsMargins(5, 3, 5, 3)
        mainLayout.addLayout(hbox)
        
        hbox.addStretch(1)
        
        self.editor = MainWindow()
        mainLayout.addWidget(self.editor)
        
        self.curfileLbl = QtGui.QLabel()
        hbox.addWidget(self.curfileLbl)
        
        self.loadingBtn = QtGui.QToolButton()
        self.loadingBtn.setText('Load Source Code')
        self.loadingBtn.clicked.connect(self.loadSourceCode)
        hbox.addWidget(self.loadingBtn)
               
        self.encodingBtn = QtGui.QComboBox()
        self.encodingBtn.addItem("utf8")     
        self.encodingBtn.addItem("gbk")
        self.encodingBtn.activated[str].connect(self.changeEncoding)
        hbox.addWidget(self.encodingBtn)
        
        self.findEdt = QtGui.QLineEdit()
        hbox.addWidget(self.findEdt)
        self.findBtn = QtGui.QToolButton()
        self.findBtn.setText('Find')
        self.findBtn.clicked.connect(self.searchCode)
        hbox.addWidget(self.findBtn)

    def changeEncoding(self, text):
        self.curfileLbl.setText(self.editor.filename)
        self.editor.encoding = str(text);
        self.editor.reload()
        
    def loadSourceCode(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Load Source Code', self.pwd)
        self.pwd = os.path.dirname(unicode(filename))
        self.editor.loadFile(filename)
        self.curfileLbl.setText(self.editor.filename)

    def searchCode(self):
        text = self.findEdt.text();
        if text == '':
            text = self.editor.editor.selectedText()
            self.findEdt.setText(text)
        
        if self.prevFind == text:
            self.editor.editor.findNext()
        else:
            self.prevFind = text
            self.editor.editor.findFirst(text, False, False, False, True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwd = CodeReviewer()
    mwd.show()
    app.exec_()