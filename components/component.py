class Component_t:
    base_ID = 0
    def __init__(self):
        self.ID = Component_t.base_ID
        Component_t.base_ID += 1