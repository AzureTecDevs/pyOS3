import TermTk as ttk
import os
root = ttk.TTk()

def textedit(par):
    from TermTk import TTkUtil, TTkUiLoader, TTk, TTkWindow
    from TermTk import pyTTkSlot
    class MyTextEditor(TTkWindow):
        def __init__(self):
            # The "TTkUiLoader" is responsible to init this custom object
            # and extend it to the "textEditWindow" created in this tutorial
            # NOTE: no "super().__init__()" is required
            TTkUiLoader.loadDict(TTkUtil.base64_deflate_2_obj(
                "eJytVltvG0UUXtvrXV96yYVSICBWFVIdJCwHoRLUvCSmMXTr1koMFarysNkd+Yy63rV2Z0ODVKniyalGPMCg8FYBggd+AU/8pv4Ezsyur0lQEuGV5T3znTnzfd/c/EL/" +
                "+ZuKpj7PRY2bBySKaRgIXlyrN+oNwQssoUJCRdd34ljwcrf79DENvPBbwY2BEzn9WOH6Q6dPBL+KWJc8Y/c8ysJI8FInjCmTJfdEzdbtPOH6Lv2OqPBL+wbh5TYNrMfU" +
                "YyDsPK/I6AtCe8CErSPoPMvAdn4BUQwztK0vcLPjeB4Neqpawc7Jh3DjgXMYJgzJINdWRL1RbH5NY7rvEzHk5r3AwTdPvnbD0O/SgeD6ypNGH2VthZFHIoSKXcownVsS" +
                "kN92ZEl1FlHyLOv1q19+SDtdSU2xtn2nF4v72gutlHDDT0dGg6AIb4L5HB1pkbBPWHSIlDV8WvYiEzEvuUB9LyLKKJWvrN5KGEPzZM8alLm5xYKvcBwBVSl5ydYIXJVv" +
                "FbtA4LptwIJdgMX7mpbTYAlfl/eyYTSZekPVzOyAm0N46wjehne4LkUJvjCSKYdQsmBlyMtNIO5T6ZY44qYK0LejBN5PZX0kycGtdBjkgWrggz2R8EKEi8TWeMENfWEX" +
                "uIlxPHACYee4iW3Ze5KWuT2tcYeMNb471lg9TWP6MycTOY3FQX2iS5Yd6YLGEaydoaI6UQF3bA0+tXVYt3Pw2Um2BrJtSjcV2dvzE1I8N9lhRvb6iCxWPQ/XygmuxbO4" +
                "Smeb4eAwI7t2eWeH887Kspdz1jiLbQnZdpyYkYzuxjxd88J0F0d0Vd3L8TVn+fJl3FHb1CfpTu1Q3B3RzH59NMBNnUrQxhKMVIKeSkATLmb361c/fT9Ln+sdB09Jnqvj" +
                "Odd0BurM5VXJzPqcOn7Yw3aMGJ7weDJu+r4lsdiqfbiKeZuuSwbMaocekVu2rPqlUe50Z4wTzmhzM9mbdmHXORhNpPH/ufDjP7MuQAAhDGZlQzQvFxjyTGztvMJyc1P+" +
                "Bk55M/TD6NQ5L6ldhmgm98q83PyF5OJ3PMfFtC6/tvLkk/W7H99t4HNnvS/OKyQ/J6SKQka39YT/pCVbtIWMf8u+JvlryF/7z303ps+rD2hArIdJf19dqOUd4njWo8A/" +
                "xLuk0k58Ri2ZIYaSYm5qEZUSkiS86oZBQFy5mOPsYuRGTAJ5PcMxL0XEJfRABqvYTnuB4wu+nOD1tXngUF9eWrV9vN5xieuxH8o7LiYsu/szRHnxKxzDb7ABv/PliJzs" +
                "DX/An1neKuYdY17Z9eW8ezWJckOOWRsX20iT4C8JyYITqDUFFd2ETZCd6U4uHqgTaG8KMgfy8KrNEH+JhN5zkwj/PzC1RprgBD0kN1qpiuQSalfRVHNW5GWm6qYrm3eJ" +
                "j6ZfvDv8jWkVTNsO3SSWFElS/xfnLV9T"), self)

            # Connect the open routine to the (open)"filePicked" event
            self.getWidgetByName("BtnOpen").filePicked.connect(self.openRoutine)
            # Connect the save routine to the (save)"filePicked" event
            self.getWidgetByName("BtnSave").filePicked.connect(self.saveRoutine)

        # This is a generic routine to open/read a file
        # and push the content to the "TextEdit" widget
        pyTTkSlot(str)
        def openRoutine(self, fileName):
            textEdit = self.getWidgetByName("TextEdit")
            with open(fileName) as fp:
                textEdit.setText(fp.read())

        # This is a generic routine to save the content of
        # the "TextEdit" widget to the chosen file
        pyTTkSlot(str)
        def saveRoutine(self, fileName):
            textEdit = self.getWidgetByName("TextEdit")
            with open(fileName, 'w') as fp:
                fp.write(textEdit.toPlainText())

    # Initialize TTK, add the window widget, and start the main loop
    root.layout().addWidget(MyTextEditor())


