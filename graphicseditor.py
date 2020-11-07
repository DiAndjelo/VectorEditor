from PyQt5 import QtWidgets

from Controller import Controller
from GraphObject import GraphObject
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    g = Controller()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
