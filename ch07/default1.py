def persona(width,height):
    print("함수기본값없음","width:",width,"height:",height)
    
    
def personb(width=4,height=4):
    print("함수기본값있음","width:",width,"height:",height)


def personc(width,height=4):
    print("함수기본값없음","width:",width,"height:",height)



persona(10,10)    
personb()
personb(20)
personc(15)
