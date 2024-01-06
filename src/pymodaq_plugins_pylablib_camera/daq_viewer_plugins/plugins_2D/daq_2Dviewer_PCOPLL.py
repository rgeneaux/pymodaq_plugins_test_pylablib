from pymodaq_plugins_pylablib_camera.daq_viewer_plugins.plugins_2D.daq_2Dviewer_GenericPylablibCamera import DAQ_2DViewer_GenericPylablibCamera
from pymodaq.control_modules.viewer_utility_classes import main

from pylablib.devices import PCO


class DAQ_2DViewer_PCOPLL(DAQ_2DViewer_GenericPylablibCamera):
    """
    """
    # Generate a  **list**  of available cameras.
    # Two cases:
    # 1) Some pylablib classes have a .list_cameras method, which returns a list of available cameras, so we can just use that
    # 2) Other classes have a .get_cameras_number(), which returns the number of connected cameras
    #    in this case we can define the list as self.camera_list = [*range(number_of_cameras)]

    # For PCO, this returns the number of connected cameras
    camera_list = [*range(PCO.get_cameras_number())]

    # Update the params (nothing to change here)
    params = DAQ_2DViewer_GenericPylablibCamera.params
    params[next((i for i, item in enumerate(params) if item["name"] == "camera_list"), None)]['limits'] = camera_list


    def init_controller(self):
        # Define the camera controller.
        # Use any argument necessary (serial_number, camera index, etc.) depending on the camera

        # Init camera with currently selected serial number in the camera list
        return PCO.PCOSC2Camera(idx=self.params.child("camera_list").value())


if __name__ == '__main__':
    main(__file__)
