import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance

import mayautils

"""Imported models like mayautils QtWidgets and tQCore into smartsave.py """


def maya_main_window():
    """Return the maya main window widget
    small function to create a Window from maya"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)



class SmartSaveUI(QtWidgets.QDialog):
    """Simple UI Class
    One class for a bunch of functions built in"""


    def __init__(self):
        """Constructor"""
        # Passing th object Simple UI as an argument to super()
        # makes this lone python 2 and 3 compatible with window
        super(SmartSaveUI, self).__init__(parent=maya_main_window())
        self.scene = mayautils.SceneFile()


        """name of GUI Window"""
        self.setWindowTitle("Smart Save")
        """resize a window"""
        self.resize(500, 200)
        """removes buttons like ?"""
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)


        """displays the widgets on the UI Window"""
        self.display_widgets()

        """Both Functions needed to display Smart Save UI"""
        self.window_layout()
        """Connect the buttons"""
        self.create_connections()


    """function that displays widgets"""
    def display_widgets(self):
        self.title_widget()
        self.directory_widget()
        self.descriptor_widget()
        self.version_widget()
        self.extension_widget()
        self.create_button()


    """Changes title name label"""
    def title_widget(self):
        """Create widgets for our UI"""
        self.title_lbl = QtWidgets.QLabel("Smart Save")
        self.title_lbl.setStyleSheet("font: bold 40px")

    def directory_widget(self):
        """label used to browse for the directory"""
        self.dir_lbl = QtWidgets.QLabel("Directory")
        self.dir_le = QtWidgets.QLineEdit()
        self.dir_file = QtWidgets.QFileDialog()


        self.dir_le.setText(self.scene.dir)




    def descriptor_widget(self):

        self.descriptor_lbl = QtWidgets.QLabel("Descripter")
        self.descriptor_le = QtWidgets.QLineEdit()
        self.descriptor_le.setText(self.scene.descriptor)

    def version_widget(self):

        self.version_lbl = QtWidgets.QLabel("Version")
        self.version_spinbox = QtWidgets.QSpinBox()
        self.version_file = QtWidgets.QFileDialog()
        self.version_spinbox.setValue(self.scene.version)


    def extension_widget(self):

        self.ext_lbl = QtWidgets.QLabel("Extension")
        self.ext_le = QtWidgets.QLineEdit()
        self.ext_le.setText(self.scene.ext)


    def create_button(self):

        self.save_btn = QtWidgets.QPushButton("Save")
        self.version_file = QtWidgets.QPushButton("Increment and Save")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.dir_file = QtWidgets.QPushButton("Browse...")


    def _directory_layout_(self):
        """Displays the directory of the function"""
        self.directory_lay = QtWidgets.QHBoxLayout()
        self.directory_le = QtWidgets.QHBoxLayout()
        self.directory_file = QtWidgets.QHBoxLayout()
        self.directory_file.addWidget(self.dir_file)
        self.directory_lay.addWidget(self.dir_lbl)
        self.directory_lay.addWidget(self.dir_le)


        self.main_layout.addLayout(self.directory_lay)
        self.directory_lay.addWidget(self.dir_file)

    def _descriptor_layout_(self):
        """A name that the user will put in For example car"""
        self.descriptor_lay = QtWidgets.QHBoxLayout()
        self.descriptor_lay.addWidget(self.descriptor_lbl)
        self.descriptor_lay.addWidget(self.descriptor_le)
        self.main_layout.addLayout(self.descriptor_lay)



    def _version_layout_(self):
        """Puts a number for the version needed"""
        self.version_lay = QtWidgets.QHBoxLayout()

        self.version_lay.addWidget(self.version_lbl)
        self.version_lay.addWidget(self.version_spinbox)

        self.main_layout.addLayout(self.version_lay)



    def _ext_layout_(self):
        """extension for the name of a file like maya that reads ma"""
        self.ext_lay = QtWidgets.QHBoxLayout()
        self.ext_lay.addWidget(self.ext_lbl)
        self.ext_lay.addWidget(self.ext_le)
        self.main_layout.addLayout(self.ext_lay)

    def _bottom_button_layout_(self):
        """Lays out button inputs for increment and save, save and close"""
        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        #
        self.bottom_btn_lay.addWidget(self.version_file)
        self.bottom_btn_lay.addWidget(self.save_btn)
        self.bottom_btn_lay.addWidget(self.cancel_btn)

        self.main_layout.addLayout(self.bottom_btn_lay)


    def window_layout(self):
        """Lay out our widges in the UI
        Widgets are layout within a window"""
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
        """Connect our widgets singals to slots
        Widgets are connected to the window so that they will execute"""
        self.cancel_btn.clicked.connect(self.cancel)
        self.save_btn.clicked.connect(self.save)
        self.version_file.clicked.connect(self.save)
        self.dir_file.clicked.connect(self._populate_scenefile_properties)


    @QtCore.Slot()
    def _populate_scenefile_properties(self):
        """Populates the SceneFile objects Properties from UI Window"""
        self.scene.dir = self.dir_le.text()
        self.scene.descriptor = self.descriptor_le.text()
        self.scene.version = self.version_spinbox.value()
        self.scene.ext = self.ext_le.text()

    @QtCore.Slot()
    def save(self):
        """Function that Saves the scene file"""
        self._populate_scenefile_properties()
        self.scene.save()
    @QtCore.Slot()
    def increment_save(self):
        """Automatically finds the next available version on disks and saves up"""
        self._populate_scenefile_properties()
        self.scene.increment_and_save()


    @QtCore.Slot()
    def cancel(self):
        """Quits the dialog box"""
        self.close()
