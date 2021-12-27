
# databaseモジュールでmycursorをインストールして、データベースへのアクセスを可能にする。
from database import mycursor  

# 任意の文字列(おつかれ)を入力として、拡張された文字列(おつかれーらいす)などのリストを出力する関数。
def extend_word(word):
    
    # 入力された文字列を配列にする。
    character_list = list(word)
    # その配列の長さ
    len_character_list = len(character_list)
    # 最終的に出力する配列を空で用意する
    result_list = []
    
    # 「おつかれ」に繋がる単語をデータベースから検索、その後先頭の単語を除いた「つかれ」に繋がる単語を検索
    # さらに「かれ」に繋がる単語を検索、ここで「かれーらいす」がデータベースで見つかる。
    # 見つかった「かれーらいす」ともともとの入力「おつかれ」を結合して、「おつかれーらいす」をresult_listに格納する。
    for i in range(0, len_character_list):
        sub_word = ''.join(word[i:])
        mycursor.execute("""SELECT * FROM words WHERE word LIKE %s""", (sub_word + "%",))
        results = mycursor.fetchall()
        
        # 「つかれ」に繋がる単語を検索して、何もヒットしなければ次へ進む。
        if len(results) == 0:
            continue
        
        for result in results:
            
            # これは仮説だが、入力された単語(おつかれ)+ 1語となる場合「おつかれは(おつかれ葉)」などは聞こえが悪く、
            # 最低でも2語「おつかれしぴ(おつかレシピ)」から聞こえが良くなるという仮説のもと1語で終わるものを排除している。
            if len(result[1]) - len(sub_word) <= 1:
                continue
            
            word_combined = result[1]
            extention_word = word + word_combined[len(sub_word):]
            result_list.append(extention_word)
        
        # 結果が21件以上になったら終了
        if len(result_list) >= 21:
            break
            
    return result_list


if __name__ == '__main__':
    
    word = 'おつかれ'
    print(extend_word(word))

# the end of code