import datetime

class Poroshok:

    body = None
    date = None
    url = None

    def __init__(self, _body, _date, _from, _id):
        self.body = [None, None, None, None]
        self.body[0] = _body[0]
        self.body[1] = _body[1]
        self.body[2] = _body[2]
        self.body[3] = _body[3]
        self.date = datetime.datetime.fromtimestamp(_date).strftime('%Y.%m.%d %H:%M:%S')
        self.url = 'https://vk.com/wall' + str(_from) + '_' + str(_id)
