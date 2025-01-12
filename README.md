# samedays


jeffrey@jabs-MacBook-Pro month % cat -n montest.py        
     1	#!/usr/local/bin/python3
     2	from calendar import Calendar 
     3	import argparse
     4	
     5	
     6	
     7	def get_mondays(year, month, day="Monday"):
     8	   obj = Calendar()
     9	   for day_of_week in obj.itermonthdates(year, month):
    10	       prin_day = day_of_week.strftime("%A %d %B")
    11	       if day in prin_day:
    12	           print (prin_day)
    13	
    14	def main():
    15	  parser = argparse.ArgumentParser()
    16	  parser.add_argument('-y', "--year")
    17	  parser.add_argument('-m', "--month")
    18	  parser.add_argument('-d', "--day")
    19	  args = parser.parse_args()
    20	
    21	
    22	  if args.year and args.month:
    23	     get_mondays(int(args.year), int(args.month))
    24	  
    25	if __name__ == "__main__":
    26	   main()
    27	   
jeffrey@jabs-MacBook-Pro month % ./montest.py --help      
usage: montest.py [-h] [-y YEAR] [-m MONTH] [-d DAY]

options:
  -h, --help         show this help message and exit
  -y, --year YEAR
  -m, --month MONTH
  -d, --day DAY
jeffrey@jabs-MacBook-Pro month % ./montest.py -y 2025 -m 1
Monday 30 December
Monday 06 January
Monday 13 January
Monday 20 January
Monday 27 January
jeffrey@jabs-MacBook-Pro month % cal 
    January 2025      
Su Mo Tu We Th Fr Sa  
          1  2  3  4  
 5  6  7  8  9 10 11  
12 13 14 15 16 17 18  
19 20 21 22 23 24 25  
26 27 28 29 30 31     



