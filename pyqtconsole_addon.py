bl_info = {
    "name": "Python console (PyQt)",
    "description": "A Python console Qt widget",
    "author": "Alex Hughes, Hannes D",
    "version": (1, 0),
    "blender": (2, 91, 0),
    "location": "Window/Python Console (Qt)",
    "category": "Development"
}

import sys
import bpy


class PyQtConsolePreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("wm.open_pyqt_console", text="Open Python Console (Qt)")


class OpenPyQtConsoleOperator(bpy.types.Operator):
    bl_idname = "wm.open_pyqt_console"
    bl_label = "Python Console (Qt)"
    console_widget = None

    def execute(self, context):
        from qtpy import QtCore
        from qtpy.QtWidgets import QApplication
        from pyqtconsole.console import PythonConsole
        from pyqtconsole.highlighter import format

        app = QApplication.instance()
        if not app:
            app = QApplication(sys.argv)

        # hookup bqt if found to keep in foreground
        parent = None
        if hasattr(app, 'blender_widget'):
            parent = app.blender_widget

        # todo get colors dynamically from blender style
        console = PythonConsole(formats={
            'keyword':    format('darkred', 'bold'),
            'operator':   format('orange'),
            'brace':      format('orange'),
            'defclass':   format('greenyellow', 'bold'),
            'string':     format('gold'),
            'string2':    format('goldenrod'),
            'comment':    format('grey', 'italic'), # done
            'self':       format('mediumorchid', 'italic'),
            'numbers':    format('deepskyblue'),
            'inprompt':   format('white', 'bold'),
            'outprompt':  format('deepskyblue', 'bold'),
            }, 
            parent=parent)


        console.setStyleSheet("QWidget {background-color:#222222}")
        console.setWindowFlags(console.windowFlags() | QtCore.Qt.Tool)
        console.setWindowTitle("Python Console")
        console.show()

        console.eval_queued()

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OpenPyQtConsoleOperator.bl_idname)


def register():
    
    from qtpy.QtWidgets import QApplication
    from pyqtconsole.console import PythonConsole
    from pyqtconsole.highlighter import format

    bpy.utils.register_class(PyQtConsolePreferences)
    bpy.utils.register_class(OpenPyQtConsoleOperator)
    bpy.types.TOPBAR_MT_window.append(menu_func)


def unregister():
    bpy.utils.unregister_class(PyQtConsolePreferences)
    bpy.utils.unregister_class(OpenPyQtConsoleOperator)
    bpy.types.TOPBAR_MT_window.remove(menu_func)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





