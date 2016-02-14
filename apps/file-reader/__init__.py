import pyos

state = None
app = None

def lines(data):
    count = 1
    for c in data.replace("\r\n", '\n'):
        if c == '\n':
            count += 1
    return count

def loadFile(path):
    f = open(path, "rU")
    contents = str(f.read())
    lnCount = lines(contents)
    scroller = pyos.GUI.ScrollableContainer((0, 0), width=app.ui.width, height=app.ui.height)
    text = pyos.GUI.MultiLineText((0, 0), contents, (0, 0, 0), 12, width=scroller.container.width, height=16*lnCount)
    scroller.addChild(text)
    app.ui.addChild(scroller)
    app.ui.refresh()
    f.close()

def onStart(s, a):
    global state, app
    state = s
    app = a
    if app.file != None:
        loadFile(app.file)
        app.file = None
    else:
        state.getApplicationList().getApp("files").getModule().FilePicker((10, 10), app, width=app.ui.width-20, height=app.ui.height-20,
                                                                          onSelect=loadFile).display()