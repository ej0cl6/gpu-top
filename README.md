## gpu-top

### Usage
```
python gpu-top.py
```

You can also use the following command to monitor the gpu usage in real time
```
watch -n 1 python gpu-top.py
```

### Example Output

```
Tue May 28 00:31:43 2019
+------------------------------------------------------------------------------+
| GPU    Fan  Temp  Perf  Pwr:Usage/Cap              Memory-Usage  Utilization |
|==============================================================================|
|   0    25%   30C    P8   120W / 250W         9726MiB / 11178MiB          61% |
|   1    25%   25C    P8     7W / 250W           10MiB / 11178MiB           0% |
|   2    25%   27C    P2   102W / 250W          659MiB / 11178MiB          40% |
|   3    25%   30C    P8     8W / 250W           10MiB / 11178MiB           0% |
|   4    25%   44C    P2    77W / 250W         1667MiB / 11178MiB          20% |
|   5    25%   29C    P8     8W / 250W           10MiB / 11178MiB           0% |
|   6    25%   23C    P8     8W / 250W           10MiB / 11178MiB           0% |
|   7    25%   24C    P8     7W / 250W           10MiB / 11178MiB           0% |
+------------------------------------------------------------------------------+
| GPU    PID  User           Process name                               Memory |
|==============================================================================|
|   0  17757  username       python train.py --data ./data --debug     9139MiB |
|   0  29673  bob            python bob.py -n 3                         577MiB |
|   2  19423  alice          python main.py --train --save              649MiB |
|   4   9897  helloworld     python test.py                            1659MiB |
+------------------------------------------------------------------------------+
```
