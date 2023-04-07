# 导入pygame模块
import pygame
# 导入random模块
import random

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("贪吃蛇")

# 设置颜色常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 设置字体
font = pygame.font.SysFont("arial", 32)

# 设置蛇的初始位置和方向
snake_x = 400
snake_y = 300
snake_dir = "right"

# 设置蛇的身体列表，每个元素是一个(x, y)坐标
snake_body = [(snake_x, snake_y)]

# 设置食物的初始位置，随机生成
food_x = random.randint(0, 39) * 20
food_y = random.randint(0, 29) * 20

# 设置游戏状态，True表示进行中，False表示结束
game_on = True

# 设置游戏时钟，控制帧率
clock = pygame.time.Clock()

# 设置游戏分数，初始为0
score = 0


# 定义一个函数，用于绘制按钮
def draw_button(text, x, y, w, h):
    # 绘制一个矩形作为按钮的背景
    pygame.draw.rect(screen, WHITE, (x, y, w, h))
    # 绘制一个矩形作为按钮的边框
    pygame.draw.rect(screen, BLACK, (x, y, w, h), 2)
    # 绘制按钮上的文字
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + w / 2, y + h / 2)
    screen.blit(text_surface, text_rect)


# 定义一个函数，用于绘制蛇的头部
def draw_snake_head(x, y):
    # 根据蛇的方向绘制不同的头部形状
    if snake_dir == "up":
        # 绘制一个绿色的圆形作为头部
        pygame.draw.circle(screen, GREEN, (x + 10, y + 10), 10)
        # 绘制两个黑色的小圆形作为眼睛
        pygame.draw.circle(screen, BLACK, (x + 6, y + 6), 2)
        pygame.draw.circle(screen, BLACK, (x + 14, y + 6), 2)
        # 绘制一个红色的小圆形作为舌头
        pygame.draw.circle(screen, RED, (x + 10, y - 2), 2)
    elif snake_dir == "down":
        # 绘制一个绿色的圆形作为头部
        pygame.draw.circle(screen, GREEN, (x + 10, y + 10), 10)
        # 绘制两个黑色的小圆形作为眼睛
        pygame.draw.circle(screen, BLACK, (x + 6, y + 14), 2)
        pygame.draw.circle(screen, BLACK, (x + 14, y + 14), 2)
        # 绘制一个红色的小圆形作为舌头
        pygame.draw.circle(screen, RED, (x + 10, y + 22), 2)
    elif snake_dir == "left":
        # 绘制一个绿色的圆形作为头部
        pygame.draw.circle(screen, GREEN, (x + 10, y + 10), 10)
        # 绘制两个黑色的小圆形作为眼睛
        pygame.draw.circle(screen, BLACK, (x + 6, y + 6), 2)
        pygame.draw.circle(screen, BLACK, (x + 6, y + 14), 2)
        # 绘制一个红色的小圆形作为舌头
        pygame.draw.circle(screen, RED, (x - 2, y + 10), 2)
    elif snake_dir == "right":
        # 绘制一个绿色的圆形作为头部
        pygame.draw.circle(screen, GREEN, (x + 10, y + 10), 10)
        # 绘制两个黑色的小圆形作为眼睛
        pygame.draw.circle(screen, BLACK, (x + 14, y + 6), 2)
        pygame.draw.circle(screen, BLACK, (x + 14, y + 14), 2)
        # 绘制一个红色的小圆形作为舌头
        pygame.draw.circle(screen, RED, (x + 22, y + 10), 2)


# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        # 如果点击了关闭按钮，退出程序
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # 如果按下了键盘，改变蛇的方向
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != "down":
                snake_dir = "up"
            if event.key == pygame.K_DOWN and snake_dir != "up":
                snake_dir = "down"
            if event.key == pygame.K_LEFT and snake_dir != "right":
                snake_dir = "left"
            if event.key == pygame.K_RIGHT and snake_dir != "left":
                snake_dir = "right"
        # 如果点击了鼠标，检查是否点击了重新开始按钮
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not game_on and 300 <= mouse_x <= 500 and 300 <= mouse_y <= 350:
                # 如果游戏结束且点击了重新开始按钮，重置游戏状态和蛇的位置和身体
                game_on = True
                snake_x = 400
                snake_y = 300
                snake_dir = "right"
                snake_body = [(snake_x, snake_y)]
                food_x = random.randint(0, 39) * 20
                food_y = random.randint(0, 29) * 20
                score = 0

    # 如果游戏进行中，更新蛇的位置和身体
    if game_on:
        # 根据方向移动蛇的头部
        if snake_dir == "up":
            snake_y -= 20
        if snake_dir == "down":
            snake_y += 20
        if snake_dir == "left":
            snake_x -= 20
        if snake_dir == "right":
            snake_x += 20

        # 检查是否撞到边界或自己，如果是，游戏结束
        if snake_x < 0 or snake_x > 780 or snake_y < 0 or snake_y > 580 or (snake_x, snake_y) in snake_body:
            game_on = False

        # 在身体列表的开头插入新的头部坐标
        snake_body.insert(0, (snake_x, snake_y))

        # 检查是否吃到食物，如果是，重新生成食物，否则删除身体列表的最后一个元素，并增加分数
        if snake_x == food_x and snake_y == food_y:
            food_x = random.randint(0, 39) * 20
            food_y = random.randint(0, 29) * 20
            score += 1
        else:
            snake_body.pop()

    # 填充背景色
    screen.fill(BLACK)

    # 绘制食物和蛇的身体，使用draw_snake_head函数绘制蛇的头部
    pygame.draw.rect(screen, RED, (food_x, food_y, 20, 20))
    for i in range(len(snake_body)):
        x, y = snake_body[i]
        if i == 0:  # 如果是第一个元素，即头部，调用draw_snake_head函数绘制
            draw_snake_head(x, y)
        else:  # 如果是其他元素，即身体，绘制一个绿色的矩形
            pygame.draw.rect(screen, GREEN, (x, y, 20, 20))

    # 如果游戏结束，显示提示文字和重新开始按钮
    if not game_on:
        text = font.render("Game Over!", True, WHITE)
        screen.blit(text, (320, 240))
        draw_button("Restart", 300, 300, 200, 50)

    # 显示当前的分数
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    # 更新屏幕显示
    pygame.display.flip()

    # 设置帧率为10
    clock.tick(10)
