# find the int
import time

# start_time = time.time()
#
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print(a, b, c)
#
# end_time = time.time()
# print("finish,time is:", end_time - start_time)

start_time = time.time()

for a in range(0, 1001):
    for b in range(0, 1001):
        if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
            print(a, b, 1000 - a - b)

end_time = time.time()
print("finish,time is:", end_time - start_time)
