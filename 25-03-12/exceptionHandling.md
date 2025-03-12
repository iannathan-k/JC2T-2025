# Exception Handling

Exception Handling in pseudocode works very similarly to python, using try except constructs. However, there are no specific errors or exceptions which are defined so all will be caught by the except.

```
DECLARE StudentFile : STRING
StudentFile <-- "StudentFile.dat"

TRY
    OPENFILE StudentFile FOR READ
EXCEPT
    OUTPUT "File Not Found!"
ENDTRY
```

Versus in python

```python
StudentFile = "StudentFile.dat"

try:
    file = open(StudentFile, 'r')
except:
    print("File Not Found!")
```