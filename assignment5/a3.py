import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


iris = sns.load_dataset("iris")

sns.boxplot(x="species", y="sepal_length", data=iris)
plt.title("붓꽃 종별 꽃받침 길이 분포")
plt.show()
