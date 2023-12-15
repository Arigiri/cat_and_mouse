import pygame, math
class character:
    def __init__(self, init_position : tuple, veloc : float, center : tuple, image) -> None:
        """
        position của nhân vật được lưu theo hệ tọa độ cực
        position = (r, phi)
            r : bán kính
            phi : góc tạo bởi đường thẳng nối từ O -> nhân vật và trục Ox
        veloc : tốc độ góc di chuyển của một nhân vật. Trong một khung hình thì góc quay sẽ thay đổi một lượng veloc
        image : hình của nhân vật đang di chuyển.
        center : tâm của pool
        """
        self.position = init_position
        self.veloc = veloc
        self.center = center 
        self.image = image
        # self.image.get_rect().center = (self.image.get_rect().width // 2, self.image.get_rect().height//2)
        print(self.position)
        pass
    
    def move(self, phi, r = 0) -> None:
        """
        cập nhật góc của nhân vật một góc phi
        """
        self.position = (self.position[0] + r, self.position[1] + phi)
        pass
    
    def update(self) -> None:
        """
        update movement of characters
        """
        self.move(self.veloc)
        
    def draw(self, surface : pygame.surface) -> None:
        """
        draw the character
        """
        position = self.get_2Dposition2Draw()
        surface.blit(self.image, position)
        pygame.draw.circle(surface, (255, 0, 0), center= position, radius=5)
        
    
    def get_2Dposition2Draw(self) -> None:
        r = self.position[0]
        phi = self.position[1]
        # print(self.image.get_rect().width)
        x = r * math.cos(phi) + self.center[0] #- self.image.get_rect().width//2
        y = r * math.sin(phi) + self.center[1] #- self.image.get_rect().height//2
        return (x, y)