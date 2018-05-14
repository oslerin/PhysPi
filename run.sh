#!/bin/bash

python2 2sht.py >/dev/null 2>&1 &

while true
do
	sleep 60
	python2 2shtplot.py
	gnuplot plotData1.plt >/dev/null 2>&1
	gnuplot plotData2.plt >/dev/null 2>&1
	sed 's/ /,/' log.dat > table.dat
	mv -f data_1.jpg data_2.jpg table.dat /var/www/html
done

