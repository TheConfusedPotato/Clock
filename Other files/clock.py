import functools
from colorama import Fore
from alarmRinging import *
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from PyQt5.QtCore import QTimer
import pygame

opener = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Other files\alarmParamters", "r+")


def Convert(string):
    li = list(string.split(" "))
    return li


a = opener.read()
opener.close()

str1 = a
allParameters = Convert(str1)

alarmsTitle = allParameters[0]
alarmsTime = allParameters[1]
alarmsDayList = allParameters[2]
alarmsTone = allParameters[3]
alarmsEnabled = allParameters[4]
alarmsTitle2 = allParameters[5]
alarmsTime2 = allParameters[6]
alarmsDayList2 = allParameters[7]
alarmsTone2 = allParameters[8]
alarmsEnabled2 = allParameters[9]
alarmsTitle3 = allParameters[10]
alarmsTime3 = allParameters[11]
alarmsDayList3 = allParameters[12]
alarmsTone3 = allParameters[13]
alarmsEnabled3 = allParameters[14]
alarmsTitle4 = allParameters[15]
alarmsTime4 = allParameters[16]
alarmsDayList4 = allParameters[17]
alarmsTone4 = allParameters[18]
alarmsEnabled4 = allParameters[19]


pygame.init()
pygame.mixer.init()

print(Fore.BLUE+alarmsDayList)
print(Fore.RED+alarmsDayList2)
print(Fore.GREEN+alarmsDayList3)
print(Fore.YELLOW+alarmsDayList4)


