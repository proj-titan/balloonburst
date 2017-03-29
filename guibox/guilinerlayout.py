import guibox

class linerlayout(guibox.guigroupobj):
    #
    def __init__(self, direction, transform):
        self.direction = direction
        self.child = []
        self.transformnext = guibox.transform(transform)#copy
    #
    def addguiobj(self, guiobj, guiarg):
        guiarg.transform.x = self.transformnext.x
        guiarg.transform.y = self.transformnext.y
        guiarg.transform.update()
        self.transformnext.x = guiarg.transform.lastx
        self.transformnext.y = guiarg.transform.lasty - 
            guiarg.transform.y
        self.child.append((guiobj, guiarg.transform, guiarg))
