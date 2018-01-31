class First:
    def __init__(self):
        print "first"

class Second:
    def __init__(self):
        print "second"
    def say(self):
        print('iam second')


class Third(First):
    def __init__(self):
        print "third"
    def say(self):
        print('iam third')

class Fourth(Third,Second):
    def __init__(self):
        # super(Fourth, self).__init__()
        Second.__init__(self)
        Third.__init__(self)
        print "that's it"


obj1=Fourth()
obj1.say()


# to handel maltiple inhertance 
# 1-for Second
#     class Fourth(Second, Third):
#     def __init__(self):
#         Second.__init__(self)
#         print "that's it"
# when make object of Fourth will redirect to seconed 
# then print 'second'


# 2-for Third
#     class Fourth(Second, Third):
#     def __init__(self):
#         Third.__init__(self)
#         print "that's it"
# when make object of Fourth will redirect to Third 
# then print 'Third'


# 3-for both 
#     class Fourth(Second, Third):
#     def __init__(self):
#         # super(Fourth, self).__init__()
#         Second.__init__(self)
#         Third.__init__(self)
#         print "that's it"
# when make object of Fourth will redirect to second and Third
# then print 'second' then 'third'




# to handel calling of the same name of function 

# 1- to call say function from second class
#        class Fourth(Second, Third):
# 
# the output of Fourth.say() will be = iam second


# 2- to call say function from third class
#         class Fourth(Third,Second)
# 
# the output of Fourth.say() will be = iam third




