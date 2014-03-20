# -*- coding: utf8 -*-
'''
Created on Mar 19, 2014

@author: wilbur
'''
import os
import json
from PyQt4 import QtGui
from PyQt4.Qsci import QsciLexerBash, QsciLexerPython, QsciLexerCPP, QsciLexerJava, QsciLexerJavaScript
from codeeditor import CodeEditor
import codecs

class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.filename = ''
        self.annotation = {}
        self.encoding = 'utf8'
        
        mainLayout = QtGui.QVBoxLayout()
        
        self.editor = CodeEditor()
        self.editor.cursorPositionChanged.connect(self.onChangeCursor)
        mainLayout.addWidget(self.editor)
        
        hbox = QtGui.QHBoxLayout()
        mainLayout.addLayout(hbox)
        
#         groupBox = QtGui.QGroupBox('category')
#         groupBox.setCheckable(False)
#         groupBox.setChecked(False)
#         
#         grid = QtGui.QGridLayout()
#         radio1 = QtGui.QRadioButton(u"风格")
#         radio2 = QtGui.QRadioButton(u"维护")
#         radio3 = QtGui.QRadioButton(u"性能")
#         radio4 = QtGui.QRadioButton(u"缺陷")
#         radio1.setChecked(True)
#         grid.addWidget(radio1, 0, 0)
#         grid.addWidget(radio2, 1, 0)
#         grid.addWidget(radio3, 0, 1)
#         grid.addWidget(radio4, 1, 1)
#         groupBox.setLayout(grid)
#         
#         hbox.addWidget(groupBox)
        
        
        self.review = QtGui.QTextEdit()
        self.review.setMaximumHeight(60)
        hbox.addWidget(self.review)
        
        self.sendBtn = QtGui.QPushButton('commit')
        self.sendBtn.clicked.connect(self.onSendPressed)
        hbox.addWidget(self.sendBtn)
        
        self.setLayout(mainLayout)
        self.show()
        
    def reload(self):
        self.loadFile(self.filename)
        
    def loadFile(self, fileName):
        if not os.path.exists(unicode(fileName)):
            self.editor.clear()
            return
        
        self.filename = unicode(fileName)
        
        f = open(self.filename, 'r')
        t = f.read()
        
        try:
            self.editor.setText(t.decode(self.encoding))
            
            lexer = QsciLexerBash()
            if self.filename.endswith('.py'):
                lexer = QsciLexerPython()
            elif self.filename.endswith('.cpp') or self.filename.endswith('.h'):
                lexer = QsciLexerCPP()
            elif self.filename.endswith('.java'):
                lexer = QsciLexerJava()
            elif self.filename.endswith('.js'):
                lexer = QsciLexerJavaScript()
                
            lexer.setFont(self.editor.font())
            self.editor.setLexer(lexer)
            
            self.loadAnnotation()
            
        except UnicodeDecodeError as e:
            QtGui.QMessageBox.question(self, 'Error', 
                                       'info: ' + str(e)
                                       )
            
        f.close()
        
    def onChangeCursor(self, line, pos):
        prevAnno = unicode(self.editor.annotation(line))
        self.review.clear()
        self.review.append(prevAnno)
            
    def onSendPressed(self):
        anno = unicode(self.review.toPlainText())
        self.addAnnotation((anno))
        
        
    def loadAnnotation(self):
        self.annotation.clear()
        if not os.path.exists((self.filename + '.info')):
            return
        
        f = open((self.filename + '.info'), 'r')
        try:
            self.annotation = json.load(f, encoding='utf8')
        except ValueError as e:
            print(e) 
            
        f.close()
        
        for p in self.annotation:
            i = (self.annotation[p])
            self.editor.annotate(int(p), (i), 0)
            self.editor.markerAdd(int(p), 1)
            
    def saveAnnotation(self):
        f = codecs.open((self.filename + '.info'), 'w', 'utf8')
        json.dump(self.annotation, 
                  f,
                  ensure_ascii=False,
                  indent=4)
        f.close()
        
    def addAnnotation(self, text):
        p = self.editor.getCursorPosition()[0]
        self.annotation[p] = text
        
        self.editor.annotate(p, text, 0)
        self.editor.markerAdd(p, 1)
        self.review.clear()
        
        self.saveAnnotation()
        
        
        