Students={}

def ReadStudents(path): #The input of this function is the path of the file which we want to read from it
    global Students #we need to specify that we will apply the modification on the global variable "Students"
    file = open(path,"r") #Connect the variable "file" to the real file on disk in that path
    stud=file.readlines() #"stud" is a list,every element in it will be a line from the file
    
    #using map: the first argument is a lambda function to create the elements of the dictionary 
    #[id,[name,exam,practical]]
    """in each line (each element of stud): id is the first element (its index 0) in the line after we split it using str.split(sep=",")
    name is the second elem (its index 1)
    exam is the third and Practical is the fourth (after converting them to float)"""
    #we start with the third element of "stud" to ignore the first two lines stud[0] and stud[1] using range(2,len(stud)) as a second parameter for map
    Students=dict(map(lambda x:[int(stud[x].split(sep=",")[0]),[stud[x].split(sep=",")[1],float(stud[x].split(sep=",")[2]),float(stud[x].split(sep=",")[3])]],range(2,len(stud))))
    file.close()
    #anyFun1=lambda x:stud[x][:len(stud[x])-1].split(sep=",")
    #anyFun2=lambda x:[int(x[0]),[x[1],float(x[2]),float(x[3])]]
    #Students=dict(map(anyFun2,map(anyFun1,range(2,len(stud)))))
    return

def Score(Exam, Practical):
    score=(0.7*Exam)+(0.3*Practical) #the score is (70% of Exam + 30% of Practical)
    return score

def isSuccess(Exam, Practical, Score):
    if ((Exam>=40) and (Practical>=40) and (Score>=60)): 
        return True #return true if Exam more than 39 AND Practical more than 69 AND Score more than 59
    else:
        return False #Otherwise return false
    
def FinalResults(Students):
    #newlambda is lambda to extend (the list) the value of every key in the dictionary Students
    #will add two elements to the list [Score of the student , Success OR Fail]
    #Score will calculate it using Score function
    #using condition assignment to put Success OR Fail
    newlambda=lambda i :Students[i].extend([Score(Students[i][1], Students[i][2]),"Success" if isSuccess(Students[i][1],Students[i][2],Score(Students[i][1], Students[i][2])) else "Fail"])
    list(map(newlambda,Students)) #map to apply newlambda on the dictionary Students
    return Students 

def Success(Students):
    #we will store in 'subStudents' the output of the function which will contain the successful students only
    """using map: the first argument is a lambda to create the elements of sub-dictionary 'subStudents' .... x is a key from the output of filter
    The second argument is a filter which return a list that contain the ids of successed students after checking
    The condition"""
    #The condition return true if the 5th element in the list of every student was success
    #So the second argument of filter is the input of the 'Success function'
    subStudents=dict(map(lambda x : [x,Students[x]],filter(lambda x:Students[x][4]=="Success",Students)))
    return subStudents
#items

def FailedButPassPractical (Students):
    #'subStudents2' will be a sub-dictionary which contain only the failed students but their practical >=40 
    #using filter to return a list that contain the ids of students who fulfill the condition
    #map to apply lambda on all Students who their ids in the list of the output of filter
    subStudents2=dict(map(lambda x : [x,Students[x]],filter(lambda x:(Students[x][4]=="Fail") and (Students[x][2]>=40),Students)))
    return subStudents2

def ScoreMean(Students):
    import functools #import this library so we can use reduce function
    #to calculate the avarage we need to sum the Scores of all students then divide the sum by the number of students
    #average=(A+B+C+D+E)/5 = (A/5)+(B/5)+(C/5)+(D/5)+(E/5)
    """so we use a map to pass on all Students in the input dictionary of this function
    and returns the scores of all students (the 4th element in the student list which its index=3) so that each score is divided by 5 (the number of students"""
    #then we used a reduce function to sum the values which return from map and return a float number (the avarage)
    avg=functools.reduce(lambda x, y:x+y ,map(lambda x:Students[x][3]/len(Students),Students))
    return avg

def Display(Students): #function to print a dictionary with specific format
    print("{0:7} {1:16} {2:8} {3:12} {4:7} {5}".format("Id","Name","Exam","Practical","Score","Success"))
    #we use map instead of (for loop) : first argument is a lambda to print every element in the dictionary with formating
    #second argument is the input of the 'Display function'
    nlambda=lambda i :print("{0:7} {1:16} {2:5.2f} {3:10.2f} {4:10.2f} {5:^12}".format(str(i),Students[i][0],Students[i][1],Students[i][2],Students[i][3],Students[i][4]))
    return list(map(nlambda,Students))

#Call all functions
ReadStudents("Students.txt") #Read a textfile named 'Students' in the same directory
FinalResults(Students)
print("All students:")
Display(Students) #Print all students
print("---------------------------------------------------------")
print("Successful students:")
Display(Success(Students)) #Print all successful students
print("---------------------------------------------------------")
print("Failed but pass practical students:")
Display(FailedButPassPractical(Students)) ##Print Failed students who pass the practical
print("............................................")
print("The avarage of Students' scores:")
print(ScoreMean(Students))