from pymodaq_plugins_pylablib_camera.daq_viewer_plugins.plugins_2D import daq_2Dviewer_GenericPylablibCamera
from pymodaq.daq_viewer.utility_classes import DAQ_Viewer_base, comon_parameters, main

from pylablib.devices import PCO


class DAQ_2DViewer_PCOTest(daq_2Dviewer_GenericPylablibCamera):
    """
    """
    def list_cameras(self):
        # Generate a  **list**  of available cameras.
        # Two cases:
        # 1) Some pylablib classes have a .list_cameras method, which returns a list of available cameras, so we can just use that
        # 2) Other classes have a .get_cameras_number(), which returns the number of connected cameras
        #    in this case we can define the list as self.camera_list = [*range(number_of_cameras)]

        # For PCO, this returns the number of connected cameras
        self.camera_list = [*range(PCO.get_cameras_number())]


    def init_controller(self):
        # Define the camera controller.
        # Use any argument necessary (serial_number, camera index, etc.) depending on the camera

        # Init camera with currently selected serial number in the camera list
        return PCO.PCOSC2Camera(idx=self.params.child("camera_list").value())



if __name__ == '__main__':
    main(__file__)
