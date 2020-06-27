import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance


def maya_main_window():
    """Return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class SimpleUI(QtWidgets.QDialog):
    """Simple UI Class"""

    def __init__(self):
        """Constructor"""
        # Passing th object Simple Ui as an argument to super()
        # makes this lone python 2 and 3 compatible
        super(SimpleUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("A Simple UI")
        # resize a window
        self.resize(500, 200)
        # removes buttons like ?
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        """Create widgets for our UI"""
        self.title_lbl = QtWidgets.QLabel("Smart Save")
        self.title_lbl.setStyleSheet("font: bold 40px")
        self.dir_lbl = QtWidgets.QLabel("Directory")
        self.dir_le = QtWidgets.QLineEdit()
        self.browse_btn = QtWidgets.QPushButton("Browse...")
        self.save_btn = QtWidgets.QPushButton("Save")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
    #display the button within Maya
    def create_layout(self):
        """Lay out our widges in the UI"""
        #horzontal layput
        self.directory_lay = QtWidgets.QHBoxLayout()
        self.directory_lay.addWidget(self.dir_lbl)
        self.directory_lay.addWidget(self.dir_le)
        self.directory_lay.addWidget(self.browse_btn)
        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        self.bottom_btn_lay.addWidget(self.save_btn)
        self.bottom_btn_lay.addWidget(self.cancel_btn)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.main_layout.addLayout(self.directory_lay)
        self.main_layout.addLayout (self.bottom_btn_lay)
        self.setLayout(self.main_layout)





