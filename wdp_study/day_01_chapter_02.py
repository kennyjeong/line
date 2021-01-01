%pyspark
import re
import numpy as np

# Initialzation
# file to read
test_file_path="/user/fp10300/wbp_study/test.txt"
test_big_file_path="/user/fp10300/wbp_study/VS14MORT.txt.gz"

# path to upload file
upload_file_path="/user/fp10300/wbp_study/testChapter2.txt"

## delete file
URI = sc._gateway.jvm.java.net.URI
Path = sc._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem

fs = FileSystem.get(URI(upload_file_path), sc._jsc.hadoopConfiguration())
fs.delete(Path(upload_file_path))

# Create RDDs & Read RDD
# file_path="/user/fp10300/wbp_study/test.txt"

## Creating RDDs
# RDD 생성하는 법1: parallelize 사용
data = sc.parallelize([('Amber', 22), ('Alfred', 23), ('Skye',4), ('Albert', 12),('Amber', 9)])
print("[Creating RDD: use parallelize] ==> data.first : {0}, data.collect : {1}".format(data.first(), data.collect()))

# RDD 생성하는 법2: 파일 읽기, text.txt -> 30,000개
data_from_file = sc.textFile(test_big_file_path, 4)
print("[Creating RDD: use file] ==> data.first : ", data.first())
print("[Creating RDD: use file] ==> data_from_file.count() : ", data_from_file.count())


## Schema
# schema-less한 구조
data_heterogenous = sc.parallelize([ ('Ferrari', 'fast'), {'Porsche': 100000}, ['Spain','visited', 4504]]).collect()
print("[Scema: schema-less structure] ==> data_heterogenous[1]['Porsche'] :", data_heterogenous[1]['Porsche'])


## Reading from files
print("[Reading from files] ==> data_from_file.take(1) : ", data_from_file.take(1))

