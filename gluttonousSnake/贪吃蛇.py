import pygame
import sys
import random
from pygame.locals import *
import time

# 初始位置
# 初始化pygame
pygame.init()  # 调用pygame模块初始函数
fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640, 480))  # 界面
pygame.display.set_caption('Snake Go!')  # 标题
image=pygame.image.load('background.png')            # 背景
pygame.display.set_icon(image)

# 定义颜色变量
redColor = pygame.Color(255, 0, 0)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)
greyColor = pygame.Color(150, 150, 150)
lightColor = pygame.Color(220, 220, 220)


# Game Over
def gameOver(playSurface, score):
    gameOverFont = pygame.font.SysFont('arial', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 125)
    playSurface.blit(gameOverSurf, gameOverRect)
    scoreFont = pygame.font.SysFont('arial', 48)
    scoreSurf = scoreFont.render('SCORE:' + str(score), True, greyColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (320, 225)
    playSurface.blit(scoreSurf, scoreRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


# 定义初始位置
snakePosition = [100, 100]  # snake位置
snakeSegments = [[100, 100], [80, 100], [30, 100]]  # snake长度
raspberryPosition = [300, 300]  # food位置
raspberrySpawned = 1  # food数量
direction = 'right'  # 方向
changeDirection = direction  # 改变方向
score = 0  # 得分

# 键盘输入判断运动
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:  # 键盘输入
            if event.key == K_RIGHT or event.key == ord('d'):  # 方向键和AWSD
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
            if event.key == K_ESCAPE:
                changeDirection == 'up'
        if changeDirection == 'right' and not direction == 'left':  # 在事件for之下，控制不能反向
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection
        if direction == 'right':  # 方向为→，snake位置加1
            snakePosition[0] += 10
        if direction == 'left':
            snakePosition[0] -= 10
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 10
        snakeSegments.insert(0, list(snakePosition))
        if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
            raspberrySpawned = 0
        else:
            snakeSegments.pop()
        if raspberrySpawned == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            raspberryPosition = [int(x * 20), int(y * 20)]
            raspberrySpawned = 1
            score += 1
        playSurface.fill(blackColor)
        for position in snakeSegments[1:]:
            pygame.draw.rect(playSurface, whiteColor, Rect(position[0], position[1], 20, 20))
        pygame.draw.rect(playSurface, lightColor, Rect(snakePosition[0], snakePosition[1], 20, 20))
        pygame.draw.rect(playSurface, redColor, Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
        pygame.display.flip()
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver(playSurface, score)
        if snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver(playSurface, score)
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface, score)
        if len(snakeSegments) < 40:
            speed = 6 * len(snakeSegments) // 4
        else:
            speed = 16
        fpsClock.tick(speed)
    if __name__ == "__main__":
        pass
