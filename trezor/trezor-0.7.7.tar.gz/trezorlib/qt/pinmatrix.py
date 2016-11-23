from __future__ import print_function
import sys
import math
from PyQt4.QtGui import (QPushButton, QLineEdit, QSizePolicy, QRegExpValidator, QLabel,
                         QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout)
from PyQt4.QtCore import QObject, SIGNAL, QRegExp, Qt

class PinButton(QPushButton):
    def __init__(self, password, encoded_value):
        super(PinButton, self).__init__('?')
        self.password = password
        self.encoded_value = encoded_value

        QObject.connect(self, SIGNAL('clicked()'), self._pressed)

    def _pressed(self):
        self.password.setText(self.password.text() + str(self.encoded_value))
        self.password.setFocus()

class PinMatrixWidget(QWidget):
    '''
        Displays widget with nine blank buttons and password box.
        Encodes button clicks into sequence of numbers for passing
        into PinAck messages of TREZOR.

        show_strength=True may be useful for entering new PIN
    '''
    def __init__(self, show_strength=True, parent=None):
        super(PinMatrixWidget, self).__init__(parent)

        self.password = QLineEdit()
        self.password.setValidator(QRegExpValidator(QRegExp('[1-9]+'), None))
        self.password.setEchoMode(QLineEdit.Password)
        QObject.connect(self.password, SIGNAL('textChanged(QString)'), self._password_changed)

        self.strength = QLabel()
        self.strength.setMinimumWidth(75)
        self.strength.setAlignment(Qt.AlignCenter)
        self._set_strength(0)

        grid = QGridLayout()
        grid.setSpacing(0)
        for y in range(3)[::-1]:
            for x in range(3):
                button = PinButton(self.password, x + y * 3 + 1)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.setFocusPolicy(Qt.NoFocus)
                grid.addWidget(button, 3 - y, x)

        hbox = QHBoxLayout()
        hbox.addWidget(self.password)
        if show_strength:
            hbox.addWidget(self.strength)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def _set_strength(self, strength):
        if strength < 3000:
            self.strength.setText('weak')
            self.strength.setStyleSheet("QLabel { color : #d00; }")
        elif strength < 60000:
            self.strength.setText('fine')
            self.strength.setStyleSheet("QLabel { color : #db0; }")
        elif strength < 360000:
            self.strength.setText('strong')
            self.strength.setStyleSheet("QLabel { color : #0a0; }")
        else:
            self.strength.setText('ULTIMATE')
            self.strength.setStyleSheet("QLabel { color : #000; font-weight: bold;}")

    def _password_changed(self, password):
        self._set_strength(self.get_strength())

    def get_strength(self):
        digits = len(set(str(self.password.text())))
        strength = math.factorial(9) / math.factorial(9 - digits)
        return strength

    def get_value(self):
        return self.password.text()

if __name__ == '__main__':
    '''
        Demo application showing PinMatrix widget in action
    '''
    a = QApplication(sys.argv)

    matrix = PinMatrixWidget()

    def clicked():
        print("PinMatrix value is", matrix.get_value())
        print("Possible button combinations:", matrix.get_strength())
        sys.exit()

    ok = QPushButton('OK')
    QObject.connect(ok, SIGNAL('clicked()'), clicked)

    vbox = QVBoxLayout()
    vbox.addWidget(matrix)
    vbox.addWidget(ok)

    w = QWidget()
    w.setLayout(vbox)
    w.move(100, 100)
    w.show()

    a.exec_()
