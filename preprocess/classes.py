class Review:
    text = None
    food = None
    price = None
    service = None
    ambiance = None
    id = None

    def __init__(self, id, text, addition=''):
        self.text = text
        self.id = id + addition

    def set_food(self, food):
        if food == 'POSITIVE':
            self.food = True
        else:
            self.food = False

    def set_price(self, price):
        if price == 'POSITIVE':
            self.price = True
        else:
            self.price = False

    def set_service(self, service):
        if service == 'POSITIVE':
            self.service = True
        else:
            self.service = False

    def set_ambiance(self, ambiance):
        if ambiance == 'POSITIVE':
            self.ambiance = True
        else:
            self.ambiance = False

    def get_aspects(self):
        aspects = [-1, -1, -1, -1]
        if self.food is None:
            aspects[0] = 0
        elif self.food:
            aspects[0] = 1
        else:
            aspects[0] = -1

        if self.price is None:
            aspects[1] = 0
        elif self.price:
            aspects[1] = 1
        else:
            aspects[1] = -1

        if self.service is None:
            aspects[2] = 0
        elif self.service:
            aspects[2] = 1
        else:
            aspects[2] = -1

        if self.ambiance is None:
            aspects[3] = 0
        elif self.ambiance:
            aspects[3] = 1
        else:
            aspects[3] = -1

        return aspects
