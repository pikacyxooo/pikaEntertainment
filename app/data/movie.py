from app.tool.fill import GetData
from app.tool.myGetUrl import Http


class PikaMovie:
    movie_url = 'https://api.douban.com/v2/movie/search?q={}'

    def search_by_keyword(self, keyword):
        url = self.movie_url.format(keyword)
        movie_json = Http.get(url)
        datas = GetData()
        datas.get_date(movie_json, keyword)
        return datas

