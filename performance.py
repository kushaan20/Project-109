import plotly.figure_factory as ff 
import pandas as pd 
import statistics 
import random 
import plotly.graph_objects as go
import csv

df = pd.read_csv('StudentsPerformance.csv')

data = df['math score'].to_list()
#weight_list = df['Weight(Pounds)'].to_list()

data_mean = statistics.mean(data)
#weight_mean = statistics.mean(weight_list)

data_median = statistics.median(data)
#weight_median = statistics.median(weight_list)

data_mode = statistics.mode(data)
#weight_mode = statistics.mode(weight_list)

print('The Mean, Median and Mode of the maths data are {}, {} and {} respectively.'.format(data_mean, data_median, data_mode))
#print('The Mean, Median and Mode of weight are {}, {} and {} respectively.'.format(weight_mean, weight_median, weight_mode))

data_stdev = statistics.stdev(data)
#weight_stdev = statistics.stdev(weight_list)

print('The Standard Deviation of height is {}'.format(data_stdev))
#print('The Standard Deviation of weight is {}'.format(weight_stdev))

data_first_std_deviation_start, data_first_std_deviation_end = data_mean-data_stdev, data_mean+data_stdev
data_second_std_deviation_start, data_second_std_deviation_end = data_mean-(2*data_stdev), data_mean+(2*data_stdev)
data_third_std_deviation_start, data_third_std_deviation_end = data_mean-(3*data_stdev), data_mean+(3*data_stdev)

#weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-weight_stdev, weight_mean+weight_stdev
#weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean-(2*weight_stdev), weight_mean+(2*weight_stdev)
#weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean-(3*weight_stdev), weight_mean+(3*weight_stdev)

fig = ff.create_distplot([data], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[data_mean, data_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[data_first_std_deviation_start, data_first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[data_first_std_deviation_start, data_first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[data_second_std_deviation_start, data_second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[data_second_std_deviation_start, data_second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

data_list_of_data_within_1_std_deviation = [result for result in data if result > data_first_std_deviation_start and result < data_first_std_deviation_end]
data_list_of_data_within_2_std_deviation = [result for result in data if result > data_second_std_deviation_start and result < data_second_std_deviation_end]
data_list_of_data_within_3_std_deviation = [result for result in data if result > data_third_std_deviation_start and result < data_third_std_deviation_end]

#weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end]
#weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]
#weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result < weight_third_std_deviation_end]

print("{}% of data of Maths lies within 1 Standard Deviation".format(len(data_list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data of Maths lies within 2 Standard Deviations".format(len(data_list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data of Maths lies within 3 Standard Deviations".format(len(data_list_of_data_within_3_std_deviation)*100.0/len(data)))


#print("{}% of data of Weight lies within 1 Standard Deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
#print("{}% of data of Weight lies within 2 Standard Deviations".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
#print("{}% of data of Weight lies within 3 Standard Deviations".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))










