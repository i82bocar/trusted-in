# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Generator.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomVerticalSeparator import QCustomVerticalSeparator
class Ui_GeneratorComponent(object):
    def setupUi(self, GeneratorComponent):
        if not GeneratorComponent.objectName():
            GeneratorComponent.setObjectName(u"GeneratorComponent")
        GeneratorComponent.resize(809, 507)
        self.verticalLayout = QVBoxLayout(GeneratorComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(GeneratorComponent)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.welcomeName = QLabel(self.frame)
        self.welcomeName.setObjectName(u"welcomeName")

        self.verticalLayout_2.addWidget(self.welcomeName)

        self.welcomeMessage = QLabel(self.frame)
        self.welcomeMessage.setObjectName(u"welcomeMessage")
        self.welcomeMessage.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.welcomeMessage)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.addBtn = QPushButton(self.frame_2)
        self.addBtn.setObjectName(u"addBtn")
        icon = QIcon()
        icon.addFile(u":/font_awesome_solid/icons/font_awesome/solid/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.addBtn)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(GeneratorComponent)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_3)

        self.widget_3 = QWidget(GeneratorComponent)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setSpacing(19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(400, 0))
        self.widget_2.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lengthLabel = QLabel(self.widget_2)
        self.lengthLabel.setObjectName(u"lengthLabel")
        font = QFont()
        font.setBold(True)
        self.lengthLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.lengthLabel)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lengthSlider = QSlider(self.frame_3)
        self.lengthSlider.setObjectName(u"lengthSlider")
        self.lengthSlider.setMinimum(4)
        self.lengthSlider.setMaximum(64)
        self.lengthSlider.setOrientation(Qt.Orientation.Horizontal)
        self.lengthSlider.setTickPosition(QSlider.TickPosition.NoTicks)

        self.horizontalLayout_2.addWidget(self.lengthSlider)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.widget_2)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.includeUppercaseSwitch = QCustomCheckBox(self.frame_4)
        self.includeUppercaseSwitch.setObjectName(u"includeUppercaseSwitch")
        self.includeUppercaseSwitch.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_4.addWidget(self.includeUppercaseSwitch, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.includeLowercaseSwitch = QCustomCheckBox(self.frame_5)
        self.includeLowercaseSwitch.setObjectName(u"includeLowercaseSwitch")
        self.includeLowercaseSwitch.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_5.addWidget(self.includeLowercaseSwitch, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.widget_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.includeNumbersSwitch = QCustomCheckBox(self.frame_6)
        self.includeNumbersSwitch.setObjectName(u"includeNumbersSwitch")
        self.includeNumbersSwitch.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_6.addWidget(self.includeNumbersSwitch, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.widget_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.includeSymbolsSwitch = QCustomCheckBox(self.frame_7)
        self.includeSymbolsSwitch.setObjectName(u"includeSymbolsSwitch")
        self.includeSymbolsSwitch.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_7.addWidget(self.includeSymbolsSwitch, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.widget_2)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator_2)

        self.generateButton = QPushButton(self.widget_2)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/generating_tokens.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generateButton.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.generateButton)


        self.horizontalLayout_12.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.customVerticalSeparator = QCustomVerticalSeparator(self.widget_3)
        self.customVerticalSeparator.setObjectName(u"customVerticalSeparator")
        self.customVerticalSeparator.setMaximumSize(QSize(16777215, 482))

        self.horizontalLayout_12.addWidget(self.customVerticalSeparator)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(300, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_4.addWidget(self.label_9)

        self.customHorizontalSeparator_4 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_4.setObjectName(u"customHorizontalSeparator_4")

        self.verticalLayout_4.addWidget(self.customHorizontalSeparator_4)

        self.generatedPasswordLineEdit = QLineEdit(self.widget_4)
        self.generatedPasswordLineEdit.setObjectName(u"generatedPasswordLineEdit")
        self.generatedPasswordLineEdit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.generatedPasswordLineEdit)

        self.customHorizontalSeparator_5 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_5.setObjectName(u"customHorizontalSeparator_5")

        self.verticalLayout_4.addWidget(self.customHorizontalSeparator_5)

        self.frame_8 = QFrame(self.widget_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.copyButton = QPushButton(self.frame_8)
        self.copyButton.setObjectName(u"copyButton")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/content_copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copyButton.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.copyButton)

        self.toggleVisibilityButton = QPushButton(self.frame_8)
        self.toggleVisibilityButton.setObjectName(u"toggleVisibilityButton")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_solid/icons/font_awesome/solid/eye-slash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggleVisibilityButton.setIcon(icon3)

        self.horizontalLayout_8.addWidget(self.toggleVisibilityButton)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.horizontalLayout_12.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(GeneratorComponent)

        QMetaObject.connectSlotsByName(GeneratorComponent)
    # setupUi

    def retranslateUi(self, GeneratorComponent):
        GeneratorComponent.setWindowTitle(QCoreApplication.translate("GeneratorComponent", u"CustomComponent", None))
        self.welcomeName.setText(QCoreApplication.translate("GeneratorComponent", u"Password Generator", None))
        self.welcomeMessage.setText(QCoreApplication.translate("GeneratorComponent", u"Create strong, secure passwords instantly.", None))
        self.addBtn.setText("")
        self.lengthLabel.setText(QCoreApplication.translate("GeneratorComponent", u"Length: 4", None))
        self.label_2.setText(QCoreApplication.translate("GeneratorComponent", u"4", None))
        self.label_3.setText(QCoreApplication.translate("GeneratorComponent", u"64", None))
        self.label_4.setText(QCoreApplication.translate("GeneratorComponent", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("GeneratorComponent", u"Include Uppercase", None))
        self.label_6.setText(QCoreApplication.translate("GeneratorComponent", u"Include Lowercase", None))
        self.label_7.setText(QCoreApplication.translate("GeneratorComponent", u"Include Numbers", None))
        self.label_8.setText(QCoreApplication.translate("GeneratorComponent", u"Include Symbols", None))
        self.generateButton.setText(QCoreApplication.translate("GeneratorComponent", u"Generate Password", None))
        self.label_9.setText(QCoreApplication.translate("GeneratorComponent", u"Generated Password", None))
        self.generatedPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("GeneratorComponent", u"Generated Pasword", None))
        self.copyButton.setText(QCoreApplication.translate("GeneratorComponent", u"Copy", None))
        self.toggleVisibilityButton.setText(QCoreApplication.translate("GeneratorComponent", u"Show/Hide", None))
    # retranslateUi

