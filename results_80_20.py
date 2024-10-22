#Student: Junayd Lateef (ASU ID: 1221505571)

# create plot (used to splot out the corelations in )
import matplotlib.pyplot as plt 
import numpy as np 

# metrics 
#[(0.8166666666666667, 0.8259469696969697, 0.8166666666666667), 
# (0.7666666666666667, 0.7835788325150027, 0.7666666666666667), 
# (0.8166666666666667, 0.8259469696969697, 0.8166666666666667), 
# (0.8166666666666667, 0.8155103668261563, 0.8166666666666667), 
# (0.8166666666666667, 0.8259469696969697, 0.8166666666666667), 
# (0.8166666666666667, 0.8155103668261563, 0.8166666666666667)]

# f1 scores
#[0.8081354859132637, 0.7481481481481482, 0.8081354859132637, 0.8158518518518518, 0.8081354859132637, 0.8158518518518518]

# Metric Data
categories = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5', 'Trial 6']
acc = (0.8166666666666667, 0.7666666666666667, 0.8166666666666667, 0.8166666666666667, 0.8166666666666667, 0.8166666666666667) 
prec = (0.8259469696969697, 0.7835788325150027, 0.8259469696969697, 0.8155103668261563, 0.8259469696969697, 0.8155103668261563) 
recall = (0.8166666666666667, 0.7666666666666667, 0.8166666666666667, 0.8166666666666667, 0.8166666666666667, 0.8166666666666667)

# Set the bar width
bar_width = 0.2

# Set the positions of the groups on the x-axis
index = np.arange(len(categories))

# Create the bars for each group
bars1 = plt.bar(index, acc, width=bar_width, label='Accuracy')
bars2 = plt.bar(index + bar_width, prec, width=bar_width, label='Precision')
bars3 = plt.bar(index + 2 * bar_width, recall, width=bar_width, label='Recall')

# Adding titles and labels
plt.title('Metric Data based on Trials (80-20)')
plt.xlabel('Trials')
plt.ylabel('Values')
plt.yticks([.76, .77, .78, .79, .80, .81, .82, .83])
plt.ylim(0.76, 0.83)
plt.xticks(index + bar_width, categories)  # Set the ticks to the center of the grouped bars
plt.legend()  # Add a legend

#Save the chart appropriately
plt.tight_layout()  
plt.savefig('./80_20_resultcharts/80_20_metrics.png')