class Ui_Form(QtWidgets.QDialog):
    def setupUi(self, Form2):
        Form2.setObjectName("Form")
        Form2.resize(350, 651)
        Form2.setStyleSheet("background-color:black")
        self.label_standard = QtWidgets.QLabel(Form2)
        self.label_standard.setGeometry(QtCore.QRect(-40, 0, 441, 851))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.label_standard.setFont(font)
        self.label_standard.setStyleSheet("QPushButton{\n"
                                          "    color:white;\n"
                                          "    background-color: rgb(52, 98, 63);\n"
                                          "    border-radius: 5px\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed{\n"
                                          "\n"
                                          "    background-color:rgb(20,20,20);\n"
                                          "    border-radius: 5px\n"
                                          "}")
        self.label_standard.setText("")
        self.label_standard.setObjectName("label_standard")
        self.label_title = QtWidgets.QLabel(Form2)
        self.label_title.setGeometry(QtCore.QRect(80, 40, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(48)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:white;\n"
                                       "background-color:rgba(0,0,0,0)")
        self.label_title.setObjectName("label_title")
        self.pushButton_standard = QtWidgets.QPushButton(Form2)
        self.pushButton_standard.setGeometry(QtCore.QRect(40, 540, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.pushButton_standard.setFont(font)
        self.pushButton_standard.setStyleSheet("QPushButton{\n"
                                               "    color:white;\n"
                                               "        background-color:rgb(20,20,20);\n"
                                               "    border-radius: 5px\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed{\n"
                                               "    background-color:black;\n"
                                               "    color:black;\n"
                                               "    border-radius: 5px\n"
                                               "}")
        self.pushButton_standard.setObjectName("pushButton_standard")
        self.pushButton_standard_2 = QtWidgets.QPushButton(Form2)
        self.pushButton_standard_2.setGeometry(QtCore.QRect(200, 540, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.pushButton_standard_2.setFont(font)
        self.pushButton_standard_2.setStyleSheet("QPushButton{\n"
                                                 "    color:white;\n"
                                                 "        background-color:rgb(20,20,20);\n"
                                                 "    border-radius: 5px\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed{\n"
                                                 "    background-color:black;\n"
                                                 "    color:black;\n"
                                                 "    border-radius: 5px\n"
                                                 "}")
        self.pushButton_standard_2.setObjectName("pushButton_standard_2")
        self.label_title_2 = QtWidgets.QLabel(Form2)
        self.label_title_2.setGeometry(QtCore.QRect(130, 220, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(36)
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet("color:white;\n"
                                         "background-color:rgb(0,0,0,0)")
        self.label_title_2.setText("")
        self.label_title_2.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-clock-100.png"))
        self.label_title_2.setObjectName("label_title_2")
        self.label_title_3 = QtWidgets.QLabel(Form2)
        self.label_title_3.setGeometry(QtCore.QRect(120, 360, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(36)
        self.label_title_3.setFont(font)
        self.label_title_3.setStyleSheet("color:white;\n"
                                         "background-color:rgba(0,0,0,0)")
        self.label_title_3.setObjectName("label_title_3")

        # noinspection PyUnresolvedReferences
        self.pushButton_standard.clicked.connect(self.close)

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "Wake up "))
        self.pushButton_standard.setText(_translate("Form", "Dismiss"))
        self.pushButton_standard_2.setText(_translate("Form", "Snooze"))
        self.label_title_3.setText(_translate("Form", "5:00 am"))

    def close(self):
        app2.closeAllWindows()
        pygame.mixer.music.stop()


class mainApp(QtWidgets.QWidget):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(821, 523)
        Form.setStyleSheet("background-color:black")
        self.labelImage = QtWidgets.QLabel(Form)
        self.labelImage.setGeometry(QtCore.QRect(560, 0, 381, 671))
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("../../../Downloads/pexels-golden-jojo-2409038 (1).jpg"))
        self.labelImage.setObjectName("labelImage")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(360, 540, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white; \n"
                                   "\n"
                                   "border-radius:5px")
        self.label_7.setObjectName("label_7")
        self.labelAlarms = QtWidgets.QLabel(Form)
        self.labelAlarms.setGeometry(QtCore.QRect(590, 50, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelAlarms.setFont(font)
        self.labelAlarms.setStyleSheet("background-color: rgba(1, 32, 15,0);\n"
                                       "color:white;\n"
                                       "")
        self.labelAlarms.setObjectName("labelAlarms")
        self.labelTimer = QtWidgets.QLabel(Form)
        self.labelTimer.setGeometry(QtCore.QRect(590, 140, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelTimer.setFont(font)
        self.labelTimer.setStyleSheet("color:white;\n"
                                      "background-color:rgba(20,20,20,0)")
        self.labelTimer.setObjectName("labelTimer")
        self.labelStopwatch = QtWidgets.QLabel(Form)
        self.labelStopwatch.setGeometry(QtCore.QRect(590, 230, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelStopwatch.setFont(font)
        self.labelStopwatch.setStyleSheet("color:white;\n"
                                          "background-color:rgba(20,20,20,0)")
        self.labelStopwatch.setObjectName("labelStopwatch")
        self.labelReminders = QtWidgets.QLabel(Form)
        self.labelReminders.setGeometry(QtCore.QRect(590, 320, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelReminders.setFont(font)
        self.labelReminders.setStyleSheet("color:white;\n"
                                          "background-color:rgba(20,20,20,0)")
        self.labelReminders.setObjectName("labelReminders")
        self.widgetAlarmsParent = QtWidgets.QWidget(Form)
        self.widgetAlarmsParent.setGeometry(QtCore.QRect(40, 60, 491, 431))
        self.widgetAlarmsParent.setObjectName("widgetAlarmsParent")
        self.widgetAlarmExtended = QtWidgets.QWidget(self.widgetAlarmsParent)
        self.widgetAlarmExtended.setGeometry(QtCore.QRect(20, 100, 431, 261))
        self.widgetAlarmExtended.setStyleSheet("background-color: rgb(25,25,25);\n"
                                               "border-radius:10px")
        self.widgetAlarmExtended.setObjectName("widgetAlarmExtended")
        self.labelAlarmsTime = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsTime.setGeometry(QtCore.QRect(320, 10, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(25)
        self.labelAlarmsTime.setFont(font)
        self.labelAlarmsTime.setStyleSheet("color:white")
        self.labelAlarmsTime.setObjectName("labelAlarmsTime")
        self.labelAlarmsMon = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsMon.setGeometry(QtCore.QRect(20, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelAlarmsMon.setFont(font)
        self.labelAlarmsMon.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsMon.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsMon.setObjectName("labelAlarmsMon")
        self.labelAlarmsTue = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsTue.setGeometry(QtCore.QRect(60, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelAlarmsTue.setFont(font)
        self.labelAlarmsTue.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsTue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsTue.setObjectName("labelAlarmsTue")
        self.labelAlarmsWed = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsWed.setGeometry(QtCore.QRect(100, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelAlarmsWed.setFont(font)
        self.labelAlarmsWed.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsWed.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsWed.setObjectName("labelAlarmsWed")
        self.labelAlarmsThu = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsThu.setGeometry(QtCore.QRect(140, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelAlarmsThu.setFont(font)
        self.labelAlarmsThu.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsThu.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsThu.setObjectName("labelAlarmsThu")
        self.labelAlarmsFri = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsFri.setGeometry(QtCore.QRect(180, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelAlarmsFri.setFont(font)
        self.labelAlarmsFri.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsFri.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsFri.setObjectName("labelAlarmsFri")
        self.labelAlarmsSat = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsSat.setGeometry(QtCore.QRect(220, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelAlarmsSat.setFont(font)
        self.labelAlarmsSat.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsSat.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsSat.setObjectName("labelAlarmsSat")
        self.labelAlarmsSun = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsSun.setGeometry(QtCore.QRect(260, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelAlarmsSun.setFont(font)
        self.labelAlarmsSun.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsSun.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsSun.setObjectName("labelAlarmsSun")
        self.labelAlarmsDelete = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsDelete.setGeometry(QtCore.QRect(10, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(14)
        self.labelAlarmsDelete.setFont(font)
        self.labelAlarmsDelete.setStyleSheet("color:white;\n"
                                             "\n"
                                             "border-radius:10px")
        self.labelAlarmsDelete.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsDelete.setObjectName("labelAlarmsDelete")
        self.labelAlarmsChangeTone = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsChangeTone.setGeometry(QtCore.QRect(130, 150, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(14)
        self.labelAlarmsChangeTone.setFont(font)
        self.labelAlarmsChangeTone.setStyleSheet("color:white;\n"
                                                 "\n"
                                                 "border-radius:10px")
        self.labelAlarmsChangeTone.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsChangeTone.setObjectName("labelAlarmsChangeTone")
        self.labelAlarmsName = QtWidgets.QLabel(self.widgetAlarmExtended)
        self.labelAlarmsName.setGeometry(QtCore.QRect(20, 10, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(28)
        self.labelAlarmsName.setFont(font)
        self.labelAlarmsName.setStyleSheet("color:white")
        self.labelAlarmsName.setObjectName("labelAlarmsName")

        self.pushButtonAlarmsSaveChanges = QtWidgets.QPushButton(self.widgetAlarmExtended)
        self.pushButtonAlarmsSaveChanges.setGeometry(QtCore.QRect(320, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(14)
        self.pushButtonAlarmsSaveChanges.setFont(font)
        self.pushButtonAlarmsSaveChanges.setStyleSheet("QPushButton{\n"
                                                       "    color:white;\n"
                                                       "    background-color: rgb(52, 98, 63);\n"
                                                       "    border-radius: 5px\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:pressed{\n"
                                                       "    color:rgb(25,25,25);\n"
                                                       "    background-color:rgb(25,25,25);\n"
                                                       "    border-radius: 5px\n"
                                                       "}")
        self.pushButtonAlarmsSaveChanges.setObjectName("pushButtonAlarmsSaveChanges")
        self.labelAlarmsTItle = QtWidgets.QLabel(self.widgetAlarmsParent)
        self.labelAlarmsTItle.setGeometry(QtCore.QRect(30, -30, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(36)
        self.labelAlarmsTItle.setFont(font)
        self.labelAlarmsTItle.setStyleSheet("color:white")
        self.labelAlarmsTItle.setObjectName("labelAlarmsTItle")

        self.lineEditChangeTitle = QtWidgets.QLineEdit(self.widgetAlarmExtended)
        self.lineEditChangeTitle.setGeometry(QtCore.QRect(20, 20, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(36)
        self.lineEditChangeTitle.setFont(font)
        self.lineEditChangeTitle.setStyleSheet("\n"
                                               "border-color:white;\n"
                                               "color:white;\n"
                                               "background-color:rgb(25,25,25)\n"
                                               "\n"
                                               "")
        self.lineEditChangeTitle.setText("")
        self.lineEditChangeTitle.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEditChangeTitle.setObjectName("lineEditChangeTitle")

        self.lineEditChangeTime = QtWidgets.QLineEdit(self.widgetAlarmExtended)
        self.lineEditChangeTime.setGeometry(QtCore.QRect(310, 10, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(28)
        self.lineEditChangeTime.setFont(font)
        self.lineEditChangeTime.setStyleSheet("\n"
                                              "border-color:white;\n"
                                              "color:white;\n"
                                              "background-color:rgb(25,25,25)\n"
                                              "\n"
                                              "")
        self.lineEditChangeTime.setText("")
        self.lineEditChangeTime.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEditChangeTime.setObjectName("lineEditChangeTitle")
        self.lineEditChangeTime.hide()

        self.lineEditChangeTitle.hide()

        """Other Ui ELements"""

        self.labelImage = QtWidgets.QLabel(Form)
        self.labelImage.setGeometry(QtCore.QRect(560, 0, 381, 671))
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("../../../Downloads/pexels-golden-jojo-2409038 (1).jpg"))
        self.labelImage.setObjectName("labelImage")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(360, 540, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white; \n"
                                   "\n"
                                   "border-radius:5px")
        self.label_7.setObjectName("label_7")
        self.labelAlarms = QtWidgets.QLabel(Form)
        self.labelAlarms.setGeometry(QtCore.QRect(590, 50, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelAlarms.setFont(font)
        self.labelAlarms.setStyleSheet("background-color: rgba(1, 32, 15,0);\n"
                                       "color:white;\n"
                                       "")
        self.labelAlarms.setObjectName("labelAlarms")
        self.labelTimer = QtWidgets.QLabel(Form)
        self.labelTimer.setGeometry(QtCore.QRect(590, 140, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelTimer.setFont(font)
        self.labelTimer.setStyleSheet("color:white;\n"
                                      "background-color:rgba(20,20,20,0)")
        self.labelTimer.setObjectName("labelTimer")
        self.labelStopwatch = QtWidgets.QLabel(Form)
        self.labelStopwatch.setGeometry(QtCore.QRect(590, 230, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelStopwatch.setFont(font)
        self.labelStopwatch.setStyleSheet("color:white;\n"
                                          "background-color:rgba(20,20,20,0)")
        self.labelStopwatch.setObjectName("labelStopwatch")
        self.labelReminders = QtWidgets.QLabel(Form)
        self.labelReminders.setGeometry(QtCore.QRect(590, 320, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelReminders.setFont(font)
        self.labelReminders.setStyleSheet("color:white;\n"
                                          "background-color:rgba(20,20,20,0)")
        self.labelReminders.setObjectName("labelReminders")
        self.widgetAlarms = QtWidgets.QWidget(Form)
        self.widgetAlarms.setGeometry(QtCore.QRect(40, 60, 491, 431))
        self.widgetAlarms.setObjectName("widgetAlarms")
        self.labelAlarmsTime1 = QtWidgets.QLabel(self.widgetAlarms)
        self.labelAlarmsTime1.setGeometry(QtCore.QRect(20, 110, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(20)
        font.setItalic(False)
        self.labelAlarmsTime1.setFont(font)
        self.labelAlarmsTime1.setStyleSheet("color:white;\n"
                                            "border-radius:20px;\n"
                                            "background-color: rgb(52, 98, 63);")
        self.labelAlarmsTime1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsTime1.setObjectName("labelAlarmsTime1")
        self.labelAlarmsTime2 = QtWidgets.QLabel(self.widgetAlarms)
        self.labelAlarmsTime2.setGeometry(QtCore.QRect(250, 110, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(20)
        font.setItalic(False)
        self.labelAlarmsTime2.setFont(font)
        self.labelAlarmsTime2.setStyleSheet("color:white;\n"
                                            "background-color:rgb(20,20,20);\n"
                                            "border-radius:20px")
        self.labelAlarmsTime2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsTime2.setObjectName("labelAlarmsTime2")
        self.labelAlarmsTime3 = QtWidgets.QLabel(self.widgetAlarms)
        self.labelAlarmsTime3.setGeometry(QtCore.QRect(20, 260, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(20)
        font.setItalic(False)
        self.labelAlarmsTime3.setFont(font)
        self.labelAlarmsTime3.setStyleSheet("color:white;\n"
                                            "background-color:rgb(20,20,20);\n"
                                            "border-radius:20px")
        self.labelAlarmsTime3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsTime3.setObjectName("labelAlarmsTime3")
        self.labelAlarmsTime4 = QtWidgets.QLabel(self.widgetAlarms)
        self.labelAlarmsTime4.setGeometry(QtCore.QRect(250, 260, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(20)
        font.setItalic(False)
        self.labelAlarmsTime4.setFont(font)
        self.labelAlarmsTime4.setStyleSheet("color:white;\n"
                                            "background-color:rgb(20,20,20);\n"
                                            "border-radius:20px")
        self.labelAlarmsTime4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlarmsTime4.setObjectName("labelAlarmsTime4")
        self.labelAlarmsTItle2 = QtWidgets.QLabel(Form)
        self.labelAlarmsTItle2.setGeometry(QtCore.QRect(80, 30, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(36)
        font.setItalic(False)
        self.labelAlarmsTItle2.setFont(font)
        self.labelAlarmsTItle2.setStyleSheet("color:white")
        self.labelAlarmsTItle2.setObjectName("labelAlarmsTItle2")

        self.widgetStopwatch = QtWidgets.QWidget(Form)
        self.widgetStopwatch.setGeometry(QtCore.QRect(60, 50, 471, 441))
        self.widgetStopwatch.setObjectName("widgetStopwatch")
        self.labelStopwatchStartbutton = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchStartbutton.setGeometry(QtCore.QRect(190, 280, 101, 101))
        self.labelStopwatchStartbutton.setStyleSheet("border-radius:10px;\n"
                                                     "\n"
                                                     "background-color: rgb(52, 98, 63);")
        self.labelStopwatchStartbutton.setText("")
        self.labelStopwatchStartbutton.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-play-50.png"))
        self.labelStopwatchStartbutton.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStopwatchStartbutton.setObjectName("labelStopwatchStartbutton")
        self.labelStopwatchClockHours = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchClockHours.setGeometry(QtCore.QRect(70, 80, 101, 151))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(72)
        self.labelStopwatchClockHours.setFont(font)
        self.labelStopwatchClockHours.setStyleSheet("color:white")
        self.labelStopwatchClockHours.setObjectName("labelStopwatchClockHours")
        self.labelStopwatchClockMinutes = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchClockMinutes.setGeometry(QtCore.QRect(200, 80, 101, 151))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(72)
        self.labelStopwatchClockMinutes.setFont(font)
        self.labelStopwatchClockMinutes.setStyleSheet("color:white")
        self.labelStopwatchClockMinutes.setObjectName("labelStopwatchClockMinutes")
        self.labelStopwatchClockSeconds = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchClockSeconds.setGeometry(QtCore.QRect(330, 80, 101, 151))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(72)
        self.labelStopwatchClockSeconds.setFont(font)
        self.labelStopwatchClockSeconds.setStyleSheet("color:white")
        self.labelStopwatchClockSeconds.setObjectName("labelStopwatchClockSeconds")
        self.labelStopwatchcolon1 = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchcolon1.setGeometry(QtCore.QRect(170, 120, 20, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(48)
        self.labelStopwatchcolon1.setFont(font)
        self.labelStopwatchcolon1.setStyleSheet("color:white")
        self.labelStopwatchcolon1.setObjectName("labelStopwatchcolon1")
        self.labelStopwatchcolon2 = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchcolon2.setGeometry(QtCore.QRect(300, 120, 20, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(48)
        self.labelStopwatchcolon2.setFont(font)
        self.labelStopwatchcolon2.setStyleSheet("color:white")
        self.labelStopwatchcolon2.setObjectName("labelStopwatchcolon2")
        self.widgetStopwatch.raise_()
        self.labelImage.raise_()
        self.label_7.raise_()
        self.labelAlarms.raise_()
        self.labelTimer.raise_()
        self.labelStopwatch.raise_()

        self.labelReminders.raise_()

        self.labelStopwatchPausebutton = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchPausebutton.setGeometry(QtCore.QRect(190, 280, 101, 101))
        self.labelStopwatchPausebutton.setStyleSheet("border-radius:10px;\n"
                                                     "\n"
                                                     "background-color: rgb(52, 98, 63);")
        self.labelStopwatchPausebutton.setText("")
        self.labelStopwatchPausebutton.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-pause-50"))
        self.labelStopwatchPausebutton.setAlignment(QtCore.Qt.AlignCenter)

        self.labelStopwatchPausebutton.hide()

        self.labelStopwatchResetbutton = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchResetbutton.setGeometry(QtCore.QRect(90, 300, 61, 61))
        self.labelStopwatchResetbutton.setStyleSheet("border-radius:10px;\n"
                                                     "\n"
                                                     "background-color: rgb(20,20,20);")
        self.labelStopwatchResetbutton.setText("")
        self.labelStopwatchResetbutton.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-reset-30 (1)"))
        self.labelStopwatchResetbutton.setAlignment(QtCore.Qt.AlignCenter)

        if alarmsEnabled == "0":
            self.labelAlarmsTime1.setStyleSheet("color:white;\n"
                                                "background-color:rgb(20,20,20);\n"
                                                "border-radius:20px")
        else:
            self.labelAlarmsTime1.setStyleSheet("color:white;\n"
                                                "border-radius:20px;\n"
                                                "background-color: rgb(52, 98, 63);")

        if alarmsEnabled2 == "0":
            self.labelAlarmsTime2.setStyleSheet("color:white;\n"
                                                "background-color:rgb(20,20,20);\n"
                                                "border-radius:20px")
        else:
            self.labelAlarmsTime2.setStyleSheet("color:white;\n"
                                                "border-radius:20px;\n"
                                                "background-color: rgb(52, 98, 63);")

        self.labelStopwatchPausebutton.mousePressEvent = functools.partial(self.pauseStopwatch)
        self.labelStopwatchStartbutton.mousePressEvent = functools.partial(self.startStopwatch)
        self.labelStopwatchResetbutton.mousePressEvent = functools.partial(self.resetStopwatch)

        self.labelStopwatchResetbutton.hide()

        self.widgetAlarmsParent.hide()

        self.labelAlarmsMon.mousePressEvent = functools.partial(self.changeDayState, day=self.labelAlarmsMon)
        self.labelAlarmsTue.mousePressEvent = functools.partial(self.changeDayState, day=self.labelAlarmsTue)
        self.labelAlarmsWed.mousePressEvent = functools.partial(self.changeDayState, day=self.labelAlarmsWed)
        self.labelAlarmsThu.mousePressEvent = functools.partial(self.changeDayState, day=self.labelAlarmsThu)
        self.labelAlarmsFri.mousePressEvent = functools.partial(self.changeDayState, day=self.labelAlarmsFri)
        self.labelAlarmsSat.mousePressEvent = functools.partial(self.changeDayState, day=self.labelAlarmsSat)
        self.labelAlarmsSun.mousePressEvent = functools.partial(self.changeDayState, day=self.labelAlarmsSun)

        self.labelAlarmsName.mousePressEvent = functools.partial(self.changeAlarmTitle)
        self.labelAlarmsTItle.mouseDoubleClickEvent = functools.partial(self.changeAlarmState)
        self.labelAlarmsTime.mousePressEvent = functools.partial(self.editAlarmTime)

        # noinspection PyUnresolvedReferences
        self.pushButtonAlarmsSaveChanges.clicked.connect(self.goBack)

        self.labelAlarmsTime1.mouseDoubleClickEvent = functools.partial(self.showAlarmsExtended, alarmNumber=0)
        self.labelAlarmsTime2.mouseDoubleClickEvent = functools.partial(self.showAlarmsExtended, alarmNumber=1)
        self.labelAlarmsTime3.mouseDoubleClickEvent = functools.partial(self.showAlarmsExtended, alarmNumber=2)
        self.labelAlarmsTime4.mouseDoubleClickEvent = functools.partial(self.showAlarmsExtended, alarmNumber=3)

        self.timer = QTimer(self)
        # noinspection PyUnresolvedReferences
        self.timer.timeout.connect(self.checkAlarmTime)
        self.timer.start(1000)

        self.widgetStopwatch.hide()

        self.labelAlarms.mousePressEvent = functools.partial(self.changeAlarmFunction, 0)
        self.labelTimer.mousePressEvent = functools.partial(self.changeAlarmFunction, 1)
        self.labelStopwatch.mousePressEvent = functools.partial(self.changeAlarmFunction, 2)
        self.labelReminders.mousePressEvent = functools.partial(self.changeAlarmFunction, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\">Hours</p></body></html>"))
        self.labelAlarms.setText(_translate("Form", "<html><head/><body><p align=\"center\">Alarms</p></body></html>"))
        self.labelTimer.setText(_translate("Form", "<html><head/><body><p align=\"center\">Timer</p></body></html>"))
        self.labelStopwatch.setText(
            _translate("Form", "<html><head/><body><p align=\"center\">Stopwatch</p></body></html>"))
        self.labelReminders.setText(
            _translate("Form", "<html><head/><body><p align=\"center\">Reminders</p></body></html>"))
        self.labelAlarmsMon.setText(_translate("Form", "M"))
        self.labelAlarmsTue.setText(_translate("Form", "T"))
        self.labelAlarmsWed.setText(_translate("Form", "W"))
        self.labelAlarmsThu.setText(_translate("Form", "T"))
        self.labelAlarmsFri.setText(_translate("Form", "F"))
        self.labelAlarmsSat.setText(_translate("Form", "S"))
        self.labelAlarmsSun.setText(_translate("Form", "S"))
        self.labelAlarmsDelete.setText(_translate("Form", "Delete Alarm"))
        self.labelAlarmsChangeTone.setText(_translate("Form", "Change alarm tone"))
        self.labelAlarmsName.setText(_translate("Form", "Wake up"))
        self.pushButtonAlarmsSaveChanges.setText(_translate("Form", "Save"))

        self.labelAlarmsTItle2.setText(_translate("Form", "Alarms"))

        self.labelAlarmsTime1.setText(_translate("Form", f"<html><head/><body><p>{alarmsTitle}</p></body></html>"))
        self.labelAlarmsTime2.setText(_translate("Form", f"<html><head/><body><p>{alarmsTitle2}</p></body></html>"))
        self.labelAlarmsTime3.setText(_translate("Form", f"<html><head/><body><p>{alarmsTitle3}</p></body></html>"))
        self.labelAlarmsTime4.setText(_translate("Form", f"<html><head/><body><p>{alarmsTitle4}</p></body></html>"))

        self.labelStopwatchClockHours.setText(_translate("Form", "00"))
        self.labelStopwatchClockMinutes.setText(_translate("Form", "00"))
        self.labelStopwatchClockSeconds.setText(_translate("Form", "00"))
        self.labelStopwatchcolon1.setText(_translate("Form", ":"))
        self.labelStopwatchcolon2.setText(_translate("Form", ":"))

    def changeAlarmFunction(self, fx, event):

        if fx == 0:

            self.widgetStopwatch.hide()
            self.widgetAlarms.show()
            self.widgetAlarmsParent.hide()

            print(Fore.GREEN+alarmsEnabled)

        if fx == 2:
            self.widgetStopwatch.show()
            self.widgetAlarms.hide()
            self.widgetAlarmsParent.hide()

    def showAlarmsExtended(self, event, alarmNumber):

        self.alarmNumber = alarmNumber

        self.widgetAlarmsParent.show()
        self.widgetAlarms.hide()

        self.labelAlarmsTItle2.hide()
        self.labelAlarmsTItle.show()

        self.loadAllElements(alarmNumber)

    # Done
    def loadAllElements(self, alarmNumber):

        global alarmsTitle, alarmsDayList, alarmsEnabled, alarmsTime, alarmsTitle2,alarmsTitle3,alarmsTitle4
        alarmNumber = self.alarmNumber

        self.labelAlarmsMon.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsTue.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsWed.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsThu.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsFri.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsSat.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")
        self.labelAlarmsSun.setStyleSheet("color:white;\n"
                                          "background-color: rgb(52, 99, 47);")

        if self.alarmNumber == 0:

            if "1" in alarmsDayList:
                self.labelAlarmsMon.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "2" in alarmsDayList:
                self.labelAlarmsTue.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "3" in alarmsDayList:
                self.labelAlarmsWed.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "4" in alarmsDayList:
                self.labelAlarmsThu.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "5" in alarmsDayList:
                self.labelAlarmsFri.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "6" in alarmsDayList:
                self.labelAlarmsSat.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "7" in alarmsDayList:
                self.labelAlarmsSun.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            alarmsTitle = alarmsTitle.replace("_", " ")
            self.labelAlarmsName.setText(alarmsTitle)

            if alarmsEnabled == "0":
                self.labelAlarmsTItle.setText("Disabled")
            else:
                self.labelAlarmsTItle.setText("Enabled")

            self.labelAlarmsTime.setText(alarmsTime)

        elif self.alarmNumber == 1:

            if "1" in alarmsDayList2:
                self.labelAlarmsMon.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "2" in alarmsDayList2:
                self.labelAlarmsTue.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "3" in alarmsDayList2:
                self.labelAlarmsWed.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "4" in alarmsDayList2:
                self.labelAlarmsThu.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "5" in alarmsDayList2:
                self.labelAlarmsFri.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "6" in alarmsDayList2:
                self.labelAlarmsSat.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "7" in alarmsDayList2:
                self.labelAlarmsSun.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            alarmsTitle2 = alarmsTitle2.replace("_", " ")
            self.labelAlarmsName.setText(alarmsTitle2)

            if alarmsEnabled2 == "0":
                self.labelAlarmsTItle.setText("Disabled")
            else:
                self.labelAlarmsTItle.setText("Enabled")

            self.labelAlarmsTime.setText(alarmsTime2)

        elif self.alarmNumber == 2:

            if "1" in alarmsDayList3:
                self.labelAlarmsMon.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "2" in alarmsDayList3:
                self.labelAlarmsTue.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "3" in alarmsDayList3:
                self.labelAlarmsWed.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "4" in alarmsDayList3:
                self.labelAlarmsThu.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "5" in alarmsDayList3:
                self.labelAlarmsFri.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "6" in alarmsDayList3:
                self.labelAlarmsSat.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "7" in alarmsDayList3:
                self.labelAlarmsSun.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            alarmsTitle3 = alarmsTitle3.replace("_", " ")
            self.labelAlarmsName.setText(alarmsTitle3)

            if alarmsEnabled3 == "0":
                self.labelAlarmsTItle.setText("Disabled")
            else:
                self.labelAlarmsTItle.setText("Enabled")

            self.labelAlarmsTime.setText(alarmsTime3)

        elif self.alarmNumber == 3:

            if "1" in alarmsDayList4:
                self.labelAlarmsMon.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "2" in alarmsDayList4:
                self.labelAlarmsTue.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "3" in alarmsDayList4:
                self.labelAlarmsWed.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "4" in alarmsDayList4:
                self.labelAlarmsThu.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "5" in alarmsDayList4:
                self.labelAlarmsFri.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "6" in alarmsDayList4:
                self.labelAlarmsSat.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            if "7" in alarmsDayList4:
                self.labelAlarmsSun.setStyleSheet("color:white;\n"
                                                  "background-color: rgb(25,25,25);")

            alarmsTitle4 = alarmsTitle4.replace("_", " ")
            self.labelAlarmsName.setText(alarmsTitle4)

            if alarmsEnabled4 == "0":
                self.labelAlarmsTItle.setText("Disabled")
            else:
                self.labelAlarmsTItle.setText("Enabled")

            self.labelAlarmsTime.setText(alarmsTime4)

    def changeDayState(self, event, day):

        global alarmsDayList, alarmsDayList2,alarmsDayList3,alarmsDayList4

        if self.alarmNumber == 0:

            if "background-color: rgb(52, 99, 47);" in day.styleSheet():
                day.setStyleSheet("color:white;\n"
                                  "background-color: rgb(25,25,25);")
                # ALARM DISABLED

                if "Mon" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("Mon", "1")
                elif "Tue" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("Tue", "2")
                elif "Wed" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("Wed", "3")
                elif "Thu" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("Thu", "4")
                elif "Fri" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("Fri", "5")
                elif "Sat" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("Sat", "6")
                elif "Sun" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("Sun", "7")

                opener.close()

                opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
                opener2.write(
                    f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")

                opener2.close()


            else:

                # ALARM ENABLED

                day.setStyleSheet("color:white;\n"
                                  "background-color: rgb(52, 99, 47);")

                if "Mon" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("1", "Mon")
                elif "Tue" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("2", "Tue")
                elif "Wed" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("3", "Wed")
                elif "Thu" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("4", "Thu")
                elif "Fri" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("5", "Fri")
                elif "Sat" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("6", "Sat")
                elif "Sun" in day.objectName():
                    alarmsDayList = alarmsDayList.replace("7", "Sun")

                opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
                opener2.write(
                    f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")

                opener2.close()

        elif self.alarmNumber == 1:

            if "background-color: rgb(52, 99, 47);" in day.styleSheet():
                day.setStyleSheet("color:white;\n"
                                  "background-color: rgb(25,25,25);")
                # ALARM DISABLED

                if "Mon" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("Mon", "1")
                elif "Tue" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("Tue", "2")
                elif "Wed" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("Wed", "3")
                elif "Thu" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("Thu", "4")
                elif "Fri" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("Fri", "5")
                elif "Sat" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("Sat", "6")
                elif "Sun" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("Sun", "7")

                opener.close()

                opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
                opener2.write(
                    f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")

                opener2.close()

            else:

                # ALARM ENABLED

                day.setStyleSheet("color:white;\n"
                                  "background-color: rgb(52, 99, 47);")

                if "Mon" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("1", "Mon")
                elif "Tue" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("2", "Tue")
                elif "Wed" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("3", "Wed")
                elif "Thu" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("4", "Thu")
                elif "Fri" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("5", "Fri")
                elif "Sat" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("6", "Sat")
                elif "Sun" in day.objectName():
                    alarmsDayList2 = alarmsDayList2.replace("7", "Sun")

                opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
                opener2.write(
                    f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")

                opener2.close()

        elif self.alarmNumber == 2:

            if "background-color: rgb(52, 99, 47);" in day.styleSheet():
                day.setStyleSheet("color:white;\n"
                                  "background-color: rgb(25,25,25);")
                # ALARM DISABLED

                if "Mon" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("Mon", "1")
                elif "Tue" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("Tue", "2")
                elif "Wed" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("Wed", "3")
                elif "Thu" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("Thu", "4")
                elif "Fri" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("Fri", "5")
                elif "Sat" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("Sat", "6")
                elif "Sun" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("Sun", "7")

                opener.close()

                opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
                opener2.write(
                    f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
                opener2.close()

            else:

                # ALARM ENABLED

                day.setStyleSheet("color:white;\n"
                                  "background-color: rgb(52, 99, 47);")

                if "Mon" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("1", "Mon")
                elif "Tue" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("2", "Tue")
                elif "Wed" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("3", "Wed")
                elif "Thu" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("4", "Thu")
                elif "Fri" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("5", "Fri")
                elif "Sat" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("6", "Sat")
                elif "Sun" in day.objectName():
                    alarmsDayList3 = alarmsDayList3.replace("7", "Sun")

                opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
                opener2.write(
                    f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
                opener2.close()

        elif self.alarmNumber == 3:

            if "background-color: rgb(52, 99, 47);" in day.styleSheet():
                day.setStyleSheet("color:white;\n"
                                  "background-color: rgb(25,25,25);")
                # ALARM DISABLED

                if "Mon" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("Mon", "1")
                elif "Tue" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("Tue", "2")
                elif "Wed" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("Wed", "3")
                elif "Thu" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("Thu", "4")
                elif "Fri" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("Fri", "5")
                elif "Sat" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("Sat", "6")
                elif "Sun" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("Sun", "7")

                opener.close()

                opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
                opener2.write(
                    f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
                opener2.close()

            else:

                # ALARM ENABLED

                day.setStyleSheet("color:white;\n"
                                  "background-color: rgb(52, 99, 47);")

                if "Mon" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("1", "Mon")
                elif "Tue" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("2", "Tue")
                elif "Wed" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("3", "Wed")
                elif "Thu" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("4", "Thu")
                elif "Fri" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("5", "Fri")
                elif "Sat" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("6", "Sat")
                elif "Sun" in day.objectName():
                    alarmsDayList4 = alarmsDayList4.replace("7", "Sun")

                opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
                opener2.write(
                    f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")

                opener2.close()


    # Done
    def changeAlarmTitle(self, event):

        self.labelAlarmsName.hide()
        self.lineEditChangeTitle.show()

        # noinspection PyUnresolvedReferences
        self.lineEditChangeTitle.returnPressed.connect(self.saveAlarmTitle)

    # Done
    def saveAlarmTitle(self):

        global alarmsTitle2, alarmsTitle,alarmsTitle3,alarmsTitle4
        newAlarmTitle = self.lineEditChangeTitle.text()

        if newAlarmTitle == "":
            self.lineEditChangeTitle.hide()
            self.labelAlarmsName.show()
        else:

            self.lineEditChangeTitle.hide()

            self.labelAlarmsName.setText(newAlarmTitle)
            self.labelAlarmsName.show()

        if " " in newAlarmTitle:
            newAlarmTitle = newAlarmTitle.replace(" ", "_")
        else:
            pass

        if self.alarmNumber == 0:

            alarmsTitle = newAlarmTitle

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
            opener2.close()

        elif self.alarmNumber == 1:

            alarmsTitle2 = newAlarmTitle

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")

            opener2.close()

        elif self.alarmNumber == 2:

            alarmsTitle3 = newAlarmTitle

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
            opener2.close()

        elif self.alarmNumber == 3:

            alarmsTitle4 = newAlarmTitle

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
            opener2.close()

    def changeAlarmState(self, event):

        global alarmsEnabled, alarmsTitle, alarmsEnabled2,alarmsEnabled3,alarmsEnabled4

        if self.alarmNumber == 0:

            if alarmsEnabled == "0":

                alarmsEnabled = "1"
                self.labelAlarmsTItle.setText("Enabled")
            else:

                alarmsEnabled = "0"
                self.labelAlarmsTItle.setText("Disabled")

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
            opener2.close()

        elif self.alarmNumber == 1:

            if alarmsEnabled2 == "0":

                alarmsEnabled2 = "1"
                self.labelAlarmsTItle.setText("Enabled")
            else:

                alarmsEnabled2 = "0"
                self.labelAlarmsTItle.setText("Disabled")

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
            opener2.close()

        elif self.alarmNumber == 2:

            if alarmsEnabled3 == "0":

                alarmsEnabled3 = "1"
                self.labelAlarmsTItle.setText("Enabled")
            else:

                alarmsEnabled3 = "0"
                self.labelAlarmsTItle.setText("Disabled")

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
            opener2.close()

        elif self.alarmNumber == 3:

            if alarmsEnabled4 == "0":

                alarmsEnabled4 = "1"
                self.labelAlarmsTItle.setText("Enabled")
            else:

                alarmsEnabled4 = "0"
                self.labelAlarmsTItle.setText("Disabled")

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
            opener2.close()

    def editAlarmTime(self, event):

        self.labelAlarmsTime.hide()
        self.lineEditChangeTime.show()

        # noinspection PyUnresolvedReferences
        self.lineEditChangeTime.returnPressed.connect(self.changeAlarmTime)

    def changeAlarmTime(self):

        global alarmsTitle, alarmsTime, alarmsTone, alarmsDayList, alarmsEnabled, alarmsTitle2, alarmsTime2, alarmsTone2, alarmsDayList2,alarmsTime3,alarmsTime4

        newAlarmTime = self.lineEditChangeTime.text()

        try:

            hours = newAlarmTime.split(":")[0]
            minutes = newAlarmTime.split(":")[1]

            minutesList = []

            for x in minutes:
                if x.isdigit():
                    minutesList.append(x)

            minutesList = str(minutesList)
            minutesList = minutesList[2:-2]

            minutesList = minutesList.replace("'", "")
            minutesList = minutesList.replace(",", "")
            minutesList = minutesList.replace(" ", "")

            if ":" not in newAlarmTime:
                pass

            elif hours == "":
                pass

            elif minutes == "":
                pass

            elif int(hours) > 24:
                pass

            elif int(minutesList) > 59:
                pass

            else:
                self.lineEditChangeTime.hide()

                newTime = self.lineEditChangeTime.text()
                self.labelAlarmsTime.show()
                self.labelAlarmsTime.setText(newTime)

            if self.alarmNumber == 0:
                alarmsTime = f"{hours}:{minutesList}"

            elif self.alarmNumber == 1:
                alarmsTime2 = f"{hours}:{minutesList}"

            elif self.alarmNumber == 2:
                alarmsTime3 = f"{hours}:{minutesList}"

            elif self.alarmNumber == 3:
                alarmsTime4 = f"{hours}:{minutesList}"

            opener2 = open(r"C:\Users\Thunder 1908\PycharmProjects\Youtube\Python Files\AlarmsParmeters", "w")
            opener2.write(
                f"{alarmsTitle} {alarmsTime} {alarmsDayList} {alarmsTone} {alarmsEnabled} {alarmsTitle2} {alarmsTime2} {alarmsDayList2} {alarmsTone2} {alarmsEnabled2} {alarmsTitle3} {alarmsTime3} {alarmsDayList3} {alarmsTone3} {alarmsEnabled3} {alarmsTitle4} {alarmsTime4} {alarmsDayList4} {alarmsTone4} {alarmsEnabled4} ")
            opener2.close()

        except:
            pass

    def goBack(self):

        self.widgetAlarmsParent.hide()
        self.widgetAlarms.show()

        self.labelAlarmsTItle2.show()
        self.labelAlarmsTItle.hide()

        self.labelAlarmsTime1.setText(f"<html><head/><body><p>{alarmsTitle}</p></body></html>")
        self.labelAlarmsTime2.setText(f"<html><head/><body><p>{alarmsTitle2}</p></body></html>")
        self.labelAlarmsTime3.setText(f"<html><head/><body><p>{alarmsTitle3}</p></body></html>")
        self.labelAlarmsTime4.setText(f"<html><head/><body><p>{alarmsTitle4}</p></body></html>")

        if alarmsEnabled == "0":
            self.labelAlarmsTime1.setStyleSheet("color:white;\n"
                                                "background-color:rgb(20,20,20);\n"
                                                "border-radius:20px")
        else:
            self.labelAlarmsTime1.setStyleSheet("color:white;\n"
                                                "border-radius:20px;\n"
                                                "background-color: rgb(52, 98, 63);")

        if alarmsEnabled2 == "0":
            self.labelAlarmsTime2.setStyleSheet("color:white;\n"
                                                "background-color:rgb(20,20,20);\n"
                                                "border-radius:20px")
        else:
            self.labelAlarmsTime2.setStyleSheet("color:white;\n"
                                                "border-radius:20px;\n"
                                                "background-color: rgb(52, 98, 63);")

        if alarmsEnabled3 == "0":
            self.labelAlarmsTime3.setStyleSheet("color:white;\n"
                                                "background-color:rgb(20,20,20);\n"
                                                "border-radius:20px")
        else:
            self.labelAlarmsTime3.setStyleSheet("color:white;\n"
                                                "border-radius:20px;\n"
                                                "background-color: rgb(52, 98, 63);")

        if alarmsEnabled4 == "0":
            self.labelAlarmsTime4.setStyleSheet("color:white;\n"
                                                "background-color:rgb(20,20,20);\n"
                                                "border-radius:20px")
        else:
            self.labelAlarmsTime4.setStyleSheet("color:white;\n"
                                                "border-radius:20px;\n"
                                                "background-color: rgb(52, 98, 63);")

    def checkAlarmTime(self):

        global alarmsDayList, alarmsDayList2, alarmsTime, alarmsTime2

        t = datetime.datetime.today()
        currentTimeHours = t.hour
        currentTimeMinutes = t.minute

        if len(str(currentTimeMinutes)) == 1:
            currentTimeMinutes = f"0{currentTimeMinutes}"

        currentTime = f"{currentTimeHours}:{currentTimeMinutes}"

        if currentTime == alarmsTime:

            self.alarmRing = QtWidgets.QDialog()
            self.ui = Ui_Form()
            self.ui.setupUi(self.alarmRing)
            self.alarmRing.show()

            pygame.mixer.init()
            pygame.mixer.music.load(fr"C:/Users/Thunder 1908/Desktop/Songs/Twenty One Pilots - Ride.mp3")
            pygame.mixer.music.play()

            self.timer.stop()

        elif currentTime == alarmsTime2:
            print("Alarm2 ringing")

        else:
            self.timer.start()

    def startStopwatch(self, event):
        # Changing the icon from play to pause

        self.labelStopwatchPausebutton.show()
        self.labelStopwatchStartbutton.hide()
        self.labelStopwatchResetbutton.hide()

        self.timerStopwatch = QTimer(self)
        # noinspection PyUnresolvedReferences
        self.timerStopwatch.timeout.connect(self.showTime)
        self.timerStopwatch.start(1000)

        pass

    def showTime(self):

        stopwatchTimeSeconds = int(self.labelStopwatchClockSeconds.text())
        stopwatchTimeMinutes = int(self.labelStopwatchClockMinutes.text())
        stopwatchTimeHours = int(self.labelStopwatchClockHours.text())

        newtimeSeconds = stopwatchTimeSeconds + 1

        self.labelStopwatchClockSeconds.setText(f"{newtimeSeconds}")

        if len(str(newtimeSeconds)) < 2:
            self.labelStopwatchClockSeconds.setText(f"0{newtimeSeconds}")

        else:
            self.labelStopwatchClockSeconds.setText(f"{newtimeSeconds}")

        if newtimeSeconds == 60:

            self.labelStopwatchClockSeconds.setText("00")
            newtimeMinutes = stopwatchTimeMinutes + 1

            if len(str(newtimeMinutes)) < 2:
                self.labelStopwatchClockMinutes.setText(f"0{newtimeMinutes}")

            else:
                self.labelStopwatchClockMinutes.setText(f"{newtimeMinutes}")

            if newtimeMinutes == 60:

                self.labelStopwatchClockMinutes.setText("00")
                newtimeHours = stopwatchTimeHours + 1

                if len(str(newtimeHours)) < 2:
                    self.labelStopwatchClockHours.setText(f"0{newtimeHours}")

                else:
                    self.labelStopwatchClockHours.setText(f"{newtimeHours}")

    def pauseStopwatch(self, event):

        self.labelStopwatchPausebutton.hide()
        self.labelStopwatchStartbutton.show()
        self.labelStopwatchResetbutton.show()
        self.timerStopwatch.stop()

    def resetStopwatch(self, event):
        self.pauseStopwatch(None)

        self.labelStopwatchClockSeconds.setText("00")
        self.labelStopwatchClockMinutes.setText("00")
        self.labelStopwatchClockHours.setText("00")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = mainApp()
    ui.setupUi(Form)
    Form.show()

    app2 = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QWidget()
    ui2 = Ui_Form()
    ui2.setupUi(Form2)

    sys.exit(app.exec_())
