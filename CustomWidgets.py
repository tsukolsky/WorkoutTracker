from PyQt4.QtGui import QMainWindow, QDialog, QComboBox, QWidget, QHBoxLayout, QPushButton, QTabBar, \
                        QTabWidget, QVBoxLayout, QMenuBar, QAction, QIcon, QLabel, QFont, \
                        QMessageBox
                        
from PyQt4.QtCore import Qt, SIGNAL
from CustomTypes import WorkoutDictionary

class NewWorkoutEditor(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        print "WorkoutEditor"
        self.__mainLayout = QVBoxLayout()
        
        # Workout Type Combo
        self.__wTypeCombo = QComboBox()
        for value in WorkoutDictionary.itervalues():
            self.__wTypeCombo.addItem(value)
        
        self.__wTypeCombo.currentIndexChanged.connect(self.__typeChanged)
        
        self.__mainLayout.addWidget(self.__wTypeCombo)
        self.setLayout(self.__mainLayout)
        
    def __typeChanged(self, newIndex):
        print "index updated to ", newIndex
        
class WorkoutTracker(QMainWindow):
    ABOUT_MENU="&About"
    VERSION_MENU="&Version"
    ADD_WORKOUT_MENU="Add &Workout"
    FILE_MENU = "&File"
    def __init__(self):
        print "Hey man"
        QMainWindow.__init__(self, None)
        self.setWindowTitle("Workout Tracker v0.1")
        self.resize(1200, 800)
        
        mainWidget = QWidget(self)
        self.__mainLayout = QVBoxLayout(mainWidget)
        mainWidget.setLayout(self.__mainLayout)
        
        self.setCentralWidget(mainWidget)
        
        self.__menu = self.__createMenu()
        
    def __createMenu(self):
        menu = self.menuBar()
        
        # File Menu ------------------------------------------
        fileMenu = menu.addMenu(WorkoutTracker.FILE_MENU)
        addWorkoutAction = QAction(menu)
        addWorkoutAction.setText(WorkoutTracker.ADD_WORKOUT_MENU)
        addWorkoutAction.triggered.connect(self.__addWorkout)
        fileMenu.addAction(addWorkoutAction)
        ## About Menu ----------------------------------------
        aboutMenu = menu.addMenu(WorkoutTracker.ABOUT_MENU)
        
        versionAction = QAction(menu)
        versionAction.setText(WorkoutTracker.VERSION_MENU)
        versionAction.triggered.connect(self.__showAbout)
        
        aboutMenu.addAction(versionAction)
    
    def __showAbout(self):
        ret = QMessageBox.information(self,"Version Info", "Workout Tracker v0.1 - Non Release Candidate")
    
    def __addWorkout(self):
        workoutWindow = NewWorkoutEditor(self)
        workoutWindow.show()