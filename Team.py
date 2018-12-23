class Team:
    def __init__(self, names, points=0, rebounds=0, assists=0, threes=0, steals=0,
                 blocks=0, turnovers=0, possessions=0, factors=[]):
        self.names = names
        self.points_allowed = points
        self.rebounds_allowed = rebounds
        self.assists_allowed = assists
        self.threes_allowed = threes
        self.steals_allowed = steals
        self.blocks_allowed = blocks
        self.opp_turnovers = turnovers
        self.possessions = possessions
        self.factors = factors
    def get_names(self):
        return self.names
    def get_points_allowed(self):
        return self.points_allowed
    def set_points_allowed(self, points):
        self.points_allowed = points
    def get_rebounds_allowed(self):
        return self.rebounds_allowed
    def set_rebounds_allowed(self, rebounds):
        self.rebounds_allowed = rebounds
    def get_assists_allowed(self):
        return self.assists_allowed
    def set_assists_allowed(self, assists):
        self.assists_allowed = assists
    def get_threes_allowed(self):
        return self.threes_allowed
    def set_threes_allowed(self, threes):
        self.threes_allowed = threes
    def get_steals_allowed(self):
        return self.steals_allowed
    def set_steals_allowed(self, steals):
        self.steals_allowed = steals
    def get_blocks_allowed(self):
        return self.blocks_allowed
    def set_blocks_allowed(self, blocks):
        self.blocks_allowed = blocks
    def get_opp_turnovers(self):
        return self.opp_turnovers
    def set_opp_turnovers(self, turnovers):
        self.opp_turnovers = turnovers
    def get_possessions(self):
        return self.possessions
    def set_possessions(self, possessions):
        self.possessions = possessions
    def get_factors(self):
        return self.factors
    def set_factors(self, factors):
        self.factors = factors