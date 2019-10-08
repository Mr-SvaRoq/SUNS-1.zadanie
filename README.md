# SUNS-1.zadanie
- Python 3.6
- Kniznica: https://scikit-learn.org/stable/

---------NACITANIE A KONVERTOVANIE DAT----------
- [1, 141.0, 3.79399991, 0.401477218, 0.581543326, 0.180746779, 0.10617952, 0.311870933, 0.06115783, 652864.0, 35530.0, 54.4, 106.3, 43.2, 4.1, 3.2, 1.2, 20270.0, -2.4, 623.2, 23.3, 23.3, 53.3, 1458.0, 3568.0, -2110.0, 61.6, 10.0, 28.5, 8.6, 5.3, 63.5, 61.0, 68.6, 26.7, 4.0, 61.6, 8.3, 42.0, 0.3, 5.0, 8.2, 0.3, 3.3, 91.1, 131.6, 39.7, 70.7, 3.7, 13.3, 27.7, 2.1, 1513.1]
[2, 109.0, 4.644000053, 0.996192753, 0.803685248, 0.731159747, 0.381498635, 0.201312944, 0.039864216, 28748.0, 2930.0, 106.9, 101.9, 17.4, 19.0, -0.1, 2.0, 11541.0, 2.6, 3984.2, 22.4, 26.0, 51.7, 1962.0, 4669.0, -2707.0, 41.4, 18.3, 40.3, 15.8, 1.7, 79.9, 75.6, 14.6, 57.4, 2.2, 106.4, 63.3, 130.0, 2.0, 36.0, 5.9, 1.3, 3.5, 111.7, 115.5, 92.5, 98.8, 68.1, 48.7, 22.9, 28.2, 8.8]
[3, 53.0, 5.872000217, 1.091864467, 1.146217465, 0.617584646, 0.233335808, 0.069436647, 0.14609611, 2381741.0, 41318.0, 17.3, 102.0, 29.3, 9.4, 2.0, 0.6, 164779.0, 3.8, 4154.1, 12.2, 37.3, 50.5, 29992.0, 47091.0, -17099.0, 10.8, 34.5, 54.7, 11.4, 3.0, 76.5, 74.1, 27.7, 70.7, 2.8, 113.0, 38.2, 135.0, 3.7, 55.0, 7.2, 0, 0, 112.7, 119.5, 101.7, 98.1, 45.1, 28.9, 31.6, 0.8, 99.8]
[4, 140.0, 3.795000076, 0.85842818, 1.10441196, 0.049868666, 0.0, 0.09792649, 0.069720335, 1246700.0, 29784.0, 23.9, 96.2, 46.8, 4.0, 3.5, 0.4, 117955.0, 3.0, 4714.1, 6.8, 51.2, 42.0, 21011.0, 8790.0, 12221.0, 4.2, 37.6, 58.2, 6.6, 6.0, 63.0, 57.4, 65.4, 44.1, 5.0, 60.8, 12.4, 146.0, 1.4, 25.0, 3.3, 0, 0, 100.4, 156.9, 22.7, 35.1, 8.2, 10.4, 38.2, 46.5, 45.7]
[5, 24.0, 6.598999977, 1.185295463, 1.440451145, 0.695137084, 0.494519204, 0.109457061, 0.059739888, 2780400.0, 44271.0, 16.2, 95.9, 24.9, 15.4, 1.0, 4.8, 632343.0, 2.4, 14564.5, 6.0, 27.8, 66.2, 57733.0, 55610.0, 2124.0, 2.0, 24.8, 73.1, 6.5, 2.3, 79.8, 72.2, 13.7, 91.8, 1.0, 143.9, 69.4, 256.0, 4.7, 85.0, 4.8, 3.8, 5.3, 109.8, 110.2, 110.3, 103.4, 102.9, 63.5, 38.9, 10.0, 5.0]
[2, 121.0, 4.375999928, 0.900596738, 1.007483721, 0.637524426, 0.198303267, 0.083488092, 0.026674422, 29743.0, 2930.0, 102.9, 88.8, 20.0, 16.9, 0.3, 6.3, 10529.0, 3.0, 3489.1, 19.0, 28.3, 52.8, 1776.0, 3230.0, -1455.0, 35.0, 15.7, 49.3, 16.6, 1.6, 77.0, 70.6, 13.2, 62.7, -0.1, 115.2, 58.2, 114.0, 1.8, 46.0, 4.5, 2.8, 2.8, 98.5, 98.5, 89.0, 88.1, 46.9, 41.6, 9.9, 11.7, 19.3]
[6, 10.0, 7.28399992, 1.484414935, 1.510041952, 0.843886793, 0.601607382, 0.47769925, 0.30118373, 7692060.0, 24451.0, 3.2, 99.3, 19.0, 21.0, 1.5, 28.2, 1230859.0, 2.4, 51352.2, 2.5, 26.5, 71.1, 189630.0, 189406.0, 224.0, 2.7, 21.2, 76.1, 5.5, 1.9, 84.4, 80.2, 3.9, 89.4, 1.5, 132.8, 84.6, 948.0, 15.3, 222.0, 9.4, 3.4, 5.2, 102.1, 102.3, 133.6, 141.3, 106.3, 75.4, 28.7, 16.2, 58.2]
[7, 13.0, 7.006000042, 1.487097263, 1.459944963, 0.815328419, 0.56776619, 0.316472322, 0.221060365, 83871.0, 8736.0, 106.0, 96.2, 14.1, 25.1, 0.6, 17.5, 376967.0, 1.0, 44117.7, 1.3, 28.3, 70.4, 145503.0, 149299.0, -3795.0, 4.7, 25.6, 69.7, 6.2, 1.4, 83.5, 78.4, 3.3, 66.0, 0.4, 157.4, 83.9, 118.0, 6.9, 158.0, 11.2, 5.2, 5.5, 102.2, 103.7, 97.6, 102.4, 89.2, 74.3, 30.6, 46.9, 166.4]
[2, 85.0, 5.234000206, 1.153601766, 1.152400255, 0.540775776, 0.398155838, 0.04526934, 0.180987507, 86600.0, 9828.0, 118.9, 99.3, 23.3, 10.1, 1.3, 2.7, 53049.0, 0.7, 5438.7, 6.7, 49.9, 43.4, 9143.0, 8532.0, 611.0, 36.7, 14.2, 49.1, 5.2, 2.1, 74.6, 68.6, 31.4, 54.6, 1.6, 111.3, 77.0, 97.0, 3.9, 61.0, 6.0, 3.4, 2.6, 105.6, 107.4, 0, 0, 27.5, 23.6, 16.8, 13.5, 623.3]
[3, 41.0, 6.086999893, 1.488412261, 1.323110461, 0.653133035, 0.536746919, 0.172668487, 0.25704217, 771.0, 1493.0, 1963.9, 168.3, 19.7, 4.6, 2.0, 51.1, 31126.0, 2.9, 22600.2, 0.3, 40.7, 59.0, 12892.0, 14749.0, -1856.0, 1.0, 33.4, 65.6, 1.3, 2.1, 77.5, 75.6, 6.9, 88.8, 1.7, 185.3, 93.5, 36.0, 23.0, 413.0, 5.0, 0.9, 2.7, 101.8, 100.6, 101.9, 102.4, 59.4, 30.9, 7.5, 0.8, 0.4]
[1, 110.0, 4.607999802, 0.586682975, 0.735131741, 0.533241034, 0.478356659, 0.172255352, 0.123717859, 147570.0, 164670.0, 1265.0, 101.7, 28.4, 7.3, 1.2, 0.9, 194466.0, 6.6, 1207.9, 15.5, 28.1, 56.3, 36031.0, 52624.0, -16593.0, 40.6, 19.1, 40.3, 4.0, 2.2, 72.9, 69.8, 33.3, 34.3, 3.6, 83.4, 14.4, 151.0, 0.5, 11.0, 2.8, 0.4, 1.9, 125.1, 116.0, 67.4, 59.8, 11.4, 15.4, 20.3, 11.0, 233.0]
[2, 67.0, 5.568999767, 1.15655756, 1.444945216, 0.637714267, 0.295400262, 0.155137509, 0.156313822, 207600.0, 9468.0, 46.7, 87.0, 16.7, 21.3, 0, 11.4, 54609.0, -3.9, 5750.8, 7.5, 38.9, 53.6, 23414.0, 27464.0, -4050.0, 9.6, 32.0, 58.4, 0.5, 1.6, 77.7, 66.5, 3.6, 76.7, 0, 123.6, 62.2, 25.0, 6.7, 122.0, 5.7, 4.1, 4.9, 101.3, 101.4, 106.4, 107.8, 100.7, 75.9, 34.5, 42.5, 7.9]
[7, 17.0, 6.890999794, 1.463780761, 1.462312698, 0.818091869, 0.539770722, 0.231503338, 0.251343131, 30528.0, 11429.0, 377.5, 97.3, 17.1, 24.6, 0.6, 12.3, 455107.0, 1.5, 40277.8, 0.7, 22.2, 77.1, 398033.0, 372713.0, 25321.0, 1.2, 21.2, 77.6, 8.3, 1.8, 83.0, 78.0, 3.5, 97.9, 0.5, 115.7, 85.1, 37.0, 8.3, 196.0, 10.6, 3.0, 6.6, 104.2, 104.2, 177.7, 156.4, 85.4, 65.0, 38.0, 22.6, 63.8]
[5, 50.0, 5.955999851, 0.907975316, 1.081417799, 0.450191766, 0.547509372, 0.240015641, 0.096581072, 22966.0, 375.0, 16.4, 99.2, 31.4, 6.2, 2.2, 15.0, 1721.0, 1.2, 4789.4, 14.6, 18.5, 66.9, 246.0, 952.0, -706.0, 16.1, 15.9, 67.9, 11.5, 2.6, 72.7, 67.2, 14.3, 44.0, 1.9, 48.9, 41.6, 117.0, 1.4, 36.0, 5.8, 0, 6.4, 110.4, 115.8, 81.8, 79.8, 28.7, 17.9, 9.4, 60.1, 3.1]
[4, 143.0, 3.657000065, 0.431085408, 0.435299844, 0.209930211, 0.425962776, 0.207948461, 0.060929015, 114763.0, 11176.0, 99.1, 99.5, 42.7, 5.0, 2.8, 2.3, 8476.0, 5.2, 779.1, 23.2, 24.9, 51.9, 410.0, 2630.0, -2220.0, 43.2, 10.2, 46.6, 1.0, 5.2, 61.4, 58.5, 67.7, 44.0, 3.7, 85.6, 6.8, 88.0, 0.6, 17.0, 4.6, 0.1, 4.4, 123.7, 134.2, 46.8, 66.7, 8.4, 22.4, 7.2, 38.7, 0.8]
[1, 97.0, 5.011000156, 0.885416389, 1.340126514, 0.495879292, 0.501537681, 0.474054545, 0.17338039, 38394.0, 808.0, 21.2, 113.1, 26.5, 7.3, 1.6, 6.6, 2074.0, 5.2, 2677.1, 17.2, 43.9, 38.8, 616.0, 1688.0, -1072.0, 56.6, 9.7, 33.7, 2.4, 2.2, 68.9, 68.6, 30.5, 38.6, 3.7, 87.1, 39.8, 71.0, 1.3, 82.0, 3.6, 0.3, 7.4, 96.9, 96.6, 87.1, 81.4, 9.2, 12.6, 8.5, 72.0, 0]
[5, 58.0, 5.822999954, 0.833756566, 1.227619052, 0.47363025, 0.558732927, 0.225560725, 0.060477726, 1098581.0, 11052.0, 10.2, 100.2, 31.6, 9.5, 1.6, 1.3, 32998.0, 4.8, 3076.8, 12.6, 31.0, 56.5, 6969.0, 8374.0, -1405.0, 29.5, 21.1, 49.4, 3.8, 3.0, 70.2, 65.3, 42.9, 68.5, 2.3, 92.2, 45.1, 231.0, 1.9, 32.0, 6.3, 0.5, 7.3, 95.7, 98.5, 85.7, 87.1, 0, 0, 53.1, 50.8, 0.8]
[2, 90.0, 5.18200016, 0.982409418, 1.069335938, 0.705186307, 0.204403177, 0.328867495, 0.0, 51209.0, 3507.0, 68.8, 96.4, 14.1, 23.4, -1.0, 0.9, 16251.0, 3.1, 4265.0, 7.3, 26.5, 66.2, 5327.0, 9130.0, -3803.0, 18.0, 30.4, 51.7, 25.4, 1.3, 78.8, 73.7, 7.6, 39.8, 0.1, 90.2, 65.1, 91.0, 5.8, 85.0, 9.6, 1.9, 0, 0, 0, 0, 0, 0, 0, 21.4, 42.7, 157.6]
[4, 142.0, 3.766000032, 1.122094154, 1.221554995, 0.341755509, 0.505196333, 0.099348448, 0.098583199, 582000.0, 2292.0, 4.0, 97.7, 31.4, 6.4, 1.8, 7.1, 14391.0, -0.3, 6360.6, 2.4, 33.4, 64.2, 7321.0, 6103.0, 1218.0, 25.7, 14.9, 59.4, 18.6, 2.9, 66.1, 59.8, 35.2, 57.4, 1.3, 169.0, 27.5, 28.0, 3.2, 44.0, 5.4, 0.4, 0, 105.8, 109.4, 0, 0, 27.7, 19.2, 9.5, 19.3, 2.8]
[5, 22.0, 6.635000229, 1.10735321, 1.431306005, 0.616552353, 0.437453747, 0.162349895, 0.111092761, 8515767.0, 209288.0, 25.0, 96.6, 21.7, 12.6, 0.9, 0.3, 1772591.0, -3.8, 8528.3, 5.2, 22.7, 72.0, 185235.0, 137552.0, 47683.0, 15.2, 21.5, 63.2, 12.4, 1.8, 78.4, 71.0, 15.8, 85.7, 1.2, 126.6, 59.1, 990.0, 2.6, 61.0, 8.3, 1.9, 6.0, 113.8, 116.8, 102.2, 97.2, 59.3, 42.4, 10.7, 59.2, 41.1]
[2, 105.0, 4.714000225, 1.161459088, 1.434379458, 0.70821768, 0.289231718, 0.113177694, 0.011051531, 111002.0, 7085.0, 65.3, 94.6, 14.2, 27.7, -0.6, 1.4, 48953.0, 3.0, 6846.8, 5.1, 27.6, 67.2, 26088.0, 28875.0, -2787.0, 6.5, 29.4, 64.1, 8.1, 1.5, 77.8, 70.8, 8.3, 73.9, -0.3, 129.3, 56.7, 104.0, 5.9, 103.0, 8.4, 4.0, 4.1, 96.7, 97.7, 97.4, 100.5, 82.9, 65.4, 19.2, 35.1, 33.7]
[4, 134.0, 4.032000065, 0.350227714, 1.043280005, 0.215844259, 0.324367851, 0.250864685, 0.120328106, 272967.0, 19193.0, 70.2, 99.5, 45.2, 3.9, 3.0, 3.9, 11065.0, 4.1, 611.1, 34.5, 21.8, 43.7, 2019.0, 3699.0, -1680.0, 80.0, 4.9, 15.1, 2.9, 5.6, 59.3, 58.0, 64.8, 29.9, 5.9, 80.6, 11.4, 31.0, 0.1, 9.0, 5.0, 0, 4.1, 86.1, 89.9, 32.2, 35.1, 3.8, 7.3, 11.0, 19.8, 32.7]
[4, 154.0, 2.904999971, 0.091622569, 0.629793584, 0.151610792, 0.059900753, 0.204435185, 0.084147945, 27830.0, 10864.0, 423.1, 96.9, 45.0, 4.4, 3.0, 2.6, 2735.0, -4.1, 244.6, 36.3, 13.9, 49.8, 123.0, 625.0, -502.0, 91.1, 2.6, 6.3, 1.7, 6.0, 58.0, 54.2, 77.8, 12.1, 5.7, 46.2, 4.9, 61.0, 0, 6.0, 7.5, 0, 5.4, 124.5, 123.1, 40.5, 44.5, 2.4, 7.7, 36.4, 10.6, 103.2]
[8, 129.0, 4.168000221, 0.601765096, 1.006238341, 0.429783404, 0.633375823, 0.385922968, 0.068105951, 181035.0, 16005.0, 90.7, 95.3, 31.3, 7.1, 1.6, 0.5, 18050.0, 7.0, 1158.7, 28.2, 29.4, 42.3, 13204.0, 15313.0, -2109.0, 42.4, 19.6, 38.0, 0.3, 2.7, 69.6, 65.5, 29.9, 20.7, 2.6, 133.0, 19.0, 255.0, 0.4, 17.0, 5.7, 0.2, 1.9, 116.2, 117.1, 0, 0, 11.8, 14.3, 20.3, 54.3, 0.3]
[4, 107.0, 4.695000172, 0.564305365, 0.946018219, 0.132892117, 0.430388749, 0.236298457, 0.051306631, 475650.0, 24054.0, 50.9, 100.2, 42.7, 4.8, 2.7, 1.6, 28416.0, 5.8, 1217.3, 22.7, 28.3, 49.1, 2130.0, 4899.0, -2768.0, 61.8, 8.7, 29.5, 4.6, 5.0, 57.7, 55.1, 67.5, 54.4, 3.6, 71.8, 20.7, 775.0, 0.3, 14.0, 4.1, 0, 3.0, 110.7, 123.5, 53.5, 62.6, 15.2, 19.7, 31.1, 40.3, 544.9]
[9, 7.0, 7.315999985, 1.479204416, 1.481348991, 0.834557652, 0.611100912, 0.435539722, 0.287371516, 9984670.0, 36624.0, 4.0, 98.5, 16.0, 23.5, 1.0, 21.8, 1552808.0, 0.9, 43205.6, 1.8, 28.6, 69.6, 388911.0, 402954.0, -14043.0, 2.1, 19.5, 78.4, 7.1, 1.6, 83.8, 79.7, 4.7, 81.8, 1.2, 81.9, 88.5, 122.0, 15.1, 324.0, 10.4, 2.5, 5.3, 101.1, 100.1, 110.0, 109.8, 0, 0, 26.3, 38.2, 155.8]
[5, 155.0, 2.693000078, 0.0, 0.0, 0.018772686, 0.270842046, 0.280876487, 0.056565076, 622984.0, 4659.0, 7.5, 97.3, 43.2, 5.5, 0.4, 1.7, 1633.0, 4.8, 333.2, 34.9, 24.8, 40.4, 213.0, 147.0, 66.0, 72.2, 4.3, 23.4, 6.9, 5.1, 51.0, 47.8, 93.5, 40.0, 2.6, 20.4, 4.6, 60.0, 0.1, 5.0, 4.2, 0, 1.2, 79.8, 107.3, 11.8, 23.0, 1.5, 4.1, 8.6, 35.6, 470.5]
[4, 36.0, 6.356999874, 1.070622325, 1.402182937, 0.595027924, 0.477487415, 0.149014473, 0.046668742, 1141748.0, 49066.0, 44.2, 96.8, 23.5, 11.6, 1.0, 0.3, 292080.0, 3.1, 6056.1, 6.8, 34.0, 59.2, 31045.0, 44831.0, -13786.0, 13.5, 16.6, 69.9, 10.5, 1.9, 77.4, 70.2, 17.9, 76.4, 1.7, 115.7, 55.9, 835.0, 1.8, 31.0, 7.2, 0, 4.5, 111.6, 115.4, 101.5, 94.8, 59.9, 51.5, 18.7, 52.8, 7127.0]
[4, 124.0, 4.290999889, 0.808964252, 0.832044363, 0.289957434, 0.435025871, 0.120852128, 0.079618134, 342000.0, 5261.0, 15.4, 100.1, 42.3, 5.2, 2.6, 8.5, 8493.0, 1.2, 1838.1, 4.7, 70.0, 25.3, 2540.0, 9793.0, -7253.0, 40.7, 25.8, 33.5, 11.5, 4.9, 64.1, 61.0, 46.5, 65.4, 3.2, 111.7, 7.6, 134.0, 0.7, 24.0, 5.2, 0, 0, 114.8, 107.0, 50.6, 58.4, 8.3, 11.1, 7.4, 65.4, 54.9]
[5, 12.0, 7.078999996, 1.109706283, 1.416403651, 0.759509265, 0.58013165, 0.214613229, 0.100106589, 51100.0, 4906.0, 96.1, 100.1, 21.6, 13.6, 1.1, 8.8, 52958.0, 3.7, 11015.0, 5.1, 21.5, 73.4, 9908.0, 15322.0, -5414.0, 11.6, 19.1, 69.3, 8.6, 1.9, 81.7, 76.7, 9.3, 76.8, 2.7, 150.7, 59.8, 340.0, 1.6, 44.0, 9.3, 1.2, 7.2, 109.5, 110.1, 125.6, 120.7, 60.9, 46.6, 35.1, 53.4, 10.1]