def cred(par=root):
    credit = ttk.TTkWindow(parent=par,pos=(1,1), size=(41,9), title="Credits", border=True)
    ttk.TTkLabel(parent=credit, pos=(1,1), text="PyOS3 (c) 2023 AzureTec\nPyTermTk (c) 2021-2023 Eugenio Parodi\nOS: PyOS3-3.0.0-108743")

def help(par=root):
    hlp = ttk.TTkWindow(parent=par,pos=(1,1), size=(41,10), title="(?) Help Menu", border=True)
    ttk.TTkLabel(parent=hlp, pos=(1,1), text="Using windows:\nTo move a window, drag the titlebar.\nTo resize a window, drag the edge.\nTo close a window, press [x].")
    
def terminal(par=root):
    term = ttk.TTkWindow(parent=par,pos=(1,1), size=(50,20), title="Logger", border=True, layout=ttk.TTkVBoxLayout())
    ttk.TTkLogViewer(parent=term)

def vm1(par=root):
    vm = ttk.TTkWindow(parent=par,pos=(1,1), size=(50,20), title="pyOS3 VM", border=True)
    apps2 = ttk.TTkButton(border=False, text="Apps", pos=(0,0), parent=vm)
    apps2.clicked.connect(lambda : log("Opened Apps", apps, vm))
    
def apps(par=root):
    app = ttk.TTkWindow(parent=par,pos=(1,1), size=(20,8), title="Apps", border=True, layout=ttk.TTkVBoxLayout())
    term1 = ttk.TTkButton(border=False, text="Logger", pos=(1,1), parent=app)
    term1.clicked.connect(lambda : log("Opened app Logger", terminal, par))
    wiw2 = ttk.TTkButton(border=False, text="pyOS3 VM", pos=(1,1), parent=app)
    wiw2.clicked.connect(lambda : logM(["Opened app pyOS3-vm", "pyOS3 VM (c) 2023 AzureTecDevs"], vm1, par))
    credit1 = ttk.TTkButton(border=False, text="Credits", pos=(1,1), parent=app)
    credit1.clicked.connect(lambda : log("Opened app Credits", cred, par))
    text1 = ttk.TTkButton(border=False, text="Text Editor", pos=(1,1), parent=app)
    text1.clicked.connect(lambda : log("Opened app Text Editor", textedit, par))

def log(msg, run, par):
    run(par)
    ttk.TTkLog.info(msg)

def logM(msg, run, par):
    run(par)
    for e in msg:
        ttk.TTkLog.info(e)
# Default App(s)
apps(root)
terminal(root)
# Taskbar
s = os.get_terminal_size()
t = s[1] - 1
apps1 = ttk.TTkButton(border=False, text="Apps", pos=(0,t), parent=root)
apps1.clicked.connect(lambda : log("Opened Apps", apps, root))
w = s[1] - 1
q = len("Apps") + 2
apps2 = ttk.TTkButton(border=False, text="?", pos=(q,w), parent=root)
apps2.clicked.connect(lambda : log("Opened Help Menu", help, root))
root.mainloop()
