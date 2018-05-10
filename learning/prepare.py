review_matrix = None

class ReviewMatrix:
    text_matrix = []
    food_matrix = []
    price_matrix = []
    service_matrix = []
    ambience_matrix = []

    def __init__(self, text_matrix=[], food_matrix=[],
                 price_matrix=[], service_matrix=[], ambience_matrix=[]):
        self.text_matrix = text_matrix
        self.food_matrix = food_matrix
        self.price_matrix = price_matrix
        self.service_matrix = service_matrix
        self.ambience_matrix = ambience_matrix


def build_review_matrix(reviews):
    global review_matrix
    if review_matrix is not None:
        return review_matrix

    matrix = ReviewMatrix()
    for r in reviews:
        matrix.text_matrix.append(r.text)
        matrix.food_matrix.append(r.food)
        matrix.price_matrix.append(r.price)
        matrix.service_matrix.append(r.service)
        matrix.ambience_matrix.append(r.ambience)
    review_matrix = matrix

    return matrix
