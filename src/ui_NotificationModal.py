# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_NotificationModal.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponentContainer import QCustomComponentContainer
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomLoadingIndicators import QCustomQProgressBar
class Ui_NotificationModal(object):
    def setupUi(self, NotificationModal):
        if not NotificationModal.objectName():
            NotificationModal.setObjectName(u"NotificationModal")
        NotificationModal.resize(491, 287)
        NotificationModal.setMinimumSize(QSize(475, 0))
        NotificationModal.setProperty("liveCompileStylesheet", True)
        NotificationModal.setProperty("paintQtDesignerUI", True)
        self.horizontalLayout = QHBoxLayout(NotificationModal)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self._ww = QWidget(NotificationModal)
        self._ww.setObjectName(u"_ww")
        self.horizontalLayout_3 = QHBoxLayout(self._ww)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(22, 22, 22, 22)
        self.notifIcon = QLabel(self._ww)
        self.notifIcon.setObjectName(u"notifIcon")
        self.notifIcon.setMinimumSize(QSize(50, 50))
        self.notifIcon.setMaximumSize(QSize(50, 50))
        self.notifIcon.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/circle-info.png"))
        self.notifIcon.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.notifIcon, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(self._ww)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QLabel(self.widget_2)
        self.header.setObjectName(u"header")
        font = QFont()
        font.setBold(True)
        self.header.setFont(font)
        self.header.setWordWrap(True)

        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.widget_2)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout.addWidget(self.customHorizontalSeparator)

        self.body = QLabel(self.widget_2)
        self.body.setObjectName(u"body")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setWordWrap(True)

        self.verticalLayout.addWidget(self.body)

        self.loadingProgressBar = QCustomQProgressBar(self.widget_2)
        self.loadingProgressBar.setObjectName(u"loadingProgressBar")

        self.verticalLayout.addWidget(self.loadingProgressBar)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.widget_2)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_2)

        self.footer = QFrame(self.widget_2)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.okayBtn = QPushButton(self.footer)
        self.okayBtn.setObjectName(u"okayBtn")

        self.horizontalLayout_2.addWidget(self.okayBtn)

        self.cancelBtn = QPushButton(self.footer)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_2.addWidget(self.cancelBtn)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self._ww)


        self.retranslateUi(NotificationModal)

        QMetaObject.connectSlotsByName(NotificationModal)
    # setupUi

    def retranslateUi(self, NotificationModal):
        NotificationModal.setWindowTitle(QCoreApplication.translate("NotificationModal", u"CustomComponentContainer", None))
        NotificationModal.setProperty("jsonStylesheetFilePath", QCoreApplication.translate("NotificationModal", u"json-styles/style.json", None))
        self.notifIcon.setText("")
        self.header.setText(QCoreApplication.translate("NotificationModal", u"Upgrade to get more trades/ Execution", None))
        self.body.setText(QCoreApplication.translate("NotificationModal", u"You have reached the trade limit on your current plan. To unlock more trading opportunities, consider upgrading your plan today.", None))
        self.okayBtn.setText(QCoreApplication.translate("NotificationModal", u"Buy / Upgrade", None))
        self.cancelBtn.setText(QCoreApplication.translate("NotificationModal", u"Get License", None))
    # retranslateUi

