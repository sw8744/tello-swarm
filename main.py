from djitellopy import TelloSwarm
import time

swarm = TelloSwarm.fromIps([
    "192.168.31.113",
    "192.168.31.145",
    "192.168.31.102",
    "192.168.31.206",
    "192.168.31.197",
    "192.168.31.192",
    "192.168.31.204",
    "192.168.31.240",
    "192.168.31.191"
])

swarm.connect()
swarm.takeoff()

# Handsclap 노래 시작

# part 1 Made by 29th 박무진 이호성
# 0s ~ 6s
swarm.parallel(1, swarm.go_xyz_speed(-550, 0, 0, 92))
swarm.parallel(2, swarm.go_xyz_speed(-450, 0, 0, 75))
swarm.parallel(3, swarm.go_xyz_speed(-350, 0, 0, 58))
swarm.parallel(4, swarm.go_xyz_speed(-250, 0, 0, 42))
swarm.parallel(5, swarm.go_xyz_speed(-150, 0, 0, 25))
swarm.parallel(6, swarm.go_xyz_speed(150, 0, 0, 25))
swarm.parallel(7, swarm.go_xyz_speed(250, 0, 0, 42))
swarm.parallel(8, swarm.go_xyz_speed(350, 0, 0, 58))
swarm.parallel(9, swarm.go_xyz_speed(450, 0, 0, 75))
swarm.parallel(10, swarm.go_xyz_speed(550, 0, 0, 92))

# 6s ~ 6.5s
swarm.filp('bl')

