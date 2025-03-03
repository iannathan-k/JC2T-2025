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