import statistics
import random
needles = 128000
estimates = 100
sum_area = 0
est_list = []

for _ in range(estimates):
    area_circle = 0
    i = 0
    for _ in range(needles):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            i += 1
    area_circle += (4 * i / needles)
    est_list.append(area_circle)

average = sum(est_list) / estimates
deviation = statistics.stdev(est_list)
print("The average is:", average)
print("The standard deviation is", deviation, "using", needles, "needles.")
