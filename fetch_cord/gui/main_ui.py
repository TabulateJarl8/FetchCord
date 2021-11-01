# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 452)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 178, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.distroInfo = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.distroInfo.setChecked(True)
        self.distroInfo.setObjectName("distroInfo")
        self.verticalLayout.addWidget(self.distroInfo)
        self.hardwareInfo = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.hardwareInfo.setChecked(True)
        self.hardwareInfo.setObjectName("hardwareInfo")
        self.verticalLayout.addWidget(self.hardwareInfo)
        self.shellInfo = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.shellInfo.setChecked(True)
        self.shellInfo.setObjectName("shellInfo")
        self.verticalLayout.addWidget(self.shellInfo)
        self.hostInfo = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.hostInfo.setChecked(True)
        self.hostInfo.setObjectName("hostInfo")
        self.verticalLayout.addWidget(self.hostInfo)
        self.memoryUnits = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.memoryUnits.setPlaceholderText("")
        self.memoryUnits.setObjectName("memoryUnits")
        self.memoryUnits.addItem("")
        self.memoryUnits.addItem("")
        self.verticalLayout.addWidget(self.memoryUnits)
        self.terminalName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.terminalName.setObjectName("terminalName")
        self.verticalLayout.addWidget(self.terminalName)
        self.terminalFont = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.terminalFont.setObjectName("terminalFont")
        self.verticalLayout.addWidget(self.terminalFont)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(250, 20, 381, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pauseCycle = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.pauseCycle.setMinimum(0)
        self.pauseCycle.setMaximum(86400)
        self.pauseCycle.setProperty("value", 0)
        self.pauseCycle.setObjectName("pauseCycle")
        self.gridLayout_2.addWidget(self.pauseCycle, 2, 1, 1, 1)
        self.pollRate = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.pollRate.setMaximum(86400)
        self.pollRate.setProperty("value", 3)
        self.pollRate.setObjectName("pollRate")
        self.gridLayout_2.addWidget(self.pollRate, 3, 1, 1, 1)
        self.cycleTime = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.cycleTime.setMinimum(15)
        self.cycleTime.setMaximum(86400)
        self.cycleTime.setProperty("value", 30)
        self.cycleTime.setObjectName("cycleTime")
        self.gridLayout_2.addWidget(self.cycleTime, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.disableNeofetchConfig = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.disableNeofetchConfig.setObjectName("disableNeofetchConfig")
        self.gridLayout_2.addWidget(self.disableNeofetchConfig, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 200, 381, 190))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.installSystemd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.installSystemd.setObjectName("installSystemd")
        self.gridLayout.addWidget(self.installSystemd, 0, 0, 1, 1)
        self.disableSystemd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.disableSystemd.setObjectName("disableSystemd")
        self.gridLayout.addWidget(self.disableSystemd, 1, 1, 1, 1)
        self.uninstallSystemd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.uninstallSystemd.setObjectName("uninstallSystemd")
        self.gridLayout.addWidget(self.uninstallSystemd, 0, 1, 1, 1)
        self.enableSystemd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.enableSystemd.setObjectName("enableSystemd")
        self.gridLayout.addWidget(self.enableSystemd, 1, 0, 1, 1)
        self.stopSystemd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stopSystemd.setObjectName("stopSystemd")
        self.gridLayout.addWidget(self.stopSystemd, 2, 1, 1, 1)
        self.testingBranch = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.testingBranch.setObjectName("testingBranch")
        self.gridLayout.addWidget(self.testingBranch, 3, 0, 1, 1)
        self.startSystemd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startSystemd.setObjectName("startSystemd")
        self.gridLayout.addWidget(self.startSystemd, 2, 0, 1, 1)
        self.update = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.update.setObjectName("update")
        self.gridLayout.addWidget(self.update, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FetchCord GUI"))
        self.distroInfo.setText(_translate("Dialog", "Show Distro Info"))
        self.hardwareInfo.setText(_translate("Dialog", "Show Hardware Info"))
        self.shellInfo.setText(_translate("Dialog", "Show Shell/Terminal Info"))
        self.hostInfo.setText(_translate("Dialog", "Show Host Info"))
        self.memoryUnits.setItemText(0, _translate("Dialog", "Mebibytes (MiB)"))
        self.memoryUnits.setItemText(1, _translate("Dialog", "Gibibytes (GiB)"))
        self.terminalName.setPlaceholderText(_translate("Dialog", "Custom Terminal Name"))
        self.terminalFont.setPlaceholderText(_translate("Dialog", "Custom Terminal Font"))
        self.pauseCycle.setSuffix(_translate("Dialog", "sec"))
        self.pollRate.setSuffix(_translate("Dialog", "sec"))
        self.cycleTime.setSuffix(_translate("Dialog", "sec"))
        self.label_4.setText(_translate("Dialog", "Cycle Time:"))
        self.label_3.setText(_translate("Dialog", "Pause Cycle:"))
        self.disableNeofetchConfig.setText(_translate("Dialog", "Disable custom Neofetch config"))
        self.label_5.setText(_translate("Dialog", "Poll Rate:"))
        self.installSystemd.setText(_translate("Dialog", "Install as systemd service"))
        self.disableSystemd.setText(_translate("Dialog", "Disable systemd service"))
        self.uninstallSystemd.setText(_translate("Dialog", "Uninstall systemd service"))
        self.enableSystemd.setText(_translate("Dialog", "Enable systemd service"))
        self.stopSystemd.setText(_translate("Dialog", "Stop systemd service"))
        self.testingBranch.setText(_translate("Dialog", "Testing Branch"))
        self.startSystemd.setText(_translate("Dialog", "Start systemd service"))
        self.update.setText(_translate("Dialog", "Update database"))