# 6.5s ~ 14s
# 처음 박자
swarm.parallel(1, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(2, swarm.go_xyz_speed(0, 0, -30, 32))
swarm.parallel(3, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(4, swarm.go_xyz_speed(0, 0, -30, 32))
swarm.parallel(5, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(6, swarm.go_xyz_speed(0, 0, -30, 32))
swarm.parallel(7, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(8, swarm.go_xyz_speed(0, 0, -30, 32))
swarm.parallel(9, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(10, swarm.go_xyz_speed(0, 0, -30, 32))

# 2번째 박자
swarm.parallel(1, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(2, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(3, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(4, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(5, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(6, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(7, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(8, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(9, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(10, swarm.go_xyz_speed(0, 0, 60, 64))

# 3번째 박자
swarm.parallel(1, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(2, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(3, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(4, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(5, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(6, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(7, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(8, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(9, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(10, swarm.go_xyz_speed(0, 0, -60, 64))

# 4번째 박자
swarm.parallel(1, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(2, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(3, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(4, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(5, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(6, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(7, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(8, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(9, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(10, swarm.go_xyz_speed(0, 0, 60, 64))

# 5번째 박자
swarm.parallel(1, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(2, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(3, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(4, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(5, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(6, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(7, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(8, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(9, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(10, swarm.go_xyz_speed(0, 0, -60, 64))

# 6번째 박자
swarm.parallel(1, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(2, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(3, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(4, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(5, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(6, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(7, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(8, swarm.go_xyz_speed(0, 0, 60, 64))
swarm.parallel(9, swarm.go_xyz_speed(0, 0, -60, 64))
swarm.parallel(10, swarm.go_xyz_speed(0, 0, 60, 64))

# 7번째 박자
swarm.parallel(1, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(2, swarm.go_xyz_speed(0, 0, -30, 32))
swarm.parallel(3, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(4, swarm.go_xyz_speed(0, 0, -30, 32))
swarm.parallel(5, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(6, swarm.go_xyz_speed(0, 0, -30, 32))
swarm.parallel(7, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(8, swarm.go_xyz_speed(0, 0, -30, 32))
swarm.parallel(9, swarm.go_xyz_speed(0, 0, 30, 32))
swarm.parallel(10, swarm.go_xyz_speed(0, 0, -30, 32))

# 마지막 박자
time.sleep(0.9375*1000)

# 14s ~ 20s
swarm.parallel(1, swarm.go_xyz_speed(0, 170, 300, 35))
swarm.parallel(2, swarm.go_xyz_speed(0, 290, 300, 45))
swarm.parallel(3, swarm.go_xyz_speed(0, 410, 300, 60))
swarm.parallel(4, swarm.go_xyz_speed(0, 530, 300, 78))
swarm.parallel(5, swarm.go_xyz_speed(0, 650, 300, 96))
swarm.parallel(6, swarm.go_xyz_speed(0, 600, 300, 87))
swarm.parallel(7, swarm.go_xyz_speed(0, 480, 300, 69))
swarm.parallel(8, swarm.go_xyz_speed(0, 360, 300, 52))
swarm.parallel(9, swarm.go_xyz_speed(0, 240, 300, 39))
swarm.parallel(10, swarm.go_xyz_speed(0, 120, 300, 33))

# part 2 Made by 29th 김한결
swarm.parallel(1, swarm.go_xyz_speed(-150, -400, 0, 78))
swarm.parallel(2, swarm.go_xyz_speed(-150, -400, 0, 78))
swarm.parallel(3, swarm.go_xyz_speed(-150, -400, 0, 78))
swarm.parallel(4, swarm.go_xyz_speed(-150, -400, 0, 78))
swarm.parallel(5, swarm.go_xyz_speed(-150, -400, 0, 78))
swarm.parallel(6, swarm.go_xyz_speed(150, -400, -200, 86))
swarm.parallel(7, swarm.go_xyz_speed(150, -400, -200, 86))
swarm.parallel(8, swarm.go_xyz_speed(150, -400, -200, 86))
swarm.parallel(9, swarm.go_xyz_speed(150, -400, -200, 86))
swarm.parallel(10, swarm.go_xyz_speed(150, -400, -200, 86))

swarm.parallel(1, swarm.go_xyz_speed(0, 200, -200, 81))
swarm.parallel(2, swarm.go_xyz_speed(0, 100, -200, 64))
swarm.parallel(3, swarm.go_xyz_speed(0, 200, -200, 81))
swarm.parallel(4, swarm.go_xyz_speed(0, 100, -200, 64))
swarm.parallel(5, swarm.go_xyz_speed(0, 200, -200, 81))

time.sleep(7 * 1000)

swarm.filp(10, 'l')
time.sleep(0.33 * 1000)
swarm.filp(9, 'l')
time.sleep(0.33 * 1000)
swarm.filp(8, 'l')
time.sleep(0.33 * 1000)
swarm.filp(7, 'l')
time.sleep(0.33 * 1000)
swarm.filp(6, 'l')
time.sleep(0.33 * 1000)

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
swarm.parallel(10, swarm.go_xyz_speed(0, 135, 0, 67))
swarm.parallel(6, swarm.go_xyz_speed(0, 135, 0, 67)) # 2초간 이동

time.sleep(1*1000)

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

time.sleep(1*1000)

swarm.parallel(9, swarm.go_xyz_speed(160, 135, 0, 70))
swarm.parallel(7, swarm.go_xyz_speed(-160, 135, 0, 70)) # 2초간 이동

swarm.land()
time.sleep(1*1000)

swarm.takeoff()
swarm.parallel(1, swarm.go_xyz_speed(-275, -40, 0, 93))
swarm.parallel(2, swarm.go_xyz_speed(-55, -20, 0, 20))
swarm.parallel(3, swarm.go_xyz_speed(55, 20, 0, 20))
swarm.parallel(4, swarm.go_xyz_speed(165, -20, 0, 55))
swarm.parallel(5, swarm.go_xyz_speed(275, 0, 0, 92))
swarm.parallel(6, swarm.go_xyz_speed(-165, 0, 0, 55))
swarm.parallel(7, swarm.go_xyz_speed(275, 0, 0, 92))
swarm.parallel(8, swarm.go_xyz_speed(110, 0, 0, 37))
swarm.parallel(9, swarm.go_xyz_speed(-275, 0, 0, 92))
swarm.parallel(10, swarm.go_xyz_speed(-330, 0, 0, 110))

time.sleep(1 * 1000)

swarm.parallel(1, swarm.go_xyz_speed(165, 0, 0, 41))
swarm.parallel(2, swarm.go_xyz_speed(220, 0, 0, 55))
swarm.parallel(3, swarm.go_xyz_speed(-220, 0, 0, 55))
swarm.parallel(4, swarm.go_xyz_speed(-110, 0, 0, 28))
swarm.parallel(5, swarm.go_xyz_speed(-165, 0, 0, 41))
swarm.parallel(6, swarm.go_xyz_speed(330, 280, 0, 108))
swarm.parallel(7, swarm.go_xyz_speed(-275, 240, 0, 91))
swarm.parallel(8, swarm.go_xyz_speed(0, 0, 0, 50))
swarm.parallel(9, swarm.go_xyz_speed(275, 320, 0, 105))
swarm.parallel(10, swarm.go_xyz_speed(220, 240, 0, 81))

time.sleep(1 * 1000)

swarm.parallel(1, swarm.go_xyz_speed(-165, -80, 0, 14))
swarm.parallel(2, swarm.go_xyz_speed(-220, 80, 0, 18))
swarm.parallel(3, swarm.go_xyz_speed(220, 160, 0, 20))
swarm.parallel(4, swarm.go_xyz_speed(-40, 0, 0, 3))
swarm.parallel(5, swarm.go_xyz_speed(165, 0, 0, 13))
swarm.parallel(6, swarm.go_xyz_speed(-220, -14, 0, 17))
swarm.parallel(7, swarm.go_xyz_speed(0, -14, 0, 1))
swarm.parallel(8, swarm.go_xyz_speed(0, -14, 0, 1))
swarm.parallel(9, swarm.go_xyz_speed(0, -14, 0, 1))
swarm.parallel(10, swarm.go_xyz_speed(0, -14, 0, 1))

time.sleep(1 * 1000)

swarm.parallel(1, swarm.go_xyz_speed(0, -14, 0, 1))
swarm.parallel(2, swarm.go_xyz_speed(0, -14, 0, 1))
swarm.parallel(3, swarm.go_xyz_speed(0, -14, 0, 1))
swarm.parallel(4, swarm.go_xyz_speed(0, -14, 0, 1))
swarm.parallel(5, swarm.go_xyz_speed(0, -14, 0, 1))
swarm.parallel(6, swarm.go_xyz_speed(0, -60, 0, 6))
swarm.parallel(7, swarm.go_xyz_speed(-165, -60, 0, 18))
swarm.parallel(8, swarm.go_xyz_speed(0, 60, 0, 6))
swarm.parallel(9, swarm.go_xyz_speed(0, 0, 0, 50))
swarm.parallel(10, swarm.go_xyz_speed(0, -60, 0, 6))

time.sleep(3 * 1000)

swarm.parallel(1, swarm.go_xyz_speed(0, 0, 0, 50))
swarm.parallel(2, swarm.go_xyz_speed(55, 30, 0, 6))
swarm.parallel(3, swarm.go_xyz_speed(-55, -30, 0, 6))
swarm.parallel(4, swarm.go_xyz_speed(0, 60, 0, 6))
swarm.parallel(5, swarm.go_xyz_speed(165, 60, 0, 18))
swarm.parallel(6, swarm.go_xyz_speed(0, -150, 0, 15))
swarm.parallel(7, swarm.go_xyz_speed(0, -30, 0, 3))
swarm.parallel(8, swarm.go_xyz_speed(55, 0, 0, 6))
swarm.parallel(9, swarm.go_xyz_speed(165, -60, 0, 18))
swarm.parallel(10, swarm.go_xyz_speed(-55, 0, 0, 6))

time.sleep(3 * 1000)

swarm.parallel(1, swarm.go_xyz_speed(-165, 60, 0, 18))
swarm.parallel(2, swarm.go_xyz_speed(0, 30, 0, 3))
swarm.parallel(3, swarm.go_xyz_speed(0, -30, 0, 3))
swarm.parallel(4, swarm.go_xyz_speed(-55, 150, 0, 16))
swarm.parallel(5, swarm.go_xyz_speed(0, 30, 0, 3))
swarm.parallel(6, swarm.go_xyz_speed(55, 150, 0, 16))
swarm.parallel(7, swarm.go_xyz_speed(0, 30, 0, 3))
swarm.parallel(8, swarm.go_xyz_speed(-55, 0, 0, 6))
swarm.parallel(9, swarm.go_xyz_speed(-165, 60, 0, 18))
swarm.parallel(10, swarm.go_xyz_speed(55, 0, 0, 6))

time.sleep(3 * 1000)

swarm.parallel(1, swarm.go_xyz_speed(165, -60, 0, 18))
swarm.parallel(2, swarm.go_xyz_speed(0, -30, 0, 3))
swarm.parallel(3, swarm.go_xyz_speed(0, 30, 0, 3))
swarm.parallel(4, swarm.go_xyz_speed(55, -150, 0, 16))
swarm.parallel(5, swarm.go_xyz_speed(0, -30, 0, 3))
swarm.parallel(6, swarm.go_xyz_speed(-55, -150, 0, 16))
swarm.parallel(7, swarm.go_xyz_speed(0, -30, 0, 3))
swarm.parallel(8, swarm.go_xyz_speed(55, 0, 0, 6))
swarm.parallel(9, swarm.go_xyz_speed(165, -60, 0, 18))
swarm.parallel(10, swarm.go_xyz_speed(-55, 0, 0, 6))

time.sleep(6 * 1000)

swarm.parallel(1, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(2, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(3, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(4, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(5, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(6, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(7, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(8, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(9, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(10, swarm.go_xyz_speed(0, 500, 0, 48))

swarm.parallel(1, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(2, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(3, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(4, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(5, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(6, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(7, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(8, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(9, swarm.go_xyz_speed(0, 500, 0, 48))
swarm.parallel(10, swarm.go_xyz_speed(0, 500, 0, 48))

swarm.parallel(1, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(2, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(3, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(4, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(5, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(6, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(7, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(8, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(9, swarm.go_xyz_speed(0, 400, 0, 48))
swarm.parallel(10, swarm.go_xyz_speed(0, 400, 0, 48))

# part 5 Made by 29th 윤준익
swarm.parallel(1, swarm.go_xyz_speed(150, -240, 0, 94))
swarm.parallel(2, swarm.go_xyz_speed(0, -30, 0, 10))
swarm.parallel(3, swarm.go_xyz_speed(-50, -120, 0, 43))
swarm.parallel(4, swarm.go_xyz_speed(-100, -150, 0, 60))
swarm.parallel(5, swarm.go_xyz_speed(-150, -180, 0, 78))
swarm.parallel(6, swarm.go_xyz_speed(100, -90, 0, 45))
swarm.parallel(7, swarm.go_xyz_speed(100, -150, 0, 60))
swarm.parallel(8, swarm.go_xyz_speed(150, -60, 0, 54))
swarm.parallel(9, swarm.go_xyz_speed(-100, -150, 0, 60))
swarm.parallel(10, swarm.go_xyz_speed(-100, -90, 0, 45))

time.sleep(3 * 1000)

# part 6 Made by 30th 이승원, 이다빈
swarm.takeoff()
swarm.filp(3, 'l')
swarm.filp(2, 'r')
time.sleep(1 * 1000)
swarm.filp(4, 'l')
swarm.filp(8, 'r')
time.sleep(1 * 1000)
swarm.filp(5, 'l')
swarm.filp(1, 'r')
time.sleep(1 * 1000)
swarm.filp(9, 'l')
swarm.filp(7, 'r')
time.sleep(1 * 1000)
swarm.filp(10, 'l')
swarm.filp(6, 'r')
time.sleep(1 * 1000)

swarm.parallel(1, swarm.go_xyz_speed(-100, 0, 0, 50))
swarm.parallel(2, swarm.go_xyz_speed(100, 30, 0, 50))
swarm.parallel(3, swarm.go_xyz_speed(-100, 30, 0, 50))
swarm.parallel(4, swarm.go_xyz_speed(0, -30, 0, 50))
swarm.parallel(5, swarm.go_xyz_speed(100, 0, 0, 50))
swarm.parallel(6, swarm.go_xyz_speed(0, 90, 0, 50))
swarm.parallel(7, swarm.go_xyz_speed(-100, 60, 0, 50))
swarm.parallel(8, swarm.go_xyz_speed(0, -30, 0, 50))
swarm.parallel(9, swarm.go_xyz_speed(100, 60, 0, 50))
swarm.parallel(10, swarm.go_xyz_speed(0, 90 ,0 ,50))

swarm.land()
swarm.end()