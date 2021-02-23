# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
import clipboard

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
#version 0.01-for Windos-Android
form_class = uic.loadUiType("autocoding.ui")[0]

'''API DATA:'''
alertHtml = "<font color=\"DeepPink\">";
notifyHtml = "<font color=\"Lime\">";
infoHtml = "<font color=\"Aqua\">";
endHtml = "</font><br>";


UIWaitForName = ("\nrc, result = DEV1.UIWaitForName(searchingObj, {}, 0)\nif rc != AT_SUCCESS:\n\tSystem.Finish(ExecutionResult.T_FAILED, \"Impossible to obtain an object information\")\n\treturn rc\nif result == False:\n\tSystem.Debug(u\"Failed to find the object : \"+{})\n\treturn AT_NOT_FOUND")
UIWaitForText = ("\nrc, result = DEV1.UIWaitForText(searchingObj, {}, 0)\nif rc != AT_SUCCESS:\n\tSystem.Finish(ExecutionResult.T_FAILED, \"UIWaitForText verb execution error\")\n\treturn rc\nif result == False:\n\tSystem.Debug(u\"Failed to find the object : \"+{})\n\treturn AT_NOT_FOUND")
UIClickByText = ("\nrc = DEV1.UIClickByText(searchingObj)\nif rc != AT_SUCCESS:\n\tSystem.Finish(ExecutionResult.T_FAILED, \"Impossible to perform a click at the specified control\")\n\treturn rc")
UIClickByName = ("\nrc = DEV1.UIClickByName(searchingObj)\nif rc != AT_SUCCESS:\n\tSystem.Finish(ExecutionResult.T_FAILED, \"Impossible to perform a click at the specified control\")\n\treturn rc")
KeyPress = ("rc = self.KeyPressByAlias(\'{}\')\nif rc != AT_SUCCESS:\n\tSystem.Debug('Could not press app_switch key')\n\treturn rc")
Scroll = ("rc = self.Scroll{}(\"++++\", ++++)\nif rc != AT_SUCCESS:\n\tSystem.Debug(u\"Fail to UIWaitForText\")\n\treturn rc")
SysSleep = ("System.Sleep({})")

