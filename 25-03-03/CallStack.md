# Tracing Recursive Functions

## Pseudocode

```
FUNCTION fact(num : INTEGER) RETURNS INTEGER
    DECLARE ans : INTEGER
    IF num = 0 THEN
        ans <-- 1
    ELSE
        ans <-- num * fact(num - 1)
    ENDIF
    RETURNS ans
ENDFUNCTION
```

## Trace

| Call Number | Function Call | num | ans         | Return Value |
|-------------|---------------|-----|-------------|--------------|
| 1           | fact(4)       | 4   | 4 * fact(3) |              |
| 2           | fact(3)       | 3   | 3 * fact(2) |              |
| 3           | fact(2)       | 2   | 2 * fact(1) |              |
| 4           | fact(1)       | 1   | 1 * fact(0) |              |
| 5           | fact(0)       | 0   | 1           | 1            |
| Continue 4  | fact(1)       | 1   | 1 * 1       | 1            |
| Continue 3  | fact(2)       | 2   | 2 * 1       | 2            |
| Continue 2  | fact(3)       | 3   | 3 * 2       | 6            |
| Continue 1  | fact(4)       | 4   | 4 * 6       | 24           |

## Review

1. The program knows that it has to return control to another function when the call stack is not empty, meaning there is still a function which has called the current one to returnt to.

2. Winding - The process of pushing the return address and the status of the program onto the call stack, occuring until the base case is met.

3. Unwinding - The process of popping the return address and returing control / reinstating the status of the program to the parent function. This occurs once the base case is met