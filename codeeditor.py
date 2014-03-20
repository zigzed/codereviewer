'''
Created on Mar 19, 2014

@author: wilbur
'''
from PyQt4 import QtGui
from PyQt4.Qsci import QsciScintilla
from zoomwidget import ZoomWidget

class CodeEditor(QsciScintilla):
    
    def __init__(self):
        super(CodeEditor, self).__init__()
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setMargin(0)
        self.setLayout(mainLayout)
        
        mainLayout.addStretch(1)
        
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.setContentsMargins(0, 0, 20, 0)
        mainLayout.addLayout(hbox1)
        
        self.zoomWidget = ZoomWidget(self)
        hbox1.addWidget(self.zoomWidget)
                
        font = QtGui.QFont()
        font.setFamily('Menlo')
        font.setFixedPitch(True)
        font.setPointSize(11)
        self.fontMetrics = QtGui.QFontMetrics(font)
         
        self.setFont(font)
        self.setMarginsFont(font)
        self.setTabWidth(4)
                  
        self.setUtf8(True)
        self.setAutoIndent(True)
        self.setIndentationGuides(True)
        self.setTabWidth(4)
        self.setIndentationWidth(4)
        self.setAnnotationDisplay(QsciScintilla.ANNOTATION_BOXED)
          
        self.setMarginWidth(0, self.fontMetrics.width('0000') + 5)
        self.setMarginLineNumbers(0, True)
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle, 2)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setEdgeMode(QsciScintilla.EdgeLine)
        self.setEdgeColumn(80)
          
        self.setCaretLineVisible(True)
        self.setReadOnly(True)
        self.setMinimumSize(800, 400)
 
        self.markerDefine(QsciScintilla.Rectangle, 1)
        self.setMarkerBackgroundColor(QtGui.QColor("#EE0000"), 1)
        self.setMarkerForegroundColor(QtGui.QColor("#EE0000"), 1)
        
        
    
    
        