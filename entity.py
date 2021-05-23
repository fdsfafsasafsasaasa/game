from errors import ImmuneObjectError
from pickle import dumps

class Entity:
    def __init__(self, id, display_name, immune=False) -> None:
        self.id = id
        self.display_name = display_name
        self.immune = immune
        
    def pickle(self) -> bytes:
        return dumps(self)

    def destroy(self, force=False) -> None:
        if self.immune and not force:
            raise ImmuneObjectError()
        del self 