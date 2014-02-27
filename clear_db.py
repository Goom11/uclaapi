from models import *
import sys

def main():

    if len (sys.argv) is 1:
        print "need moar args"
        return
    
    if 'hours' in sys.argv:
        for hour in Hour.objects:
            print "deleting hour object"
            hour.delete()

if __name__ == "__main__":
            main()
