#-------------------------------------------------------------------------
# qsci_simple_pythoneditor.pyw
#
# QScintilla sample with PyQt
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------
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

        #fileHanding
        self.fullFileName=""
        self.fileName=""
        self.fileExtention=""
        self.saveStatus="No"
        self.TabID=0

        # Set the default font

        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(16)
        self.setFont(font)
        self.setMarginsFont(font)
        #self.setColor(QColor('lightblue'))
        self.setPaper(QColor('lightblue'))
                # Margin 0 is used for line numbers
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#232323"))
        self.setMarginsForegroundColor(QColor("#FFF"))

        # Clickable margin 1 for showing markers
        self.setMarginSensitivity(1, True)
        #self.connect(self,
        #    SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'),
        #    self.on_margin_clicked)
        self.markerDefine(QsciScintilla.RightArrow,
            self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"),
            self.ARROW_MARKER_NUM)

        # Brace matching: enable for a brace immediately before or after
        # the current position
        #
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Current line visible with special background color
        #self.setCaretLineVisible(True)
        self.setCaretLineVisible(False)


        # Set Python lexer
        # Set style for Python comments (style number 1) to a fixed-width
        # courier.
        #
        #lexer = QsciLexerPython()
        lexer = QsciLexerCPP(self,False)
        lexer.setDefaultFont(font)

        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0);
        lexer.setColor(QColor("#A95151"), 1);
        lexer.setColor(QColor("#6C51A9"), 2);
        lexer.setColor(QColor("#BDA5F4"), 3);
        lexer.setColor(QColor("#46939C"), 4);
        lexer.setColor(QColor("#C5BA40"), 5);
        lexer.setColor(QColor("#296C39"), 6); # String normal
        lexer.setColor(QColor("#96A82F"), 7);
        lexer.setColor(QColor("#A87F2F"), 8);
        lexer.setColor(QColor("#FDD68A"), 9);
        lexer.setColor(QColor("#E1898F"), 10);

        self.setCaretForegroundColor(QColor("#FFFFFF"))
       # self.setCaretLineBackgroundColor(QColor("#898888"))



        self.setLexer(lexer)



        api = Qsci.QsciAPIs(lexer)
        ## Add autocompletion strings
        for key in keyword.kwlist + dir(__builtins__):
            api.add(key)
        api.add("aLongString")
        api.add("aLongerString")
        api.add("aDifferentString")
        api.add("sOmethingElse")
        ## Compile the api for use in the lexer
        api.prepare()



        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionReplaceWord(False)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionSource(Qsci.QsciScintilla.AcsAll)




        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)


        shortcut_ctrl_space =  QShortcut(QKeySequence("Ctrl+Space"),self);
        #self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCompleteFromAll()));

        # not too small
        self.setMinimumSize(600, 450)

    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)
    def openFile(self,fileName):
        #fileName = QFileDialog.getOpenFileName()
        #print(fileName[0])
        self.fullFileName = fileName[0]
        tfileName=fileName[0]
        tfileName=tfileName.split('/')
        self.fileName = tfileName[len(tfileName)-1]
        #print(self.fileName)
        ext = self.fileName.split('.')
        self.fileExtention = ext[len(ext)-1]
       # print(self.fileExtention)
        self.setText(open(self.fullFileName).read())
        self.saveStatus = "Yes"
        return self.fullFileName

    def saveFile(self):
        if self.saveStatus == "Yes":
            f = open(self.fullFileName, "w")
            f.write(self.text())
        else:
            fileName = QFileDialog.getSaveFileName()
            # print(fileName[0])
            self.fullFileName = fileName[0]
            tfileName = fileName[0]
            tfileName = tfileName.split('/')
            self.fileName = tfileName[len(tfileName) - 1]
            print(self.fileName)
            ext = self.fileName.split('.')
            self.fileExtention = ext[len(ext) - 1]
            f = open(self.fullFileName, "w")
            f.write(self.text())
        self.saveStatus = "Yes"
        return self.fullFileName
    def getFullFileName(self):
        return self.fullFileName

    def setCommand(self,Command):
        pass
    def setFullFileNmae(self,Fname):
        self.fullFileName=Fname