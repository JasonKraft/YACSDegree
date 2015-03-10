import django

def main():
    print "Hello World! This is an experimental string detailing the current Django Version!"
    print "My version of Django currently is: " + django.get_version()
main()