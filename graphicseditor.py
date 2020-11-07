from PyQt5 import QtWidgets
from View import Editor
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    g = Editor()
    g.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
