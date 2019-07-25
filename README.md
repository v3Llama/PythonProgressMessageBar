# PythonProgressMessageBar
A simple python progress bar that prints a message with progress underneath

Python 3.x and greater

# Usage
```
important_things = ["important"] * 100

  with ProgWithMsg() as p:
    for idx in range(len(important_things)):

      msg = "processing important thing no. {}".format(idx)
      p.update(idx, len(important_things), msg)
      time.sleep(0.1)
```
