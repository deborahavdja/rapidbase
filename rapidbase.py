import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox
from PyQt5.QtGui import QIcon
import screen_brightness_control as sbc

class RapidBase:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self.app)

        self.menu = QMenu()
        
        # Create Brightness Menu
        self.brightness_menu = QMenu("Brightness")
        for level in range(0, 110, 10):  # Levels 0, 10, ..., 100
            action = QAction(f"{level}%", self.app)
            action.triggered.connect(lambda checked, l=level: self.set_brightness(l))
            self.brightness_menu.addAction(action)
        
        # Create Contrast Menu
        self.contrast_menu = QMenu("Contrast")
        for level in range(0, 110, 10):  # Levels 0, 10, ..., 100
            action = QAction(f"{level}%", self.app)
            action.triggered.connect(lambda checked, l=level: self.set_contrast(l))
            self.contrast_menu.addAction(action)

        # Add menus to the tray icon menu
        self.menu.addMenu(self.brightness_menu)
        self.menu.addMenu(self.contrast_menu)

        # Add Exit option
        exit_action = QAction("Exit", self.app)
        exit_action.triggered.connect(self.exit_app)
        self.menu.addAction(exit_action)

        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()

    def set_brightness(self, level):
        try:
            sbc.set_brightness(level)
            QMessageBox.information(None, "Brightness", f"Brightness set to {level}%")
        except Exception as e:
            QMessageBox.critical(None, "Error", str(e))

    def set_contrast(self, level):
        # Placeholder for contrast; actual implementation will depend on the library or method used
        QMessageBox.information(None, "Contrast", f"Contrast set to {level}% (Placeholder)")

    def exit_app(self):
        self.app.quit()

if __name__ == "__main__":
    rapid_base = RapidBase()
    sys.exit(rapid_base.app.exec_())