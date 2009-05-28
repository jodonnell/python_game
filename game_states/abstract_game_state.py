from game import errors


class AbstractGameState():
    def __init__(self):
        raise errors.AbstractClassError()

    def update(self):
        raise errors.AbstractClassError()

    def draw(self):
        raise errors.AbstractClassError()
