#Student: Junayd Lateef (ASU ID: 1221505571)
# create plot (used to splot out the corelations in )
import matplotlib.pyplot as plt 
import numpy as np 

# F1 Data
cats = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5', 'Trial 6']
f1scores = [0.8490972979522597, 0.8387008547008546, 0.8490972979522597, 0.8741551400922124, 0.8490972979522597, 0.8741551400922124]

# Create bar chart
plt.bar(cats, f1scores)

# Add labels and title
plt.xlabel('Trials')
plt.ylabel('F1 Scores')
plt.yticks([.83, .84, .85, .86, .87, .88])
plt.ylim(0.83, 0.88)
plt.title('F1 Scores based on each Trial (70-30)')

#Save the chart appropriately
plt.tight_layout()  
plt.savefig('./70_30_resultcharts/70_30_f1scores.png')