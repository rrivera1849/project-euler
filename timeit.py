
import time
import sys
from subprocess import call

f = sys.argv[1]

start = time.time()
command = 'python {}'.format(f)
call(command.split(' '))

print('Time Taken: {}'.format(time.time() - start))
