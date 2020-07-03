import logging

import pymel.core as pmc
from pymel.core.system import Path

log = logging.getLogger(__name__)


class SceneFile(object):
    """This class represents a DCC software scene file

    Attributes for UI titles in maya
       dir (Path to the project that it is set to)
       descriptor (str or name of title user puts)
       version (constant number 1 to infinity)
       ext (str, name of program to open up)
    """

    def __init__(self, dir ='', descriptor='main', version=1, ext='ma'):
        # leave one space
        self._dir = Path(dir)
        self.descriptor = descriptor
        self.version = version
        self.ext = ext


    @property
    #gets the location from computer
    def dir(self):
        print("getting")
        return Path(self._dir)
    #sets location of folder
    @dir.setter
    def dir(self, val):
        print("setting")
        self._dir = Path(val)


    #  METHOD
    def basename(self):
        """Returns the DCC scene file name
        e.g. ship_001.ma

        Returns:
            str: the name of the scene file

        """
        name_pattern = "{descriptor}_{version:03d}.{ext}"
        name = name_pattern.format(descriptor=self.descriptor,
                                   version=self.version,
                                   ext=self.ext)
        return name

    def path(self):

        return Path(self.dir) / self.basename()
    """Function to continue running without by excepting Only RuntimeError"""
    def save(self):
        try:
            pmc.system.saveAs(self.path())
            # Anytype of Runtime Exception be specific
        except RuntimeError:
            log.warning("Missing directories. Creating directories")
            self.dir.makedirs_p()
            pmc.system.saveAs(self.path())
