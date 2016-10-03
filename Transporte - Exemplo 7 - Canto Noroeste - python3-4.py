# -*- coding: utf-8 -*-

# Programa desenvolvido em python para resolução de problema de transporte delimitado utilizando o método do canto
# noroeste para resolução.

# DESENVOLVIDO NA VERSÃO 3.4 python E PyQt4 (com Qt 4.8.7)
# INTERFACE GRÁFICA CRIADA COM O QtDesigner E TRADUZIDA PARA O PYTHON (COM O SUPORTE DA BIBLIOTECA PyQt 4) POR MEIO DO
#   UTILITÁRIO pyuic4 DISPONÍVEL NO DOWNLOAD DO KIT PyQt.
#
# PyQt > https://www.riverbankcomputing.com/software/pyqt/download
#   Inclue:
#       PyQt4
#       Qt
#       Qt Designer
#       Qt Linguist
#       Qt Assistant
#       pyuic4
#       pylupdate4
#       lrelease
#       pyrcc4
#       QScintilla
#
# Form implementation generated from reading ui file 'guinoroeste.ui'
#
# Created by: PyQt4 UI code generator 4.11.4

# IMPORTA AS BIBLIOTECAS DO PyQt QUE DÃO SUPORTE À INTERFACE GRÁFICA CRIADA PELO Qt Designer
from PyQt4 import QtCore, QtGui
import sys

