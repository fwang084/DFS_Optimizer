class Team:
    def __init__(self, name, possessions=0, points=0, rebounds=0):
        self.name = name
        self.possessions = possessions
        self.points_allowed = points
        self.rebounds_allowed = rebounds
    def get_name(self):
        return self.name
    def get_possessions(self):
        return self.possessions
    def set_possessions(self, possessions):
        self.possesions = possessions
    def get_points_allowed(self):
        return self.points_allowed
    def set_points_allowed(self, points):
        self.points_allowed = points
    def get_rebounds_allowed(self):
        return self.rebounds_allowed
    def set_rebounds_allowed(self, rebounds):
        self.rebounds_allowed = rebounds