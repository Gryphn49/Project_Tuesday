# import the library
from appJar import gui
# create a GUI variable called app


def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Input:")
        print("Input:", usr)

app = gui()

app.addLabelEntry("Input:")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)


app.go()
