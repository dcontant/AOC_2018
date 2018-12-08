from datetime import datetime
import re
from collections import Counter

with open('AOC2018_4.data', 'r') as f:
    data = f.read().split('\n')
    
clean_logs = []
for log in data:
    y,m,d,h,minutes,action = re.search(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (Guard #\d+|falls asleep|wakes up)',log).groups()
    log_entry = [datetime(int(y), int(m), int(d), int(h), int(minutes)), action]
    clean_logs.append(log_entry)
clean_logs = sorted(clean_logs)

guards = dict()

for log in clean_logs:
    time, action = log
    action, id_num = action.split(' ')
    if action == 'Guard':
        active = id_num
    elif action == 'falls':
        start = time.minute
    elif action == 'wakes':
        end = time.minute
        current = guards.get(active, Counter())
        current.update(list(range(start, end)))
        guards[active] = current
        
_, target_guard  = max([(sum(guards[g].values()),g) for g in guards])
d = guards[target_guard]
print('part 1:', sorted(d, key = d.get).pop() * int(target_guard[1:]))

_, target_guard = max([(max(guards[g].values()),g) for g in guards])
tg = target_guard
d = guards[tg]
print('part 2:', sorted(d, key= d.get).pop() * int(tg[1:]))
