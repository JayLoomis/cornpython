import uuid

class Enemy:
    def __init__(self, hp=100):
        self.id = uuid.uuid1()
        self.hit_points = hp
        self.subscribers = []

    def take_damage(self, dmg_amt, dmg_type):
        if self.hit_points > dmg_amt:
            self.hit_points -= dmg_amt
        else:
            self.hit_points = 0

    def subscribe(self, callback):
        """ Enables the caller to subscribe for messages.

        The caller provides a callback to receive messages from this object.

        Params
            callback - A function of the signature:
                func(sender_id, event_type, event_message)
        """
        self.subscribers.append(callback)

    def fire_message(self, event_type, event_message):
        for sub in self.subscribers:
            sub(self.id, event_type, event_message)