#Student: Junayd Lateef (ASU ID: 1221505571)

# create plot (used to splot out the corelations in )
import matplotlib.pyplot as plt 
import numpy as np 

# Metric Data
categories = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5', 'Trial 6']
acc = (0.8555555555555555, 0.8444444444444444, 0.8555555555555555, 0.8777777777777778, 0.8555555555555555, 0.8777777777777778) 
prec = (0.8557165861513687, 0.8421271538918599, 0.8557165861513687, 0.8771649001369961, 0.8557165861513687, 0.8771649001369961) 
recall = (0.8555555555555555, 0.8444444444444444, 0.8555555555555555, 0.8777777777777778, 0.8555555555555555, 0.8777777777777778)

# Set the bar width
bar_width = 0.2

# Set the positions of the groups on the x-axis
index = np.arange(len(categories))

# Create the bars for each group
bars1 = plt.bar(index, acc, width=bar_width, label='Accuracy')
bars2 = plt.bar(index + bar_width, prec, width=bar_width, label='Precision')
bars3 = plt.bar(index + 2 * bar_width, recall, width=bar_width, label='Recall')

# Adding titles and labels
plt.title('Metric Data based on Trials (70-30)')
plt.xlabel('Trials')
plt.ylabel('Values')
plt.yticks([.81, .82, .83, .84, .85, .86, .87, .88])
plt.ylim(0.81, 0.88)
plt.xticks(index + bar_width, categories)  # Set the ticks to the center of the grouped bars
plt.legend()  # Add a legend

#Save the chart appropriately
plt.tight_layout()  
plt.savefig('./70_30_resultcharts/70_30_metrics.png')