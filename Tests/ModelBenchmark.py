
import math
import time

from Handlers import FileImageGrabber
from Handlers.RcnnPeopleCountingStrategy import RcnnPeopleCountingStrategy


dataset = []

model = RcnnPeopleCountingStrategy()
grabber = FileImageGrabber("")

errors = []
execution_times = []

for file_name, actual_count in dataset:
    image = grabber.image_path = file_name

    start = time.time()
    calculated_count = model.CountPeople(image)
    end = time.time()

    error = calculated_count - actual_count
    execution_time = end - start

    errors.append(error)
    execution_times.append(execution_time)



mean_execution_time = 0
max_execution_time = 0
max_execution_time_file = ""
min_execution_time = math.inf
min_execution_time_file = ""

mean_error = 0
mean_squared_error = 0
max_error = 0
max_error_file = ""
min_error = math.inf
min_error_file = ""


file_names = [item[0] for item in dataset]
for file_name, execution_time, error  in zip(file_names, execution_times, errors):
    mean_execution_time += execution_time

    if execution_time > max_execution_time:
        max_execution_time = execution_time
        max_execution_time_file = file_name

    if execution_time < min_execution_time:
        min_execution_time = execution_time
        min_execution_time_file = file_name

    mean_error += error

    if error > max_error:
        max_error = error
        max_error_file = file_name

    if error < min_error:
        min_error = error
        min_error_file = file_name
    

mean_execution_time /= len(execution_times)
mean_error /= len(errors)

print(f"""
--- Benchmark Statistics ---

Mean Execution Time:    {mean_execution_time}
Max Execution Time:     {min_execution_time} - {min_execution_time_file}
Min Execution Time:     {max_execution_time} - {max_execution_time_file}

Mean Error:         {mean_error}
Mean Squared Error: {mean_squared_error}
Max Error:          {max_error} - {max_error_file}
Min Error:          {min_error} - {min_error_file}
""".strip())

