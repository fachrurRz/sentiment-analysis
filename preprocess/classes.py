class Review:
    text = None
    food = None
    price = None
    service = None
    ambiance = None
    id = None

    def __init__(self, id, text):
        self.text = text
        self.id = id

    def set_food(self, food):
        if food == 'POSITIVE':
            self.food = True
        self.food = False

    def set_price(self, price):
        if price == 'POSITIVE':
            self.price = True
        self.price = False

    def set_service(self, service):
        if service == 'POSITIVE':
            self.service = True
        self.service = False

    def set_ambiance(self, ambiance):
        if ambiance == 'POSITIVE':
            self.ambiance = True
        self.ambiance = False

