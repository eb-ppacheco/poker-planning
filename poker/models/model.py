class Board:
    def __init__(self, name, url, roles, admin):
        self.name = name
        self.url = url
        self.admin = admin
        self.tasks = []
        self.players = []
        self.active_task = None
