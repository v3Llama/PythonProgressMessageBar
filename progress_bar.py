import shutil

WIDTH = 50

class ProgWithMsg(object):

    def __init__(self, width=WIDTH):

        self.width = width

    def __enter__(self):

        return self
    
    def update(self, done, total, msg=None):

        if msg: 
            termw = shutil.get_terminal_size((80, 20))[0]
            clear = " " * (termw - 1 - len(msg))
            print(msg + clear, flush=True)
        
        prog = int(WIDTH * done / total) + 1
        bar = "\r[{}{}] {:.02f}% {}/{}".format('=' * prog, ' ' * (WIDTH - prog), ((done+1)/total) * 100, done + 1, total)
        print(bar, end="\r", flush=True)

    def __exit__(self, exc_type, exc_value, traceback): 
        
        print()