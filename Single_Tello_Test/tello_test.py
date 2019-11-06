from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())
exists_command_file = False

if len(sys.argv) == 2:
    file_name = sys.argv[1]
    
    f = open(file_name, 'r')
    commands = f.readlines()
    exists_command_file = True

tello = Tello()

if exists_command_file:
    for command in commands:
        if command != '' and command != '\n':
            command = command.rstrip()
    
            if command.find('delay') != -1:
                sec = float(command.partition('delay')[2])
                print(f'delay {sec}')
                time.sleep(sec)
                pass
            else:
                tello.send_command(command)
else:
    tello.send_command('command')
    print('===== command list =====')
    print('takeoff\nland\nflip\nforward n(cm)\nback n(cm)\nleft n(cm)\nright n(cm)')
    print('========================')
    while True: 
        try:
            command = input('input: ')
            
            if not command:
                print('invalid message')
                break
    
            if 'end' in command:
                print ('...')
                tello.on_close()
                break
    
            # Send data
            tello.send_command(command)
        except KeyboardInterrupt:
            print ('\n . . .\n')
            tello.on_close()
            break

log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)
