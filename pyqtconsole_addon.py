import sys

from qtpy.QtWidgets import QApplication
from pyqtconsole.console import PythonConsole
from pyqtconsole.highlighter import format

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

if not QApplication.instance():
    app = QApplication(sys.argv)
    
console.setStyleSheet("QWidget {background-color:#222222}")
console.show()

console.eval_queued()
