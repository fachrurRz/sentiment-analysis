from xml.dom.minidom import parse
import xml.dom.minidom
from preprocess.classes import Review


def get_reviews(filename):
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement

    # Get all the reviews
    raw_reviews = collection.getElementsByTagName("review")
    reviews = []
    for raw_review in raw_reviews:
        id = raw_review.getAttribute('rid')
        text_tag = raw_review.getElementsByTagName('text')[0]
        text = text_tag.childNodes[0].data
        aspects_tag = raw_review.getElementsByTagName('aspects')
        if aspects_tag:
            aspects_tag = aspects_tag[0]
            aspects = aspects_tag.getElementsByTagName('aspect')

            if filename == "train.xml":
                review = Review(id, text)
            else:
                review = Review(id, text)
            for aspect_tag in aspects:
                if aspect_tag.getAttribute('category') == 'FOOD':
                    food = aspect_tag.getAttribute('polarity')
                    review.set_food(food)
                if aspect_tag.getAttribute('category') == 'PRICE':
                    price = aspect_tag.getAttribute('polarity')
                    review.set_price(price)
                if aspect_tag.getAttribute('category') == 'SERVICE':
                    service = aspect_tag.getAttribute('polarity')
                    review.set_service(service)
                if aspect_tag.getAttribute('category') == 'AMBIENCE':
                    ambiance = aspect_tag.getAttribute('polarity')
                    review.set_ambiance(ambiance)
            reviews.append(review)
        else:
            review = Review(id, text)
            reviews.append(review)

    return reviews
