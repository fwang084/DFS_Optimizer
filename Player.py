class Player:
    def __init__(self, name, team, positions, minutes, opponent, avg_stats, proj_stats, price, proj_score, image=None):
        self.name = name
        self.team = team
        self.positions = positions
        self.avg_minutes = minutes
        self.proj_minutes = minutes
        self.opponent = opponent
        self.avg_stats = avg_stats
        self.proj_stats = proj_stats
        self.price = price
        self.proj_score = proj_score
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
    def get_avg_stats(self):
        return self.avg_stats
    def set_avg_stats(self, avg_stats):
        self.avg_stats = avg_stats
    def get_proj_stats(self):
        return self.proj_stats
    def set_proj_stats(self, proj_stats):
        self.proj_stats = proj_stats
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_proj_score(self):
        return self.proj_score
    def set_proj_score(self, proj_score):
        self.proj_score = proj_score

