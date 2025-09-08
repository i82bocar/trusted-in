# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_EditUsernameForm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
class Ui_EditUsernameForm(object):
    def setupUi(self, EditUsernameForm):
        if not EditUsernameForm.objectName():
            EditUsernameForm.setObjectName(u"EditUsernameForm")
        EditUsernameForm.resize(478, 234)
        EditUsernameForm.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(EditUsernameForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(EditUsernameForm)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.widget)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout_2.addWidget(self.customHorizontalSeparator_2)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.firstNameEdit = QLineEdit(self.frame)
        self.firstNameEdit.setObjectName(u"firstNameEdit")
        self.firstNameEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.firstNameEdit)

        self.lastNameEdit = QLineEdit(self.frame)
        self.lastNameEdit.setObjectName(u"lastNameEdit")
        self.lastNameEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.lastNameEdit)


        self.verticalLayout_2.addWidget(self.frame)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.widget)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_2.addWidget(self.customHorizontalSeparator)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.saveButton = QPushButton(self.frame_2)
        self.saveButton.setObjectName(u"saveButton")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.cancelButton = QPushButton(self.frame_2)
        self.cancelButton.setObjectName(u"cancelButton")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancelButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(EditUsernameForm)

        QMetaObject.connectSlotsByName(EditUsernameForm)
    # setupUi

    def retranslateUi(self, EditUsernameForm):
        EditUsernameForm.setWindowTitle(QCoreApplication.translate("EditUsernameForm", u"Frame", None))
        self.label.setText(QCoreApplication.translate("EditUsernameForm", u"Update Your Name", None))
        self.firstNameEdit.setPlaceholderText(QCoreApplication.translate("EditUsernameForm", u"First Name", None))
        self.lastNameEdit.setPlaceholderText(QCoreApplication.translate("EditUsernameForm", u"Last Name", None))
        self.saveButton.setText(QCoreApplication.translate("EditUsernameForm", u"Save Changes", None))
        self.cancelButton.setText(QCoreApplication.translate("EditUsernameForm", u"Cancel", None))
    # retranslateUi

