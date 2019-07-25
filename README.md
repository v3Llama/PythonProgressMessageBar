# PythonProgressMessageBar
A simple python progress bar that prints a message with progress underneath

Python 3.x and greater

# Usage
```
important_things = ["important"] * 20

  with ProgWithMsg() as p:
    for idx in range(len(important_things)):

      msg = "processing important thing no. {}".format(idx)
      p.update(idx, len(important_things), msg)
      time.sleep(0.1)
```
### Results
```
PS C:\PythonProgressMessageBar> python .\test.py
processing important thing no. 0
processing important thing no. 1
processing important thing no. 2
processing important thing no. 3
processing important thing no. 4
processing important thing no. 5
processing important thing no. 6
processing important thing no. 7
processing important thing no. 8
processing important thing no. 9
processing important thing no. 10
processing important thing no. 11
processing important thing no. 12
processing important thing no. 13
processing important thing no. 14
processing important thing no. 15
processing important thing no. 16
processing important thing no. 17
processing important thing no. 18
processing important thing no. 19
[================================================  ] 100.00% 20/20
```
