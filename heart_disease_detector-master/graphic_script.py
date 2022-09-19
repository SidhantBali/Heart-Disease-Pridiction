# python 3
# -*- coding: utf-8 -*-
import os

from decision_tree import DecisionTree
import matplotlib.pyplot as plt
import pandas

path_to_dataset = os.path.join('dataset', 'joint_dataset.data')

with open(path_to_dataset, 'r') as f:
    dataset = [[float(a) for a in line.split(',')] for line in f.read().split('\n') if line is not '']
    
    
test_dataset = dataset[(len(dataset)//2):]
dataset = dataset[:(len(dataset)//2)]

results_classifier = []

approaches = 100
max_depths = 20

for approach in range(approaches):
    result_of_approach = []
    for i in range(max_depths):
        d_tree = DecisionTree(max_depth=(i+1))
        d_tree.load_to_datset(dataset)
        
        d_tree.training_classifier()
        
        true_classifier = 0     #counter of currect predictions
        false_classifier = 0    #counter of false predictions
        
        for test_data in test_dataset:
            predict_class = d_tree.predict_by_classification([test_data[:-1]])[0]
            correct = int(test_data[-1])
            
            if predict_class == correct:
                true_classifier += 1
            else:
                false_classifier += 1
                
        true_per = true_classifier/(true_classifier + false_classifier) * 100
        result_of_approach.append(true_per)
    results_classifier.append(result_of_approach)

depths = [i+1 for i in range(max_depths)]
    
    
    
folder_name = 'pictures'
name_png = 'predict.png'
new_name = name_png

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

count = 0
while True:
    path_to_picture = os.path.join(folder_name,new_name)
    if os.path.exists(path_to_picture):
        count += 1
        new_name = name_png.split('.')
        new_name = str(new_name[0] + str(count) + '.' + new_name[1])
    else:
        break
    
sum_results = [0 for _ in range(len(results_classifier[0]))]
for approach in results_classifier:
    sum_results = [x+y for x,y in zip(sum_results, approach)]
        
size_results = len(results_classifier)
avg_results = [x/size_results for x in sum_results]
        
df = pandas.DataFrame(
    {
        'avg_results':avg_results,
        'depth_of_tree':depths
    }
)

best_depth = avg_results.index(max(avg_results)) + 1
print(f"Best depth for the predict is {best_depth}")
    
ax = plt.gca()
df.plot(sharey=True, kind='line',x='depth_of_tree',y='avg_results',ax=ax, label=f'avg of {approaches} approaches')
plt.savefig(path_to_picture)
