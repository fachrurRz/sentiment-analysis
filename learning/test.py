from .prepare import ReviewMatrix
from .train import train_food_reviews, train_price_reviews, \
    train_service_reviews, train_ambience_reviews

def predict_reviews(review_matrix):
    food = predict_food(review_matrix)
    price = predict_price(review_matrix)
    service = predict_service(review_matrix)
    ambience = predict_ambience(review_matrix)
    return ReviewMatrix(review_matrix.text_matrix, food, price, service, ambience)

def predict_food(test_matrix):
    nb = train_food_reviews(test_matrix)
    predictions = nb.predict(test_matrix.text_matrix)
    return predictions

def predict_price(test_matrix):
    nb = train_price_reviews(test_matrix)
    predictions = nb.predict(test_matrix.text_matrix)
    return predictions

def predict_service(test_matrix):
    nb = train_service_reviews(test_matrix)
    predictions = nb.predict(test_matrix.text_matrix)
    return predictions

def predict_ambience(test_matrix):
    nb = train_ambience_reviews(test_matrix)
    predictions = nb.predict(test_matrix.text_matrix)
    return predictions
