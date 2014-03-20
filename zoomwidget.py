'''
Created on Mar 19, 2014

@author: wilbur
'''
from PyQt4 import QtCore, QtGui

class ZoomWidget(QtGui.QLabel):
    def __init__(self, editor):
        QtGui.QLabel.__init__(self)
        
        self.editor = editor
        self.zvalue = 0
        
        self.setFixedHeight(130)
        self.setFixedWidth(38)
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setMargin(1)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)
        
        self.increaseBtn = QtGui.QToolButton()
        self.increaseBtn.setFixedHeight(36)
        self.increaseBtn.setFixedWidth(36)
        self.increaseBtn.setText('+')
        self.increaseBtn.clicked.connect(self.zoomIn)
        mainLayout.addWidget(self.increaseBtn)
        
        self.zoomBox = QtGui.QSpinBox()
        self.zoomBox.setMinimum(0)
        self.zoomBox.setMaximum(100)
        self.zoomBox.setReadOnly(True)
        self.zoomBox.setAlignment(QtCore.Qt.AlignHCenter)
        self.zoomBox.setButtonSymbols(2)
        self.zoomBox.setSingleStep(10)
        self.zoomBox.setSuffix('%')
        self.zoomBox.valueChanged.connect(self.changeZoomValue)
        mainLayout.addWidget(self.zoomBox)
        
        self.decreaseBtn = QtGui.QToolButton()
        self.decreaseBtn.setFixedHeight(36)
        self.decreaseBtn.setFixedWidth(36)
        self.decreaseBtn.setText('-')
        self.decreaseBtn.clicked.connect(self.zoomOut)
        mainLayout.addWidget(self.decreaseBtn)
        
        self.increaseBtn.setStyleSheet(
                                       """
                           QToolButton {
                               background: transparent;
                           }
                           QToolButton:hover {
                               background: grey;
                           }
                           """
                                       )
        self.decreaseBtn.setStyleSheet(
                                       """
                           QToolButton {
                               background: transparent;
                           }
                           QToolButton:hover {
                               background: grey;
                           }
                           """
                                       )
        
    def changeZoomValue(self, value):
        if self.zvalue > value:
            self.editor.zoomOut()
        elif self.zvalue < value:
            self.editor.zoomIn()
        else:
            self.editor.zoomOut()
            
        self.zvalue = value
        
    def zoomIn(self):
        self.zoomBox.setValue(self.zoomBox.value() + 10)
        
    def zoomOut(self):
        self.zoomBox.setValue(self.zoomBox.value() - 10)
        
        
