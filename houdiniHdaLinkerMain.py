try:
    from PySide2 import QtWidgets, QtCore, QtGui
except:
    from Qt import QtWidgets, QtCore, QtGui

try:
    import hou
except ModuleNotFoundError:
    pass

from uiHoudiniHdaLinker import Ui_Form
from uiHoudiniHdaLinkerDialog import Ui_Dialog
import sys, os, glob, json, time

class areYouSure(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, listToDelete):
        super(areYouSure, self).__init__()
        self.setupUi(self)
        self.listItems = listToDelete
        self.initList()

        self.pushDecline.clicked.connect(self.close)
        self.pushAccept.clicked.connect(self.delete)
        
    def initList(self):
        for item in self.listItems:
            self.listWidget.addItem(item[0])
    def delete(self):
        for item in self.listItems:
            name = item[0]
            path = item[1]
            if os.path.exists(path):
                print("{} is going to be removed".format(name))

class Model(QtGui.QStandardItemModel):
    def __init__(self):
        super(Model, self).__init__()
        self.currentText = "default"

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.currentText = value
            self.dataChanged.emit(index, index)
            
            return True
        else:
            return False

class hdaLinker(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(hdaLinker, self).__init__()
        self.setupUi(self)
        self.hdaLoaderRoot = "/media/white/tools/scripts/houdini/houdiniLoadHda/"
        self.keySequence = ""
        ###

        self.pushDelete.hide()
        self.pushDelete.setStyleSheet("background-color:rgb(255,0,0)")

        ###
        self.readComments()
        self.initTable()
        self.tableView.setColumnHidden(1, True)
        

        self.model.dataChanged.connect(self.commentSelected)

        self.lineEditFilter.textChanged.connect(self.filterTable)
        self.checkBoxFilterChecked.stateChanged.connect(self.filterTable)
        self.pushCheck.clicked.connect(self.checkSelected)
        self.pushUncheck.clicked.connect(self.uncheckSelected)
        self.pushCreateLinks.clicked.connect(self.createLinks)
        self.pushRemoveLinks.clicked.connect(self.removeLinks)
        self.pushDelete.clicked.connect(self.deleteHda)


    def closeEvent(self, event):
        self.setParent(None)
        self.updateCommentsFile()
        #self.close()
        
    def keyPressEvent(self, event):
        self.keySequence += event.text()
        if "iddqd" in self.keySequence:
            
            if self.pushDelete.isHidden():
                self.pushDelete.show()
                self.tableView.setColumnHidden(1, False)
            else:
                self.pushDelete.hide()
                self.tableView.setColumnHidden(1, True)
            self.keySequence = ""
        #print(self.keySequence)
        
    def readComments(self):
        #root = "/media/white/tools/scripts/houdini/houdiniLoadHda/"
        self.comment_path = os.path.join(self.hdaLoaderRoot, ".usercomments")
        try:
            with open(self.comment_path, 'r') as f:
                try:
                    self.comments = json.load(f)
                except ValueError:
                    self.comments = {}
        except IOError:
            self.comments = {}

    def updateCommentsFile(self):
        comments_list = {}
        checkDeleteList = {}
        for row, file in enumerate(self.files_names):
            index = self.model.index(row,2)
            #proxyIndex = self.proxy.mapFromSource(index)
            comment = self.model.itemFromIndex(index).text()
            comments_list[file] = comment
            
            checkDelIndex = self.model.index(row,1)
            #checkDelProxyIndex = self.proxy.mapFromSource(checkDelIndex)
            checkDeleteList[file] = self.model.itemFromIndex(checkDelIndex).checkState() == QtCore.Qt.CheckState.Checked

        with open(self.comment_path, 'w') as f:

            self.comments["__comments"] = comments_list
            self.comments["__checkDelete"] = checkDeleteList
            jsn = json.dumps(self.comments, indent=4)
            f.write(jsn)
    def deleteHda(self):
        #print("Dont even try to do this!!!")
        listToDelete = []
        for row, fileName in enumerate(self.files_names):
            checkDelIndex = self.model.index(row,1)
            if self.model.itemFromIndex(checkDelIndex).checkState() == QtCore.Qt.CheckState.Checked:
                filePath = self.files_paths[row]
                listToDelete.append((fileName, filePath))
        dialog = areYouSure(listToDelete)
        #dialog.setParent(self)
        #dialog.show()
        dialog.exec_()

    def commentSelected(self): ##########################################################
        selectionModel = self.tableView.selectionModel()
        selected = selectionModel.selectedIndexes()
        for index in selected:
            srcIndex = self.proxy.mapToSource(index)
            if srcIndex.column() == 2:
                item = self.model.itemFromIndex(srcIndex)
                item.setText(self.model.currentText)
                #print(item.row(), self.model.currentText)
                #self.model.itemFromIndex(srcIndex).setCheckState(QtCore.Qt.CheckState.Checked)

    def initTable(self):
        #self.model = QtGui.QStandardItemModel(self)
        self.model = Model()
        root = "/media/white/tools/otls"
        self.files_paths = glob.glob(os.path.join(root, "*.hda"))
        self.files_names = [os.path.split(filepath)[1] for filepath in self.files_paths]
        self.hda_folders = glob.glob(os.path.join(root, "hda_*"))
        self.hda_labels = ["HDA", "Delete", "Comment"]
        [self.hda_labels.append(os.path.split(path)[1][4:]) for path in self.hda_folders]
        self.hda_folders.insert(0, "blanc")
        self.hda_folders.insert(1, "blanc")
        self.hda_folders.insert(2, "blanc")
        #self.hda_labels.insert(0,"HDA")
        #self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #start = time.time()
        #timeExist = 0.0
        for row, file in enumerate(self.files_names):
            rowItems = []
            for column, label in enumerate(self.hda_labels):
                
                if column == 0:
                    item = QtGui.QStandardItem("{}".format(file))
                    item.setEditable(False)
                    rowItems.append(item)
                elif column == 1:
                    item = QtGui.QStandardItem()
                    item.setCheckable(True)
                    try:
                        if self.comments["__checkDelete"][file]:
                            state = QtCore.Qt.CheckState.Checked
                        else:
                            state = QtCore.Qt.CheckState.Unchecked
                    except:
                        state = QtCore.Qt.CheckState.Unchecked
                    item.setCheckState(state)
                    item.setEditable(False)
                    rowItems.append(item)
                elif column == 2:
                    try:
                        comment = QtGui.QStandardItem("{}".format(self.comments["__comments"][file]))
                        comment.setEditable(True)
                        rowItems.append(comment)
                    except KeyError:
                        comment = QtGui.QStandardItem("")
                        comment.setEditable(True)
                        rowItems.append(comment)
                else:
                    item = QtGui.QStandardItem("{}".format(label))
                    item.setCheckable(True)
                    item.setEditable(False)
                    #start = time.time()
                    inHdaFolder = os.path.isfile(os.path.join(self.hda_folders[column], file))
                    #end = time.time()
                    #timeExist += (end - start)
                    if inHdaFolder:
                        item.setCheckState(QtCore.Qt.CheckState.Checked)
                    rowItems.append(item)
            self.model.invisibleRootItem().appendRow(rowItems)
            #end = time.time()
            #print(end - start)
        #print("check files - {} sec".format(timeExist))

        self.model.setHorizontalHeaderLabels(self.hda_labels)
        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)
        self.tableView.setModel(self.proxy)
        
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        
    def filterChecked(self):
        roleCheck = QtCore.Qt.CheckStateRole
        state = QtCore.Qt.CheckState.Checked
        nrows = self.model.rowCount()
        start = self.model.index(0,0)
        checkedList = self.model.match(start, roleCheck, state, nrows)
        if self.checkBoxFilterChecked.isChecked():
            #self.proxy.setFilterRole(QtCore.Qt.checkStateRole)

            for row in range(self.model.rowCount()):
                rowChecked = False
                for col in range(self.model.columnCount()-3):
                    index = self.model.index(row,col+3)
                    #srcIndex = self.proxy.mapToSource(index)
                    item = self.model.itemFromIndex(index)
                    rowChecked = rowChecked or (item.checkState() == QtCore.Qt.CheckState.Checked)
                    print(rowChecked)
                print("row {} checked {}".format(row, rowChecked))
                #item = self.proxy.item(row,0)
                if not rowChecked:
                    self.tableView.hideRow(row)
                else:
                    self.tableView.showRow(row)
        else:
            for row in range(self.proxy.rowCount()):
                #index = self.proxy.index(row,0)
                #item = self.model.item(row,0)
                #if not index in checkedList:
                #    self.listView.showRow(row)
                #if not index in checkedList:
                    #self.listView.hideRow(row)
                self.tableView.showRow(row)

    def filterTable(self):
        text = self.lineEditFilter.text()
        search = QtCore.QRegExp(    text,
                                    QtCore.Qt.CaseInsensitive,
                                    QtCore.QRegExp.RegExp
                                    )
        self.filterChecked()
        self.proxy.setFilterRegExp(search)   

    def checkSelected(self):
        selectionModel = self.tableView.selectionModel()
        selected = selectionModel.selectedIndexes()
        for index in selected:
            srcIndex = self.proxy.mapToSource(index)
            if srcIndex.column() != 0 and srcIndex.column() != 2:
                self.model.itemFromIndex(srcIndex).setCheckState(QtCore.Qt.CheckState.Checked)

    def uncheckSelected(self):
        selectionModel = self.tableView.selectionModel()
        selected = selectionModel.selectedIndexes()
        for index in selected:
            srcIndex = self.proxy.mapToSource(index)
            if srcIndex.column() != 0 and srcIndex.column() != 2:
                self.model.itemFromIndex(srcIndex).setCheckState(QtCore.Qt.CheckState.Unchecked)

    def createLinks(self):
        selectionModel = self.tableView.selectionModel()
        selected = selectionModel.selectedIndexes()

        for row, file in enumerate(self.files_paths):
            for column, folder in enumerate(self.hda_folders):
                if column > 2:
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
