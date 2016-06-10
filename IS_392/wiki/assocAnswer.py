import os
from lxml.html.clean import Cleaner
import re
from collections import Counter
import csv
import sys
import itertools

csv.field_size_limit(sys.maxsize)

def dictionary_write(hash, filename):
	writer = csv.writer(open(str(filename)+'.csv', 'wb'))
	for key, value in hash.items():
   		writer.writerow([key, value])

def dictionary_read(filename):
	reader = csv.reader(open(str(filename)+'.csv', 'rb'))
	return dict(reader)


def association():
	sup = .97
	conf = .8
	print "obh"
	docAmount = 596.0

	first = dictionary_read("frequencies")
	second = {}
	third = {}
	thirdOne= {}
	fourth = {}
	final = {}
	seen = []
	answer = {}
	count = 0
	for y in first:
		fSupport = len(eval(first[y]))/float(docAmount)
		if fSupport >= sup:
			second[y]= eval(first[y])
	print second
	print len(second)

	sec = list(itertools.combinations(second, 2))
	print sec
	for z in sec:
		matches = 0
		x = z[0]
		y = z[1]
		for a in zip(sorted(eval(first[x])), sorted(eval(first[y]))):
			#for b in eval(first[y]):
			#if a in eval(first[y]):
			if a[0] == a[1]:
			#print x+","+y
				matches += 1
			#break;
			#print(len(third))
			#if len(third) > 3:
				#break

		if matches/docAmount >= sup:
			#print x+","+y+":"+str(matches/docAmount)
			if x < y:
				third[x+","+y] = matches/docAmount
			else:
				third[y+","+x] = matches/docAmount
	print third
	print len(third)
	print "boy"
	for x in third:
		a = x.split(",")
		thirdOne[a[0]] = 1
		thirdOne[a[1]] = 2

	thr = list(itertools.combinations(thirdOne, 3))
	print thr
	for x in thr:
		matches = 0
		for m in zip(sorted(eval(first[x[0]])), sorted(eval(first[x[1]])), sorted(eval(first[x[2]]))):
			if m[0] == m[1] and m[1] == m[2] and m[0] == m[2]:
				print str(x)
				matches += 1
		if matches/docAmount >= sup:
			print str(x)+","+str(matches/docAmount)
			fourth[x] = matches/docAmount

	print fourth
	print len(fourth)
	for a in fourth:
		x = a[0]
		y = a[1]
		z = a[2]
		print a
		#support = rule(first,x,y,z)/float(docAmount)
		confidence = ruler(first,x,y,z)
		if confidence >= conf:
			if x < y:
				final[x+y+z] ="{"+x+", "+y+"} => {"+z+"}; support="+str(fourth[a])+", confidence="+str(confidence)
			else:
				final[y+x+z] = "{"+y+", "+x+"} => {"+z+"}; support="+str(fourth[a])+", confidence="+str(confidence)

	return final

def ruler(all, o,t,th):
	match = 0
	denom = 0
	for m in zip(sorted(eval(all[o])),sorted(eval(all[t])),sorted(eval(all[th]))):
		if m[0] == m[1]:
			denom += 1
		if m[0] == m[1] and m[1] == m[2] and m[0] == m[2]:
			match += 1
	try:
		return match/float(denom)
	except:
		return "bad"
