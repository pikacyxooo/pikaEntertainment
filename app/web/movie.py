import json

from flask import request, render_template

from app.data.movie import PikaMovie
from . import web


@web.route('/')
def index():
    return render_template('jinja2_base.html')


@web.route('/movie/search')
def search_movie():
    q = request.args['q']
    movie = PikaMovie()
    movie_info = movie.search_by_keyword(q)
    return render_template('jinja2_search_result.html', movie_info = movie_info)
    # return json.dumps(movie_info, default=lambda o: o.__dict__)

