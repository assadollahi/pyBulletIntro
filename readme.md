## About The Project

pyBullet is a great framework to simulate physics for robots.
I wanted to have a very simple intro into pyBullet, that is a bit more complex than a "hello world".
It should contain a user controllable robot to demonstrate in python how to control it as well as other physical objects to interact with.
This is a mashup of some URDF files and a python script that play well together. 
The URDF files don't have .obj files in them nor do they contain images and textures. 
Thus, they are easily human readable which is the whole goal of this repo. 

Here's what you get:
[![](http://img.youtube.com/vi/UqWcz4s8a7Y/0.jpg)](http://www.youtube.com/watch?v=UqWcz4s8a7Y "pyBulletIntro")

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This demo has been developed on Ubuntu Linux, thus the paths in the python script should be changed when running on windows.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/assadollahi/pyBulletIntro.git
   ```
2. Install pyBullet
   ```sh
   pip3 install pyBullet
   ```


## Usage

To run this intro: ```python3 turtleKeyboardMove.py```


## License

Distributed under the Apache License 2.0. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Corresponding Blog Category: [https://assadollahi.de/category/pybullet/](https://assadollahi.de/category/pybullet)
Project Link: [https://github.com/assadollahi/pyBulletIntro](https://github.com/assadollahi/pyBulletIntro)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [https://github.com/erwincoumans/pybullet_robots/blob/master/turtlebot.py] (https://github.com/erwincoumans/pybullet_robots/blob/master/turtlebot.py) turtle keyboard movement
* [https://industrial-training-master.readthedocs.io/en/melodic/_source/session3/Intro-to-URDF.html] (https://industrial-training-master.readthedocs.io/en/melodic/_source/session3/Intro-to-URDF.html) URDF definition of a box
* [https://www.theconstructsim.com/exploring-ros-2-wheeled-robot-part-01/] (https://www.theconstructsim.com/exploring-ros-2-wheeled-robot-part-01/) URDF definition of a two wheeled robot, I further simplified