# REALIZA TESTES DE EXECUÇÃO DA INTERFACE
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    # CRIA ELEMENTOS GRÁFICOS NA INTERFACE DO LAYOUT OBEDECENDO UMA ESTRUTURA DEFINIDA (GRID)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(700, 350)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 40, 221, 141))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(230, 40, 231, 141))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_5.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame_2)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 1, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_5.addWidget(self.label_15, 2, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame_2)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_5.addWidget(self.label_16, 3, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_5.addWidget(self.label_13, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.label_17 = QtGui.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(0, 10, 691, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(460, 70, 221, 111))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_22 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_7.addWidget(self.label_22, 3, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_7.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.frame_3)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_7.addWidget(self.label_23, 1, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.frame_3)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_7.addWidget(self.label_24, 2, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_7.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_7.addWidget(self.label_21, 0, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_7.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.frame_3)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_7.addWidget(self.label_25, 3, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.frame_3)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_7.addWidget(self.label_26, 1, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.frame_3)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_7.addWidget(self.label_27, 1, 3, 1, 1)
        self.label_28 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_7.addWidget(self.label_28, 0, 2, 1, 1)
        self.label_29 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_7.addWidget(self.label_29, 0, 3, 1, 1)
        self.label_30 = QtGui.QLabel(self.frame_3)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_7.addWidget(self.label_30, 2, 2, 1, 1)
        self.label_31 = QtGui.QLabel(self.frame_3)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_7.addWidget(self.label_31, 2, 3, 1, 1)
        self.label_32 = QtGui.QLabel(self.frame_3)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_7.addWidget(self.label_32, 3, 2, 1, 1)
        self.label_33 = QtGui.QLabel(self.frame_3)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_7.addWidget(self.label_33, 3, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.label_34 = QtGui.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(475, 50, 191, 20))
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 201, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.frame_4 = QtGui.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(230, 190, 451, 151))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_35 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_9.addWidget(self.label_35, 3, 0, 1, 1)
        self.label_36 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_9.addWidget(self.label_36, 1, 0, 1, 1)
        self.label_37 = QtGui.QLabel(self.frame_4)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_9.addWidget(self.label_37, 1, 1, 1, 1)
        self.label_38 = QtGui.QLabel(self.frame_4)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_9.addWidget(self.label_38, 2, 1, 1, 1)
        self.label_39 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_9.addWidget(self.label_39, 0, 0, 1, 1)
        self.label_40 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_9.addWidget(self.label_40, 0, 1, 1, 1)
        self.label_41 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_9.addWidget(self.label_41, 2, 0, 1, 1)
        self.label_42 = QtGui.QLabel(self.frame_4)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_9.addWidget(self.label_42, 3, 1, 1, 1)
        self.label_43 = QtGui.QLabel(self.frame_4)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_9.addWidget(self.label_43, 1, 2, 1, 1)
        self.label_44 = QtGui.QLabel(self.frame_4)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_9.addWidget(self.label_44, 1, 3, 1, 1)
        self.label_45 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_9.addWidget(self.label_45, 0, 2, 1, 1)
        self.label_46 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_9.addWidget(self.label_46, 0, 3, 1, 1)
        self.label_47 = QtGui.QLabel(self.frame_4)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.gridLayout_9.addWidget(self.label_47, 2, 2, 1, 1)
        self.label_48 = QtGui.QLabel(self.frame_4)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.gridLayout_9.addWidget(self.label_48, 2, 3, 1, 1)
        self.label_49 = QtGui.QLabel(self.frame_4)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.gridLayout_9.addWidget(self.label_49, 3, 2, 1, 1)
        self.label_50 = QtGui.QLabel(self.frame_4)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.gridLayout_9.addWidget(self.label_50, 3, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.label_51 = QtGui.QLabel(Form)
        self.label_51.setGeometry(QtCore.QRect(30, 270, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_51.setFont(font)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.label_52 = QtGui.QLabel(Form)
        self.label_52.setGeometry(QtCore.QRect(50, 290, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_52.setFont(font)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(17, 180, 661, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.frame.raise_()
        self.frame_2.raise_()
        self.label_17.raise_()
        self.frame_3.raise_()
        self.label_22.raise_()
        self.label_34.raise_()
        self.pushButton.raise_()
        self.frame_4.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.line.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # DEFINE AS PROPRIEDADES DO ELEMENTOS GRÁFICOS (ex. TEXTO DE EXIBIÇÃO)
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Programação Linear - Transporte - Trabalho 7", None))
        self.label_4.setText(_translate("Form", "2", None))
        self.label_3.setText(_translate("Form", "1", None))
        self.label_2.setText(_translate("Form", "Armazém", None))
        self.label.setText(_translate("Form", " Arroz disponível (kg)", None))
        self.label_5.setText(_translate("Form", "3", None))
        self.label_6.setText(_translate("Form", "200", None))
        self.label_7.setText(_translate("Form", "150", None))
        self.label_8.setText(_translate("Form", "100", None))
        self.label_10.setText(_translate("Form", "A", None))
        self.label_11.setText(_translate("Form", " Centro Consumidor", None))
        self.label_9.setText(_translate("Form", "B", None))
        self.label_12.setText(_translate("Form", "Demanda (kg)", None))
        self.label_14.setText(_translate("Form", "100", None))
        self.label_15.setText(_translate("Form", "300", None))
        self.label_16.setText(_translate("Form", "250", None))
        self.label_13.setText(_translate("Form", "C", None))
        self.label_17.setText(_translate("Form", "TRANSPORTE DE ARROZ ENTRE UM ARMAZÉM E UM CENTRO CONSUMIDOR", None))
        self.label_22.setText(_translate("Form", "3", None))
        self.label_19.setText(_translate("Form", "1", None))
        self.label_23.setText(_translate("Form", "$ 10", None))
        self.label_24.setText(_translate("Form", "$ 4", None))
        self.label_20.setText(_translate("Form", " De/Para", None))
        self.label_21.setText(_translate("Form", "A", None))
        self.label_18.setText(_translate("Form", "2", None))
        self.label_25.setText(_translate("Form", "$ 15", None))
        self.label_26.setText(_translate("Form", "$ 5", None))
        self.label_27.setText(_translate("Form", "$ 12", None))
        self.label_28.setText(_translate("Form", "B", None))
        self.label_29.setText(_translate("Form", "C", None))
        self.label_30.setText(_translate("Form", "$ 9", None))
        self.label_31.setText(_translate("Form", "$ 15", None))
        self.label_32.setText(_translate("Form", "$ 8", None))
        self.label_33.setText(_translate("Form", "$ 6", None))
        self.label_34.setText(_translate("Form", "Custos unitários de transporte ($/kg)", None))
        self.pushButton.setText(_translate("Form", "Calcular transporte e custo mínimo", None))
        self.pushButton.clicked.connect(self.calculoNoroeste)
        self.label_35.setText(_translate("Form", "3", None))
        self.label_36.setText(_translate("Form", "1", None))
        self.label_37.setText(_translate("Form", "-", None))
        self.label_38.setText(_translate("Form", "-", None))
        self.label_39.setText(_translate("Form", " De/Para", None))
        self.label_40.setText(_translate("Form", "A", None))
        self.label_41.setText(_translate("Form", "2", None))
        self.label_42.setText(_translate("Form", "-", None))
        self.label_43.setText(_translate("Form", "-", None))
        self.label_44.setText(_translate("Form", "-", None))
        self.label_45.setText(_translate("Form", "B", None))
        self.label_46.setText(_translate("Form", "C", None))
        self.label_47.setText(_translate("Form", "-", None))
        self.label_48.setText(_translate("Form", "-", None))
        self.label_49.setText(_translate("Form", "-", None))
        self.label_50.setText(_translate("Form", "-", None))
        self.label_51.setText(_translate("Form", "Custo mínimo:", None))
        self.label_52.setText(_translate("Form", "$ -", None))

    # CALCULO DO CANTO NOROESTE PARA O PROBLEMA DELIMITADO
    def calculoNoroeste(self):
        # recebe uma matriz, zera a coluna informada e retorna a nova matriz
        def zerarColuna(matriz, linha, coluna):
            lin = linha + 1

            while lin <= 3:
                matriz[lin][coluna] = 0
                lin += 1

            return matriz

        # recebe uma matriz, zera a linha informada e retorna a nova matriz
        def zerarLinha(matriz, linha, coluna):
            col = coluna + 1

            while col <= 3:
                matriz[linha][col] = 0
                col += 1

            return matriz

        # recebe uma matriz e a exibe formatada
        def exibirMatriz(matriz):
            row_labels = [1, 2, 3, 'N']
            print("     A   B   C   D")
            for row_label, row in zip(row_labels, matriz):
                print('%s [%s]' % (row_label, ' '.join('%03s' % x for x in row)))
            print("")

        # recebe a matriz de custos exibe formatada
        def exibirMatrizCustos(matriz):
            row_labels = [1, 2, 3]
            print("    A   B   C")
            for row_label, row in zip(row_labels, matriz):
                print('%s [%s]' % (row_label, ' '.join('$%02s' % x for x in row)))
            print("")

        # DEFINIÇÃO DAS MATRIZES COM OS DADOS DO PROBLEMA
        # matriz que guarda os destinos necessários, junto com as demandas e as disponibilidades
        quant = [['', '', '', 200],
                 ['', '', '', 150],
                 ['', '', '', 300],
                 [100, 300, 250, '']]

        # matriz com os custos de transporte da origem i para o consumidor j
        custos = [[10, 5, 12],
                  [4, 9, 15],
                  [15, 8, 6]]

        # matriz com os nomes de exibição para cada posição
        nomes = [['1A', '1B', '1C'],
                 ['2A', '2B', '2C'],
                 ['3A', '3B', '3C']]

        print("RESOLUÇÃO PROBLEMA DE TRANSPORTE - CANTO NOROESTE")
        print("Linhas equivalem a Armazens (i = 1, 2, 3)")
        print("Colunas equivalem a centro consumidor (j = A, B, C)")
        print("D (na coluna) equivale a DISPONIBILIDADE de arroz no armazém i")
        print("N (na linha) equivale a NECESSIDADE de arroz no centro consumidor j")
        print("")

        print("Matriz de custos para transporte do armazém i para o centro consumidor j")
        exibirMatrizCustos(custos)
        print("Matriz inicial: ")
        exibirMatriz(quant)

        # define a posição do canto noroeste: começa na primeira posição da matriz
        cantolin = cantocol = 0

        # percorre todos os campos da matriz realizando o cálculo do canto noroeste
        # SUCESSO: se a última linha e a última fileira forem zeros
        while cantolin < 3 and cantocol < 3:
            print("Canto noroeste => %s " % (nomes[cantolin][cantocol]))

            # se houver mais disponibilidade do que demanda, utilize toda a demanda
            if quant[cantolin][3] > quant[3][cantocol]:
                quant[cantolin][cantocol] = quant[3][cantocol]  # atribuindo toda a demanda necessária para a localidade
                quant[cantolin][3] -= quant[3][cantocol]  # retira o valor da demanda da disponibilidade
                quant = zerarColuna(quant, cantolin, cantocol)  # zera a coluna (atendeu toda a demanda)
                cantocol += 1  # posiciona o canto noroeste na próxima coluna (mas na mesma linha)
                print("Matriz parcial calculada: ")
                exibirMatriz(quant)
            else:  # realiza o processo acima, mas quando há mais demanda do que disponibilidade
                quant[cantolin][cantocol] = quant[cantolin][3]
                quant[3][cantocol] -= quant[cantolin][3]
                quant = zerarLinha(quant, cantolin, cantocol)
                cantolin += 1
                print("Matriz parcial calculada: ")
                exibirMatriz(quant)

        # EXIBIÇÃO DOS RESULTADOS
        i = j = 0
        custo = 0
        # percorre a matriz com os dados (ignorando a coluna 3 (disponibilidade) e linha 3 (demanda))
        while i < 3:  # percorrerá linhas 0, 1 e 2 da matriz
            while j < 3:  # percorrerá as colunas 0, 1 e 2 da matriz
                custo += quant[i][j] * custos[i][j]  # calcula o custo total de acordo com a qtd e custo de transporte
                j += 1  # passa para a próxima coluna
            i += 1  # passa para a próxima linha
            j = 0  # retorna para a primeira coluna (para percorrer todas as colunas da linha novamente)

        # exibe a matriz resultado
        print("Matriz final: ")
        exibirMatriz(quant)

        print("Custo mínimo calculado: $ ", custo)

        # ATUALIZANDO INTERFACE GRÁFICA COM OS VALORES CALCULADOS
        # O NOME DOS CAMPOS (label_52, 37, etc...) FORAM GERADOS AUTOMATICAMENTE, MAS SÃO IDENTIFICADOS PELA SUA
        #  NA INTERFACE GRÁFICA
        self.label_52.setText(_translate("Form", str("$ %d" % custo), None))

        # TABELA COM OS LABELS (TEXTOS NA INTERFACE GRÁFICA) CONFORME A SUA POSIÇÃO EXIBIDA NA TABELA
        tabelaResultadoGUI = [[self.label_37, self.label_43, self.label_44],
                              [self.label_38, self.label_47, self.label_48],
                              [self.label_42, self.label_49, self.label_50]]

        # PERCORRE TODA A TABELA DE CAMPOS DA INTERFACE GRÁFICA ATRIBUINDO O VALOR CONTIDO NA MESMA POSIÇÃO DA MATRIZ
        #   RESULTANTE
        i = j = 0
        while i < 3:
            while j < 3:
                tabelaResultadoGUI[i][j].setText(_translate("Form", str(quant[i][j]), None))
                j += 1
            i += 1
            j = 0

# INICIALIZAÇÃO DO PROGRAMA
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
