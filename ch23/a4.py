import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
sales = [50, 70, 30, 85, 40]


plt.bar(fruits, sales, color='skyblue')
plt.title('과일별 판매량')
plt.xlabel('과일')
plt.ylabel('판매량')
plt.show()