---------STRING and REGION(2. STLPEC) DICTIONARY----------
- {'Southern Asia': 1, 'Central and Eastern Europe': 2, 'Middle East and Northern Africa': 3, '-': 0, 'Sub-Saharan Africa': 4, 'Latin America and Caribbean': 5, 'Australia and New Zealand': 6, 'Western Europe': 7, '~0.0': 0, 'Southeastern Asia': 8, 'North America': 9}

---------NORMALIZACIA VSETKYCH DAT----------
- [[0.         0.90540541 0.23815701 ... 0.44662309 0.01825843 0.21230532]
 [0.125      0.68918919 0.42202034 ... 0.34204793 0.38483146 0.00123474]
 [0.25       0.31081081 0.68764876 ... 0.53159041 0.         0.01400309]
 ...
 [0.375      0.19594595 0.79255892 ... 0.25054466 0.73033708 1.        ]
 [0.375      0.79054054 0.34566296 ... 0.0043573  0.90730337 0.0077031 ]
 [0.5        0.03378378 0.94873459 ... 0.60784314 0.73876404 0.00141715]]

---------EUKLIDOVA VZDIALENOST----------
- [[0.         2.47304931 2.34342924 1.9850071  3.24805177 2.47006376
  4.22249135 3.92066052 2.3810488  3.81036694 2.09179475 3.21230268
  4.11282194 2.29144062 1.43082434 2.32237979 2.27448173 3.11072365
  2.15743443 3.55212627 3.20019615 1.31763687 1.18007902 2.22003953
  1.61098061 4.24263751 1.76843983 2.95360521 2.07023181 3.14069281]
 [2.47304931 0.         1.62245678 2.86868693 1.79741001 0.90055417
  2.97548226 2.39796663 1.66125076 2.87198523 1.88480149 1.71339597
  2.75047753 1.74898391 2.32380276 1.95770946 1.90342362 2.11731519
  2.0056742  2.66424272 1.41499467 2.64384943 3.03935239 2.11991433
  2.37209124 3.31478375 2.9497951  1.8484904  2.40322492 1.72485724]
 [2.34342924 1.62245678 0.         2.19256133 1.79166927 1.67223372
  2.9502016  2.65258082 1.69536685 2.58881235 1.77411426 2.07256033
  2.83445863 1.8917817  2.31213681 2.3641561  1.82172821 2.4580963
  1.86680959 2.68507868 2.02439927 2.60221132 3.06294532 2.26941442
  2.25660154 3.14330511 3.08187216 1.89859778 2.04710078 1.89751757]
 [1.9850071  2.86868693 2.19256133 0.         3.17650108 2.78081108
  4.3060668  3.98734412 2.4733519  3.72046777 2.37325654 3.20687791
  4.18653405 2.50032727 1.85436072 2.67726009 2.32258084 3.26869149
  2.14190544 3.57938125 3.24440953 2.15672081 2.45687391 2.30563607
  1.86044242 4.29054026 2.37773079 2.99906111 1.61170407 3.25776646]
 [3.24805177 1.79741001 1.79166927 3.17650108 0.         1.85476766
  2.10232246 1.70981038 2.02253113 2.60204924 2.56321916 1.41789779
  1.99278929 2.11344182 2.99963838 2.74600027 2.05650804 2.84795979
  2.47732688 2.14796788 1.51676559 3.4022479  3.81700334 2.83640657
  2.89422758 2.78543835 3.85453154 1.80811459 3.0079534  1.37707577]
 [2.47006376 0.90055417 1.67223372 2.78081108 1.85476766 0.
  3.18390071 2.59803141 1.47417772 2.88625828 1.9236057  1.7726222
  2.92587965 1.86170939 2.30771097 2.17206014 2.09819266 2.04232137
  1.76918877 2.74505214 1.36266009 2.64465234 3.08359344 2.26199713
  2.41586809 3.44811176 2.86727727 2.00513577 2.34970122 2.06689396]
 [4.22249135 2.97548226 2.9502016  4.3060668  2.10232246 3.18390071
  0.         1.67596504 3.19226933 2.87026701 3.66066758 2.58706165
  1.8372716  3.10056267 4.07161205 3.48221855 3.20077949 3.63115607
  3.6178507  2.45894361 2.73200771 4.35594244 4.77149263 3.74952507
  3.87761515 2.004967   4.83385502 2.69145498 4.04287444 2.30324724]
 [3.92066052 2.39796663 2.65258082 3.98734412 1.70981038 2.59803141
  1.67596504 0.         2.5761024  2.77617106 3.33829307 1.7993325
  1.41273999 2.62260669 3.73154483 3.10918465 2.75440182 2.94885227
  3.1235905  2.61693657 1.88479636 4.07000307 4.449119   3.28236069
  3.71253126 2.24569312 4.50395247 2.42436238 3.62793285 1.70122169]
 [2.3810488  1.66125076 1.69536685 2.4733519  2.02253113 1.47417772
  3.19226933 2.5761024  0.         2.64715927 1.90442773 1.94388651
  3.05381689 1.88997261 2.25512819 2.02154509 1.93714398 2.26167129
  1.52104046 2.77800639 1.98085757 2.45922797 2.95342661 2.06856348
  2.28632437 3.27522107 2.87059027 2.10454668 2.04283518 2.19107172]
 [3.81036694 2.87198523 2.58881235 3.72046777 2.60204924 2.88625828
  2.87026701 2.77617106 2.64715927 0.         3.00872289 2.70759036
  2.94778443 2.86077646 3.56573271 3.09212215 3.06619435 3.43183141
  2.96214606 3.43621762 2.86353831 3.85421866 4.36415703 3.44074903
  3.63627468 3.20260169 4.3561301  2.97174565 3.35828613 2.68496564]
 [2.09179475 1.88480149 1.77411426 2.37325654 2.56321916 1.9236057
  3.66066758 3.33829307 1.90442773 3.00872289 0.         2.72383562
  3.54647048 1.9834046  1.79233612 1.95420774 1.97259253 2.74458601
  1.99895299 3.02907874 2.58709919 2.07078878 2.61248007 1.82818298
  1.90790373 3.69456749 2.47188794 2.35787686 2.13058798 2.51859148]
 [3.21230268 1.71339597 2.07256033 3.20687791 1.41789779 1.7726222
  2.58706165 1.7993325  1.94388651 2.70759036 2.72383562 0.
  2.31514945 2.26094668 3.09902517 2.59065804 2.33243433 2.68661121
  2.55098325 2.59267836 1.19569451 3.47003909 3.73456824 2.9217817
  3.10360527 3.14141302 3.81328139 2.13411807 2.90976393 1.82601481]
 [4.11282194 2.75047753 2.83445863 4.18653405 1.99278929 2.92587965
  1.8372716  1.41273999 3.05381689 2.94778443 3.54647048 2.31514945
  0.         2.91490765 3.95580558 3.45416192 2.96614555 3.43588091
  3.47203621 2.65533155 2.36933345 4.2921728  4.60697762 3.74459856
  3.93348166 2.06901475 4.72464202 2.73857194 3.95376017 2.08038228]
 [2.29144062 1.74898391 1.8917817  2.50032727 2.11344182 1.86170939
  3.10056267 2.62260669 1.88997261 2.86077646 1.9834046  2.26094668
  2.91490765 0.         1.84199534 1.58419809 1.39881194 2.52073761
  1.85672964 2.51885879 2.251022   2.29783867 2.82431235 1.85480697
  1.99003098 3.0973647  2.74321906 1.78574699 2.09823696 1.5933383 ]
 [1.43082434 2.32380276 2.31213681 1.85436072 2.99963838 2.30771097
  4.07161205 3.73154483 2.25512819 3.56573271 1.79233612 3.09902517
  3.95580558 1.84199534 0.         1.87931192 1.94526224 3.22854216
  1.92821902 3.41273326 2.99015945 1.14004257 1.77118175 1.58068318
  1.14129061 4.10664697 1.45764161 2.67824491 1.64005304 2.83554173]
 [2.32237979 1.95770946 2.3641561  2.67726009 2.74600027 2.17206014
  3.48221855 3.10918465 2.02154509 3.09212215 1.95420774 2.59065804
  3.45416192 1.58419809 1.87931192 0.         1.67598825 2.78408008
  2.31771206 3.08351249 2.65360755 2.01362691 2.75894127 1.76989605
  1.95798125 3.47741752 2.60104379 2.33591599 2.06081703 2.26091689]
 [2.27448173 1.90342362 1.82172821 2.32258084 2.05650804 2.09819266
  3.20077949 2.75440182 1.93714398 3.06619435 1.97259253 2.33243433
  2.96614555 1.39881194 1.94526224 1.67598825 0.         2.56821707
  2.15259219 2.709666   2.34060137 2.26263763 2.70749775 1.80924547
  1.72308434 3.12003808 2.74031594 1.94933148 2.13233619 1.62471689]
 [3.11072365 2.11731519 2.4580963  3.26869149 2.84795979 2.04232137
  3.63115607 2.94885227 2.26167129 3.43183141 2.74458601 2.68661121
  3.43588091 2.52073761 3.22854216 2.78408008 2.56821707 0.
  2.37123298 3.25094012 2.17519382 3.34060436 3.80215288 2.68119132
  3.19141216 3.43252101 3.40889554 2.70402669 2.95190604 2.66445861]
 [2.15743443 2.0056742  1.86680959 2.14190544 2.47732688 1.76918877
  3.6178507  3.1235905  1.52104046 2.96214606 1.99895299 2.55098325
  3.47203621 1.85672964 1.92821902 2.31771206 2.15259219 2.37123298
  0.         2.97816739 2.36190107 2.27404913 2.79923683 1.88700821
  2.09072268 3.65248149 2.52501297 2.33714207 1.69694805 2.5187136 ]
 [3.55212627 2.66424272 2.68507868 3.57938125 2.14796788 2.74505214
  2.45894361 2.61693657 2.77800639 3.43621762 3.02907874 2.59267836
  2.65533155 2.51885879 3.41273326 3.08351249 2.709666   3.25094012
  2.97816739 0.         2.6114826  3.74073912 4.06121456 3.24289818
  3.22328014 2.74095348 4.10855262 2.20028849 3.3269121  2.28193528]
 [3.20019615 1.41499467 2.02439927 3.24440953 1.51676559 1.36266009
  2.73200771 1.88479636 1.98085757 2.86353831 2.58709919 1.19569451
  2.36933345 2.251022   2.99015945 2.65360755 2.34060137 2.17519382
  2.36190107 2.6114826  0.         3.44166124 3.81055238 2.78508858
  3.06693437 3.17569761 3.68945799 2.01099302 2.93463315 1.76420779]
 [1.31763687 2.64384943 2.60221132 2.15672081 3.4022479  2.64465234
  4.35594244 4.07000307 2.45922797 3.85421866 2.07078878 3.47003909
  4.2921728  2.29783867 1.14004257 2.01362691 2.26263763 3.34060436
  2.27404913 3.74073912 3.44166124 0.         1.33033277 1.81485364
  1.33215405 4.33425764 1.46343689 3.10793949 1.99675695 3.23290872]
 [1.18007902 3.03935239 3.06294532 2.45687391 3.81700334 3.08359344
  4.77149263 4.449119   2.95342661 4.36415703 2.61248007 3.73456824
  4.60697762 2.82431235 1.77118175 2.75894127 2.70749775 3.80215288
  2.79923683 4.06121456 3.81055238 1.33033277 0.         2.5266759
  1.90253983 4.73268132 1.8182118  3.58802    2.59910526 3.67971195]
 [2.22003953 2.11991433 2.26941442 2.30563607 2.83640657 2.26199713
  3.74952507 3.28236069 2.06856348 3.44074903 1.82818298 2.9217817
  3.74459856 1.85480697 1.58068318 1.76989605 1.80924547 2.68119132
  1.88700821 3.24289818 2.78508858 1.81485364 2.5266759  0.
  1.65920202 3.70717667 2.12218117 2.47696405 1.89586129 2.5612143 ]
 [1.61098061 2.37209124 2.25660154 1.86044242 2.89422758 2.41586809
  3.87761515 3.71253126 2.28632437 3.63627468 1.90790373 3.10360527
  3.93348166 1.99003098 1.14129061 1.95798125 1.72308434 3.19141216
  2.09072268 3.22328014 3.06693437 1.33215405 1.90253983 1.65920202
  0.         4.06878715 1.69569011 2.4302844  1.74226764 2.74524087]
 [4.24263751 3.31478375 3.14330511 4.29054026 2.78543835 3.44811176
  2.004967   2.24569312 3.27522107 3.20260169 3.69456749 3.14141302
  2.06901475 3.0973647  4.10664697 3.47741752 3.12003808 3.43252101
  3.65248149 2.74095348 3.17569761 4.33425764 4.73268132 3.70717667
  4.06878715 0.         4.72873525 3.12671067 4.0006735  2.74394519]
 [1.76843983 2.9497951  3.08187216 2.37773079 3.85453154 2.86727727
  4.83385502 4.50395247 2.87059027 4.3561301  2.47188794 3.81328139
  4.72464202 2.74321906 1.45764161 2.60104379 2.74031594 3.40889554
  2.52501297 4.10855262 3.68945799 1.46343689 1.8182118  2.12218117
  1.69569011 4.72873525 0.         3.47194752 2.20952846 3.7932666 ]
 [2.95360521 1.8484904  1.89859778 2.99906111 1.80811459 2.00513577
  2.69145498 2.42436238 2.10454668 2.97174565 2.35787686 2.13411807
  2.73857194 1.78574699 2.67824491 2.33591599 1.94933148 2.70402669
  2.33714207 2.20028849 2.01099302 3.10793949 3.58802    2.47696405
  2.4302844  3.12671067 3.47194752 0.         2.57806424 1.51911735]
 [2.07023181 2.40322492 2.04710078 1.61170407 3.0079534  2.34970122
  4.04287444 3.62793285 2.04283518 3.35828613 2.13058798 2.90976393
  3.95376017 2.09823696 1.64005304 2.06081703 2.13233619 2.95190604
  1.69694805 3.3269121  2.93463315 1.99675695 2.59910526 1.89586129
  1.74226764 4.0006735  2.20952846 2.57806424 0.         2.88147211]
 [3.14069281 1.72485724 1.89751757 3.25776646 1.37707577 2.06689396
  2.30324724 1.70122169 2.19107172 2.68496564 2.51859148 1.82601481
  2.08038228 1.5933383  2.83554173 2.26091689 1.62471689 2.66445861
  2.5187136  2.28193528 1.76420779 3.23290872 3.67971195 2.5612143
  2.74524087 2.74394519 3.7932666  1.51911735 2.88147211 0.        ]]

---------K MEANS----------
- [ 3  9  4 17 16  9 18  0  4 10 19  2  0  7 15 14  7  6 12  5  2  3 13 14 15 11 13  8  1 16]

Process finished with exit code 0
