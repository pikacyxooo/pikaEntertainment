class GetData:
    def __init__(self):
        self.total = 0
        self.count = 0
        self.keyword = ''
        self.subjects = []

    def get_date(self, data, keyword):
        self.total = data['total']
        self.count = data['count']
        self.keyword = keyword
        self.subjects = [FillData(subject) for subject in data['subjects']]


class FillData:
    def __init__(self, data):
        self.title = data['title'] or ''
        self.original_title = data['original_title'] or ''
        self.genres = '、'.join(data['genres']) or ''
        self.year = data['year'] or ''
        self.img = data['images']['small'] or ''
        self.rating = data['rating']['average'] or ''
        self.casts = '、'.join([cast['name'] for cast in data['casts']]) or ''
        self.directors = '、'.join([director['name'] for director in data['directors']]) or ''
        # self.director = data['directors'][0]['name'] or ''
