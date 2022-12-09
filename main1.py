# Creating the distribution
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

data = np.arange(1, 10, 0.01)
pdf = norm.pdf(data, loc=5.3, scale=1)

# Probability of height to be under 4.5 ft.
prob_1 = norm(loc=5.3, scale=1).cdf(4.5)
print(prob_1)

# probability that the height of the person will be between 6.5 and 4.5 ft.

cdf_upper_limit = norm(loc=5.3, scale=1).cdf(6.5)
cdf_lower_limit = norm(loc=5.3, scale=1).cdf(4.5)

prob_2 = cdf_upper_limit - cdf_lower_limit
print(prob_2)

# probability that the height of a person chosen randomly will be above 6.5ft

cdf_value = norm(loc=5.3, scale=1).cdf(6.5)
prob_3 = 1 - cdf_value
print(prob_3)

plt.plot(data,pdf , color = 'red')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
plt.show()