from fuzzywuzzy import fuzz


class ChatbotService:
    def __init__(self, menu_items):
        #self.state = self.welcome_state
        self.basket = []
        self.greet_customer()
        self.menu = menu_items

    def greet_customer(self):
        print("Hartelijk welkom! Ik ben uw Digitaal Ober, hoe kan ik u van dienst zijn?")

    def check_item(self, wish):
        return max(
            (dish for dish in self.menu if fuzz.ratio(wish, dish) >= 80), default=None
        )
