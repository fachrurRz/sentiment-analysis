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
        self.food = str(food)
        # if food == 1:
        #     self.food = '1'
        # elif food == -1:
        #     self.food = '-1'
        # self.food = '5'

    def set_price(self, price):
        self.price = str(price)
        # if price == 1:
        #     self.price = '1'
        # elif price == -1:
        #     self.price = '-1'
        # self.price = '5'

    def set_service(self, service):
        self.service = str(service)
        # if service == 1:
        #     self.service = '1'
        # elif service == -1:
        #     self.service = '-1'
        # self.service = '5'

    def set_ambiance(self, ambiance):
        # if ambiance == 1:
        #     self.ambiance = '1'
        # elif ambiance == -1:
        #     self.ambiance = '-1'
        # self.ambiance = '5'
        self.ambiance = str(ambiance)
