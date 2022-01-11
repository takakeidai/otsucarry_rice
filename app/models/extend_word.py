from configparser import Error

from app.models.database import session_scope
from app.models.search_word import search_word
from app.models.translate_alphabetically import conversion
from app.models.database import Ohayou
from app.models.database import Oyasumi
from app.models.database import Gomenne
from app.models.database import Otsukare
import json

def create_extend_word(word):
    
    # 入力された文字列を配列にする。
    character_list = list(word)
    # その配列の長さ
    len_character_list = len(character_list)
    # 最終的に出力する配列を空で用意する
    result_list = []
    
    # 見出しの作成 gomenne
    # title = conversion.do(word)
    # print(title)
    
    # 「おつかれ」に繋がる単語をデータベースから検索、その後先頭の単語を除いた「つかれ」に繋がる単語を検索
    # さらに「かれ」に繋がる単語を検索、ここで「かれーらいす」がデータベースで見つかる。
    # 見つかった「かれーらいす」ともともとの入力「おつかれ」を結合して、「おつかれーらいす」をresult_listに格納する。
    for i in range(len_character_list-1, -1, -1):
        sub_word = ''.join(word[i:])
        results = search_word(sub_word)
        
        # ひらがなをアルファベット表記に変える関数を作成する。
        for result in results:
            extention_word = word + result[len(sub_word):]
            result_list.append(extention_word)
    
    return result_list


def get_extended_word_ohayo(callback, word = 'おはよう'):
    
    alphabet_title = conversion.do(word)
    outcome_list = []
    try:
        with session_scope() as session:
            tittle_in_database = session.query(Ohayou).filter_by(
                title=alphabet_title).first()
            print(tittle_in_database)
    except Error as e:
        raise
    
    if tittle_in_database is None:
        result_list  = callback(word)
        for result in result_list:
            database = Ohayou(title=alphabet_title,created_word = result )
            try:
                with session_scope() as session:
                    session.add(database)
            except Error as e:
                raise e
        
    with session_scope() as session:
        from_database = session.query(Ohayou).filter_by(
            title = alphabet_title).all()
        
    for data in from_database:
        id_text_dict = dict(id=data.id, text=data.created_word)
        outcome_list.append(id_text_dict)
    
    outcome = {alphabet_title : outcome_list}

    return outcome

def get_extended_word_oyasumi(callback, word = 'おやすみ'):
    
    alphabet_title = conversion.do(word)
    outcome_list = []
    try:
        with session_scope() as session:
            tittle_in_database = session.query(Oyasumi).filter_by(
                title=alphabet_title).first()
            print(tittle_in_database)
    except Error as e:
        raise
    
    if tittle_in_database is None:
        result_list  = callback(word)
        for result in result_list:
            database = Oyasumi(title=alphabet_title,created_word = result )
            try:
                with session_scope() as session:
                    session.add(database)
            except Error as e:
                raise e
        
    with session_scope() as session:
        from_database = session.query(Oyasumi).filter_by(
            title = alphabet_title).all()
        
    for data in from_database:
        id_text_dict = dict(id=data.id, text=data.created_word)
        outcome_list.append(id_text_dict)
    
    outcome = {alphabet_title : outcome_list}

    return outcome

def get_extended_word_gomenne(callback, word = 'ごめんね'):
    
    alphabet_title = conversion.do(word)
    outcome_list = []
    try:
        with session_scope() as session:
            tittle_in_database = session.query(Gomenne).filter_by(
                title=alphabet_title).first()
            print(tittle_in_database)
    except Error as e:
        raise
    
    if tittle_in_database is None:
        result_list  = callback(word)
        for result in result_list:
            database = Gomenne(title=alphabet_title,created_word = result )
            try:
                with session_scope() as session:
                    session.add(database)
            except Error as e:
                raise e
        
    with session_scope() as session:
        from_database = session.query(Gomenne).filter_by(
            title = alphabet_title).all()
        
    for data in from_database:
        id_text_dict = dict(id=data.id, text=data.created_word)
        outcome_list.append(id_text_dict)
    
    outcome = {alphabet_title : outcome_list}

    return outcome


def get_extended_word_otsukare(callback, word = 'おつかれ'):
    
    alphabet_title = conversion.do(word)
    outcome_list = []
    try:
        with session_scope() as session:
            tittle_in_database = session.query(Otsukare).filter_by(
                title=alphabet_title).first()
            print(tittle_in_database)
    except Error as e:
        raise
    
    if tittle_in_database is None:
        result_list  = callback(word)
        for result in result_list:
            database = Otsukare(title=alphabet_title,created_word = result )
            try:
                with session_scope() as session:
                    session.add(database)
            except Error as e:
                raise e
        
    with session_scope() as session:
        from_database = session.query(Otsukare).filter_by(
            title = alphabet_title).all()
        
    for data in from_database:
        id_text_dict = dict(id=data.id, text=data.created_word)
        outcome_list.append(id_text_dict)
    
    outcome = {alphabet_title : outcome_list}

    return outcome


def get_all_extended_word():
    all_data = []
    result_ohayo = get_extended_word_ohayo(create_extend_word)
    result_oyasumi = get_extended_word_oyasumi(create_extend_word)
    result_gomenne = get_extended_word_gomenne(create_extend_word)
    result_otsukare = get_extended_word_otsukare(create_extend_word)
    all_data.append(result_ohayo['ohayou'])
    all_data.append(result_oyasumi['oyasumi'])
    all_data.append(result_gomenne['gomenne'])
    all_data.append(result_otsukare['otsukare'])

    return all_data


    
# end of line break
        