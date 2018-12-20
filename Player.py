class Player:
    def __init__(self, name, team, position, minutes, stats=[0,0,0,0,0,0,0], price = 0, image=None):
        self.name = name
        self.team = team
        self.position = position
        self.avg_minutes = minutes
        self.expected_minutes = minutes
        self.avg_stats = stats
        self.proj_stats = stats
        self.price = price
        self.proj_points = 0
        self.image = image
    def get_name(self):
        return self.name
    def get_team(self):
        return self.team
    def get_position(self):
        return self.position
    def set_position(self, position):
        self.position=position
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

