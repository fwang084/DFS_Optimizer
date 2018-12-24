class Player:
    def __init__(self, name, team, positions, minutes, opponent, avg_stats, proj_stats, price, image=None):
        self.name = name
        self.team = team
        self.positions = positions
        self.avg_minutes = minutes
        self.proj_minutes = minutes
        self.opponent = opponent
        self.avg_stats = avg_stats
        self.proj_stats = proj_stats
        self.price = price
        self.proj_points = 0
        self.image = image
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_team(self):
        return self.team
    def set_team(self, team):
        self.team = team
    def get_opponent(self):
        return self.opponent
    def set_opponent(self, opponent):
        self.opponent = opponent
    def get_positions(self):
        return self.positions
    def set_positions(self, positions):
        self.positions=positions
    def get_proj_minutes(self):
        return self.proj_minutes
    def set_minutes(self, proj_minutes):
        self.proj_minutes = proj_minutes
    def get_proj_stats(self):
        return self.proj_stats
    def set_stats(self, proj_stats):
        self.proj_stats = proj_stats
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_proj_points(self):
        return self.proj_points
    def set_proj_points(self, stats):
        self.generate_projection(stats)
    def generate_projection(self, stats):
        """
        Sets a player's projected points by taking in a list of projected stats and calculating their points using DraftKings rules:
        1pt per point, 1.25:assist, 1.5:rebound, 2:steal, 2:block, 0.5:3-pointer, -0.5:turnover
        Additional bonus of 1.5 for a double-double and 3 for a triple-double
        :param stats: list of: points, rebounds, assists, steals, blocks, 3s, turnovers
        :return: None
        """
        doubles=0
        doubles_bonus=0
        for x in stats[:5]:
            if x >= 10:
                doubles+=1
        if doubles>=3:
            doubles_bonus = 4.5
        elif double==2:
            doubles_bonus = 1.5
        self.proj_points = stats[0] + 1.25*stats[1] + 1.5*stats[2] + 2*stats[3] + 2*stats[4] + 0.5*stats[5] - 0.5*stats[6] + doubles_bonus

