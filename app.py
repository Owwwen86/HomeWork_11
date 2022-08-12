# -*- coding: cp1251 -*-
from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill, \
    get_candidates_by_similar_name

FILENAME = 'candidates.json'
data = (load_candidates_from_json(FILENAME))
app = Flask(__name__)


# Главная страница со ссылками на странички кандидатов
@app.route("/")
def page_index():
    return render_template('list.html', data=data)


# Страницы кандидатов
@app.route("/candidate/<x>")
def page_candidate(x):
    candidate = get_candidates_by_name(x, data)
    return render_template('card.html', candidate=candidate)


# Страница поиска кандидата по совпадению имени
@app.route("/candidate/search/<candidate_name>")
def search_name(candidate_name):
    candidate = get_candidates_by_similar_name(candidate_name, data)
    count_candidate = len(candidate)
    return render_template('search.html', candidate=candidate, count_candidate=count_candidate)


# Поиск кандидатов по навыкам
@app.route("/skill/<skill_name>")
def search_skill(skill_name):
    candidate = get_candidates_by_skill(skill_name, data)
    count_candidate = len(candidate)
    return render_template('skill.html', candidate=candidate, count_candidate=count_candidate)


if __name__ == '__main__':
    app.run(host='127.0.0.2', port=1100)