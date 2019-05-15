import os
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic
import cv2
import numpy as np
SAVE_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'MAPIR_Processing_dockwidget_Viewer_Save.ui'))

class SaveDialog(QtWidgets.QDialog, SAVE_CLASS):

    def __init__(self, parent=None):
        """Constructor."""
        super(SaveDialog, self).__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)

    def on_ViewerSaveFileButton_released(self):
        with open(os.path.dirname(__file__) + os.sep + "instring.txt", "r+") as instring:
            self.ViewerSaveFile.setText(QtWidgets.QFileDialog.getExistingDirectory(directory=instring.read()))
            instring.truncate(0)
            instring.seek(0)
            instring.write(self.ViewerSaveFile.text())

            self.SaveButton.setStyleSheet("QComboBox {width: 75; height: 23;}")
            self.SaveButton.setEnabled(True)

    def on_SaveButton_released(self):
        try:
            ftosave = self.parent.KernelBrowserFile.text().split(r'/')[-1].split('.')
            if self.SaveLutBox.isChecked() == True and self.parent.LUT_to_save is not None:
                cv2.imwrite(self.ViewerSaveFile.text() + os.sep + ftosave[0] + '_LUT.' + ftosave[1], self.parent.LUT_to_save)

            if self.SaveIndexBox.isChecked() == True and self.parent.index_to_save is not None:
                self.parent.index_to_save = self.parent.index_to_save.astype("float32")
                cv2.imwrite(self.ViewerSaveFile.text() + os.sep + ftosave[0] + '_NDVI.' + ftosave[1], self.parent.index_to_save)


        except Exception as e:
            print(e)
        self.close()

    def on_CancelButton_released(self):
        self.close()
