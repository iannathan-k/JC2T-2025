# 1a)

Jobs = [[None, None] for _ in range(100)]
NumberOfJobs = None

# b)

def Initialize():
    global NumberOfJobs
    NumberOfJobs = 0
    for i in range(100):
        Jobs[i][0] = -1
        Jobs[i][1] = -1

# c)

def AddJob(job_num, job_priority):
    global NumberOfJobs
    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs][0] = job_num
        Jobs[NumberOfJobs][1] = job_priority
        NumberOfJobs += 1
        print("Added")

# d)

Initialize()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

# e)

def InsertionSort():
    for i in range(1, NumberOfJobs):
        key = Jobs[i][1]
        j = i - 1
        while key < Jobs[j][1] and j >= 0:
            Jobs[j], Jobs[j + 1] = Jobs[j + 1], Jobs[j]
            j -= 1

# f)

def PrintArray():
    for job in Jobs[:NumberOfJobs]:
        print(str(job[0]), "priority", str(job[1]))

# g)(i) && (ii)

InsertionSort()
PrintArray()