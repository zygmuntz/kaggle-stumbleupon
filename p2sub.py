"""
convert a predictions file to submission format using sampleSubmission.csv
usage: p2sub.py sampleSubmission.csv p.txt p.csv
"""

import sys
import csv
import json

print __doc__

sample_sub_file = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

s_f = open( sample_sub_file )
i_f = open( input_file )
o_f = open( output_file, 'wb' )

reader = csv.reader( s_f )
writer = csv.writer( o_f )

headers = reader.next()
writer.writerow( headers )

for line in reader:

	url_id = line[0]
	p = i_f.next().strip()
	writer.writerow( [ url_id, p ] )	

	
	