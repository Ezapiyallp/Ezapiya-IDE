from PyQt5 import Qsci
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciLexerCPP, QsciLexerJava, QsciLexerJavaScript, \
    QsciLexerCSharp, QsciLexerHTML, QsciLexerCSS, QsciLexerXML, QsciLexerSQL
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"),self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)
        #lexer = QsciLexerPython()
        lexer = QsciLexerCPP()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))

        lexer.setColor(QColor("#FFFFFF"), 0)#  Default = 0
        lexer.setColor(QColor("#FEFB02"), 1)# Comment = 1
        lexer.setColor(QColor("#FE6905"), 2)# CommentLine = 2
        lexer.setColor(QColor("#FECC05"), 3)# CommentDoc = 3
        lexer.setColor(QColor("#A9FE05"), 4)#  Number = 4
        lexer.setColor(QColor("#88E22B"), 5)# Keyword = 5
        lexer.setColor(QColor("#8CDCFE"), 6)#  DoubleQuotedString = 6
        lexer.setColor(QColor("#05C6FE"), 7)#  SingleQuotedString = 7
        lexer.setColor(QColor("#058CFE"), 8)#  UUID = 8
        lexer.setColor(QColor("#05C6FE"), 9)#  PreProcessor = 9
        lexer.setColor(QColor("#FECC05"), 10)#  Operator = 10
        lexer.setColor(QColor("#FFF"), 11)#  Identifier = 1
        lexer.setColor(QColor("#05C6FE"), 12)# UnclosedString = 12
        lexer.setColor(QColor("#AC7DCE"), 13)# VerbatimString = 13
        lexer.setColor(QColor("#88E22B"), 14)# Regex = 14
        lexer.setColor(QColor("#E7DB74"), 15)# CommentLineDoc = 15
        lexer.setColor(QColor("#60D8EF"), 16)# KeywordSet2 = 16
        lexer.setColor(QColor("#B36932"), 17)#  CommentDocKeyword = 17
        lexer.setColor(QColor("#519ABA"), 18)# CommentDocKeywordError = 18
        lexer.setColor(QColor("#CDD100"), 19)# GlobalClass = 19
        lexer.setColor(QColor("#05C6FE"), 20)# RawString = 20
        lexer.setColor(QColor("#CE9172"), 21)# TripleQuotedVerbatimString = 21
        lexer.setColor(QColor("#EC5166"), 22)# HashQuotedString = 22
        lexer.setColor(QColor("#C5A84F"), 23)#  PreProcessorComment = 23,
        lexer.setColor(QColor("#B9644F"), 24)#   PreProcessorCommentLineDoc = 2
        lexer.setColor(QColor("#C3485C"), 25)# UserLiteral = 25
        lexer.setColor(QColor("#498B60"), 26)# TaskMarker = 26
        lexer.setColor(QColor("#E1898F"), 27)# EscapeSequence = 27
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
        self.zoomIn()
        self.zoomIn()
        self.zoomIn()
        shortcut_ctrl_space =  QShortcut(QKeySequence("Ctrl+Space"),self);
        #self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCompleteFromAll()));
        self.setMinimumSize(600, 450)

    def on_margin_clicked(self, nmargin, nline, modifiers):
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)

    def findFunction(self,wordToFind,forward):
        if forward:
            line, index = self.getSelection()[2:]
        else:
            line, index = self.getSelection()[:2]

        self.findFirst(wordToFind, False, False, False, False, True, line, index, False)

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
        if self.fileExtention == "java":
            self.setJavalexer()
        if self.fileExtention == "js":
            self.setJavaScriptlexer()
        if self.fileExtention == "cs":
            self.setCSharplexer()
        if self.fileExtention == "html" or self.fileExtention == "htm":
            self.setHtmllexe()

        if self.fileExtention == "sql":
            self.setSQLlexe()
        if self.fileExtention == "xml":
            self.setXMLlexe()
        if self.fileExtention == "css":
            self.setCSSlexe()

        return self.fullFileName

    def openFile_form_command_line(self,fileName):
        self.fullFileName = fileName
        tfileName=fileName
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
        if self.fileExtention == "java":
            self.setJavalexer()
        if self.fileExtention == "js":
            self.setJavaScriptlexer()
        if self.fileExtention == "cs":
            self.setCSharplexer()
        if self.fileExtention == "html" or self.fileExtention == "htm":
            self.setHtmllexe()

        if self.fileExtention == "sql":
            self.setSQLlexe()
        if self.fileExtention == "xml":
            self.setXMLlexe()
        if self.fileExtention == "css":
            self.setCSSlexe()

        return self.fullFileName

    def getSaveStatus(self):
        return self.saveStatus

    def saveFile(self, fileName):
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

        if self.fileExtention == "c" or self.fileExtention == "cpp":
            self.setCpplexer()
        if self.fileExtention == "py":
            self.setPythonlexer()
        if self.fileExtention == "java":
            self.setJavalexer()
        if self.fileExtention == "js":
            self.setJavaScriptlexer()
        if self.fileExtention == "cs":
            self.setCSharplexer()
        if self.fileExtention == "html" or self.fileExtention == "htm":
            self.setHtmllexe()
        if self.fileExtention == "css":
            self.setXMLlexe()
        if self.fileExtention == "sql":
            self.setSQLlexe()
        if self.fileExtention == "sql":
            self.setSQLlexe()
        if self.fileExtention == "xml":
            self.setXMLlexe()
        if self.fileExtention == "css":
            self.setCSSlexe()


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
        self.markerDefine(QsciScintilla.RightArrow,self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"),self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)

        lexer = QsciLexerCPP()


        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#FFFFFF"), 0)  # Default = 0
        lexer.setColor(QColor("#FEFB02"), 1)  # Comment = 1
        lexer.setColor(QColor("#FE6905"), 2)  # CommentLine = 2
        lexer.setColor(QColor("#FECC05"), 3)  # CommentDoc = 3
        lexer.setColor(QColor("#A9FE05"), 4)  # Number = 4
        lexer.setColor(QColor("#88E22B"), 5)  # Keyword = 5
        lexer.setColor(QColor("#8CDCFE"), 6)  # DoubleQuotedString = 6
        lexer.setColor(QColor("#05C6FE"), 7)  # SingleQuotedString = 7
        lexer.setColor(QColor("#058CFE"), 8)  # UUID = 8
        lexer.setColor(QColor("#05C6FE"), 9)  # PreProcessor = 9
        lexer.setColor(QColor("#FECC05"), 10)  # Operator = 10
        lexer.setColor(QColor("#FFF"), 11)  # Identifier = 1
        lexer.setColor(QColor("#05C6FE"), 12)  # UnclosedString = 12
        lexer.setColor(QColor("#AC7DCE"), 13)  # VerbatimString = 13
        lexer.setColor(QColor("#88E22B"), 14)  # Regex = 14
        lexer.setColor(QColor("#E7DB74"), 15)  # CommentLineDoc = 15
        lexer.setColor(QColor("#60D8EF"), 16)  # KeywordSet2 = 16
        lexer.setColor(QColor("#B36932"), 17)  # CommentDocKeyword = 17
        lexer.setColor(QColor("#519ABA"), 18)  # CommentDocKeywordError = 18
        lexer.setColor(QColor("#CDD100"), 19)  # GlobalClass = 19
        lexer.setColor(QColor("#05C6FE"), 20)  # RawString = 20
        lexer.setColor(QColor("#CE9172"), 21)  # TripleQuotedVerbatimString = 21
        lexer.setColor(QColor("#EC5166"), 22)  # HashQuotedString = 22
        lexer.setColor(QColor("#C5A84F"), 23)  # PreProcessorComment = 23,
        lexer.setColor(QColor("#B9644F"), 24)  # PreProcessorCommentLineDoc = 2
        lexer.setColor(QColor("#C3485C"), 25)  # UserLiteral = 25
        lexer.setColor(QColor("#498B60"), 26)  # TaskMarker = 26
        lexer.setColor(QColor("#E1898F"), 27)  # EscapeSequence = 27
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretWidth(5)
        self.setTabWidth(4)
        self.setIndentationGuides(True)
        self.setTabIndents(True)
        self.setAutoIndent(True)
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        #self.setZoom(2)
        my_list = [".", " ", "{","}","[","]","(",")", ":", ";"]
        #self.autoCompletionFillups()
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)
        lexer = QsciLexerPython()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#FFF"), 0)# Default = 0
        lexer.setColor(QColor("#05FE40"), 1)# Comment = 1
        lexer.setColor(QColor("#FFF"), 2)#  Number = 2#
        lexer.setColor(QColor("#E7DB74"), 3)#  DoubleQuotedString = 3#
        lexer.setColor(QColor("#B36932"), 4)# SingleQuotedString = 4#
        lexer.setColor(QColor("#FEFB02"), 5)#    Keyword = 5#
        lexer.setColor(QColor("#E7DB74"), 6)# TripleSingleQuotedString = 6#
        lexer.setColor(QColor("#E7DB74"), 7)# TripleDoubleQuotedString = 7#
        lexer.setColor(QColor("#88E22B"), 8)#  ClassName = 8#
        lexer.setColor(QColor("#FDD68A"), 9)#  FunctionMethodName = 9#
        lexer.setColor(QColor("#EC5166"), 10)#  Operator = 10#
        lexer.setColor(QColor("#60D8EF"), 11)#  Identifier = 11#
        lexer.setColor(QColor("#C5A84F"), 12)# CommentBlock = 12
        lexer.setColor(QColor("#B9644F"), 13)#  UnclosedString = 13
        lexer.setColor(QColor("#C3485C"), 14)#  HighlightedIdentifier = 14
        lexer.setColor(QColor("#498B60"), 15)# Decorator = 15

        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "{","}","[","]","(",")", ":", ";"]
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)
        lexer = QsciLexerJava()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#FFFFFF"), 0)  # Default = 0
        lexer.setColor(QColor("#FEFB02"), 1)  # Comment = 1
        lexer.setColor(QColor("#FE6905"), 2)  # CommentLine = 2
        lexer.setColor(QColor("#FECC05"), 3)  # CommentDoc = 3
        lexer.setColor(QColor("#A9FE05"), 4)  # Number = 4
        lexer.setColor(QColor("#88E22B"), 5)  # Keyword = 5
        lexer.setColor(QColor("#8CDCFE"), 6)  # DoubleQuotedString = 6
        lexer.setColor(QColor("#05C6FE"), 7)  # SingleQuotedString = 7
        lexer.setColor(QColor("#058CFE"), 8)  # UUID = 8
        lexer.setColor(QColor("#05C6FE"), 9)  # PreProcessor = 9
        lexer.setColor(QColor("#FECC05"), 10)  # Operator = 10
        lexer.setColor(QColor("#FFF"), 11)  # Identifier = 1
        lexer.setColor(QColor("#05C6FE"), 12)  # UnclosedString = 12
        lexer.setColor(QColor("#AC7DCE"), 13)  # VerbatimString = 13
        lexer.setColor(QColor("#88E22B"), 14)  # Regex = 14
        lexer.setColor(QColor("#E7DB74"), 15)  # CommentLineDoc = 15
        lexer.setColor(QColor("#60D8EF"), 16)  # KeywordSet2 = 16
        lexer.setColor(QColor("#B36932"), 17)  # CommentDocKeyword = 17
        lexer.setColor(QColor("#519ABA"), 18)  # CommentDocKeywordError = 18
        lexer.setColor(QColor("#CDD100"), 19)  # GlobalClass = 19
        lexer.setColor(QColor("#05C6FE"), 20)  # RawString = 20
        lexer.setColor(QColor("#CE9172"), 21)  # TripleQuotedVerbatimString = 21
        lexer.setColor(QColor("#EC5166"), 22)  # HashQuotedString = 22
        lexer.setColor(QColor("#C5A84F"), 23)  # PreProcessorComment = 23,
        lexer.setColor(QColor("#B9644F"), 24)  # PreProcessorCommentLineDoc = 2
        lexer.setColor(QColor("#C3485C"), 25)  # UserLiteral = 25
        lexer.setColor(QColor("#498B60"), 26)  # TaskMarker = 26
        lexer.setColor(QColor("#E1898F"), 27)  # EscapeSequence = 27
        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "{","}","[","]","(",")", ":", ";"]
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

    def setJavaScriptlexer(self):
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)
        lexer = QsciLexerJavaScript()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#FFFFFF"), 0)  # Default = 0
        lexer.setColor(QColor("#FEFB02"), 1)  # Comment = 1
        lexer.setColor(QColor("#FE6905"), 2)  # CommentLine = 2
        lexer.setColor(QColor("#FECC05"), 3)  # CommentDoc = 3
        lexer.setColor(QColor("#A9FE05"), 4)  # Number = 4
        lexer.setColor(QColor("#88E22B"), 5)  # Keyword = 5
        lexer.setColor(QColor("#8CDCFE"), 6)  # DoubleQuotedString = 6
        lexer.setColor(QColor("#05C6FE"), 7)  # SingleQuotedString = 7
        lexer.setColor(QColor("#058CFE"), 8)  # UUID = 8
        lexer.setColor(QColor("#05C6FE"), 9)  # PreProcessor = 9
        lexer.setColor(QColor("#FECC05"), 10)  # Operator = 10
        lexer.setColor(QColor("#FFF"), 11)  # Identifier = 1
        lexer.setColor(QColor("#05C6FE"), 12)  # UnclosedString = 12
        lexer.setColor(QColor("#AC7DCE"), 13)  # VerbatimString = 13
        lexer.setColor(QColor("#88E22B"), 14)  # Regex = 14
        lexer.setColor(QColor("#E7DB74"), 15)  # CommentLineDoc = 15
        lexer.setColor(QColor("#60D8EF"), 16)  # KeywordSet2 = 16
        lexer.setColor(QColor("#B36932"), 17)  # CommentDocKeyword = 17
        lexer.setColor(QColor("#519ABA"), 18)  # CommentDocKeywordError = 18
        lexer.setColor(QColor("#CDD100"), 19)  # GlobalClass = 19
        lexer.setColor(QColor("#05C6FE"), 20)  # RawString = 20
        lexer.setColor(QColor("#CE9172"), 21)  # TripleQuotedVerbatimString = 21
        lexer.setColor(QColor("#EC5166"), 22)  # HashQuotedString = 22
        lexer.setColor(QColor("#C5A84F"), 23)  # PreProcessorComment = 23,
        lexer.setColor(QColor("#B9644F"), 24)  # PreProcessorCommentLineDoc = 2
        lexer.setColor(QColor("#C3485C"), 25)  # UserLiteral = 25
        lexer.setColor(QColor("#498B60"), 26)  # TaskMarker = 26
        lexer.setColor(QColor("#E1898F"), 27)  # EscapeSequence = 27
        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "{","}","[","]","(",")", ":", ";"]
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
        # self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCom

    def setCSharplexer(self):
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)
        lexer = QsciLexerCSharp()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#FFFFFF"), 0)  # Default = 0
        lexer.setColor(QColor("#FEFB02"), 1)  # Comment = 1
        lexer.setColor(QColor("#FE6905"), 2)  # CommentLine = 2
        lexer.setColor(QColor("#FECC05"), 3)  # CommentDoc = 3
        lexer.setColor(QColor("#A9FE05"), 4)  # Number = 4
        lexer.setColor(QColor("#88E22B"), 5)  # Keyword = 5
        lexer.setColor(QColor("#8CDCFE"), 6)  # DoubleQuotedString = 6
        lexer.setColor(QColor("#05C6FE"), 7)  # SingleQuotedString = 7
        lexer.setColor(QColor("#058CFE"), 8)  # UUID = 8
        lexer.setColor(QColor("#05C6FE"), 9)  # PreProcessor = 9
        lexer.setColor(QColor("#FECC05"), 10)  # Operator = 10
        lexer.setColor(QColor("#FFF"), 11)  # Identifier = 1
        lexer.setColor(QColor("#05C6FE"), 12)  # UnclosedString = 12
        lexer.setColor(QColor("#AC7DCE"), 13)  # VerbatimString = 13
        lexer.setColor(QColor("#88E22B"), 14)  # Regex = 14
        lexer.setColor(QColor("#E7DB74"), 15)  # CommentLineDoc = 15
        lexer.setColor(QColor("#60D8EF"), 16)  # KeywordSet2 = 16
        lexer.setColor(QColor("#B36932"), 17)  # CommentDocKeyword = 17
        lexer.setColor(QColor("#519ABA"), 18)  # CommentDocKeywordError = 18
        lexer.setColor(QColor("#CDD100"), 19)  # GlobalClass = 19
        lexer.setColor(QColor("#05C6FE"), 20)  # RawString = 20
        lexer.setColor(QColor("#CE9172"), 21)  # TripleQuotedVerbatimString = 21
        lexer.setColor(QColor("#EC5166"), 22)  # HashQuotedString = 22
        lexer.setColor(QColor("#C5A84F"), 23)  # PreProcessorComment = 23,
        lexer.setColor(QColor("#B9644F"), 24)  # PreProcessorCommentLineDoc = 2
        lexer.setColor(QColor("#C3485C"), 25)  # UserLiteral = 25
        lexer.setColor(QColor("#498B60"), 26)  # TaskMarker = 26
        lexer.setColor(QColor("#E1898F"), 27)  # EscapeSequence = 27
        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "{","}","[","]","(",")", ":", ";"]

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
        # self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCom

    def setHtmllexe(self):
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)
        lexer = QsciLexerHTML()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0)  # Default = 0
        lexer.setColor(QColor("#A95151"), 1)  # Tag = 1
        lexer.setColor(QColor("#6C51A9"), 2)  # UnknownTag = 2
        lexer.setColor(QColor("#BDA5F4"), 3)  # Attribute = 3
        lexer.setColor(QColor("#46939C"), 4)  # UnknownAttribute = 4
        lexer.setColor(QColor("#C5BA40"), 5)  # HTMLNumber = 5
        lexer.setColor(QColor("#296C39"), 6)  # HTMLDoubleQuotedString = 6
        lexer.setColor(QColor("#96A82F"), 7)  # HTMLSingleQuotedString = 7
        lexer.setColor(QColor("#A87F2F"), 8)  # OtherInTag = 8
        lexer.setColor(QColor("#FDD68A"), 9)  # HTMLComment = 9
        lexer.setColor(QColor("#E1898F"), 10)  # Entity = 10
        lexer.setColor(QColor("#E1898F"), 11)  # XMLTagEnd = 11
        lexer.setColor(QColor("#E1898F"), 12)  # XMLStart = 12
        lexer.setColor(QColor("#E1898F"), 13)  # XMLEnd = 13
        lexer.setColor(QColor("#E1898F"), 14)  # Script = 14
        lexer.setColor(QColor("#E1898F"), 15)  # ASPAtStart = 15
        lexer.setColor(QColor("#E1898F"), 16)  # ASPStart = 16
        lexer.setColor(QColor("#E1898F"), 17)  # CDATA = 17
        lexer.setColor(QColor("#E1898F"), 18)  # PHPStart = 18
        lexer.setColor(QColor("#E1898F"), 19)  # HTMLValue = 19
        lexer.setColor(QColor("#E1898F"), 20)  # ASPXCComment = 20
        lexer.setColor(QColor("#E1898F"), 21)  # SGMLDefault = 21
        lexer.setColor(QColor("#E1898F"), 22)  # SGMLCommand = 22
        lexer.setColor(QColor("#A69C9C"), 23)  # SGMLParameter = 23
        lexer.setColor(QColor("#A69C9C"), 24)  # SGMLDoubleQuotedString = 24
        lexer.setColor(QColor("#A69C9C"), 25)  # SGMLSingleQuotedString = 25
        lexer.setColor(QColor("#A69C9C"), 26)  # SGMLError = 26
        lexer.setColor(QColor("#A69C9C"), 27)  # SGMLSpecial = 27
        lexer.setColor(QColor("#A69C9C"), 28)  # SGMLEntity = 28
        lexer.setColor(QColor("#A69C9C"), 29)  # SGMLComment = 29
        lexer.setColor(QColor("#A69C9C"), 30)  # SGMLParameterComment = 30
        lexer.setColor(QColor("#A69C9C"), 31)  # SGMLBlockDefault = 31
        lexer.setColor(QColor("#A69C9C"), 40)  # JavaScriptStart = 40
        lexer.setColor(QColor("#A69C9C"), 41)  # JavaScriptDefault = 41
        lexer.setColor(QColor("#A69C9C"), 42)  # JavaScriptComment = 42
        lexer.setColor(QColor("#A69C9C"), 43)  # JavaScriptCommentLine = 43
        lexer.setColor(QColor("#A69C9C"), 44)  # JavaScriptCommentDoc = 44
        lexer.setColor(QColor("#A69C9C"), 45)  # JavaScriptNumber = 45
        lexer.setColor(QColor("#A69C9C"), 46)  # JavaScriptWord = 46
        lexer.setColor(QColor("#A69C9C"), 47)  # JavaScriptKeyword = 47
        lexer.setColor(QColor("#A69C9C"), 48)  # JavaScriptDoubleQuotedString = 48
        lexer.setColor(QColor("#A69C9C"), 49)  # JavaScriptSingleQuotedString = 49
        lexer.setColor(QColor("#A69C9C"), 50)  # JavaScriptSymbol = 50
        lexer.setColor(QColor("#A69C9C"), 51)  # JavaScriptUnclosedString = 51
        lexer.setColor(QColor("#A69C9C"), 52)  # JavaScriptRegex = 52
        lexer.setColor(QColor("#A69C9C"), 55)  # ASPJavaScriptStart = 55
        lexer.setColor(QColor("#A69C9C"), 56)  # ASPJavaScriptDefault = 56
        lexer.setColor(QColor("#A69C9C"), 57)  # ASPJavaScriptComment = 57
        lexer.setColor(QColor("#A69C9C"), 58)  # ASPJavaScriptCommentLine = 58
        lexer.setColor(QColor("#A69C9C"), 59)  # ASPJavaScriptCommentDoc = 59
        lexer.setColor(QColor("#A69C9C"), 60)  # ASPJavaScriptNumber = 60
        lexer.setColor(QColor("#A69C9C"), 61)  # ASPJavaScriptWord = 61
        lexer.setColor(QColor("#A69C9C"), 62)  # ASPJavaScriptKeyword = 62
        lexer.setColor(QColor("#A69C9C"), 63)  # ASPJavaScriptDoubleQuotedString = 63
        lexer.setColor(QColor("#A69C9C"), 54)  # ASPJavaScriptSingleQuotedString = 64
        lexer.setColor(QColor("#A69C9C"), 65)  # ASPJavaScriptSymbol = 65
        lexer.setColor(QColor("#A69C9C"), 66)  # ASPJavaScriptUnclosedString = 66
        lexer.setColor(QColor("#A69C9C"), 67)  # ASPJavaScriptRegex = 67
        lexer.setColor(QColor("#A69C9C"), 70)  # VBScriptStart = 70
        lexer.setColor(QColor("#A69C9C"), 71)  # VBScriptDefault = 71
        lexer.setColor(QColor("#A69C9C"), 72)  # VBScriptComment = 72
        lexer.setColor(QColor("#A69C9C"), 73)  # VBScriptNumber = 73
        lexer.setColor(QColor("#A69C9C"), 74)  # VBScriptKeyword = 74
        lexer.setColor(QColor("#A69C9C"), 75)  # VBScriptString = 75
        lexer.setColor(QColor("#A69C9C"), 76)  # VBScriptIdentifier = 76
        lexer.setColor(QColor("#A69C9C"), 77)  # VBScriptUnclosedString = 77
        lexer.setColor(QColor("#A69C9C"), 80)  # ASPVBScriptStart = 80
        lexer.setColor(QColor("#A69C9C"), 81)  # ASPVBScriptDefault = 81
        lexer.setColor(QColor("#A69C9C"), 82)  # ASPVBScriptComment = 82
        lexer.setColor(QColor("#A69C9C"), 83)  # ASPVBScriptNumber = 83
        lexer.setColor(QColor("#A69C9C"), 84)  # ASPVBScriptKeyword = 84
        lexer.setColor(QColor("#A69C9C"), 85)  # ASPVBScriptString = 85
        lexer.setColor(QColor("#A69C9C"), 86)  # ASPVBScriptIdentifier = 86
        lexer.setColor(QColor("#A69C9C"), 87)  # ASPVBScriptUnclosedString = 87
        lexer.setColor(QColor("#A69C9C"), 90)  # PythonStart = 90
        lexer.setColor(QColor("#A69C9C"), 91)  # PythonDefault = 91
        lexer.setColor(QColor("#A69C9C"), 92)  # PythonComment = 92
        lexer.setColor(QColor("#A69C9C"), 93)  # PythonNumber = 93
        lexer.setColor(QColor("#A69C9C"), 94)  # PythonDoubleQuotedString = 94
        lexer.setColor(QColor("#A69C9C"), 95)  # PythonSingleQuotedString = 95
        lexer.setColor(QColor("#A69C9C"), 96)  # PythonKeyword = 96
        lexer.setColor(QColor("#A69C9C"), 97)  # PythonTripleSingleQuotedString = 97
        lexer.setColor(QColor("#A69C9C"), 98)  # PythonTripleDoubleQuotedString = 98
        lexer.setColor(QColor("#A69C9C"), 99)  # PythonClassName = 99
        lexer.setColor(QColor("#A69C9C"), 100)  # PythonFunctionMethodName = 100
        lexer.setColor(QColor("#A69C9C"), 101)  # PythonOperator = 101
        lexer.setColor(QColor("#A69C9C"), 102)  # PythonIdentifier = 102
        lexer.setColor(QColor("#A69C9C"), 105)  # ASPPythonStart = 105
        lexer.setColor(QColor("#A69C9C"), 106)  # ASPPythonDefault = 106
        lexer.setColor(QColor("#A69C9C"), 107)  # ASPPythonComment = 107
        lexer.setColor(QColor("#A69C9C"), 108)  # ASPPythonNumber = 108
        lexer.setColor(QColor("#A69C9C"), 109)  # ASPPythonDoubleQuotedString = 109
        lexer.setColor(QColor("#A69C9C"), 110)  # ASPPythonSingleQuotedString = 110
        lexer.setColor(QColor("#A69C9C"), 111)  # ASPPythonKeyword = 111
        lexer.setColor(QColor("#A69C9C"), 112)  # ASPPythonTripleSingleQuotedString = 112
        lexer.setColor(QColor("#A69C9C"), 113)  # ASPPythonTripleDoubleQuotedString = 113
        lexer.setColor(QColor("#A69C9C"), 114)  # ASPPythonClassName = 114
        lexer.setColor(QColor("#A69C9C"), 115)  # ASPPythonFunctionMethodName = 115
        lexer.setColor(QColor("#A69C9C"), 116)  # ASPPythonOperator = 116
        lexer.setColor(QColor("#A69C9C"), 117)  # ASPPythonIdentifier = 117
        lexer.setColor(QColor("#A69C9C"), 118)  # PHPDefault = 118
        lexer.setColor(QColor("#A69C9C"), 119)  # PHPDoubleQuotedString = 119
        lexer.setColor(QColor("#A69C9C"), 120)  # PHPSingleQuotedString = 120
        lexer.setColor(QColor("#A69C9C"), 121)  # PHPKeyword = 121
        lexer.setColor(QColor("#A69C9C"), 122)  # PHPNumber = 122
        lexer.setColor(QColor("#A69C9C"), 123)  # PHPVariable = 123
        lexer.setColor(QColor("#A69C9C"), 124)  # PHPComment = 124
        lexer.setColor(QColor("#A69C9C"), 125)  # PHPCommentLine = 125
        lexer.setColor(QColor("#A69C9C"), 126)  # PHPDoubleQuotedVariable = 126
        lexer.setColor(QColor("#A69C9C"), 127)  # PHPOperator = 127

        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "{","}","[","]","(",")","<",">", ":", ";"]

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
        # self.connect(shortcut_ctrl_space, SIGNAL(activated()), self,SLOT(autoCom

    def setCSSlexe(self):
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)
        lexer = QsciLexerCSS()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0)  # Default = 0
        lexer.setColor(QColor("#A95151"), 1)  # Tag = 1,
        lexer.setColor(QColor("#6C51A9"), 2)  # ClassSelector = 2,
        lexer.setColor(QColor("#BDA5F4"), 3)  # PseudoClass = 3,
        lexer.setColor(QColor("#46939C"), 4)  # UnknownPseudoClass = 4,
        lexer.setColor(QColor("#C5BA40"), 5)  # Operator = 5,
        lexer.setColor(QColor("#296C39"), 6)  # CSS1Property = 6,
        lexer.setColor(QColor("#96A82F"), 7)  # UnknownProperty = 7,
        lexer.setColor(QColor("#A87F2F"), 8)  # Value = 8,
        lexer.setColor(QColor("#FDD68A"), 9)  # Comment = 9,
        lexer.setColor(QColor("#E1898F"), 10)  # IDSelector = 10,
        lexer.setColor(QColor("#E1898F"), 11)  # Important = 11,
        lexer.setColor(QColor("#E1898F"), 12)  # AtRule = 12,
        lexer.setColor(QColor("#E1898F"), 13)  # DoubleQuotedString = 13,
        lexer.setColor(QColor("#E1898F"), 14)  # SingleQuotedString = 14,
        lexer.setColor(QColor("#E1898F"), 15)  # CSS2Property = 15,
        lexer.setColor(QColor("#E1898F"), 16)  # Attribute = 16,
        lexer.setColor(QColor("#E1898F"), 17)  # CSS3Property = 17,
        lexer.setColor(QColor("#E1898F"), 18)  # PseudoElement = 18,
        lexer.setColor(QColor("#E1898F"), 19)  # ExtendedCSSProperty = 19,
        lexer.setColor(QColor("#E1898F"), 20)  # ExtendedPseudoClass = 20,
        lexer.setColor(QColor("#E1898F"), 21)  # ExtendedPseudoElement = 21,
        lexer.setColor(QColor("#E1898F"), 22)  # MediaRule = 22,
        lexer.setColor(QColor("#E1898F"), 23)  # Variable = 23


        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "{", "}", "[", "]", "(", ")", ":", ";"]
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
    def setXMLlexe(self):
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretForegroundColor(QColor("#000000"))
        self.setCaretLineVisible(True)
        lexer = QsciLexerXML()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0)  # Default = 0
        lexer.setColor(QColor("#A95151"), 1)  # Comment = 1
        lexer.setColor(QColor("#6C51A9"), 2)  # Number = 2
        lexer.setColor(QColor("#BDA5F4"), 3)  # DoubleQuotedString = 3
        lexer.setColor(QColor("#46939C"), 4)  # SingleQuotedString = 4
        lexer.setColor(QColor("#C5BA40"), 5)  # Keyword = 5
        lexer.setColor(QColor("#296C39"), 6)  # TripleSingleQuotedString = 6
        lexer.setColor(QColor("#96A82F"), 7)  # TripleDoubleQuotedString = 7
        lexer.setColor(QColor("#A87F2F"), 8)  # ClassName = 8
        lexer.setColor(QColor("#FDD68A"), 9)  # FunctionMethodName = 9
        lexer.setColor(QColor("#E1898F"), 10)  # Operator = 10
        lexer.setColor(QColor("#E1898F"), 11)  # Identifier = 11
        lexer.setColor(QColor("#E1898F"), 12)  # CommentBlock = 12
        lexer.setColor(QColor("#E1898F"), 13)  # UnclosedString = 13
        lexer.setColor(QColor("#E1898F"), 14)  # HighlightedIdentifier = 14
        lexer.setColor(QColor("#E1898F"), 15)  # Decorator = 15

        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "{", "}", "[", "]", "(", ")", ":", ";"]
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
    def setSQLlexe(self):
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
        self.markerDefine(QsciScintilla.RightArrow, self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineBackgroundColor(QColor("#264026"))
        self.setCaretLineVisible(True)
        lexer = QsciLexerSQL()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0)  # Default = 0
        lexer.setColor(QColor("#A95151"), 1)  # Comment = 1
        lexer.setColor(QColor("#6C51A9"), 2)  # CommentLine = 2
        lexer.setColor(QColor("#BDA5F4"), 3)  #   CommentDoc = 3
        lexer.setColor(QColor("#46939C"), 4)  #  Number = 4
        lexer.setColor(QColor("#C5BA40"), 5)  # Keyword = 5
        lexer.setColor(QColor("#296C39"), 6)  #  DoubleQuotedString = 6
        lexer.setColor(QColor("#96A82F"), 7)  # SingleQuotedString = 7
        lexer.setColor(QColor("#A87F2F"), 8)  # PlusKeyword = 8,
        lexer.setColor(QColor("#FDD68A"), 9)  #  PlusPrompt = 9
        lexer.setColor(QColor("#E1898F"), 10)  #  Operator = 10
        lexer.setColor(QColor("#E1898F"), 11)  # Identifier = 11
        lexer.setColor(QColor("#E1898F"), 13)  #  PlusComment = 13,
        lexer.setColor(QColor("#E1898F"), 15)  # CommentLineHash = 15,
        lexer.setColor(QColor("#E1898F"), 17)  # CommentDocKeyword = 17,
        lexer.setColor(QColor("#E1898F"), 18)  #  CommentDocKeywordError = 18
        lexer.setColor(QColor("#E1898F"), 19)  # KeywordSet5 = 19
        lexer.setColor(QColor("#E1898F"), 20)  #  KeywordSet6 = 20,
        lexer.setColor(QColor("#E1898F"), 21)  #  KeywordSet7 = 21
        lexer.setColor(QColor("#E1898F"), 22)  # KeywordSet8 = 22
        lexer.setColor(QColor("#E1898F"), 23)  # QuotedIdentifier = 23,
        lexer.setColor(QColor("#E1898F"), 24)  #   QuotedOperator = 24


        self.setCaretForegroundColor(QColor("#FFFFFF"))
        my_list = [".", " ", "{", "}", "[", "]", "(", ")", ":", ";"]
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




