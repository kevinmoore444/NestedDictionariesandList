# PART 1

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15

# #Change the last_name of the first student from 'Jordan' to 'Bryant'

# students[0]["last_name"] = "Bryant"

# #In the sports_directory, change 'Messi' to 'Andres'

# sports_directory["soccer"][0] = "Andres"

# #Change the value 20 in z to 30

# z[0]["y"] = 30

# PART 2

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel

# def iterateDictionary(students):
#     for i in range(0,len(students)):
#         print(students[i])

# iterateDictionary(students)

# PART 3

#print(students[0]["first_name"])

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iteratedictionary2(key_name, some_list):
#      for i in range(0,len(some_list)):
#           print(some_list[i][key_name])

# iteratedictionary2("last_name", students)


# Challenge 4

# print(len(dojo["locations"]))
# print(dojo["locations"][0])


# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# def printinfo(company_name):
#      for each_key in company_name:
#           print(f"{each_key} {len(company_name[each_key])}")
#           for item in company_name[each_key]:
#                print(item)

# printinfo(dojo)



# def printinfo(dojo)
#      for i in range(0, len(list))
          

# printInfo(dojo)