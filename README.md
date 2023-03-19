# pyqtconsole_addon
a Blender add-on wrapper for [pyqtconsole](https://github.com/pyqtconsole/pyqtconsole), a QtWidget Python console.
![image](https://user-images.githubusercontent.com/3758308/226176132-224c5290-4f54-42c9-945a-55eaa89fc6a6.png)



## Installation
- ensure you have either PySide2 or PyQt5 installed. (PySide2 recommended)
- OPTIONAL: I recommend to install the addon [bqt](https://github.com/techartorg/bqt) to keep the console correctly in the foreground. (Uses PySide2)
- Install this add-on (the .py file), 
  - either put it in an add-on folder, 
  - or install through `Edit/Preferences... (menu) -> add-ons (tab) -> Install (button)`
- install the python module [pyqtconsole](https://pypi.org/project/pyqtconsole/) in your [blender modules](https://docs.blender.org/manual/en/latest/advanced/blender_directory_layout.html) folder. 
  - either pip install manually `pip install pyqtconsole` with correct settings. `-t my-target-folder` & `cd` to blender's pip.exe
    - Ensure you use the pip in the blender folder
    - and [target](https://pip.pypa.io/en/stable/cli/pip_install/#:~:text=%2Dt%2C-,%2D%2Dtarget,-%3Cdir%3E%23) a blender modules folder
  - or use the [blender pip add-on](https://github.com/amb/blender_pip) and install `pyqtconsole`
  - or manually paste the python module from [pyqtconsole](https://github.com/pyqtconsole/pyqtconsole) in a blender modules folder. e.g. `addons/modules` & install the dependencies `qtpy` & `jedi` yourself 
