from djitellopy import TelloSwarm
import time

swarm = TelloSwarm.fromIps([
    "192.168.31.113",
    "192.168.31.192",
    "192.168.31.102",
    "192.168.31.240",
    "192.168.31.191",
    "192.168.31.204",
    "192.168.31.197",
    "192.168.31.209",
    "192.168.31.206",
    "192.168.31.145"
])

swarm.connect()
j = 1
for i in swarm:
    print(j, i.get_battery(), '/', end=' ')
    j += 1
while True:
    input_value = input('press t to takeoff : ')
    if input_value == 't':
        break
    else:
        continue

swarm.takeoff()

swarm.parallel(lambda i, tello: tello.move_up(200) if i % 2 else tello.move_up(300))
swarm.parallel(lambda i, tello: tello.move_up(100) if i % 2 else tello.move_down(100))
swarm.parallel(lambda i, tello: tello.move('forward', 500))
swarm.parallel(lambda i, tello: tello.move('forward', 500))
swarm.parallel(lambda i, tello: tello.move('back', 500))
swarm.parallel(lambda i, tello: tello.move('back', 500))
swarm.parallel(lambda i, tello: tello.move_down(100) if i % 2 else tello.move_up(100))
swarm.parallel(lambda i, tello: tello.flip('f'))

swarm.land()
swarm.end()