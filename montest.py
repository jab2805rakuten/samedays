#!/usr/local/bin/python3
from calendar import Calendar 
import argparse



def get_mondays(year, month, day="Monday"):
   obj = Calendar()
   for day_of_week in obj.itermonthdates(year, month):
       prin_day = day_of_week.strftime("%A %d %B")
       if day in prin_day:
           print (prin_day)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-y', "--year")
  parser.add_argument('-m', "--month")
  parser.add_argument('-d', "--day")
  args = parser.parse_args()


  if args.year and args.month:
     get_mondays(int(args.year), int(args.month))
  
if __name__ == "__main__":
   main()
   
