class Team:
    def __init__(self, names, possessions=0, points=0, rebounds=0, threes=0, steals_allowed=0, opp_turnovers=0):
        self.names = names
        self.possessions = possessions
        self.points_allowed = points
        self.rebound_percentage = rebounds
        self.threes_allowed = threes
        self.steals_allowed = steals_allowed
        self.opp_turnovers = opp_turnovers
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
    def get_threes_allowed(self):
        return self.threes_allowed
    def set_threes_allowed(self, threes):
        self.threes_allowed = threes
    def get_steals_allowed(self):
        return self.steals_allowed
    def set_steals_allowed(self, steals):
        self.steals_allowed = steals
    def get_opp_turnovers(self):
        return self.opp_turnovers
    def set_opp_turnovers(self, turnovers):
        self.opp_turnovers = turnovers