''':'''

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize=14
        self.setWindowTitle("자동생성기")
        self.setWindowIcon(QtGui.QIcon("TestNode.ico"))
        self.menuBar()
        

        ##버튼에 기능을 연결하는 코드
        self.genButton.clicked.connect(self.button1Function)#UIClick
        self.genButton2.clicked.connect(self.button2Function)#UIWait
        self.genButton3.clicked.connect(self.button3Function)#Wait+Click
        self.genButton4.clicked.connect(self.button4Function)#KeyPress
        self.genButton5.clicked.connect(self.button5Function)#Scroll
        self.genButton6.clicked.connect(self.button6Function)#Sleep
        ##
        ##라디오 버튼
        self.ui_text.clicked.connect(self.groupboxRadFunction)#버튼1 = Text
        self.ui_name.clicked.connect(self.groupboxRadFunction)#버튼2 = Name
        self.ui_text.setChecked(True)#Radio Text버튼 기본 적용
        ##
        ##콤보박스
        self.KeypresscomboBox.currentIndexChanged.connect(self.comboboxFunction)
        self.ScrollComboBox.currentIndexChanged.connect(self.comboboxFunction1)
        ##
        ##체크박스
        self.checkBox.stateChanged.connect(self.checkBoxState)
        self.checkBox.setChecked(True)#Radio Text버튼 기본 적용
        ##
        

    



    #Radio 버튼 맵핑
    #TEXT & NAME
    def groupboxRadFunction(self) :
        
        if self.ui_text.isChecked():
            print("ui_text.isChecked")
        elif self.ui_name.isChecked(): 
            print("ui_name.isChecked")        
    

    #체크박스 맵핑
    def checkBoxState(self) :
        #자동복사 명령어 :: clipboard.copy(self.plainTextEdit.toPlainText())
        if self.checkBox.isChecked() == True:
            print ("Auto Copy oN")
        elif self.checkBox.isChecked() == False:
            print ("Auto Copy OFF")


    ##콤보박스 맵핑
    #키입력
    def comboboxFunction(self) :
        if self.KeypresscomboBox.currentText():
            wanttopresskey = self.KeypresscomboBox.currentText()
            print(wanttopresskey)
    #스크롤
    def comboboxFunction1(self) :
        if self.ScrollComboBox.currentText():
            wanttoscroll = self.ScrollComboBox.currentText()
            print(wanttoscroll)



    #btn_1이 눌리면 작동할 함수
    def button1Function(self) :#UICLICK
        searchingObj = self.lineEdit.toPlainText()
        self.plainTextEdit.clear()
        searchtext = "searchingObj = "+"\""+searchingObj + "\""
        self.label_2.setText("Result for UIClick by %s" %searchingObj)
        if self.checkBox.isChecked() == True:
            if self.ui_text.isChecked():#Text 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIClickByText)
                clipboard.copy(self.plainTextEdit.toPlainText())
            else:#name 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIClickByName)
                clipboard.copy(self.plainTextEdit.toPlainText())
        else:
            if self.ui_text.isChecked():#Text 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIClickByText)
            else:#name 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIClickByName)


    #btn_2가 눌리면 작동할 함수
    def button2Function(self) :#UIWAIT
        waitTimeout = 1000*int(self.timeEdit.toPlainText())#Waittimeout 불러오는 함수
        searchingObj = self.lineEdit.toPlainText()
        self.plainTextEdit.clear()
        searchtext = "searchingObj = "+"\""+searchingObj + "\""
        self.label_2.setText("Result for UIWait for %s" %searchingObj)
        if self.checkBox.isChecked() == True:
            if self.ui_text.isChecked():#Text 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIWaitForText.format(waitTimeout, searchtext))
                clipboard.copy(self.plainTextEdit.toPlainText())
            else:#Name 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIWaitForName.format(waitTimeout, searchtext))
                clipboard.copy(self.plainTextEdit.toPlainText())
        else:
            if self.ui_text.isChecked():#Text 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIWaitForText.format(waitTimeout, searchtext))
            else:#Name 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIWaitForName.format(waitTimeout, searchtext))

    #btn_3이 눌리면 작동할 함수
    def button3Function(self) :#확인 + 클릭 (Wait + Click)
        waitTimeout = 1000*int(self.timeEdit.toPlainText())#Waittimeout 불러오는 함수
        searchingObj = self.lineEdit.toPlainText()
        self.plainTextEdit.clear()
        searchtext = "searchingObj = "+"\""+searchingObj + "\""
        self.label_2.setText("Result for UIWait+UIClick by %s" %searchingObj)
        if self.checkBox.isChecked() == True:
            if self.ui_text.isChecked():#TEXT 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIWaitForText.format(waitTimeout, searchtext)+UIClickByText)
                clipboard.copy(self.plainTextEdit.toPlainText())
            else:#NAME 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIWaitForName.format(waitTimeout, searchtext)+UIClickByName)
                clipboard.copy(self.plainTextEdit.toPlainText())
        else:
            if self.ui_text.isChecked():#TEXT 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIWaitForText.format(waitTimeout, searchtext)+UIClickByText)
            else:#NAME 클릭시
                self.plainTextEdit.appendPlainText(searchtext+UIWaitForName.format(waitTimeout, searchtext)+UIClickByName)


    #btn_4가 눌리면 작동할 함수
    def button4Function(self) :#KeyPress 코드 생성
        wanttopresskey = self.KeypresscomboBox.currentText()
        self.plainTextEdit.clear()
        self.label_2.setText("Result for KeyPress %s" %wanttopresskey)
        if self.checkBox.isChecked() == True:
            self.plainTextEdit.appendPlainText(KeyPress.format(wanttopresskey))
            clipboard.copy(self.plainTextEdit.toPlainText())
        else:
            self.plainTextEdit.appendPlainText(KeyPress.format(wanttopresskey))


    #btn_5가 눌리면 작동할 함수
    def button5Function(self) :#스크롤 코드 생성
        wanttoscroll = self.ScrollComboBox.currentText()
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(Scroll.format(wanttoscroll))
        self.label_2.setText("Result for Scroll %s" %wanttoscroll)
        if self.checkBox.isChecked() == True:
            clipboard.copy(self.plainTextEdit.toPlainText())


    #btn_6이 눌리면 작동할 함수            
    def button6Function(self) :#슬립 코드 생성
        waitTimeout = 1000*int(self.timeEdit.toPlainText())#Waittimeout 불러오는 함수
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(SysSleep.format(waitTimeout))
        self.label_2.setText("Result for Sleep time %s" %waitTimeout)
        if self.checkBox.isChecked() == True:
            clipboard.copy(self.plainTextEdit.toPlainText())


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()