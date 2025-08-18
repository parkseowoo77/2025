import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("🎀 헬로키티 미니게임 🎀")
clock = pygame.time.Clock()

# --- 캐릭터별 리소스 로드 ---
characters = {
    "헬로키티 🎀": {
        "char": pygame.transform.scale(pygame.image.load("hello.png"), (60, 60)),
        "bg": pygame.transform.scale(pygame.image.load("bg_hello.png"), (400, 600)),
        "ribbon": pygame.transform.scale(pygame.image.load("ribbon_hello.png"), (40, 40))
    },
    "마이멜로디 🐰": {
        "char": pygame.transform.scale(pygame.image.load("melody.png"), (60, 60)),
        "bg": pygame.transform.scale(pygame.image.load("bg_melody.png"), (400, 600)),
        "ribbon": pygame.transform.scale(pygame.image.load("ribbon_melody.png"), (40, 40))
    },
    "쿠로미 🖤": {
        "char": pygame.transform.scale(pygame.image.load("kuromi.png"), (60, 60)),
        "bg": pygame.transform.scale(pygame.image.load("bg_kuromi.png"), (400, 600)),
        "ribbon": pygame.transform.scale(pygame.image.load("ribbon_kuromi.png"), (40, 40))
    }
}

# --- 캐릭터 선택 화면 ---
font = pygame.font.SysFont(None, 40)
selected = None
running = True
while running and selected is None:
    screen.fill((255, 255, 255))
    title = font.render("캐릭터를 선택하세요!", True, (0, 0, 0))
    screen.blit(title, (80, 100))

    y = 200
    for idx, name in enumerate(characters.keys()):
        text = font.render(name, True, (0, 0, 0))
        rect = text.get_rect(center=(200, y))
        screen.blit(text, rect)
        if pygame.mouse.get_pressed()[0]:
            if rect.collidepoint(pygame.mouse.get_pos()):
                selected = name
        y += 80

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(30)

if not running:
    pygame.quit()
    exit()

# --- 선택된 캐릭터 리소스 ---
char_img = characters[selected]["char"]
bg_img = characters[selected]["bg"]
ribbon_img = characters[selected]["ribbon"]
player = pygame.Rect(180, 500, 60, 60)

# --- 리본 생성 ---
ribbons = [pygame.Rect(random.randint(0, 360), random.randint(-600, 0), 40, 40) for _ in range(5)]

score = 0
while running:
    # 배경
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player.right < 400:
        player.move_ip(5, 0)

    # 리본 이동
    for r in ribbons:
        r.move_ip(0, 5)
        if r.top > 600:
            r.topleft = (random.randint(0, 360), -30)
        if player.colliderect(r):
            score += 1
            r.topleft = (random.randint(0, 360), -30)
        screen.blit(ribbon_img, r)

    # 캐릭터
    screen.blit(char_img, player)

    # 점수
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

