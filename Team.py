class Team:
    def __init__(self, names, possessions=0, points=0, rebounds=0, turnovers=0):
        self.names = names
        self.possessions = possessions
        self.points_allowed = points
        self.rebound_percentage = rebounds
        self.turnovers = turnovers
    def get_names(self):
        return self.names
    def get_possessions(self):
        return self.possessions
    def set_possessions(self, possessions):
        self.possesions = possessions
    def get_points_allowed(self):
        return self.points_allowed
    def set_points_allowed(self, points):
        self.points_allowed = points
    def get_rebound_percentage(self):
        return self.rebound_percentage
    def set_rebound_percentage(self, rebounds):
        self.rebound_percentage = rebounds