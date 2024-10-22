#Student: Junayd Lateef (ASU ID: 1221505571)
# create plot (used to splot out the corelations in )
import matplotlib.pyplot as plt 
import numpy as np 

# F1 Data
cats = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5', 'Trial 6']
f1scores = [0.8196488328857673, 0.807156862745098, 0.8196488328857673, 0.8494807031723581, 0.8196488328857673, 0.8494807031723581]

# Create bar chart
plt.bar(cats, f1scores)

# Add labels and title
plt.xlabel('Trials')
plt.ylabel('F1 Scores')
plt.yticks([.81, .82, .83, .84, .85])
plt.ylim(0.81, 0.85)
plt.title('F1 Scores based on each Trial (75-25)')

#Save the chart appropriately
plt.tight_layout()  
plt.savefig('./75_25_resultcharts/75_25_f1scores.png')