from .train import *

review_matrix = None

class ReviewMatrix:

    def __init__(self, text_matrix=[], food_matrix=[],
                 price_matrix=[], service_matrix=[], ambience_matrix=[]):
        self.text_matrix = text_matrix
        self.food_matrix = food_matrix
        self.price_matrix = price_matrix
        self.service_matrix = service_matrix
        self.ambience_matrix = ambience_matrix


def build_review_matrix(text_matrix=[], food_matrix=[],
                 price_matrix=[], service_matrix=[], ambience_matrix=[], forced=False):
    global review_matrix
    if review_matrix is not None and not forced:
        return review_matrix
    m = ReviewMatrix()
    m.text_matrix = text_matrix
    m.food_matrix = food_matrix
    m.price_matrix = price_matrix
    m.service_matrix = service_matrix
    m.ambience_matrix = ambience_matrix
    review_matrix = m

    return m


def build_from_objects(reviews, forced=False):
    global review_matrix
    if review_matrix is not None and not forced:
        return review_matrix

    matrix = ReviewMatrix()
    for r in reviews:
        text = r.text
        if forced:
            v = get_vocabulary()
            for w in r.text:
                if w not in v:
                    text.remove(w)
        matrix.text_matrix.append(" ".join(text))
        matrix.food_matrix.append(r.food)
        matrix.price_matrix.append(r.price)
        matrix.service_matrix.append(r.service)
        matrix.ambience_matrix.append(r.ambiance)
    review_matrix = matrix

    return matrix