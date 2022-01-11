
from app.models.extend_word import get_extend_word
from app.models.extend_word import create_extend_word

if __name__=='__main__':
    
    word = 'おはよう'
    print(get_extend_word(word, create_extend_word))

# end of line break