# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_About.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        if not AboutForm.objectName():
            AboutForm.setObjectName(u"AboutForm")
        AboutForm.resize(600, 600)
        AboutForm.setMinimumSize(QSize(600, 600))
        self.verticalLayout = QVBoxLayout(AboutForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(AboutForm)
        self.header.setObjectName(u"header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.welcomeName = QLabel(self.frame_2)
        self.welcomeName.setObjectName(u"welcomeName")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.welcomeName.setFont(font)

        self.verticalLayout_2.addWidget(self.welcomeName)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.closeBtn = QPushButton(self.frame_3)
        self.closeBtn.setObjectName(u"closeBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(AboutForm)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout.addWidget(self.customHorizontalSeparator)

        self.scrollArea = QScrollArea(AboutForm)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -764, 560, 1485))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/images/images/logo-horizontal-150px.png"))
        self.label_3.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(AboutForm)

        QMetaObject.connectSlotsByName(AboutForm)
    # setupUi

    def retranslateUi(self, AboutForm):
        AboutForm.setWindowTitle(QCoreApplication.translate("AboutForm", u"Form", None))
        self.welcomeName.setText(QCoreApplication.translate("AboutForm", u"About", None))
        self.closeBtn.setText("")
        self.label.setText(QCoreApplication.translate("AboutForm", u"<html><head/><body><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700;\">About TrustedIn</span></h2><p><span style=\" font-weight:700;\">TrustedIn</span> is a cross-platform desktop application designed to securely store, generate, and manage passwords and other sensitive information such as payment cards, contacts, bank accounts, and private notes. Developed with strong encryption and user-centric design, TrustedIn serves as a secure vault, empowering users to protect their digital identity with confidence and ease.</p><p>Originally created as a <span style=\" font-weight:700;\">Final Degree Project</span> at the <span style=\" font-weight:700;\">University of C\u00f3rdoba (Spain)</span>, the application combines academic rigor with real-world relevance, offering a powerful and intuitive solution to modern security challenges.</p><hr/><h3 style=\" margin-top:14px; margin-bottom:12px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Key Features</span></h3><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Encrypted Vault Storage</span><br/>Securely manage passwords, bank details, contacts, and notes using AES-256 and ChaCha20 encryption.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Password Generation</span><br/>Create strong, customized passwords based on user-defined criteria: length, symbols, numbers, and more.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Custom Encryption Se"
                        "lection</span><br/>Choose between different database encryption algorithms to suit your security preferences.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Security Health Analysis</span><br/>Identify weak, old, or reused credentials and receive suggestions for improving your digital hygiene.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Multi-Account Support</span><br/>Use multiple accounts on the same device, allowing shared usage while keeping data isolated and encrypted.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Offline Access &amp; Local Storage</span><br/>All data is stored <span style=\" font-weight:700;\">locally</span> and remains accessible offline\u2014n"
                        "o cloud storage, no external exposure.</li></ul><hr/><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Tech Stack</span></h3><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Language</span>: Python 3.11</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">GUI Framework</span>: PySide2 / PyQt5</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Database</span>: SQLite (Encrypted Local DB)</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">IDE</span>: PyCharm, VS Code</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">OS Compatibility</span>: Windows 11, Ubuntu 22.04</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Encryption</span>: AES-256, ChaCha20, PBKDF2</li></ul><hr/><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Academic Affiliation</span></h3><p>This application was developed as part of the <span style=\" font-weight:700;\">Final Degree Project (Trabajo Fin de Grado)</span> for the <span style=\" font-weight:700;\">Bachelor\u2019s Degree in Computer Engineering</span> at:</p><p><span style=\" font-weight:"
                        "700;\">University of C\u00f3rdoba, Spain</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("AboutForm", u"<html><head/><body><p><span style=\" font-weight:700;\">Project Director:</span> Dr. Juan Antonio Romero del Castillo<br/>Associate Professor, Department of Computer Science and Numerical Analysis</p><p><span style=\" font-weight:700;\">Author:</span> Rub\u00e9n Borrego Canovaca</p><hr/><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Privacy Commitment</span></h3><p>TrustedIn follows a <span style=\" font-weight:700;\">zero-knowledge architecture</span>. All your information stays encrypted on your device. We do not track, store, or transmit any personal data to external servers.</p><hr/><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Contact</span></h3><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><"
                        "li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Email</span>: <a href=\"mailto:support@trustedin.app\"><span style=\" text-decoration: underline; color:#8c61b8;\">support@trustedin.app</span></a></li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Phone</span>: +34-606-25-27-55</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Website</span>: <a href=\"https://trustedin.app/\"><span style=\" text-decoration: underline; color:#8c61b8;\">https://trustedin.app</span></a></li></ul><hr/><p><span style=\" font-weight:700;\">&quot;Your trust, your data, your control \u2014 TrustedIn.&quot;</span></p></body></html>", None))
    # retranslateUi

