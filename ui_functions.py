from run import *

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.side_menu_container.width()
            maxExtend = maxWidth
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.side_menu_container, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()



    def maximize_window(self):
        # If window maximized
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()



    