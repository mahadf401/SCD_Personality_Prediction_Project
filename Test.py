##imports
import pickle
import pandas as pd
import matplotlib.pyplot as plt

## import model from the file
model = pickle.load(open('models/personality_model2.pkl', 'rb'))

## function to generate a bar chart
def generate_chart(data):
    #print(data.info())
    # Create a list of the columns for each personality trait
    col_list = list(data)
    #print(col_list)
    ext = col_list[0:10]
    est = col_list[10:20]
    agr = col_list[20:30]
    csn = col_list[30:40]
    opn = col_list[40:50] 
    my_sums = pd.DataFrame()
    my_sums['extroversion'] = data[ext].sum(axis=1)/10
    my_sums['neurotic'] = data[est].sum(axis=1)/10
    my_sums['agreeable'] = data[agr].sum(axis=1)/10
    my_sums['conscientious'] = data[csn].sum(axis=1)/10
    my_sums['open'] = data[opn].sum(axis=1)/10
    my_sums['cluster'] = my_sums.idxmax(axis=1)
    presonality_prediction= my_sums['cluster']
    my_sum = my_sums.drop('cluster', axis=1)
    # Uncomment to see a bar graph using matplotlib
    #plt.bar(my_sum.columns, my_sum.iloc[0,:], color='blue', alpha=0.2)
    #plt.plot(my_sum.columns, my_sum.iloc[0,:], color='red')
    #plt.title('Your Personality Traits')
    #plt.xticks(rotation=45)
    #plt.ylim(0,4)
    
    return presonality_prediction.values[0] ,my_sums