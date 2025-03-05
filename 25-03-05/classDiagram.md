# Class Diagrams

Class diagrams are used to illustrate the different properties of classes and their uses.

## General Layout

| ClassName  |                         |
|------------|-------------------------|
| Attributes | Descriptions / Comments |
| Functions  | Descriptions / Comments |

>Note that the descriptions or comments of the attributes and functions are not necessary, but optional so they do not always need to be included in the diagram.

## Example

```python
class Person:
    def __init__(self, name, dob, gender):
        self.name = name
        self.dob = dob
        self.gender = gender

    def walk():
        print("The person is walking")

    def run():
        print("The person is running")
```

| Person                                                    |                                                               |
|-----------------------------------------------------------|---------------------------------------------------------------|
| Name : STRING <br> DOB : STRING <br> Gender : STRING <br> | Name of Person <br> Date of Birth <br> Gender of Person <br>  |
| Constructor() <br> Walk() <br> Run() <br>                 | Constructor that takes in name, DOB and Gender <br> <br> <br> |