#Define Function
def extractInformation(row):
    selected_indices = [
         2,4,5,6,7,9,10,11,12,13,14,15,16,17,18,
         19,21,22,23,24,25,27,28,29,30,32,33,34,
         36,37,38,39,40,41,42,43,44,45,46,47,48,
         49,50,51,52,53,54,55,56,58,60,61,62,63,
         64,65,66,67,68,69,70,71,72,73,74,75,76,
         77,78,79,81,82,83,84,85,87,89
    ]

    '''
        Input record schema
        schema: n-m (o) -- xxx
            n - position from
            m - position to
            o - number of characters
            xxx - description
        1. 1-19 (19) -- reserved positions
        2. 20 (1) -- resident status
        3. 21-60 (40) -- reserved positions
        4. 61-62 (2) -- education code (1989 revision)
        5. 63 (1) -- education code (2003 revision)
        6. 64 (1) -- education reporting flag
        7. 65-66 (2) -- month of death
        8. 67-68 (2) -- reserved positions
        9. 69 (1) -- sex
        10. 70 (1) -- age: 1-years, 2-months, 4-days, 5-hours, 6-minutes, 9-not stated
        11. 71-73 (3) -- number of units (years, months etc)
        12. 74 (1) -- age substitution flag (if the age reported in positions 70-74 is calculated using dates of birth and death)
        13. 75-76 (2) -- age recoded into 52 categories
        14. 77-78 (2) -- age recoded into 27 categories
        15. 79-80 (2) -- age recoded into 12 categories
        16. 81-82 (2) -- infant age recoded into 22 categories
        17. 83 (1) -- place of death
        18. 84 (1) -- marital status
        19. 85 (1) -- day of the week of death
        20. 86-101 (16) -- reserved positions
        21. 102-105 (4) -- current year
        22. 106 (1) -- &
        23. 107 (1) -- manner of death
        24. 108 (1) -- manner of disposition
        25. 109 (1) -- autopsy
        26. 110-143 (34) -- reserved positions
        27. 144 (1) -- activity code
        28. 145 (1) -- place of injury
        29. 146-149 (4) -- ICD code
        30. 150-152 (3) -- 358 cause recode
        31. 153 (1) -- reserved position
        32. 154-156 (3) -- 113 cause recode
        33. 157-159 (3) -- 130 infant cause recode
        34. 160-161 (2) -- 39 cause recode
        35. 162 (1) -- reserved position
        36. 163-164 (2) -- number of entity-axis conditions
        37-56. 165-304 (140) -- list of up to 20 conditions
        57. 305-340 (36) -- reserved positions
        58. 341-342 (2) -- number of record axis conditions
        59. 343 (1) -- reserved position
        60-79. 344-443 (100) -- record axis conditions
        80. 444 (1) -- reserve position
        81. 445-446 (2) -- race
        82. 447 (1) -- bridged race flag
        83. 448 (1) -- race imputation flag
        84. 449 (1) -- race recode (3 categories)
        85. 450 (1) -- race recode (5 categories)
        86. 461-483 (33) -- reserved positions
        87. 484-486 (3) -- Hispanic origin
        88. 487 (1) -- reserved
        89. 488 (1) -- Hispanic origin/race recode
     '''

    record_split = re\
        .compile(
            r'([\s]{19})([0-9]{1})([\s]{40})([0-9\s]{2})([0-9\s]{1})([0-9]{1})([0-9]{2})' +
            r'([\s]{2})([FM]{1})([0-9]{1})([0-9]{3})([0-9\s]{1})([0-9]{2})([0-9]{2})' +
            r'([0-9]{2})([0-9\s]{2})([0-9]{1})([SMWDU]{1})([0-9]{1})([\s]{16})([0-9]{4})' +
            r'([YNU]{1})([0-9\s]{1})([BCOU]{1})([YNU]{1})([\s]{34})([0-9\s]{1})([0-9\s]{1})' +
            r'([A-Z0-9\s]{4})([0-9]{3})([\s]{1})([0-9\s]{3})([0-9\s]{3})([0-9\s]{2})([\s]{1})' +
            r'([0-9\s]{2})([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})' +
            r'([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})' +
            r'([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})' +
            r'([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})([A-Z0-9\s]{7})' +
            r'([A-Z0-9\s]{7})([\s]{36})([A-Z0-9\s]{2})([\s]{1})([A-Z0-9\s]{5})([A-Z0-9\s]{5})' +
            r'([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})' +
            r'([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})' +
            r'([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})' +
            r'([A-Z0-9\s]{5})([A-Z0-9\s]{5})([A-Z0-9\s]{5})([\s]{1})([0-9\s]{2})([0-9\s]{1})' +
            r'([0-9\s]{1})([0-9\s]{1})([0-9\s]{1})([\s]{33})([0-9\s]{3})([0-9\s]{1})([0-9\s]{1})')
    try:
        rs = np.array(record_split.split(row))[selected_indices]
    except:
        rs = np.array(['-99'] * len(selected_indices))
    return rs

#Call function
data_from_file_conv = data_from_file.map(extractInformation)
print("[Call Function] ==> data_from_file_conv.map(lambda row: row).take(1) : ", data_from_file_conv.map(lambda row: row).take(1))

#Transformation
## map()
data_2014 = data_from_file_conv.map(lambda row: int(row[16]))
print("[Transformation: map] ==> data_2014.take(10) : ", data_2014.take(10))

# can select more columns
data_2014_2 = data_from_file_conv.map(lambda row: (row[16], int(row[16])))
print("[Transformation: map] ==> more columns : data_2014_2.take(10) : ", data_2014_2.take(10))


## filter
data_filtered = data_from_file_conv.filter(lambda row: row[16] == '2014' and row[21] == '0')
print("[Transformation: filter] ==> data_filtered.count() : ", data_filtered.count())

## filter
data_filtered = data_from_file_conv.filter(lambda row: row[5] == 'F' and row[21] == '0')
print("[Transformation: filter] ==> data_filtered.count() : ", data_filtered.count())


## flatMap
data_2014_flat = data_from_file_conv.flatMap(lambda row: (row[16], int(row[16]) + 1))
print("[Transformation: flatMap] ==> data_2014_flat.take(10) : ", data_2014_flat.take(10))


## distinct
distinct_gender = data_from_file_conv.map( lambda row: row[5]).distinct().collect()
print("[Transformation: distinct] ==> distinct_gender : ", distinct_gender)


