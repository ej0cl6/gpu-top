import subprocess
import re

gpu_stats = subprocess.getoutput("nvidia-smi").split('\n')
n_line = len(gpu_stats)

print(gpu_stats[0])
print("+------------------------------------------------------------------------------+")
print("| GPU    Fan  Temp  Perf   Pwr:Usage/Cap            Memory-Usage   Utilization |")
print("|==============================================================================|")

# find gpu info start
i = 1
while i < n_line and not gpu_stats[i].startswith("|=="):
    i += 1
i += 1

# print gpu info
while i < n_line:
    if gpu_stats[i].startswith("+--"):
        i += 1
    elif gpu_stats[i].startswith("|"):
        gpu_id = int(gpu_stats[i][1:5])
        gpu_info = gpu_stats[i+1].split('|')
        gpu_temp = gpu_info[1].strip()
        gpu_mem = gpu_info[2].strip()
        gpu_utl = gpu_info[3][:8]
        print("| {} {} {} {} |".format(str(gpu_id).rjust(3), gpu_temp.rjust(32), gpu_mem.rjust(25), gpu_utl.rjust(13)))
        i += 2
    else:
        break

# find pid info start
while i < n_line and not gpu_stats[i].startswith("|=="):
    i += 1
i += 1

# print pid info
pid_results = []
pids = []
while i < n_line:
    if gpu_stats[i].startswith("+--"):
        i += 1
    elif gpu_stats[i].startswith("|"):
        pid_info = re.split(r'\s+', gpu_stats[i])
        gpu_id = pid_info[1]
        pid = pid_info[2]
        pmem = pid_info[5]
        pid_results.append((gpu_id, pid, pmem))
        pids.append(pid)
        i += 1
    else:
        break

pid_stats = subprocess.getoutput("ps -o pid,user,cmd -p {}".format(",".join(pids))).split('\n')
pid_pair = [re.split(r'\s+', line.strip(), 2) for line in pid_stats[1:]]
pid2user = {pair[0]: pair[1] for pair in pid_pair}
pid2cmd = {pair[0]: pair[2] for pair in pid_pair}

print("+------------------------------------------------------------------------------+")
print("| GPU    PID  User           Process name                               Memory |")
print("|==============================================================================|")

for gpu_id, pid, pmem in pid_results:
    print("| {} {}  {} {} {} |".format(gpu_id.rjust(3), pid.rjust(6), pid2user[pid][:14].ljust(14), pid2cmd[pid][:39].ljust(39), pmem.rjust(9)))
print("+------------------------------------------------------------------------------+")

