from djitellopy import TelloSwarm
import time
swarm = TelloSwarm.fromIps([
    "192.168.5.64",
    "192.168.5.33",
    "192.168.5.54",
    "192.168.5.44",
    "192.168.5.81",
    "192.168.5.30",
    "192.168.5.38",
    "192.168.5.50",
    "192.168.5.22",
    "192.168.5.37"
])

swarm.connect()
j = 1
cannot_flip = []
charge_required = []
for i in swarm:
    battery = i.get_battery()
    print(j, battery, '/', end=' ')
    if battery <= 50:
        cannot_flip.append(j)
    if battery <= 20:
        charge_required.append(j)
    j += 1
print('\n')
print('Drones which Cannot Flip : ', end='')
for i in cannot_flip:
    print('#' + str(i), end=' ')
print('\n')
print('Drones which Require Charging : ', end='')
for i in charge_required:
    print('#' + str(i), end=' ')
print('\n')

while True:
    input_value = input('press t to takeoff : ')
    if input_value == 't':
        break
    else:
        continue

# I ain't worried
swarm.takeoff()
swarm.parallel(lambda i, tello: tello.move_up(300) if i % 2 else tello.move_up(400))
swarm.parallel(lambda i, tello: tello.move_up(100) if i % 2 else tello.move_up(0))
swarm.parallel(lambda i, tello: tello.move_forward(150))
swarm.parallel(lambda i, tello: tello.move_back(150) if i % 2 == 1 else tello.move_back(0))
swarm.parallel(lambda i, tello: tello.move_down(300) if i in [3, 7, 4, 8] else tello.move_down(0))
swarm.parallel(lambda i, tello: tello.move_up(300) if i in [3, 7, 4, 8] else tello.move_down(300))
swarm.parallel(lambda i, tello: tello.move_down(300) if i in [3, 7, 4, 8] else tello.move_down(0))
swarm.parallel(lambda i, tello: tello.move_back(150) if i % 2 == 1 else tello.move_back(0))
swarm.land()

# Legends Never Die
j = 1
for i in swarm:
    if j in [1, 5, 9]:
        i.takeoff()
    j += 1

j = 1
for i in swarm:
    if j in [2, 6, 10]:
        i.takeoff()
    j += 1

j = 1
for i in swarm:
    if j in [3, 4, 7, 8]:
        i.takeoff()
    j += 1

swarm.parallel(lambda i, tello: tello.move_up(300))
j = 1
for i in swarm:
    if j in [1, 9]:
        i.move_back(30)
    elif j in [2, 10]:
        i.move_forward(30)
    elif j in [3, 7]:
        i.move_forward(70)
    elif j in [4, 8]:
        i.move_back(70)
    elif j in [5]:
        i.move_forward(170)
    elif j in [6]:
        i.move_back(170)
    j += 1

swarm.end()