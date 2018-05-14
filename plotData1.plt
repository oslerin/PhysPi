reset
set title "SHT1 Temperature and Humidity Plot"
set datafile separator ", "
set term jpeg size 800, 700
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set xrange [ * : * ]
set format x "%m-%d %H:%M:%S"
set xtics rotate by -45
set xtics nomirror
set ylabel "Temperature (C)"
set yrange[ * : * ]
set y2label "Humidity (%)"
set y2range[ * : * ]
set ytics nomirror
set y2tics
set output "data_1.jpg"
plot "log.dat" using 1:2 title "Temperature", "log.dat" using 1:3 title "Humidity"