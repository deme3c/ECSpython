from .component import Component_t

class PhysicsComponent_t(Component_t):
    def __init__(self, eID, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.entityID = eID