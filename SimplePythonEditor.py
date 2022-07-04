
import os
import sys
import PyQt5
from PyQt5 import Qsci
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython,QsciLexerCPP
from PyQt5.QtWidgets import QApplication, QShortcut, QFileDialog
import keyword
class SimplePythonEditor(QsciScintilla):
    ARROW_MARKER_NUM = 8
    def __init__(self, parent=None):
        super(SimplePythonEditor, self).__init__(parent)
        self.fullFileName = ""
        self.fileName = ""
        self.fileExtention = ""
        self.saveStatus = "No"
        self.TabID=0
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(16)
        self.setFont(font)
        self.setMarginsFont(font)
        self.setPaper(QColor('lightblue'))
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#232323"))
        self.setMarginsForegroundColor(QColor("#FFF"))
        self.setMarginSensitivity(1, True)
        self.markerDefine(QsciScintilla.RightArrow,
            self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"),
            self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineVisible(False)
        #lexer = QsciLexerPython()
        lexer = QsciLexerCPP(self,False)
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0)
        lexer.setColor(QColor("#A95151"), 1)
        lexer.setColor(QColor("#6C51A9"), 2)
        lexer.setColor(QColor("#BDA5F4"), 3)
        lexer.setColor(QColor("#46939C"), 4)
        lexer.setColor(QColor("#C5BA40"), 5)
        lexer.setColor(QColor("#296C39"), 6) # String normal
        lexer.setColor(QColor("#96A82F"), 7)
        lexer.setColor(QColor("#A87F2F"), 8)
        lexer.setColor(QColor("#FDD68A"), 9)
        lexer.setColor(QColor("#E1898F"), 10)
        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = ["."]
        self.setAutoCompletionWordSeparators(my_list)
        self.setLexer(lexer)
        api = Qsci.QsciAPIs(lexer)
        for key in keyword.kwlist + dir(__builtins__):
            api.add(key)
        api.add("aLongString")
        api.add("aLongerString")
        api.add("aDifferentString")
        api.add("sOmethingElse")
        api.prepare()
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionReplaceWord(False)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionSource(Qsci.QsciScintilla.AcsAll)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)
        shortcut_ctrl_space =  QShortcut(QKeySequence("Ctrl+Space"),self);
        #self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCompleteFromAll()));
        self.setMinimumSize(600, 450)

    def on_margin_clicked(self, nmargin, nline, modifiers):
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)

    def openFile(self,fileName):
        self.fullFileName = fileName[0]
        tfileName=fileName[0]
        tfileName=tfileName.split('/')
        self.fileName = tfileName[len(tfileName)-1]
        ext = self.fileName.split('.')
        self.fileExtention = ext[len(ext)-1]
        f = open(self.fullFileName,"r")
        self.setText(f.read())
        f.close()
        self.saveStatus = "Yes"
        return self.fullFileName

    def getSaveStatus(self):
        return self.saveStatus

    def saveFile(self,fileName):
        self.fullFileName = fileName[0]
        tfileName = fileName[0]
        tfileName = tfileName.split('/')
        self.fileName = tfileName[len(tfileName) - 1]
        print(self.fileName)
        ext = self.fileName.split('.')
        self.fileExtention = ext[len(ext) - 1]
        f = open(self.fullFileName, "w")
        f.write(self.text())
        f.close()
        self.saveStatus = "Yes"

    def getFullFileName(self):
        return self.fullFileName

    def setCommand(self, Command):
        pass
    def setFullFileNmae(self, Fname):
        self.fullFileName = Fname