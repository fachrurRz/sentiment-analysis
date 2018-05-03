from xml.dom.minidom import parse
import xml.dom.minidom
from preprocess.classes import Review

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("train.xml")
collection = DOMTree.documentElement

# Get all the reviews
raw_reviews = collection.getElementsByTagName("review")


def get_reviews():
    reviews = []
    for raw_review in raw_reviews:
        text_tag = raw_review.getElementsByTagName('text')[0]
        text = text_tag.childNodes[0].data
        aspects_tag = raw_review.getElementsByTagName('aspects')[0]
        aspects = aspects_tag.getElementsByTagName('aspect')

        review = Review(text)
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
            if aspect_tag.getAttribute('category') == 'AMBIANCE':
                ambiance = aspect_tag.getAttribute('polarity')
                review.set_ambiance(ambiance)
        reviews.append(review)

    return reviews


