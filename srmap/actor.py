class Actor:
    def __init__(self, position=(0, 0), size=(0, 0), type='', properties=None):
        self.position = position
        self.size = size
        self.type = type
        self.properties = [] if properties is None else properties
