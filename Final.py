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
while True:
    input_value = input('press t to takeoff Drone #1, #5, #9 : ')
    if input_value == 't':
        break
    else:
        continue

j = 1
for i in swarm:
    if j in [1, 5, 9]:
        i.takeoff()
    j += 1

while True:
    input_value = input('press t to takeoff Drone #2, #6, #10: ')
    if input_value == 't':
        break
    else:
        continue
j = 1
for i in swarm:
    if j in [2, 6, 10]:
        i.takeoff()
    j += 1

while True:
    input_value = input('press t to takeoff Drone #3, #4, #7, #8: ')
    if input_value == 't':
        break
    else:
        continue
j = 1
for i in swarm:
    if j in [3, 4, 7, 8]:
        i.takeoff()
    j += 1

swarm.parallel(lambda i, tello: tello.move_up(300))
j = 1
for i in swarm:
    if j in [1, 9]:
        i.move_forward(150)
    elif j in [2, 10]:
        i.move_back(300)
    elif j in [5]:
        i.move_forward(132)
    elif j in [6]:
        i.move_back(132)
    j += 1

swarm.parallel(lambda i, tello: tello.move_down(200) if i in [3, 4, 5, 6, 7, 8] else tello.move_down(0))
j = 1
for i in swarm:
    if j in [2, 10]:
        i.move_forward(300)
    elif j in [1, 9]:
        i.move_back(150)
    elif j in [4, 8]:
        i.move_forward(50)
    elif j in [5]:
        i.move_back(132)
    j += 1

j = 1
for i in swarm:
    if j in [6]:
        i.move_up(300)
    elif j in [1, 2, 9, 10]:
        i.move_down(300)
    elif j in [3, 4, 5, 7, 8]:
        i.move_down(100)
    j += 1

swarm.parallel(lambda i, tello: tello.flip('f') if i in [6] else tello.move_back(0))
swarm.land()

# GODS
while True:
    input_value = input('press t to takeoff Drone #1, #10 : ')
    if input_value == 't':
        break
    else:
        continue

j = 1
for i in swarm:
    if j in [1, 10]:
        i.takeoff()
    j += 1

while True:
    input_value = input('press t to takeoff Drone #2, #3, #8, #9 : ')
    if input_value == 't':
        break
    else:
        continue
j = 1
for i in swarm:
    if j in [2, 3, 8, 9]:
        i.takeoff()
    j += 1

while True:
    input_value = input('press t to takeoff Drone #4, #5, #6, #7: ')
    if input_value == 't':
        break
    else:
        continue
j = 1
for i in swarm:
    if j in [4, 5, 6, 7]:
        i.takeoff()
    j += 1

swarm.parallel(lambda i, tello: tello.move_up(200))
# FIXME: 파도타기 추가
j = 1
for i in swarm:
    if j in [2, 8]:
        i.move_back(73)
    elif j in [3, 9]:
        i.move_forward(73)
    elif j in [4, 6]:
        i.move_back(150)
    elif j in [5, 7]:
        i.move_forward(150)
    elif j in [10]:
        i.move_left(100)
    elif j in [2]:
        i.move_right(100)
    j += 1
swarm.parallel(lambda i, tello: tello.move_down(200) if i in [1, 4, 5, 8, 9] else tello.move_down(0))
swarm.parallel(lambda i, tello: tello.flip('f'))
swarm.land()
swarm.end()