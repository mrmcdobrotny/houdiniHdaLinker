from PySide2 import QtWidgets, QtCore, QtGui
import sys, os, glob
from uiHoudiniHdaLinker import Ui_Form

try:
    import hou
except ModuleNotFoundError:
    pass

class hdaLinker(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(hdaLinker, self).__init__()
        self.setupUi(self)

        self.initTable()

        self.lineEditFilter.textChanged.connect(self.filterTable)
        self.pushCheck.clicked.connect(self.checkSelected)
        self.pushUncheck.clicked.connect(self.uncheckSelected)
        self.pushCreateLinks.clicked.connect(self.createLinks)
        self.pushRemoveLinks.clicked.connect(self.removeLinks)

    def closeEvent(self, event):
        self.setParent(None)
        self.close()
        

    def initTable(self):
        self.model = QtGui.QStandardItemModel(self)
        root = "/media/white/tools/otls"
        self.files_paths = glob.glob(os.path.join(root, "*.hda"))
        self.files_names = [os.path.split(filepath)[1] for filepath in self.files_paths]
        self.hda_folders = glob.glob(os.path.join(root, "hda_*"))
        self.hda_labels = []
        [self.hda_labels.append(os.path.split(path)[1][4:]) for path in self.hda_folders]
        self.hda_folders.insert(0, "blanc")        
        self.hda_labels.insert(0,"HDA")

        for row, file in enumerate(self.files_names):
            rowItems = []
            for column, label in enumerate(self.hda_labels):
                
                if column == 0:
                    rowItems.append(QtGui.QStandardItem("{}".format(file)))
                else:
                    item = QtGui.QStandardItem("{}".format(label))
                    item.setCheckable(True)
                    inHdaFolder = os.path.exists(os.path.join(self.hda_folders[column], file))
                    if inHdaFolder:
                        item.setCheckState(QtCore.Qt.CheckState.Checked)
                    rowItems.append(item)

            self.model.invisibleRootItem().appendRow(rowItems)


        self.model.setHorizontalHeaderLabels(self.hda_labels)
        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)
        self.tableView.setModel(self.proxy)
        
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


    def filterTable(self):
        text = self.lineEditFilter.text()
        search = QtCore.QRegExp(    text,
                                    QtCore.Qt.CaseInsensitive,
                                    QtCore.QRegExp.RegExp
                                    )

        self.proxy.setFilterRegExp(search)   

    def checkSelected(self):
        selectionModel = self.tableView.selectionModel()
        selected = selectionModel.selectedIndexes()
        for index in selected:
            srcIndex = self.proxy.mapToSource(index)
            if srcIndex.column() != 0:
                self.model.itemFromIndex(srcIndex).setCheckState(QtCore.Qt.CheckState.Checked)

    def uncheckSelected(self):
        selectionModel = self.tableView.selectionModel()
        selected = selectionModel.selectedIndexes()
        for index in selected:
            srcIndex = self.proxy.mapToSource(index)
            if srcIndex.column() != 0:
                self.model.itemFromIndex(srcIndex).setCheckState(QtCore.Qt.CheckState.Unchecked)

    def createLinks(self):
        selectionModel = self.tableView.selectionModel()
        selected = selectionModel.selectedIndexes()

        for row, file in enumerate(self.files_paths):
            for column, folder in enumerate(self.hda_folders):
                if column != 0:
                    #index = self.proxy.index(row,column)
                    #srcIndex = self.proxy.mapToSource(index)
                    index = self.model.index(row, column)
                    proxyIndex = self.proxy.mapFromSource(index)
                    if proxyIndex in selected or not self.checkProcessSelected.isChecked():
                        item = self.model.itemFromIndex(index)
                        checkState = item.checkState()
                        if checkState == QtCore.Qt.CheckState.Checked:
                            new_link = os.path.join(self.hda_folders[column], self.files_names[row])
                            inHdaFolder = os.path.exists(new_link)
                            if not inHdaFolder:
                                print("Creating symlink {}".format(new_link))
                                ln = os.popen("ln -s {} {}".format(file, new_link))
                                ln.close()
        

    def removeLinks(self):
        links = []
        selectionModel = self.tableView.selectionModel()
        selected = selectionModel.selectedIndexes()
        for row, file in enumerate(self.files_paths):
            for column, folder in enumerate(self.hda_folders):
                if column != 0:
                    #index = self.proxy.index(row,column)
                    #srcIndex = self.proxy.mapToSource(index)
                    index = self.model.index(row, column)
                    proxyIndex = self.proxy.mapFromSource(index)
                    if proxyIndex in selected or not self.checkProcessSelected.isChecked():
                        item = self.model.itemFromIndex(index)
                        checkState = item.checkState()
                        if checkState == QtCore.Qt.CheckState.Unchecked:
                            new_link = os.path.join(self.hda_folders[column], self.files_names[row])
                            inHdaFolder = os.path.exists(new_link)
                            if inHdaFolder:
                                print(new_link)
                                rm = os.popen("rm {}".format(new_link))
                                rm.close()

def main():
    if __name__ == 'houdiniHdaLinkerMain':
        #print(__name__)
        #app = QtWidgets.QApplication()
        mainWin = hdaLinker()
        mainWin.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
        #mainWin.setParent(None)
        mainWin.show()
        #ret = app.exec_()
        #sys.exit( ret )    

if __name__ == '__main__':
    #print(__name__)
    app = QtWidgets.QApplication(sys.argv)
    mainWin = hdaLinker()
    mainWin.show()
    ret = app.exec_()
    sys.exit( ret )
