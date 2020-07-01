import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance

import mayautils

"""Imported models like mayautils QtWidgets and tQCore """


"""Create an increment and save function
create a path for the browse button
set up directory in  Ui Save Scene"""


#small function to create a Window from maya
def maya_main_window():
    """Return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


#One class for a bunch of functions built in
class SmartSaveUI(QtWidgets.QDialog):
    """Simple UI Class"""

    def __init__(self):
        """Constructor"""
        # Passing th object Simple UI as an argument to super()
        # makes this lone python 2 and 3 compatible
        super(SmartSaveUI, self).__init__(parent=maya_main_window())
        self.scene = mayautils.SceneFile()

        #name of GUI Window
        self.setWindowTitle("Smart Save")
        # resize a window
        self.resize(500, 200)
        # removes buttons like ?
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.window_layout()
        self.create_connections()
        #self._filepath_()

    def create_widgets(self):
        """Create widgets for our UI"""
        self.title_lbl = QtWidgets.QLabel("Smart Save")
        self.title_lbl.setStyleSheet("font: bold 40px")
        #label used to browse for the directory
        self.dir_lbl = QtWidgets.QLabel("Directory")
        self.dir_le = QtWidgets.QLineEdit()
        self.dir_le.setText(self.scene.dir)
        #Browse button
        self.browse_btn = QtWidgets.QPushButton("Browse...")


        self.descriptor_lbl = QtWidgets.QLabel("Descripter")
        self.descriptor_le = QtWidgets.QLineEdit()
        self.descriptor_le.setText(self.scene.descriptor)

        self.version_lbl = QtWidgets.QLabel("Version")
        self.version_spinbox = QtWidgets.QSpinBox()
        self.version_spinbox.setValue(self.scene.version)

        self.ext_lbl = QtWidgets.QLabel("Extension")
        self.ext_le = QtWidgets.QLineEdit()
        self.ext_le.setText(self.scene.ext)

        self.save_btn = QtWidgets.QPushButton("Save")
        self.increment_save_btn = QtWidgets.QPushButton("Increment and Save")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

    def _directory_layout_(self):
        # horzontal layput
        self.directory_lay = QtWidgets.QHBoxLayout()
        self.directory_le = QtWidgets.QHBoxLayout()
        self.directory_lay.addWidget(self.dir_lbl)
        self.directory_lay.addWidget(self.dir_le)
        self.directory_lay.addWidget(self.browse_btn)
        self.directory_le.addWidget(self.browse_btn)
        self.main_layout.addLayout(self.directory_lay)


    def _descriptor_layout_(self):
        self.descriptor_lay = QtWidgets.QHBoxLayout()
        self.descriptor_lay.addWidget(self.descriptor_lbl)
        self.descriptor_lay.addWidget(self.descriptor_le)
        self.main_layout.addLayout(self.descriptor_lay)

    # display the button within Maya


    def _version_layout_(self):
            self.version_lay = QtWidgets.QHBoxLayout()
            self.version_lay.addWidget(self.version_lbl)
            self.version_lay.addWidget(self.version_spinbox)
            self.main_layout.addLayout(self.version_lay)

    def _ext_layout_(self):
        self.ext_lay = QtWidgets.QHBoxLayout()
        self.ext_lay.addWidget(self.ext_lbl)
        self.ext_lay.addWidget(self.ext_le)
        self.main_layout.addLayout(self.ext_lay)

    def _bottom_button_layout_(self):
        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        self.bottom_btn_lay.addWidget(self.increment_save_btn)
        self.bottom_btn_lay.addWidget(self.save_btn)
        self.bottom_btn_lay.addWidget(self.cancel_btn)
        self.main_layout.addLayout(self.bottom_btn_lay)

    #Widgets are layout within a window
    def window_layout(self):
        """Lay out our widges in the UI"""
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self._directory_layout_()
        self._descriptor_layout_()
        self._version_layout_()
        self._ext_layout_()
        self._bottom_button_layout_()
        self.setLayout(self.main_layout)
        self.main_layout.addStretch()



    def create_connections(self):
        """Connect our widgets singals to slots"""
        self.cancel_btn.clicked.connect(self.cancel)
        self.save_btn.clicked.connect(self.save)
        self.increment_save_btn.clicked.connect(self.increment_save)


    @QtCore.Slot()
    def _populate_scenefile_properties(self):
        """Populates the SceneFile objects Properties from UI Window"""
        self.scene.dir = self.dir_le.text()
        self.scene.descriptor = self.descriptor_le.text()
        self.scene.version = self.version_spinbox.value()
        self.scene.ext = self.ext_le.text()
        self.browse_btn.ext = self.scene

    @QtCore.Slot()
    def save(self):
        """Saves the scene file"""
        self._populate_scenefile_properties()
        self.scene.save()
    @QtCore.Slot()
    def increment_save(self):
        """Automatically finds the next availble version on disks and saves up"""
        self._populate_scenefile_properties()
        self.scene.increment_and_save()


    @QtCore.Slot()
    def cancel(self):
        """Quits the dialog"""
        self.close()
