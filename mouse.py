import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QDialog
from PyQt5 import uic, QtCore, QtGui
from collections import defaultdict
import win32gui, win32api

macro_list = defaultdict(list)

class ShowDialog(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('mouse.ui', self)

        self.timer = timer = QtCore.QTimer() # 실시간 연결
        timer.setInterval(8)
        timer.timeout.connect(self.tick)
        timer.start()

    def tick(self):  # 마우스 위치 실시간 받기
        x, y = win32api.GetCursorPos()
        self.textBrowser_X.setText(str(x))
        self.textBrowser_Y.setText(str(y))

    #if(self.btnMove.isChecked()):

    #btnMove 이동
    #btnLeftClick 왼쪽 클릭
    #btnLeftPushed 왼쪽 누른상태
    #btnUnpushed 뗀상태
    #btnRightClick 오른쪽 클릭
    #btnRightPushed 오른쪽 누른상태
    #plainTextEdit_X x 좌표
    #plainTextEdit_Y y 좌표

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowDialog()
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

    sys.exit(app.exec_())
