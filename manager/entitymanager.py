from ..components.entity import Entity_t 
from ..components.physicscomponent import PhysicsComponent_t
from ..components.rendercomponent import RenderComponent_t

from typing import TypeVar, Generic

class EntityManager_t:
    def __init__(self):
        self.entity_list: list[Entity_t] = []
        self.physics_components: list[PhysicsComponent_t] = []
        self.render_components: list[RenderComponent_t] = []
        
    