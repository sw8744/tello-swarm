from djitellopy import TelloSwarm
from djitellopy import Tello
import time

IPs = [
    "192.168.31.113",
    "192.168.31.145",
    "192.168.31.102",
    "192.168.31.206",
    "192.168.31.197",
    "192.168.31.192",
    "192.168.31.204",
    "192.168.31.240",
    "192.168.31.191"
]

swarm = TelloSwarm.fromIps(IPs)

locate = []

swarm.connect()
swarm.takeoff()
swarm.parallel(lambda i, tello: tello.up(500))

# Handsclap 노래 시작
# part 1 Made by 29th 박무진 이호성
# 0s ~ 6s
locate = [(-500, 0, 0, 92), (-450, 0, 0, 75), (-350, 0, 0, 58), (-250, 0, 0, 42), (-150, 0, 0, 25), (150, 0, 0, 25), (250, 0, 0, 42), (350, 0, 0, 58), (450, 0, 0, 75), (500, 0, 0, 92)]

swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# 6s ~ 6.5s
swarm.parallel(lambda i, tello: tello.flip('bl'))

# 6.5s ~ 14s
# 처음 박자
locate = [(0, 0, 30, 32), (0, 0, -30, 32), (0, 0, 30, 32), (0, 0, -30, 32), (0, 0, 30, 32), (0, 0, -30, 32), (0, 0, 30, 32), (0, 0, -30, 32), (0, 0, 30, 32), (0, 0, -30, 32)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# 2번째 박자
locate = [(0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# 3번째 박자
locate = [(0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# 4번째 박자
locate = [(0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# 5번째 박자
locate = [(0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# 6번째 박자
locate = [(0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64), (0, 0, -60, 64), (0, 0, 60, 64)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# 7번째 박자
locate = [(0, 0, 30, 32), (0, 0, -30, 32), (0, 0, 30, 32), (0, 0, -30, 32), (0, 0, 30, 32), (0, 0, -30, 32), (0, 0, 30, 32), (0, 0, -30, 32), (0, 0, 30, 32), (0, 0, -30, 32)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# 마지막 박자
swarm.sync(0.9375)

# 14s ~ 20s
locate = [(0, 170, 300, 35), (0, 290, 300, 45), (0, 410, 300, 60), (0, 530, 300, 78), (0, 650, 300, 96), (0, 600, 300, 87), (0, 480, 300, 69), (0, 360, 300, 52), (0, 240, 300, 39), (0, 120, 300, 33)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# part 2 Made by 29th 김한결
locate = [(-150, -400, 0, 78), (-150, -400, 0, 78), (-150, -400, 0, 78), (-150, -400, 0, 78), (-150, -400, 0, 78), (150, -400, -200, 86), (150, -400, -200, 86), (150, -400, -200, 86), (150, -400, -200, 86), (150, -400, -200, 86)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))


locate = [(0, 200, -200, 81), (0, 100, -200, 64), (0, 200, -200, 81), (0, 100, -200, 64), (0, 200, -200, 81), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(7)

swarm.filp(10, 'l')
swarm.sync(0.33)
swarm.filp(9, 'l')
swarm.sync(0.33)
swarm.filp(8, 'l')
swarm.sync(0.33)
swarm.filp(7, 'l')
swarm.sync(0.33)
swarm.filp(6, 'l')
swarm.sync(0.33)

swarm.filp(1, 'l')
swarm.filp(2, 'l')
swarm.filp(3, 'l')
swarm.filp(4, 'l')
swarm.filp(5, 'l')
swarm.filp(6, 'l')
swarm.filp(7, 'l')
swarm.filp(8, 'l')
swarm.filp(9, 'l')
swarm.filp(10, 'l')

# part 3 Made by 30th 함정훈
locate = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 135, 0, 67), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 135, 0, 67)]
swarm.parallel(10, swarm.go_xyz_speed(0, 135, 0, 67))
swarm.parallel(6, swarm.go_xyz_speed(0, 135, 0, 67)) # 2초간 이동

swarm.sync(1)

swarm.parallel(10, swarm.go_xyz_speed(270, 135, 0, 100))
swarm.parallel(9, swarm.go_xyz_speed(160, 135, 0, 70))
swarm.parallel(6, swarm.go_xyz_speed(-270, 135, 0, 100))
swarm.parallel(7, swarm.go_xyz_speed(160, 135, 0, 70))

swarm.filp(8, 'r')
swarm.filp(2, 'r')
swarm.filp(4, 'r')
swarm.filp(5, 'r')
swarm.filp(3, 'r')
swarm.filp(1, 'r') # 3초간 이동과 플립

swarm.sync(1)

swarm.parallel(9, swarm.go_xyz_speed(160, 135, 0, 70))
swarm.parallel(7, swarm.go_xyz_speed(-160, 135, 0, 70)) # 2초간 이동

swarm.land()
swarm.sync(1)

swarm.takeoff()
locate = [(-275, 40, 0, 93), (-55, 20, 0, 20), (55, -20, 0, 20), (165, 20, 0, 55), (275, 0, 0, 92), (-165, 0, 0, 55), (275, 0, 0, 92), (110, 0, 0, 37), (-275, 0, 0, 92), (-330, 0, 0, 110)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(1)

locate = [(165, 0, 0, 41), (220, 0, 0, 55), (-220, 0, 0, 55), (-110, 0, 0, 28), (-165, 0, 0, 41), (330, 280, 0, 108), (-275, 240, 0, 91), (0, 0, 0, 50), (275, 320, 0, 105), (220, 240, 0, 81)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(1)

locate = [(-165, -80, 0, 14), (-220, 80, 0, 18), (220, 160, 0, 20), (-40, 0, 0, 3), (165, 0, 0, 13), (-220, -14, 0, 17), (0, -14, 0, 1), (0, -14, 0, 1), (0, -14, 0, 1), (0, -14, 0, 1)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(1)

locate = [(0, -14, 0, 1), (0, -14, 0, 1), (0, -14, 0, 1), (0, -14, 0, 1), (0, -14, 0, 1), (0, -60, 0, 6), (-165, -60, 0, 18), (0, 60, 0, 6), (0, 0, 0, 50), (0, -60, 0, 6)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(3)

locate = [(0, 0, 0, 50), (55, 30, 0, 6), (-55, -30, 0, 6), (0, 60, 0, 6), (165, 60, 0, 18), (0, -150, 0, 15), (0, -30, 0, 3), (55, 0, 0, 6), (165, -60, 0, 18), (-55, 0, 0, 6)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(3)

locate = [(-165, 60, 0, 18), (0, 30, 0, 3), (0, -30, 0, 3), (-55, 150, 0, 16), (0, 30, 0, 3), (55, 150, 0, 16), (0, 30, 0, 3), (-55, 0, 0, 6), (-165, 60, 0, 18), (55, 0, 0, 6)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(3)

locate = [(165, -60, 0, 18), (0, 30, 0, 3), (0, -30, 0, 3), (55, -150, 0, 16), (0, 30, 0, 3), (-55, -150, 0, 16), (0, 30, 0, 3), (55, 0, 0, 6), (165, -60, 0, 18), (-55, 0, 0, 6)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(6)

locate = [(0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48)]
swarm. parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

locate = [(0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48), (0, 500, 0, 48)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

locate = [(0, 400, 0, 48), (0, 400, 0, 48), (0, 400, 0, 48), (0, 400, 0, 48), (0, 400, 0, 48), (0, 400, 0, 48), (0, 400, 0, 48), (0, 400, 0, 48), (0, 400, 0, 48), (0, 400, 0, 48)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

# part 5 Made by 29th 윤준익
locate = [(150, -240, 0, 94), (0, 30, 0, 10), (-50, -120, 0, 43), (-100, -150, 0, 60), (-150, -180, 0, 78), (100, -90, 0, 45), (100, -150, 0, 60), (150, -60, 0, 54), (-100, -150, 0, 60), (-100, -90, 0, 45)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.sync(3)

# part 6 Made by 30th 이승원, 이다빈 # FIXME
flip = []
swarm.filp(3, 'l')
swarm.filp(2, 'r')
swarm.sync(1)
swarm.filp(4, 'l')
swarm.filp(8, 'r')
swarm.sync(1)
swarm.filp(5, 'l')
swarm.filp(1, 'r')
swarm.sync(1)
swarm.filp(9, 'l')
swarm.filp(7, 'r')
swarm.sync(1)
swarm.filp(10, 'l')
swarm.filp(6, 'r')
swarm.sync(1)

locate = [(-100, 0, 0, 50), (100, 0, 0, 50), (-100, 0, 0, 50), (100, 0, 0, 50), (-100, 0, 0, 50), (100, 0, 0, 50), (-100, 0, 0, 50), (100, 0, 0, 50), (-100, 0, 0, 50), (100, 0, 0, 50)]
swarm.parallel(lambda i, tello: tello.go_xyz_speed(locate[i][0], locate[i][1], locate[i][2], locate[i][3]))

swarm.land()
swarm.end()