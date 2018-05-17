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
            self.food = '1'
        elif food == 'NEGATIVE':
            self.food = '-1'
        self.food = '0'

    def set_price(self, price):
        if price == 'POSITIVE':
            self.price = '1'
        elif price == 'NEGATIVE':
            self.price = '-1'
        self.price = '0'

    def set_service(self, service):
        if service == 'POSITIVE':
            self.service = '1'
        elif service == 'NEGATIVE':
            self.service = '-1'
        self.service = '0'

    def set_ambiance(self, ambiance):
        if ambiance == 'POSITIVE':
            self.ambiance = '1'
        elif ambiance == 'NEGATIVE':
            self.ambiance = '-1'
        self.ambiance = '0'
