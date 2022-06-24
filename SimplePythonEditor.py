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
from PyQt5.QtWidgets import QApplication


class SimplePythonEditor(QsciScintilla):
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None):
        super(SimplePythonEditor, self).__init__(parent)

        # Set the default font
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)
        #self.setColor(QColor('lightblue'))
        self.setPaper(QColor('lightblue'))
                # Margin 0 is used for line numbers
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))

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
        self.setCaretLineVisible(True)


        # Set Python lexer
        # Set style for Python comments (style number 1) to a fixed-width
        # courier.
        #
        #lexer = QsciLexerPython()
        lexer = QsciLexerCPP()
        lexer.setDefaultFont(font)

        lexer.setDefaultPaper(QColor("#3c3c3c"))
        lexer.setDefaultColor(QColor("#f9f9f9"))
        lexer.setColor(QColor("#A69C9C"), 0);
        lexer.setColor(QColor("#A95151"), 1);
        lexer.setColor(QColor("#6C51A9"), 2);
        lexer.setColor(QColor("#BDA5F4"), 3);
        lexer.setColor(QColor("#46939C"), 4);
        lexer.setColor(QColor("#C5BA40"), 5);
        lexer.setColor(QColor("#479F5C"), 6);
        lexer.setColor(QColor("#96A82F"), 7);
        lexer.setColor(QColor("#A87F2F"), 8);
        lexer.setColor(QColor("#FDD68A"), 9);
        lexer.setColor(QColor("#E1898F"), 10);

        self.setCaretForegroundColor(QColor("#FFFFFF"))
        self.setCaretLineBackgroundColor(QColor("#000000"))

        self.setLexer(lexer)

        ## setup autocompletion
        api = Qsci.QsciAPIs(lexer)
        pyqt_path = os.path.dirname(PyQt5.__file__)
        api.load(os.path.join(pyqt_path, "Qt/qsci/api/python/Python-3.6.api"))

        api.prepare()
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionSource(Qsci.QsciScintilla.AcsAll)



        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        # not too small
        self.setMinimumSize(600, 450)

    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)