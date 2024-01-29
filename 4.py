#List Comprehension

my_list=[i for i in range(10) if i>5]
print(my_list)


#Lambda function

numbers=[1,2,3]
squared=list(map(lambda x:x**2,numbers))
print(squared)