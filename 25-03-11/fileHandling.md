# File Handling

## Important Information

Note that in file handling (Ch. 14), we do not treat these files like text files which we can read or write lines of text to. Instead, we treat them as **Binary Files** which we can store **records** to. Binary files use a ***.dat*** file exetension.

This also means you cannot apply *Bubble Sort*, *Linear Search*, *Binary Search* or any other typical algorithm on binary files. This is because these algorithms can only be applied to arrays.

For the rest of this file, we will apply the following code.

```
TYPE StudentRecord
    DECLARE StudentID : INTEGER
    DECLARE StudentName : STRING
ENDTYPE

DECLARE Student : StudentRecord
DECLARE StudentFile : STRING
StudentFile <-- "StudentFile.dat"
```

## Types of File Handling

### 1. Serial

**Serial** is the most intuitive way of storing records in a file. It stores records one after the other, so the only order that the records follow is the order they were entered in.

To search for a specific record, we must read one record at a time.

```
# Appending to a Serial File
OPENFILE StudentFile FOR APPEND

PUTRECORD StudentFile, Student

CLOSEFILE StudentFile

# Reading From a Serial File
OPENFILE StudentFile FOR READ

WHILE NOT EOF(StudentFile)
    GETRECORD StudentFile, Student
    OUTPUT Student.StudentID
    OUTPUT Student.StudentName
ENDWHILE

CLOSEFILE StudentFile
```

### 2. Sequential

**Sequential** is when the records are stored in ascending or descending order of a **specific key field**. 

However, this doesn't mean we can jump to a specific record even if we know where it is supposed to exist. We must still read one record at a time, making search just as long as in serial.

In writing to a serial file, there are two methods.

a. Reading each line into an array, inserting the new record into that array, and writing everything back into the file.

b. Creating a new file with the new record inserted where it is supposed to be, and delete the old file.

```
DECLARE TempStudent : StudentRecord
DECLARE Flag : BOOLEAN

# Appending to a Sequential File
OPENFILE StudentFile FOR READ
OPENFILE NewStudentFile FOR WRITE

# Add Until Our New Record's Place
flag <-- FALSE
WHILE NOT flag
    GETRECORD StudentFile, TempStudent

    # Insert the new file into it's place
    IF TempStudent.StudentID < Student.StudentID THEN
        PUTRECORD NewStudentFile, Student
        flag <-- TRUE
    ENDIF

    PUTRECORD NewStudentFile, TempStudent

    # In case it is at the very back
    IF EOF(StudentFile) THEN
        PUTRECORD NewStudentFile, Student
        flag <-- TRUE
    ENDIF
    
ENDWHILE

# Add The Remaining Records
WHILE NOT EOF(StudentFile)
    GETRECORD StudentFile, TempStudent
    PUTRECORD NewStudentFile, TempStudent
ENDWHILE

CLOSEFILE StudentFile
CLOSEFILE NewStudentFile

# Replace the Old File
DELETE StudentFile
RENAME StudentNewFile, StudentFile
```

### 3. Random

Random is the most important, because using random files allows us to directly skip to a certain record if we have the hashed address without having to access every other file before.

Random files cannot be opened using READ or WRITE, but rather its own RANDOM. RANDOM allows both reading and writing to the file at the same time.

To avoid overwriting the old values already existing at a given address, you can use either **open hashing** or **closed hashing**. 

a. **Open Hashing** - Go to the given address. If it already has a record keep moving down by one until an open address is found.

b. **Closed Hashing** - Go to the given address. If it already has a record go to a dedicated overflow area to add the record.

```
DECLARE Address : INTEGER

OPENFILE StudentFile FOR RANDOM

# Get the address based on a hashing function
Address <-- Hash(Student.StudentID)

# Move the pointer to the address
SEEK(StudentFile, Address)

# Overwrites the data at the address
PUTRECORD StudentFile, Student

# Gets the record at the address
GETRECORD StudentFile, Student

CLOSEFILE StudentFile
```