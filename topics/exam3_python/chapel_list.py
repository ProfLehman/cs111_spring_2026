"""
# creating empty lists

# huid (huntington id)
# huid = [] #empty
# credit = [] #empty

huid = ["s222", "s333"] #two entries
credit = [32, 25] 

huid.append("s111")
credit.append( 28 )

print( "HU id: ", huid )
print( "Chapel Credits: ", credit )

# use sentinel loop to add additional students
new_id = input('Enter HUID "Done" to quit: ')

while new_id != "Done":

    # add huid to list
    huid.append( new_id )
    
    # ask for chapels and add to credit list
    new_credit = int( input("Enter #chapels: ")  )
    credit.append( new_credit )
    
    new_id = input('Enter HUID "Done" to quit: ')
    # go up to while

print()
print( "HU id: ", huid )
print( "Chapel Credits: ", credit )
"""

huid =  ['s222', 's333', 's111', 's444', 's555', 's666', 's777', 's888', 's999']
credit = [32, 25, 18, 33, 37, 18, 15, 14, 26]

print()
print( "HU id: ", huid )
print( "Chapel Credits: ", credit )
print( )

print( "Number of students: ", len( huid ) )
print( "Total credits for all HU students: ", sum( credit ) )
print( "Most credits: ", max( credit ) )
print( "Least credits: ", min( credit ) )

avg = sum(credit)/len(credit)
print( "Average credits: ", avg )

print()
print( "first student in list", huid[0], credit[0] )
print( "last student in list", huid[-1], credit[-1] )


print( )

# HU ID's for all students that have completed 30 or more chapels

low = 0
done = 0

i = 0
while i < len(huid):
    
    if credit[ i ] < 25:
#        print( huid[ i ], credit[ i ] )
        low = low + 1

    if credit[ i ] >= 30:
        done = done + 1

    i = i + 1

print("30+ :-) ", done )
print("less than 25 ", low )







