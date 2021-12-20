# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiHoudiniHdaLinkerBXxOHD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
try:
    from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
        QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
        QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
        QPixmap, QRadialGradient)
    from PySide2.QtWidgets import *
except:
    from Qt.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
        QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
    from Qt.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
        QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
        QPixmap, QRadialGradient)
    from Qt.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(850, 800)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.checkProcessSelected = QCheckBox(Form)
        self.checkProcessSelected.setObjectName(u"checkProcessSelected")
        self.checkProcessSelected.setLayoutDirection(Qt.RightToLeft)
        self.checkProcessSelected.setChecked(False)

        self.horizontalLayout_3.addWidget(self.checkProcessSelected)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 7, 2, 1, 1)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_2.addWidget(self.tableView, 1, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushCheck = QPushButton(Form)
        self.pushCheck.setObjectName(u"pushCheck")
        self.pushCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.pushCheck)

        self.pushUncheck = QPushButton(Form)
        self.pushUncheck.setObjectName(u"pushUncheck")
        self.pushUncheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.pushUncheck)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushRemoveLinks = QPushButton(Form)
        self.pushRemoveLinks.setObjectName(u"pushRemoveLinks")
        self.pushRemoveLinks.setMinimumSize(QSize(150, 0))
        self.pushRemoveLinks.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_2.addWidget(self.pushRemoveLinks)

        self.pushCreateLinks = QPushButton(Form)
        self.pushCreateLinks.setObjectName(u"pushCreateLinks")
        self.pushCreateLinks.setMinimumSize(QSize(150, 0))
        self.pushCreateLinks.setMaximumSize(QSize(1000, 16777215))
        self.pushCreateLinks.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.pushCreateLinks)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditFilter = QLineEdit(Form)
        self.lineEditFilter.setObjectName(u"lineEditFilter")

        self.horizontalLayout.addWidget(self.lineEditFilter)

        self.checkBoxFilterChecked = QCheckBox(Form)
        self.checkBoxFilterChecked.setObjectName(u"checkBoxFilterChecked")

        self.horizontalLayout.addWidget(self.checkBoxFilterChecked)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.pushDelete = QPushButton(Form)
        self.pushDelete.setObjectName(u"pushDelete")
        self.pushDelete.setMaximumSize(QSize(500, 100))
        font = QFont()
        font.setPointSize(9)
        self.pushDelete.setFont(font)

        self.gridLayout_2.addWidget(self.pushDelete, 7, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkProcessSelected.setText(QCoreApplication.translate("Form", u"Process Selected Only", None))
        self.pushCheck.setText(QCoreApplication.translate("Form", u"Check Selected", None))
        self.pushUncheck.setText(QCoreApplication.translate("Form", u"Uncheck Selected", None))
        self.pushRemoveLinks.setText(QCoreApplication.translate("Form", u"Remove Links", None))
        self.pushCreateLinks.setText(QCoreApplication.translate("Form", u"Create Links", None))
        self.label.setText(QCoreApplication.translate("Form", u"Filter", None))
        self.checkBoxFilterChecked.setText(QCoreApplication.translate("Form", u"Filter Checked", None))
        self.pushDelete.setText(QCoreApplication.translate("Form", u"Delete Assets", None))
    # retranslateUi

