# image_converter ROS 2 Package

This package provides `img_con_node`, which converts images from a camera to grayscale or color based on a service call, and a launch file `image_conversion_launch.py` to start the camera and image conversion node together.

## Getting Started

### 1. Clone the repository into the `src` folder of your ROS 2 workspace
   
### 2. Build and source the workspace

### 3. Run the launch file
```bash
ros2 launch image_converter image_conversion_launch.py
```
### 4. Change image mode using the service

#### Switch to Grayscale
```bash
ros2 service call /set_greyscale_mode std_srvs/srv/SetBool "{data: true}"
```
#### Switch back to Color
```bash
ros2 service call /set_greyscale_mode std_srvs/srv/SetBool "{data: false}"
```
### 5. View the output image:
You can view the output image topic published by the node using **RViz2**:
```bash
ros2 run rviz2 rviz2
```
- Add an **Image** display in RViz2  
- Set the **Topic** to the output image topic (as configured in your launch file or node parameters)  
- You should see the camera image in grayscale or color depending on the mode.

Make sure your ROS 2 workspace is sourced before running any commands. The node publishes output images to the topic specified in the launch file or parameters.
