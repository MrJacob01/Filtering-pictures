# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'work.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime

import PIL.Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QDialog, QPushButton, QMainWindow, QTreeView, QApplication, QMessageBox, \
    QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtGui import QPixmap, QStandardItem, QStandardItemModel, QImage, QFont, QColor
import sys



# def openImage(self, image_label):
#     image_file, _ = QFileDialog.getOpenFileName(self, "Open Image",
#                                                 "", "PNG Files (*.png);;JPG Files (*.jpeg *.jpg );;Bitmap Files (*.bmp);;\
#             GIF Files (*.gif)")
#
#     if image_file:
#         self.parent.zoom_factor = 1
#         self.parent.print_act.setEnabled(True)
#         self.parent.updateActions()
#         self.parent.brightness_slider.setValue(0)
#         image_format = self.image.format()
#         self.image = QImage(image_file)  # manipulated area
#         self.original_image = self.image.copy()  # Original image
#         self.setPixmap(QPixmap().fromImage(self.image))
#         self.resize(self.pixmap().size())
#     elif image_file == "":
#         # User selected Cancel
#         pass
#     else:
#         QMessageBox.information(self, "Error", "Unable to open image.", QMessageBox.Ok)


class MouseClick(QtWidgets.QGraphicsObject):
    def __init__(self):
        super().__init__()


"""   in TreeView change path on image  """


class StandardItem(QStandardItemModel):
    def __init__(self, path: list):
        super().__init__()

        data = []

        for img in path:
            print(img)
            image = QImage(img)
            item = QStandardItem()
            pxmap = QPixmap.fromImage(image).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            item.setData(QtCore.QVariant(pxmap), Qt.DecorationRole)

            data.append(item)
        self.appendColumn(data)




""" Open system files """


class Dl(QDialog):
    pt = None
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Open File', self)

    def open_file(self):
        res = QFileDialog.getOpenFileNames(self, 'Open File', "C:/", "jpg Files (*jpg *JPG *jpeg);;PNG Files (*png);;")
        self.pt = res[0]




""" UI Window """


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._list_img: list = []
        self.__add, self.__dele = 0, 0
        self._number = 0
        self.__local_img = None
        self.hsv = None
        self.mouse_ = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 960)
        MainWindow.setStyleSheet("gridline-color: rgb(94, 92, 100);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)


        self.back_label_right = QtWidgets.QLabel(self.centralwidget)
        self.back_label_right.setGeometry(QtCore.QRect(1600, 0, 330, 960))
        self.back_label_right.setObjectName("RightLabel")
        self.back_label_right.setStyleSheet("background-color: rgb(94, 92, 100)")

        self.graphicsView_2 = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(480, 11, 1000, 1000))
        self.graphicsView_2.resize(1200, 960)
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1610, 130, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1750, 130, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1610, 160, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label = QtWidgets.QLabel

        self.slider = QtWidgets.QSlider(Qt.Horizontal, self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(1610, 210, 200, 20))
        self.slider.setObjectName("slider")

        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 350, 960))
        self.treeView.setObjectName("treeView")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1135, 22))
        self.menubar.setObjectName("menubar")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")

        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")

        self.menuEdit.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionExport)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.msg_box_name = QMessageBox()
        self.msg_box_name.setIcon(QMessageBox.Information)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open File"))
        self.pushButton_3.setText(_translate("MainWindow", "Save File"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete img"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExport.setText(_translate("MainWindow", "Export"))

    def buttons(self):
        self.pushButton.clicked.connect(self.add_img)
        self.pushButton_2.clicked.connect(self.delet_img)
        self.pushButton_3.clicked.connect(self._save_)
        self.actionSave.triggered.connect(self._save_)
        self.actionOpen.triggered.connect(self.add_img)



    def PixmapOnPage(self, path=None):
        if path is not None:
            print(str(path))
            pixmap = QPixmap(str(path)).scaled(1000, 1000, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.graphicsView_2.setPixmap(pixmap)
        else:
            pixmap = QPixmap(path).scaled(1000, 1000, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.graphicsView_2.setPixmap(pixmap)


    def add_img(self):
        self.btn = Dl()
        self.btn.open_file()
        if self.btn.pt != '':
            if self._list_img == '':
                for i in self.btn.pt:
                    self._list_img.append(i)
            else:
                for i in self.btn.pt:
                    self._list_img.append(i)
            self.PixmapOnPage(self._list_img)
            self._number += 1

        self._set_image()


        if self.pushButton.clicked:
            self.__add += 1

    def _set_image(self):
        self.treeView.setModel(StandardItem(list(self._list_img)))
        self.treeView.setCursor(Qt.PointingHandCursor)

        self.treeView.expandAll()


        self.treeView.clicked.connect(self.mouse)

    def mouse(self, value):
        self.__local_img = int(value.row())
        self.mouse_ = int(value.row())
        self.PixmapOnPage(str(self._list_img[value.row()]))


    def delet_img(self):
        if self._list_img is not None:
            self._list_img.pop(self.mouse_)
            if len(self._list_img) >= 1:
                self.PixmapOnPage(list(self._list_img[0]))
            elif len(self._list_img) == 0:
                self.PixmapOnPage()
                self._number = 0
            else:
                self.msg_box_name.setIcon(QMessageBox.Warning)
                self.msg_box_name.setWindowTitle("Warning message")
                self.msg_box_name.setText("Add image !")
                self.msg_box_name.exec_()
        else:
            self.msg_box_name.setWindowTitle("Info message")
            self.msg_box_name.setText("Choose one image !")
            self.msg_box_name.exec_()


        self._set_image()


        if self.pushButton_2.clicked:
            self.__dele += 1


    def _save_(self):
        self.msg_box_name.setWindowTitle("Info message")
        self.msg_box_name.setText("Did you want to save images!")
        self.msg_box_name.exec_()
        for i in self._list_img:
            with PIL.Image.open(str(i)) as im:
                im.save(f"D:\{str(i).split('/')[-1]}", dpi=(300, 300))

        self.msg_box_name.setWindowTitle("Info message")
        self.msg_box_name.setText("Saved successful!")
        self.msg_box_name.exec_()


    def scroll_item(self):
        listBox = QVBoxLayout(self)
        self.setLayout(listBox)

        self.verticalScrollBar = QScrollArea(self)
        listBox.addWidget(self.verticalScrollBar)
        self.verticalScrollBar.setWidgetResizable(True)
        scrollContent = QWidget(self.verticalScrollBar)

        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        for item in self._list_img:
            scrollLayout.addWidget(item)
        self.verticalScrollBar.setWidget(scrollContent)


    # def change(self, value):
    #     h, s, v = cv2.split(self)
    #     r = 180 - value
    #     h[h > r] = 180
    #     h[h <= r] += value
    #     hsv_final = cv2.merge((h, s, v))
    #     img = cv2.cvtColor(hsv_final, cv2.COLOR_HSV2RGB)
    #     self.PixmapOnPage(img)



"""
    def _exit_(self, app):
        self.msg_box_name.setWindowTitle("Info message")
        self.msg_box_name.setText("You should exit !")
        self.msg_box_name.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg_box_name.exec_()
        if self.msg_box_name.clickedButton() == QMessageBox.Ok:
            sys.exit(app.exec_())
"""


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.buttons()
    MainWindow.show()
    sys.exit(app.exec_())

"""



        
        
        """