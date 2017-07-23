

from pyspark import SparkConf, SparkContext
from datetime import datetime
import json
from operator import add
import os
import time
from constants import *

def secondToMin(sec):
	return time.strftime("%H:%M:%S", time.gmtime(sec))
def averageTime(type_,visits):
	# min_=int(min(visit_time,key=lambda item:item[1])[0])
    max_ =max(visits,key=lambda item:item[1])[1]
    min_=min(visits,key=lambda item:item[1])[1]
    
    return type_,secondToMin(max_-min_)

path=os.path.dirname(os.path.abspath(__file__))
ouptput_file=path+"/data.json"
def main(hdfs_uri):


	sc = SparkContext()
	events_rdd = sc.newAPIHadoopFile(
	    hdfs_uri,
	    'org.apache.avro.mapreduce.AvroKeyInputFormat',
	    'org.apache.avro.mapred.AvroKey',
	    'org.apache.hadoop.io.NullWritable',
	    keyConverter='io.divolte.spark.pyspark.avro.AvroWrapperToJavaConverter').map(lambda (k,v): k)

    
	events_rdd.cache()
	data=dict()
	total_event_count = events_rdd.count()
	data[VISITS]=total_event_count
	# Get the first event in our dataset (which isn't ordered yet).
	#an_event = events_rdd.take(1)

	# Find the session with the most events.


	distinct_events = events_rdd.map(lambda event: (event[EVENTYPE],1)).reduceByKey(add).collect()
	#.map(lambda event: (event['eventType'], event['timestamp'])) \
	# Simple function for rendering timestamps.

	# Print the results we accumulated, with some whitespace at the
	# front to separate this from the logging.
	distinct_events= dict(distinct_events)
	data[DISTINCT_EVENTS]=dict(distinct_events)

	unique_visits=events_rdd.map(lambda event:event[REMOTE_HOST],1).distinct().count()
	data[UNIQUE_VISITS]=unique_visits

	session_rdd=events_rdd.map(lambda event:(event[REMOTE_HOST],event[TIMESTAMP]))
	
	avg=session_rdd.groupBy(lambda e:e[0]).map(lambda e:averageTime(e[0],e[1])).collect()
	data[AVERAGE_VISIT]=dict(avg)

	with open(ouptput_file,"w") as h:
	    h.write(json.dumps(data, indent=2))
	    h.close()
if __name__ == "__main__":
    import sys
    if (len(sys.argv) >= 2):
        main(*sys.argv[1:])
    else:
        print >> sys.stderr, "Usage: spark-submit [...] analyse.py PATH_TO_DIVOLTE_LOGS"
