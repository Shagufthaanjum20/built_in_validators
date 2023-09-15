from django import templater
register=template.library()
#def swap(value):
   # return value.swapcase()
   #register.filter('swapcase',swap)
def count(value):
    return value.count()
    register.filter('count'.count)

