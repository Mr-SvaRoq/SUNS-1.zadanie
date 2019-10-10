
# def my_function():
#   print("Hello from a function")

# class Car:
#
#     def __init__(self, speed=0):
#         self.speed = speed
#         self.odometer = 0
#         self.time = 0
#
#     def say_state(self):
#         print("I'm going {} kph!".format(self.speed))
#
#     def accelerate(self):
#         self.speed += 5
#
#     def brake(self):
#         self.speed -= 5
#
#     def step(self):
#         self.odometer += self.speed
#         self.time += 1
#
#     def average_speed(self):
#         if self.time != 0:
#             return self.odometer / self.time
#         else:
#             pass

    # data_reader = DataReader();
    # my_car = Car()
    # print("I'm a car!")
    # while True:
    #     action = input("What should I do? [A]ccelerate, [B]rake, "
    #              "show [O]dometer, or show average [S]peed?").upper()
    #     if action not in "ABOS" or len(action) != 1:
    #         print("I don't know how to do that")
    #         continue
    #     if action == 'A':
    #         my_car.accelerate()
    #     elif action == 'B':
    #         my_car.brake()
    #     elif action == 'O':
    #         print("The car has driven {} kilometers".format(my_car.odometer))
    #     elif action == 'S':
    #         print("The car's average speed was {} kph".format(my_car.average_speed()))
    #     my_car.step()
    #     my_car.say_state()

# class DataReader:
#     import csv
#
#     with open('data_krajiny.csv', mode='r') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#                 line_count += 1
#         print(f'Processed {line_count} lines.')S

import csv
import numpy as np
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import KMeans

if __name__ == '__main__':
    allData = []
    stringDictionary = {}
    stringDictionaryKey = 1
    countryDictionary = []

    print('\n---------NACITANIE A KONVERTOVANIE DAT----------')
    with open('data_krajiny.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # how many rows do you want
            if line_count == 31:
                break
            if line_count == 0:
                line_count += 1
            else:
                newLineOfArray = []
                counter = -1
                for x in row:
                    counter += 1
                    if counter == 10 or counter == 0:
                        continue
                    # if len(newLineOfArray) == 0:
                    #     newLineOfArray.append(0)
                    #     countryDictionary.append(x)
                    #     continue
                    try:
                        floatValue = float(x)
                        newLineOfArray.append(floatValue)
                    except ValueError:
                        if not stringDictionary.get(x):
                            if x == '-' or x == '~0.0' or x == '-~0.0':
                                stringDictionary[x] = 0
                            else:
                                stringDictionary[x] = stringDictionaryKey
                                stringDictionaryKey += 1
                            newLineOfArray.append(stringDictionary[x])
                        elif stringDictionary.get(x):
                            newLineOfArray.append(stringDictionary[x])
                allData.append(newLineOfArray)
                line_count += 1
    for row in allData:
        print(row)

    print('\n---------STRING and REGION(2. STLPEC) DICTIONARY----------')
    print(stringDictionary)
    # X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
    # kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

    # transformer = Normalizer().fit(allData)
    # print(transformer.transform(allData))

    with open("allDataConvert.csv", 'w', newline='') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(allData)

    print('\n---------NORMALIZACIA VSETKYCH DAT----------')
    scaler = MinMaxScaler()
    scaler.fit(allData)
    scaledAllData = scaler.transform(allData)
    print(scaledAllData)

    with open("normal.csv", 'w', newline='') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(scaledAllData)

    print('\n---------EUKLIDOVA VZDIALENOST----------')
    euclideanAllData = euclidean_distances(scaledAllData, scaledAllData)
    print(euclideanAllData)
    with open("euclideanAllData.csv", 'w', newline='') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        # for row in euclideanAllData:
            # csvWriter.writerow(row)
        csvWriter.writerows(euclideanAllData)
    # overenie normalizacie ?
    # index = 3
    # print(countryDictionary[index])
    # print(scaledAllData[index])

    print('\n---------K MEANS----------')
    kmeans = KMeans(n_clusters=20, random_state=0).fit(euclideanAllData)
    print(kmeans.labels_)
    # counter = 0
    # for k in kmeans.labels_:
    #     print(counter)
    #     counter +=1
    # print(kmeans.cluster_centers_)



