# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_RightSidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomSidebar import QCustomSidebar
from Custom_Widgets.QCustomVerticalSeparator import QCustomVerticalSeparator
class Ui_RightBarComponent(object):
    def setupUi(self, RightBarComponent):
        if not RightBarComponent.objectName():
            RightBarComponent.setObjectName(u"RightBarComponent")
        RightBarComponent.resize(400, 318)
        self.verticalLayout = QVBoxLayout(RightBarComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.customSidebar = QCustomSidebar(RightBarComponent)
        self.customSidebar.setObjectName(u"customSidebar")
        self.customSidebar.setMinimumSize(QSize(0, 0))
        self.customSidebar.setMaximumSize(QSize(0, 0))
        self.customSidebar.setProperty("animationDuration", 1000)
        self.verticalLayout_2 = QVBoxLayout(self.customSidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.customSidebar)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closeBtn = QPushButton(self.widget)
        self.closeBtn.setObjectName(u"closeBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.closeBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.customVerticalSeparator = QCustomVerticalSeparator(self.widget)
        self.customVerticalSeparator.setObjectName(u"customVerticalSeparator")

        self.horizontalLayout.addWidget(self.customVerticalSeparator)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.customVerticalSeparator_2 = QCustomVerticalSeparator(self.widget)
        self.customVerticalSeparator_2.setObjectName(u"customVerticalSeparator_2")

        self.horizontalLayout.addWidget(self.customVerticalSeparator_2)

        self.clearBtn = QPushButton(self.widget)
        self.clearBtn.setObjectName(u"clearBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/delete_sweep.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.clearBtn)


        self.verticalLayout_2.addWidget(self.widget)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.customSidebar)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_2.addWidget(self.customHorizontalSeparator)

        self.notificationsContainer = QWidget(self.customSidebar)
        self.notificationsContainer.setObjectName(u"notificationsContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.notificationsContainer.sizePolicy().hasHeightForWidth())
        self.notificationsContainer.setSizePolicy(sizePolicy1)
        self.notificationsContainer.setMinimumSize(QSize(282, 0))
        self.verticalLayout_3 = QVBoxLayout(self.notificationsContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 194, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.notificationsContainer)


        self.verticalLayout.addWidget(self.customSidebar)


        self.retranslateUi(RightBarComponent)

        QMetaObject.connectSlotsByName(RightBarComponent)
    # setupUi

    def retranslateUi(self, RightBarComponent):
        RightBarComponent.setWindowTitle(QCoreApplication.translate("RightBarComponent", u"CustomComponent", None))
        self.customSidebar.setProperty("defaultWidth", QCoreApplication.translate("RightBarComponent", u"0", None))
        self.customSidebar.setProperty("defaultHeight", QCoreApplication.translate("RightBarComponent", u"parent", None))
        self.customSidebar.setProperty("collapsedWidth", QCoreApplication.translate("RightBarComponent", u"0", None))
        self.customSidebar.setProperty("collapsedHeight", QCoreApplication.translate("RightBarComponent", u"parent", None))
        self.customSidebar.setProperty("expandedWidth", QCoreApplication.translate("RightBarComponent", u"300", None))
        self.customSidebar.setProperty("expandedHeight", QCoreApplication.translate("RightBarComponent", u"parent", None))
        self.customSidebar.setProperty("toggleButtonName", QCoreApplication.translate("RightBarComponent", u"closeBtn", None))
        self.customSidebar.setProperty("iconCollapsed", "")
        self.customSidebar.setProperty("iconExpanded", "")
        self.closeBtn.setText("")
        self.label.setText(QCoreApplication.translate("RightBarComponent", u"Notifications", None))
        self.clearBtn.setText("")
    # retranslateUi

