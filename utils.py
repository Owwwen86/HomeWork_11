# -*- coding: cp1251 -*-
import json
from Candidate import Candidate


def load_candidates_from_json(path):
    """Функция возвращает список всех кандидатов"""
    def load_from_json(filename):
        with open(filename, encoding='utf-8') as json_file:
            data_from_json = json.load(json_file)
        return data_from_json
    data = load_from_json(path)
    arr = []
    for item in data:
        candidate = Candidate(item['id'], item['name'], item['picture'], item['position'],
                              item['gender'], item['age'], item['skills'])
        arr.append(candidate)
    return arr


def get_candidate(candidate_id, arr):
    """Функция возвращает одного кандидата по его id"""
    for item in arr:
        if item.id == candidate_id:
            return item


def get_candidates_by_name(candidate_name, arr):
    """Функция возвращает кандидатов по имени"""
    for item in arr:
        if item.name == candidate_name:
            return item


def get_candidates_by_similar_name(candidate_name, arr):
    """Функция возвращает кандидатов по имени"""
    data = []
    for item in arr:
        if candidate_name.lower() in item.name.lower():
            data.append(item)
    return data


def get_candidates_by_skill(skill_name, arr):
    """Функция возвращает кандидатов по навыку"""
    data = []
    for item in arr:
        skills_old = item.skills.split(',')
        skills = [skill.strip().lower() for skill in skills_old]
        for i in range(0, len(skills)):
            if skill_name.lower() == skills[i]:
                data.append(item)
    return data