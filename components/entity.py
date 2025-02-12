class Entity_t:
    Base_ID = 0
    def __init__(self):
        self.entity_id = self.Base_ID
        Entity_t.Base_ID += 1
        