## sample
fraction = 0.1
data_sample = data_from_file_conv.sample(False, 0.1, 666)
print("[Transformation: sample] data_sample.take(1) ==> ", data_sample.take(1))
print("[Transformation: sample] 10% count ==> Original Count={0}, Sample Count={1}".format(data_from_file_conv.count(), data_sample.count()))
print("[Transformation: sample] 20% count ==> Original Count={0}, Sample Count={1}".format(data_from_file_conv.count(), data_from_file_conv.sample(False, 0.2, 666).count()))


## leftOuterJoin
rdd1 = sc.parallelize([('a', 1), ('b', 4), ('c',10)])
rdd2 = sc.parallelize([('a', 4), ('a', 1), ('b', '6'), ('d', 15)])
print("[Transformation: leftOuterJoin] rdd1.leftOuterJoin(rdd2) ==> ", rdd1.leftOuterJoin(rdd2).collect())


## join
print("[Transformation: leftOuterJoin] rdd1.join(rdd2) ==> ", rdd1.join(rdd2).collect())


## intersection
print("[Transformation: leftOuterJoin] rdd1.intersection(rdd2) ==> ", rdd1.intersection(rdd2).collect())


## repartition
print("[Transformation: repartition] before repartition len(rdd1.glom().collect()) ==> ", len(rdd1.glom().collect()))
print("[Transformation: repartition] after repartition len(rdd1.glom().collect()) ==> ", len(rdd1.repartition(4).glom().collect()))


data_from_file_conv = data_from_file.map(extractInformation)
print("[Call Function] ==> data_from_file_conv.map(lambda row: row).take(1) : ", data_from_file_conv.map(lambda row: row).take(1))

#Action


## take
print("[Action: take] data_from_file_conv.take(1) ==> ", data_from_file_conv.take(1))
print("[Action: take] data_from_file_conv.take(1) ==> ", data_from_file_conv.take(3))


## takeSample
print("[Action: takeSample] data_from_file_conv.takeSample(False, 1, 667) ==> ", data_from_file_conv.takeSample(False, 1, 667))
print("[Action: takeSample] data_from_file_conv.takeSample(False, 2, 667) ==> ", data_from_file_conv.takeSample(False, 2, 667))


## reduce
print("[Action: reduce] rdd1 ==> ", rdd1.collect())
print("[Action: reduce] rdd1.map(lambda row: row[1]).reduce(lambda x, y: x + y) ==> ", rdd1.map(lambda row: row[1]).reduce(lambda x, y: x + y))

data_reduce = sc.parallelize([1, 2, .5, .1, 5, .2], 1)
print("[Action: reduce] data_reduce ==> ", data_reduce.collect())
print("[Action: reduce] data_reduce.reduce(lambda x, y: x / y) ==> ", data_reduce.reduce(lambda x, y: x / y))
print("[Action: reduce] data_reduce.reduce(lambda x, y: x + y) ==> ", data_reduce.reduce(lambda x, y: x + y))
print("[Action: reduce] data_reduce.reduce(lambda x, y: x - y) ==> ", data_reduce.reduce(lambda x, y: x - y))


## reduceByKey
data_key = sc.parallelize([('a', 4),('b', 3),('c', 2),('a', 8),('d', 2),('b', 1),('d', 3)],4)
print("[Action: reduceByKey] data_key ==> ", data_key.collect())
print("[Action: reduceByKey] data_key.reduceByKey(lambda x, y: x + y).collect() ==> ", data_key.reduceByKey(lambda x, y: x + y).collect())


## count
print("[Action: count] data_reduce.count() ==> ", data_reduce.count())
print("[Action: count] data_key.countByKey().items() ==> ", data_key.countByKey().items())


## saveAsText
print("[Action: saveAsText] data_key ==> ", data_key.collect())
data_key.saveAsTextFile(upload_file_path)

def parseInput(row):
    import re

    pattern = re.compile(r'\(\'([a-z])\', ([0-9])\)')
    row_split = pattern.split(row)

    return (row_split[1], int(row_split[2]))

data_key_reread = sc.textFile('/user/fp10300/wbp_study/testChapter2.txt').map(parseInput)
print("[Action: saveAsText] data_key_reread.collect() ==> ", data_key_reread.collect())


## foreach
def f(x):
    print(x)

print("[Action: foreach] data_key.foreach(f) ==> ")
data_key.foreach(f)


