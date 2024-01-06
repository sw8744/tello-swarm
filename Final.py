from djitellopy import TelloSwarm
import time

swarm = TelloSwarm.fromIps([
    "192.168.5.64",
    "192.168.5.33",
    "192.168.5.53",
    "192.168.5.47",
    "192.168.5.82",
    "192.168.5.30",
    "192.168.5.49",
    "192.168.5.52",
    "192.168.5.21",
    "192.168.5.37"
])

def BatteryCheck():
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
    if len(cannot_flip) > 0:
        print('Drones which Cannot Flip : ', end='')
        for i in cannot_flip:
            print('#' + str(i), end=' ')
        print('\n')
    if len(charge_required) > 0:
        print('Drones which Require Charging : ', end='')
        for i in charge_required:
            print('#' + str(i), end=' ')
        print('\n')

def WaitUntilPressT(message: str):
    while True:
        input_value = input(message)
        if input_value == 't':
            break
        else:
            continue

swarm.connect()
BatteryCheck()
WaitUntilPressT('press t to takeoff : ')

# I ain't worried
swarm.takeoff()
swarm.parallel(lambda i, tello: tello.move_up(300) if i % 2 else tello.move_up(400))
swarm.parallel(lambda i, tello: tello.move_up(100) if i % 2 else time.sleep(0))
swarm.parallel(lambda i, tello: tello.move_forward(150))
swarm.parallel(lambda i, tello: tello.move_back(150) if i % 2 == 1 else time.sleep(0))
swarm.parallel(lambda i, tello: tello.move_down(300) if i in [2, 6, 3, 7] else time.sleep(0))
swarm.parallel(lambda i, tello: tello.move_up(300) if i in [2, 6, 3, 7] else tello.move_down(300))
swarm.parallel(lambda i, tello: tello.move_down(300) if i in [2, 6, 3, 7] else time.sleep(0))
swarm.parallel(lambda i, tello: tello.move_back(150) if i % 2 == 1 else time.sleep(0))
swarm.land()

# Legends Never Die
WaitUntilPressT('press t to takeoff : ')
swarm.takeoff()
swarm.parallel(lambda i, tello: tello.move_up(250))

WaitUntilPressT('press t to move : ')
swarm.parallel(lambda i, tello: tello.move_back(100) if i in [1, 3, 5, 7, 9] else tello.move_forward(100))
swarm.parallel(lambda i, tello: tello.move_up(100))
swarm.parallel(lambda i, tello: tello.move_forward(100) if i in [1, 3, 5, 7, 9] else tello.move_back(100))
swarm.parallel(lambda i, tello: tello.move_down(100))

WaitUntilPressT('press t to move back Drone #6 : ')
swarm.parallel(lambda i, tello: tello.move_back(200) if i in [5] else tello.move_forward(30))

WaitUntilPressT('press t to move up Drone #6 : ')
swarm.parallel(lambda i, tello: tello.move_up(50) if i in [5] else tello.move_down(50))

WaitUntilPressT('press t to flip Drone #6 : ')
swarm.parallel(lambda i, tello: tello.flip('f') if i in [5] else time.sleep(0))
swarm.parallel(lambda i, tello: tello.move_up(100) if i in [5] else tello.move_down(200))

WaitUntilPressT('press t to flip Drone #6 : ')
swarm.parallel(lambda i, tello: tello.flip('b') if i in [5] else time.sleep(0))
swarm.parallel(lambda i, tello: tello.land() if i not in [5] else time.sleep(0))
swarm.parallel(lambda i, tello: tello.land if i in [5] else time.sleep(0))
swarm.land()
swarm.end()

# GODS
print('Please Change the Battery')
WaitUntilPressT('press t to connect : ')
swarm.connect()
BatteryCheck()

WaitUntilPressT('press t to takeoff : ')
swarm.takeoff()

swarm.parallel(lambda i, tello: tello.move_up(250))
swarm.parallel(lambda i, tello: tello.flip('b') if i in [1, 3, 5, 7, 9] else tello.flip('f'))
swarm.parallel(lambda i, tello: tello.flip('f') if i in [1, 3, 5, 7, 9] else tello.flip('b'))
swarm.parallel(lambda i, tello: tello.move_down(60) if i in [2, 6, 3, 7] else time.sleep(0))
swarm.parallel(lambda i, tello: tello.move_up(60) if i in [2, 6, 3, 7] else time.sleep(0))
swarm.parallel(lambda i, tello: tello.move_up(100))
swarm.parallel(lambda i, tello: tello.flip('f'))
swarm.parallel(lambda i, tello: tello.move_down(250))

WaitUntilPressT('press t to move up : ')
swarm.parallel(lambda i, tello: tello.go_xyz_speed(0, 0, 250, 21))
swarm.land()
swarm.end()