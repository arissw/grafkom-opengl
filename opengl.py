from pyglet.gl import *

wdw = pyglet.window.Window()

@wdw.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3ub(51, 255, 51)
    glVertex2f(wdw.width/2, 0)
    glVertex2f(0, wdw.height/2)
    glVertex2f(wdw.width/4, wdw.height)
    glVertex2f(wdw.width/4 * 3, wdw.height)
    glVertex2f(wdw.width, wdw.height/2)
    glEnd()

pyglet.app.run()