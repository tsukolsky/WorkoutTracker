from tools import prop

SWIM=0
BIKE=1
RUN=2
BRIC_SB=3
BRIC_BR=4
BRIC_SR=5
TRIAT=6
BODYC=7
CORE=8

WorkoutDictionary = dict()
WorkoutDictionary[SWIM] = 'Swimming'
WorkoutDictionary[BIKE] = 'Biking'
WorkoutDictionary[RUN] = 'Running'
WorkoutDictionary[BRIC_SB] = 'Brick - Swim and Bike'
WorkoutDictionary[BRIC_BR] = 'Brick - Bike and Run'
WorkoutDictionary[BRIC_SR] = 'Brick - Swim and Run'
WorkoutDictionary[TRIAT] = 'Swim + Bike + Run'
WorkoutDictionary[BODYC] = 'Body Circuits'

class WorkoutManager():
    def __init__(self):
        self.__workoutDict = dict()
        
    def AddWorkout(self, workout):
        rootName = workout.Name
        dName = workout.Name
        wIteration = 1
        while dName in self.__workoutDict.iterkeys():
            dName = "%s %d"%(rootName, wIteration)
            wIteration += 1
        workout.Name = dName
        self.__workoutDict[dName] = workout
        
    def DeleteWorkout(self, workoutName):
        if workoutName in self.__workoutDict.iterkeys():
            del self.__workoutDict[workoutName]
            return True
        else:
            print "No workout to delete with name %s"%workoutName
            return False

    def GetWorkout(self, workoutName):
        if workoutName in self.__workoutDict.iterkeys():
            return self.__workoutDict[workoutName]
        else:
            print "No workout to get named %s"%workoutName
            return None
        
class Workout():
    def __init__(self, name, wType, durationDict, distanceDict, notes):
        self.__Name = name
        self.__WorkoutType = wType
        self.__Duration = durationDict
        self.__Distance = distanceDict
        self.__Notes = notes
        
    @prop
    def Name(self): return {'prefix': '_Workout__', 'fset':None}
    
    @prop
    def WorkoutType(self): return {'prefix': '_Workout__', 'fset': None}
    
    @prop 
    def Duration(self): return {'prefix': '_Workout__', 'fset':None}
        
    @prop 
    def Distance(self): return {'prefix': '_Workout__', 'fset':None}
        
    @prop 
    def Notes(self): return {'prefix': '_Workout__', 'fset':None}
    