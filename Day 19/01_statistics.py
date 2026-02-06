# Python is widely used in:
# Data analysis
# Machine learning
# Research & academia
# Financial analysis
# Scientific computing

# Why Python is popular for statistics?
# Simple syntax
# Huge ecosystem of libraries
# Strong visualization support
# Works well with AI/ML frameworks


import statistics

# mean() → average
# median() → middle value
# mode() → most frequent value
# harmonic_mean()
# geometric_mean()

data=[10,20,30,40]
# sum = 100 so avg = 100/4=25
print(statistics.mean(data))
print(statistics.median(data))   
print(statistics.mode(data)) 


# variance() → sample variance
# pvariance() → population variance
# stdev() → sample standard deviation
# pstdev() → population std deviation

print(statistics.variance(data))
print(statistics.stdev(data))


# for real-world use case:
# Small simple list → statistics
# Large numerical data → numpy
# Hypothesis testing → scipy
# Dataset analysis → pandas
# ML pipeline → numpy + pandas + sklearn