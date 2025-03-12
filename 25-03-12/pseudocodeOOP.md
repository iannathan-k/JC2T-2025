# Object Oriented Programming in Pseudocode
## Basic Definition

To define a class, start with the **CLASS** keyword followed by the class name, similar to how we declare **TYPE** or records.

In a class, any instance variables can either be **PUBLIC** or **PRIVATE**. This determines their visibility for those trying to access from outside the object itself. However, you do not need to use the **DECLARE** keyword like in records.

```
CLASS Person
    PUBLIC ID : INTEGER
    PRIVATE Name : STRING
    PRIVATE Age : INTEGER
ENDCLASS
```

The constructor is defined as a **PUBLIC** procedure which has the name ***NEW***, and does not require any self or this, like in other programming languages.

```
# Constructor
PUBLIC PROCEDURE NEW(PersonName : STRING, PersonAge : INTEGER)
    Name <-- PersonName
    Age <-- PersonAge
ENDPROCEDURE
```

Getters and setters must be defined as functions and procedures respectively. This is because setters do not return any values, while getters do. These must also be **PUBLIC** so that it can be interfaced with.

```
# Getters
PUBLIC FUNCTION GetName() RETURNS STRING
    RETURN Name
ENDFUNCTION

PUBLIC FUNCTION GetAge() RETURNS INTEGER
    RETURN Age
ENDFUNCTION

# Setters
PUBLIC PROCEDURE SetName(PersonName : STRING)
    Name <-- PersonName
ENDPROCEDURE

PUBLIC PROCEDURE SetAge(PersonAge : INTEGER)
    Age <-- PersonAge
ENDPROCEDURE
```

The full class definiton would look like this.

```
CLASS Person
    PRIVATE Name : STRING
    PRIVATE Age : INTEGER

    # Constructor
    PUBLIC PROCEDURE NEW(PersonName : STRING, PersonAge : INTEGER)
        Name <-- PersonName
        Age <-- PersonAge
    ENDPROCEDURE

    # Getters
    PUBLIC FUNCTION GetName() RETURNS STRING
        RETURN Name
    ENDFUNCTION

    PUBLIC FUNCTION GetAge() RETURNS INTEGER
        RETURN Age
    ENDFUNCTION

    # Setters
    PUBLIC PROCEDURE SetName(PersonName : STRING)
        Name <-- PersonName
    ENDPROCEDURE

    PUBLIC PROCEDURE SetAge(PersonAge : INTEGER)
        Age <-- PersonAge
    ENDPROCEDURE
ENDCLASS
```

## Inheritance

Pseudocode also supports inheritance similar to the way python does it. Let's build off of our previous example. Note that when we **INHERITS** person, we also inherit its functions, procedures and variables.

```
CLASS Student INHERTIS Person
    PRIVATE Grade : CHAR
ENDCLASS
```

However, we should also make our own constructor for this new class which uses the SUPER keyword to access the parent class. Otherwise, it would inherit the parent constructor.

```
# Constructor
PUBLIC PROCEDURE NEW(StudentName : STRING, StudentAge : INTEGER, StudentGrade : CHAR)
    SUPER.NEW(StudentName, StudentAge)
    Grade <-- StudentGrade
ENDPROCEDURE
```

We should also create new getter and setters for the new ***Grade*** variable.

```
# Getters
PUBLIC FUNCTION GetGrade() RETURNS CHAR
    RETURN Grade
ENDFUNCTION

# Setters
PUBLIC PROCEDURE SetGrade(StudentGrade : CHAR)
    Grade <-- StudentGrade
ENDPROCEDURE
```

Altogether the child class will look like this

```
CLASS Student INHERTIS Person
    PRIVATE Grade : CHAR

    # Constructor
    PUBLIC PROCEDURE NEW(StudentName : STRING, StudentAge : INTEGER, StudentGrade : CHAR)
        SUPER.NEW(StudentName, StudentAge)
        Grade <-- StudentGrade
    ENDPROCEDURE

    # Getters
    PUBLIC FUNCTION GetGrade() RETURNS CHAR
        RETURN Grade
    ENDFUNCTION

    # Setters
    PUBLIC PROCEDURE SetGrade(StudentGrade : CHAR)
        Grade <-- StudentGrade
    ENDPROCEDURE
ENDCLASS
```

## Instantiating Objects

To instantiate an object we follow java by using the **NEW** keyword. Note that this is not refering to the constructor, but a completely new keyword.

```
Student <-- NEW Student("Ian", 15, 'A')
OUTPUT Student.GetName()
```

> Ian

And if we want to change some variable or part of the object

```
# Original Grade
OUPTUT Student.GetGrade()

# New Grade
Student.SetGrade('B')
OUTPUT Student.GetGrade()
```

> A\
> B