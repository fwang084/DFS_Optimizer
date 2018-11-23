class Player:
    def __init__(self, name, team, position, minutes=0, stats=0, price=0, proj_points=0, image=None):
        self.name = name
        self.team = team
        self.position = position
        self.minutes = minutes
        self.expected_minutes = minutes
        self.stats = stats
        self.price = price
        self.proj_points = proj_points
        self.image = image
    def get_name(self):
        return self.name
    def get_team(self):
        return self.team
    def get_minutes(self):
        return self.minutes
    def set_minutes(self, minutes):
        self.minutes = minutes
    def expected_minutes_change(self, new_minutes):
        self.expected_minutes = new_minutes
    def get_stats(self):
        return self.stats
    def set_stats(self, stats):
        self.stats = stats
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_proj_points(self):
        return self.proj_points
    def set_proj_points(self, proj_points):
        self.proj_points = proj_points

