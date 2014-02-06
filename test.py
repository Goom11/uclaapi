from models import *

for course in Course.objects:
    print "course: %s, instructor: %s" % (course.name, course.instructor)
    for book in course.books:
        print "     title: %s, SKU: %s" % (book.title, book.SKU)
