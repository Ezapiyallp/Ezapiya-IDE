from PyQt5 import Qsci
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython,QsciLexerCPP,QsciLexerJava
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

        if self.fileExtention=="c" or self.fileExtention=="cpp" :
            self.setCpplexer()
        if self.fileExtention=="py":
            self.setPythonlexer()

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

        if self.fileExtention == "c" or self.fileExtention=="cpp" :
            self.setCpplexer()
        if self.fileExtention == "py":
            self.setPythonlexer()


    def getFullFileName(self):
        return self.fullFileName

    def setCommand(self, Command):
        pass
    def setFullFileNmae(self, Fname):
        self.fullFileName = Fname

    def setCpplexer(self):
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(16)
        lexer = QsciLexerCPP(self, False)
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0)#  Default = 0
        lexer.setColor(QColor("#A95151"), 1)# Comment = 1
        lexer.setColor(QColor("#6C51A9"), 2)# CommentLine = 2
        lexer.setColor(QColor("#BDA5F4"), 3)# CommentDoc = 3
        lexer.setColor(QColor("#46939C"), 4)#  Number = 4
        lexer.setColor(QColor("#C5BA40"), 5)# Keyword = 5
        lexer.setColor(QColor("#296C39"), 6)#  DoubleQuotedString = 6
        lexer.setColor(QColor("#96A82F"), 7)#  SingleQuotedString = 7
        lexer.setColor(QColor("#A87F2F"), 8)#  UUID = 8
        lexer.setColor(QColor("#FDD68A"), 9)#  PreProcessor = 9
        lexer.setColor(QColor("#E1898F"), 10)#  Operator = 10
        lexer.setColor(QColor("#E1898F"), 11)#  Identifier = 1
        lexer.setColor(QColor("#E1898F"), 12)# UnclosedString = 12
        lexer.setColor(QColor("#E1898F"), 13)# VerbatimString = 13
        lexer.setColor(QColor("#E1898F"), 14)# Regex = 14
        lexer.setColor(QColor("#E1898F"), 15)# CommentLineDoc = 15
        lexer.setColor(QColor("#E1898F"), 16)# KeywordSet2 = 16
        lexer.setColor(QColor("#E1898F"), 17)#  CommentDocKeyword = 17
        lexer.setColor(QColor("#E1898F"), 18)# CommentDocKeywordError = 18
        lexer.setColor(QColor("#E1898F"), 19)# GlobalClass = 19
        lexer.setColor(QColor("#E1898F"), 20)# RawString = 20
        lexer.setColor(QColor("#E1898F"), 21)# TripleQuotedVerbatimString = 21
        lexer.setColor(QColor("#E1898F"), 22)# HashQuotedString = 22
        lexer.setColor(QColor("#E1898F"), 23)#  PreProcessorComment = 23,
        lexer.setColor(QColor("#E1898F"), 24)#   PreProcessorCommentLineDoc = 2
        lexer.setColor(QColor("#E1898F"), 25)# UserLiteral = 25
        lexer.setColor(QColor("#E1898F"), 26)# TaskMarker = 26
        lexer.setColor(QColor("#E1898F"), 27)# EscapeSequence = 27
        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "-", ":", ";"]
        self.autoCompletionFillups()
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
        shortcut_ctrl_space = QShortcut(QKeySequence("Ctrl+Space"), self);
        # self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCompleteFromAll()));

    def setPythonlexer(self):
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(16)
        lexer = QsciLexerPython(self, False)
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0)# Default = 0
        lexer.setColor(QColor("#A95151"), 1)# Comment = 1
        lexer.setColor(QColor("#6C51A9"), 2)#  Number = 2
        lexer.setColor(QColor("#BDA5F4"), 3)#  DoubleQuotedString = 3
        lexer.setColor(QColor("#46939C"), 4)# SingleQuotedString = 4
        lexer.setColor(QColor("#C5BA40"), 5)#    Keyword = 5
        lexer.setColor(QColor("#296C39"), 6)# TripleSingleQuotedString = 6
        lexer.setColor(QColor("#96A82F"), 7)# TripleDoubleQuotedString = 7
        lexer.setColor(QColor("#A87F2F"), 8)#  ClassName = 8
        lexer.setColor(QColor("#FDD68A"), 9)#  FunctionMethodName = 9
        lexer.setColor(QColor("#E1898F"), 10)#  Operator = 10
        lexer.setColor(QColor("#E1898F"), 11)#  Identifier = 11
        lexer.setColor(QColor("#E1898F"), 12)# CommentBlock = 12
        lexer.setColor(QColor("#E1898F"), 13)#  UnclosedString = 13
        lexer.setColor(QColor("#E1898F"), 14)#  HighlightedIdentifier = 14
        lexer.setColor(QColor("#E1898F"), 15)# Decorator = 15

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
        shortcut_ctrl_space = QShortcut(QKeySequence("Ctrl+Space"), self);
        # self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCompleteFromAll()));

    def setJavalexer(self):
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(16)
        lexer = QsciLexerJava(self, False)
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0)  # Default = 0
        lexer.setColor(QColor("#A95151"), 1)  # Comment = 1
        lexer.setColor(QColor("#6C51A9"), 2)  # CommentLine = 2
        lexer.setColor(QColor("#BDA5F4"), 3)  # CommentDoc = 3
        lexer.setColor(QColor("#46939C"), 4)  # Number = 4
        lexer.setColor(QColor("#C5BA40"), 5)  # Keyword = 5
        lexer.setColor(QColor("#296C39"), 6)  # DoubleQuotedString = 6
        lexer.setColor(QColor("#96A82F"), 7)  # SingleQuotedString = 7
        lexer.setColor(QColor("#A87F2F"), 8)  # UUID = 8
        lexer.setColor(QColor("#FDD68A"), 9)  # PreProcessor = 9
        lexer.setColor(QColor("#E1898F"), 10)  # Operator = 10
        lexer.setColor(QColor("#E1898F"), 11)  # Identifier = 1
        lexer.setColor(QColor("#E1898F"), 12)  # UnclosedString = 12
        lexer.setColor(QColor("#E1898F"), 13)  # VerbatimString = 13
        lexer.setColor(QColor("#E1898F"), 14)  # Regex = 14
        lexer.setColor(QColor("#E1898F"), 15)  # CommentLineDoc = 15
        lexer.setColor(QColor("#E1898F"), 16)  # KeywordSet2 = 16
        lexer.setColor(QColor("#E1898F"), 17)  # CommentDocKeyword = 17
        lexer.setColor(QColor("#E1898F"), 18)  # CommentDocKeywordError = 18
        lexer.setColor(QColor("#E1898F"), 19)  # GlobalClass = 19
        lexer.setColor(QColor("#E1898F"), 20)  # RawString = 20
        lexer.setColor(QColor("#E1898F"), 21)  # TripleQuotedVerbatimString = 21
        lexer.setColor(QColor("#E1898F"), 22)  # HashQuotedString = 22
        lexer.setColor(QColor("#E1898F"), 23)  # PreProcessorComment = 23,
        lexer.setColor(QColor("#E1898F"), 24)  # PreProcessorCommentLineDoc = 2
        lexer.setColor(QColor("#E1898F"), 25)  # UserLiteral = 25
        lexer.setColor(QColor("#E1898F"), 26)  # TaskMarker = 26
        lexer.setColor(QColor("#E1898F"), 27)  # EscapeSequence = 27
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
        shortcut_ctrl_space = QShortcut(QKeySequence("Ctrl+Space"), self);
        # self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCompleteFromAll()));