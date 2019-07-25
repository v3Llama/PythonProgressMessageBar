import time
import shutil

WIDTH = 50

def prog_msg(done, total, msg=None):

    if msg: 
        termw = shutil.get_terminal_size((80, 20))[0]
        clear = " " * (termw - 1 - len(msg))
        print(msg + clear, flush=True)
    
    prog = int(WIDTH * done / total) + 1
    bar = "\r[{}{}] {:.02f}% {}/{}".format('=' * prog, ' ' * (WIDTH - prog), ((done+1)/total) * 100, done + 1, total)
    print(bar, end="\r", flush=True)

r = 137
for i in range(r):

    msg = "The value is " + str(i)
    prog_msg(i, r, msg)
    time.sleep(0.1)

print()