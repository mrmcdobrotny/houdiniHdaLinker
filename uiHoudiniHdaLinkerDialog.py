# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiHoudiniHdaLinkerDialogOXWeRX.ui'
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
    
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(352, 298)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushDecline = QPushButton(Dialog)
        self.pushDecline.setObjectName(u"pushDecline")
        self.pushDecline.setMinimumSize(QSize(100, 0))
        self.pushDecline.setMaximumSize(QSize(1000, 16777215))

        self.horizontalLayout_2.addWidget(self.pushDecline)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushAccept = QPushButton(Dialog)
        self.pushAccept.setObjectName(u"pushAccept")
        self.pushAccept.setMinimumSize(QSize(100, 0))
        self.pushAccept.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.pushAccept)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"The following files are to be deleted permanently:", None))
        self.pushDecline.setText(QCoreApplication.translate("Dialog", u"Decline", None))
        self.pushAccept.setText(QCoreApplication.translate("Dialog", u"Accept", None))
    # retranslateUi

