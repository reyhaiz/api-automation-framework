from faker import Faker
fake = Faker()

class DataGenerator:

    @staticmethod
    def valid_post():
        return {
            "title":  fake.sentence(nb_words=5),
            "body":   fake.paragraph(nb_sentences=3),
            "userId": fake.random_int(min=1, max=10)
        }

    @staticmethod
    def post_empty_title():
        return {"title": "", "body": fake.paragraph(), "userId": 1}

    @staticmethod
    def post_very_long_title(length=10000):
        return {"title": "A" * length, "body": fake.paragraph(), "userId": 1}