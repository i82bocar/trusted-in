# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_SideBar.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomSidebar import QCustomSidebar
from Custom_Widgets.QCustomSidebarButton import QCustomSidebarButton
from Custom_Widgets.QCustomSidebarLabel import QCustomSidebarLabel
class Ui_SidebarComponent(object):
    def setupUi(self, SidebarComponent):
        if not SidebarComponent.objectName():
            SidebarComponent.setObjectName(u"SidebarComponent")
        SidebarComponent.resize(384, 485)
        self.verticalLayout = QVBoxLayout(SidebarComponent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.customSidebar = QCustomSidebar(SidebarComponent)
        self.customSidebar.setObjectName(u"customSidebar")
        self.verticalLayout_2 = QVBoxLayout(self.customSidebar)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.customSidebar)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.logoLabel = QCustomSidebarLabel(self.widget)
        self.logoLabel.setObjectName(u"logoLabel")
        icon = QIcon()
        icon.addFile(u":/images/images/TRUSTED IN_GREY.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoLabel.setProperty("icon", icon)
        self.logoLabel.setProperty("iconSize", QSize(141, 100))

        self.verticalLayout_3.addWidget(self.logoLabel)

        self.menuBtn = QCustomSidebarButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        self.menuBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/menu_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon1)
        self.menuBtn.setProperty("hideOnCollapse", False)
        self.menuBtn.setProperty("labelHidden", False)

        self.verticalLayout_3.addWidget(self.menuBtn)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.widget)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator)

        self.dashboardBtn = QCustomSidebarButton(self.widget)
        self.dashboardBtn.setObjectName(u"dashboardBtn")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/dashboard_customize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboardBtn.setIcon(icon2)
        self.dashboardBtn.setProperty("hideOnCollapse", False)

        self.verticalLayout_3.addWidget(self.dashboardBtn)

        self.vaultBtn = QCustomSidebarButton(self.widget)
        self.vaultBtn.setObjectName(u"vaultBtn")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_solid/icons/font_awesome/solid/vault.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vaultBtn.setIcon(icon3)
        self.vaultBtn.setProperty("hideOnCollapse", False)

        self.verticalLayout_3.addWidget(self.vaultBtn)

        self.generatorBtn = QCustomSidebarButton(self.widget)
        self.generatorBtn.setObjectName(u"generatorBtn")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/generating_tokens.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generatorBtn.setIcon(icon4)
        self.generatorBtn.setProperty("hideOnCollapse", False)

        self.verticalLayout_3.addWidget(self.generatorBtn)

        self.securityScanBtn = QCustomSidebarButton(self.widget)
        self.securityScanBtn.setObjectName(u"securityScanBtn")
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/shield.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.securityScanBtn.setIcon(icon5)
        self.securityScanBtn.setProperty("hideOnCollapse", False)

        self.verticalLayout_3.addWidget(self.securityScanBtn)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(self.customSidebar)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.settingsBtn = QCustomSidebarButton(self.widget_2)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon6)
        self.settingsBtn.setProperty("hideOnCollapse", False)

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.userBtn = QCustomSidebarButton(self.widget_2)
        self.userBtn.setObjectName(u"userBtn")
        icon7 = QIcon()
        icon7.addFile(u":/font_awesome_solid/icons/font_awesome/solid/circle-user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.userBtn.setIcon(icon7)
        self.userBtn.setProperty("hideOnCollapse", False)

        self.verticalLayout_4.addWidget(self.userBtn)

        self.aboutBtn = QCustomSidebarButton(self.widget_2)
        self.aboutBtn.setObjectName(u"aboutBtn")
        icon8 = QIcon()
        icon8.addFile(u":/material_design/icons/material_design/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aboutBtn.setIcon(icon8)

        self.verticalLayout_4.addWidget(self.aboutBtn)


        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.customSidebar)


        self.retranslateUi(SidebarComponent)

        QMetaObject.connectSlotsByName(SidebarComponent)
    # setupUi

    def retranslateUi(self, SidebarComponent):
        SidebarComponent.setWindowTitle(QCoreApplication.translate("SidebarComponent", u"CustomComponent", None))
        self.customSidebar.setProperty("defaultWidth", QCoreApplication.translate("SidebarComponent", u"150", None))
        self.customSidebar.setProperty("defaultHeight", QCoreApplication.translate("SidebarComponent", u"parent", None))
        self.customSidebar.setProperty("collapsedWidth", QCoreApplication.translate("SidebarComponent", u"60", None))
        self.customSidebar.setProperty("collapsedHeight", QCoreApplication.translate("SidebarComponent", u"parent", None))
        self.customSidebar.setProperty("expandedWidth", QCoreApplication.translate("SidebarComponent", u"150", None))
        self.customSidebar.setProperty("expandedHeight", QCoreApplication.translate("SidebarComponent", u"parent", None))
        self.customSidebar.setProperty("toggleButtonName", QCoreApplication.translate("SidebarComponent", u"menuBtn", None))
        self.customSidebar.setProperty("iconCollapsed", QCoreApplication.translate("SidebarComponent", u":/material_design/icons/material_design/menu.png", None))
        self.customSidebar.setProperty("iconExpanded", QCoreApplication.translate("SidebarComponent", u":/material_design/icons/material_design/menu_open.png", None))
        self.logoLabel.setProperty("text", "")
        self.menuBtn.setProperty("labelText", QCoreApplication.translate("SidebarComponent", u"Menu", None))
        self.dashboardBtn.setProperty("labelText", QCoreApplication.translate("SidebarComponent", u"Dashboard", None))
        self.vaultBtn.setProperty("labelText", QCoreApplication.translate("SidebarComponent", u"Vault", None))
        self.generatorBtn.setProperty("labelText", QCoreApplication.translate("SidebarComponent", u"Generator", None))
        self.securityScanBtn.setProperty("labelText", QCoreApplication.translate("SidebarComponent", u"Security Scan", None))
        self.settingsBtn.setProperty("labelText", QCoreApplication.translate("SidebarComponent", u"Settings", None))
        self.userBtn.setProperty("labelText", QCoreApplication.translate("SidebarComponent", u"User", None))
        self.aboutBtn.setProperty("labelText", QCoreApplication.translate("SidebarComponent", u"About", None))
    # retranslateUi

