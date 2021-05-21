import logging
import pymel.core as pmc
from pymel.core.system import Path

log = logging.getLogger(__name__)


# var = scene
class SceneFile(object):
    """This class represents a DCC software scene file

    Attributes for UI titles in maya
       dir (Path to the project that it is set to)
       descriptor (str or name of title user puts)
       version (constant number 1 to infinity)
       ext (str, name of program to open up)
    """

    def __init__(self, dir='', descriptor='main', version=1, ext='ma'):
        # leave one space
        self._dir = Path(dir)
        self.descriptor = descriptor
        self.version = version
        self.ext = ext
        # self.scene = pmc.system.sceneName

        # Private function
        # if scene:
        # self._init_properties_from_path(self.scene)

    @property
    def dir(self):
        print("getting")
        return Path(self._dir)

    """gets the location from computer"""

    @dir.setter
    def dir(self, val):
        print("setting")
        self._dir = Path(val)

    """sets location of folder"""

    """A Method used to store the PythonPath """

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

    def _init_properties_from_path(self, path):
        self._dir = Path.dirname()
        self.ext = Path.ext[1:]
        self.descriptor, version = path.name.split("_")
        self.version = int(version.split(".")[0][1:])

    """Function to continue running without by excepting Only RuntimeError"""

    @property
    def next_avil_ver(self):
        pattern = "{descriptor}_v*.{ext}".format(descriptor=self.descriptor,
                                                 ext=self.ext)
        self.dir.files()
        matched_scenes = [file for file in self.dir.files()
                          if file.fnmatch(pattern)]
        versions = [int(scene.name.split("_v")[1].split(".")[0])
                    for scene in matched_scenes]
        # removes duplicate in list
        versions = list(set(versions))
        versions.sort()
        return versions[-1] + 1

    def save(self):
        try:
            pmc.system.saveAs(self.path())
            # Anytype of Runtime Exception be specific
        except RuntimeError:
            log.warning("Missing directories. Creating directories")
            self.dir.makedirs_p()
            pmc.system.saveAs(self.path())

    def increment_and_save(self):
        self.version = self.next_avil_ver
        self.save()
