#! /usr/bin/python

f = open("tasks.txt")
lines = f.readlines()
f.close()
for line in lines:
	line = line.strip()
	parseBuffer = line
	print parseBuffer

	quoteStart = parseBuffer.find('"')
	parseBuffer = parseBuffer[quoteStart+1:]
	quoteEnd = parseBuffer.find('"')
	#print quoteStart, quoteEnd
	userToken = parseBuffer[0:quoteEnd]
	parseBuffer = parseBuffer[quoteEnd+1:]
	print "'"+userToken+"'"

	commaStart = parseBuffer.find(',')
	parseBuffer = parseBuffer[commaStart+1:]
	quoteStart = parseBuffer.find('"')
	parseBuffer = parseBuffer[quoteStart+1:]
	quoteEnd = parseBuffer.find('"')
	taskToken = parseBuffer[0:quoteEnd]
	parseBuffer = parseBuffer[quoteEnd+1:]
	print "'"+taskToken+"'"

	commaStart = parseBuffer.find(',')
	parseBuffer = parseBuffer[commaStart+1:]
	tokens = parseBuffer.split(',')
	for token in tokens:
		token = token.strip()
		print "'"+token+"'"
