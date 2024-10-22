#Student: Junayd Lateef (ASU ID: 1221505571)
# create plot 
import matplotlib.pyplot as plt 
import numpy as np 

# F1 Data
cats = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5', 'Trial 6']
f1scores = [0.8081354859132637, 0.7481481481481482, 0.8081354859132637, 0.8158518518518518, 0.8081354859132637, 0.8158518518518518]

# Create bar chart
plt.bar(cats, f1scores)

# Add labels and title and create the graph
plt.xlabel('Trials')
plt.ylabel('F1 Scores')
plt.yticks([.74, .75, .76, .77, .78, .79, .80, .81, .82])
plt.ylim(0.74, 0.82)
plt.title('F1 Scores based on each Trial (80-20)')

#Save the chart 
plt.tight_layout()  
plt.savefig('./80_20_resultcharts/80_20_f1scores.png')