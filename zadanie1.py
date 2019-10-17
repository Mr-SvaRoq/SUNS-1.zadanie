import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

if __name__ == '__main__':
    allData = []
    stringDictionary = {}
    stringDictionaryKey = 1
    countryDictionary = []
    regionDictionary = []

    print('\n---------NACITANIE A KONVERTOVANIE DAT-------ECH---')
    with open('data_krajiny.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # how many rows do you want //prvych 30 krajin
            if line_count == 31:
                break
            if line_count == 0:
                print(row)
                line_count += 1
            else:
                newLineOfArray = []
                counter = -1
                for x in row:
                    counter += 1
                    if counter == 10:
                        continue
                    # na zapamatanie regionu
                    if counter == 1:
                        regionDictionary.append(x)
                    # na zapamatanie country
                    if counter == 0:
                        countryDictionary.append(x)
                        continue
                    # ak je cislo, da, ak nie konvertuje
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
    print(countryDictionary)
    for row in allData:
        print(row)

    print('\n---------STRING and REGION(2. STLPEC) DICTIONARY----------')
    print(stringDictionary)
    print('\n---------ONLY REGION(2. STLPEC) DICTIONARY----------')
    print(regionDictionary)

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
        csvWriter.writerows(euclideanAllData)

    print('\n---------K MEANS----------')
    # pocet regionov a tak, to by bolo fajn opravit, ze dam pocet klastrov ako je regionov a ptm porovnam, ci to sedi s originialnimi datami
    kmeans = KMeans(n_clusters=10).fit(scaledAllData)
    # print(kmeans.cluster_centers_)


    # kolko chcem skupin/klastrov

    with open("K-means.csv", 'w', newline='') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerow(countryDictionary)
        csvWriter.writerow(kmeans.labels_)
        csvWriter.writerow(regionDictionary)
    set(kmeans.labels_)
    print(kmeans.labels_)
    print(set(kmeans.labels_))


    print('\n---------DB SCAN----------')
    dbscan = DBSCAN(eps=1.68, min_samples=1).fit(scaledAllData)
    print(dbscan.labels_)
    print(set(dbscan.labels_))
    with open("DBscan.csv", 'w', newline='') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerow(countryDictionary)
        csvWriter.writerow(dbscan.labels_)
        csvWriter.writerow(regionDictionary)

    print('\n---------K MEANS - Cluster Centers----------')
    # dataIndex = 0
    with open("euclideanClusterCenters.csv", 'w', newline='') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')

        for dataIndex in range(0, 10):
            for data in scaledAllData:
                foo = [kmeans.cluster_centers_[dataIndex], data]
                # euclideanClusterCenters = euclidean_distances(kmeans.cluster_centers_[0], scaledAllData[0])
                euclideanClusterCenters = euclidean_distances(foo, foo)
                # print(euclideanClusterCenters)
            csvWriter.writerows(euclideanClusterCenters)

    with open("cluster_centers_.csv", 'w', newline='') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(kmeans.cluster_centers_)

# https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
# https://scikit-learn.org/stable/datasets/index.html
