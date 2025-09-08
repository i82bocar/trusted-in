# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_QCustomQMainWindow.ui'
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
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponentContainer import QCustomComponentContainer
from Custom_Widgets.QCustomQMainWindow import QCustomQMainWindow
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
class Ui_CustomMainWindow(object):
    def setupUi(self, CustomMainWindow):
        if not CustomMainWindow.objectName():
            CustomMainWindow.setObjectName(u"CustomMainWindow")
        CustomMainWindow.resize(832, 128)
        CustomMainWindow.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/images/images/TRUSTED IN_GREY.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        CustomMainWindow.setWindowIcon(icon)
        CustomMainWindow.setProperty("liveCompileStylesheet", True)
        CustomMainWindow.setProperty("paintQtDesignerUI", True)
        self.centralwidget = QWidget(CustomMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.mainBodyPages = QCustomQStackedWidget(self.centralwidget)
        self.mainBodyPages.setObjectName(u"mainBodyPages")
        self.mainBodyPages.setProperty("slideTransition", True)
        self.mainBodyPages.setProperty("transitionTime", 1000)
        self.mainBodyPages.setProperty("fadeTime", 1000)
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.verticalLayout = QVBoxLayout(self.welcomePage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.welcomeComponentLoader = QCustomComponentContainer(self.welcomePage)
        self.welcomeComponentLoader.setObjectName(u"welcomeComponentLoader")
        self.welcomeComponentLoader.setProperty("previewComponent", False)

        self.verticalLayout.addWidget(self.welcomeComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.mainBodyPages.addWidget(self.welcomePage)
        self.contentPage = QWidget()
        self.contentPage.setObjectName(u"contentPage")
        self.horizontalLayout_2 = QHBoxLayout(self.contentPage)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.sideBarComponentLoader = QCustomComponentContainer(self.contentPage)
        self.sideBarComponentLoader.setObjectName(u"sideBarComponentLoader")
        self.sideBarComponentLoader.setMinimumSize(QSize(0, 0))
        self.sideBarComponentLoader.setProperty("previewComponent", False)

        self.horizontalLayout_2.addWidget(self.sideBarComponentLoader, 0, Qt.AlignmentFlag.AlignLeft)

        self.scrollArea = QScrollArea(self.contentPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 762, 78))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.contentPages = QCustomQStackedWidget(self.scrollAreaWidgetContents)
        self.contentPages.setObjectName(u"contentPages")
        self.contentPages.setProperty("slideTransition", True)
        self.contentPages.setProperty("transitionTime", 1000)
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.verticalLayout_3 = QVBoxLayout(self.dashboardPage)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashboardComponentLoader = QCustomComponentContainer(self.dashboardPage)
        self.dashboardComponentLoader.setObjectName(u"dashboardComponentLoader")

        self.verticalLayout_3.addWidget(self.dashboardComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.contentPages.addWidget(self.dashboardPage)
        self.vaultPage = QWidget()
        self.vaultPage.setObjectName(u"vaultPage")
        self.verticalLayout_4 = QVBoxLayout(self.vaultPage)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vaultComponentLoader = QCustomComponentContainer(self.vaultPage)
        self.vaultComponentLoader.setObjectName(u"vaultComponentLoader")
        self.vaultComponentLoader.setProperty("previewComponent", True)

        self.verticalLayout_4.addWidget(self.vaultComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.contentPages.addWidget(self.vaultPage)
        self.generatorPage = QWidget()
        self.generatorPage.setObjectName(u"generatorPage")
        self.verticalLayout_6 = QVBoxLayout(self.generatorPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.generatorComponentLoader = QCustomComponentContainer(self.generatorPage)
        self.generatorComponentLoader.setObjectName(u"generatorComponentLoader")
        self.generatorComponentLoader.setProperty("previewComponent", False)

        self.verticalLayout_6.addWidget(self.generatorComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.contentPages.addWidget(self.generatorPage)
        self.securityPage = QWidget()
        self.securityPage.setObjectName(u"securityPage")
        self.verticalLayout_5 = QVBoxLayout(self.securityPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.securityScanComponentLoader = QCustomComponentContainer(self.securityPage)
        self.securityScanComponentLoader.setObjectName(u"securityScanComponentLoader")
        self.securityScanComponentLoader.setProperty("previewComponent", False)

        self.verticalLayout_5.addWidget(self.securityScanComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.contentPages.addWidget(self.securityPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_7 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.settingsComponentLoader = QCustomComponentContainer(self.settingsPage)
        self.settingsComponentLoader.setObjectName(u"settingsComponentLoader")
        self.settingsComponentLoader.setProperty("previewComponent", False)

        self.verticalLayout_7.addWidget(self.settingsComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.contentPages.addWidget(self.settingsPage)
        self.userPage = QWidget()
        self.userPage.setObjectName(u"userPage")
        self.verticalLayout_9 = QVBoxLayout(self.userPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.userComponentLoader = QCustomComponentContainer(self.userPage)
        self.userComponentLoader.setObjectName(u"userComponentLoader")

        self.verticalLayout_9.addWidget(self.userComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.contentPages.addWidget(self.userPage)

        self.verticalLayout_8.addWidget(self.contentPages, 0, Qt.AlignmentFlag.AlignTop)

        self.footerComponentLoader = QCustomComponentContainer(self.scrollAreaWidgetContents)
        self.footerComponentLoader.setObjectName(u"footerComponentLoader")

        self.verticalLayout_8.addWidget(self.footerComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.rightBarComponentLoader = QCustomComponentContainer(self.contentPage)
        self.rightBarComponentLoader.setObjectName(u"rightBarComponentLoader")
        self.rightBarComponentLoader.setMinimumSize(QSize(0, 0))
        self.rightBarComponentLoader.setProperty("previewComponent", False)

        self.horizontalLayout_2.addWidget(self.rightBarComponentLoader, 0, Qt.AlignmentFlag.AlignRight)

        self.mainBodyPages.addWidget(self.contentPage)
        self.loginpage = QWidget()
        self.loginpage.setObjectName(u"loginpage")
        self.verticalLayout_2 = QVBoxLayout(self.loginpage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loginComponentLoader = QCustomComponentContainer(self.loginpage)
        self.loginComponentLoader.setObjectName(u"loginComponentLoader")

        self.verticalLayout_2.addWidget(self.loginComponentLoader, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.mainBodyPages.addWidget(self.loginpage)

        self.horizontalLayout.addWidget(self.mainBodyPages)

        CustomMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomMainWindow)

        self.mainBodyPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(CustomMainWindow)
    # setupUi

    def retranslateUi(self, CustomMainWindow):
        CustomMainWindow.setWindowTitle(QCoreApplication.translate("CustomMainWindow", u"TrustedIn", None))
        CustomMainWindow.setProperty("appTheme", QCoreApplication.translate("CustomMainWindow", u"Dark", None))
        self.welcomeComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_Welcome.py", None))
        self.sideBarComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_SideBar.py", None))
        self.dashboardComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_Dashboard.py", None))
        self.vaultComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_Vault.py", None))
        self.generatorComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_Generator.py", None))
        self.securityScanComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_SecurityScan.py", None))
        self.settingsComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_Settings.py", None))
        self.userComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_User.py", None))
        self.footerComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_Footer.py", None))
        self.rightBarComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_RightSidebar.py", None))
        self.loginComponentLoader.setProperty("filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_LoginForm.py", None))
    # retranslateUi

