#Question 1
ages=[19,22,19,24,20,25,26,24,25,24]
sortedlist=sorted(ages)  #sorting the list
print(sortedlist)
min_age=min(ages)  #min of the list
max_age=max(ages)  # maximum in the list
print(min_age,max_age)
sortedlist.append(min_age)  # adding min and max to the list
sortedlist.append(max_age)
length=len(sortedlist)
if length%2==0:                  #calculating median if length of list is even
    median_index=int(length/2)
    a=median_index
    median_age=(sortedlist[a]+sortedlist[a-1])/2
else:                            #calculating median if length of list is odd
    median_index=length//2
    median_age=sortedlist[median_index+1]
print(median_age)
average_age=sum(sortedlist)/length   #average
print(average_age)
range_ages=max_age-min_age      #range
print(range_ages)

#Question 2

dog={} #creating dog dictionary 
dog.update({"name":""}) #adding keys to dictionary 
dog.update({"color":""})
dog.update({"breed":""})
dog.update({"legs TV":""})
dog.update({"age":"0"})
print("Dog Dictionary: ")
print(dog)

student ={} # creating student dictionary 
student["first_name"] =""
student["last_name"] =""
student["gender"] =""
student["age"] =0
student["marital_status"] =""
student["skills"] =[]
student["country"] =""
student["city"] =""
student["address"] =""
print("length of the student: " +str(len(student)))     #length of student dictionary 

skills= student["skills"]
print("type of skills: ")
print(type(skills)) # checking data type of student dictionary 

student["skills"].append("sports")
student["skills"].append("riding") # modifying student dictionary 
print("new skills: ")
print(student["skills"])

print("student keys: ")
print(student.keys()) # printing student dictionary keys using keys() function 
print("student values: ")
print(student.values()) #printing student dictionary values using value() function'''

#Question 3


brothers=("anand","barath","cherry","daniel") # creating brothers tuple
sisters=("alekya","brethi","chelsie")         # creating sisters tuple
siblings=brothers+sisters                     #assigning brothers and sisters to siblings tuple
print(siblings)
print(len(siblings))                         # length of siblings list
family_members=siblings+("radha","krishna") # adding father and mother name to family_members 
print(family_members)

#Question 4

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))       #length of the list
it_companies.add("Accenture")
print(it_companies)
c_list=["Cognizant","Wipro"] #adding two or more companies to list
it_companies.update(c_list)
print(it_companies)
it_companies.remove("Wipro") #removing company from the list
# difference between discard() and remove() methods

#The Discard() method removes the specified item from the set.
#This method is different from the remove() method, because the remove() method will raise an error
#if the specified item does not exist, and the discard() method will not.

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(A.union(B))  #union
print(A.intersection(B)) #Intersection
print(A.issubset(B))     #subset
print(A.isdisjoint(B))   #disjoint
A_unionB=A.union(B)      #joining A set with Bset and Bset with Aset
B_unionA=B.union(A)
print(A_unionB,B_unionA)
print(A.symmetric_difference(B))     #symmetric difference
del(A)
del(B)      #delete A and B sets
#print(A)
#print(B)
setof_age=set(age)       #converting list to age
print(len(age))         #length of the set
print(len(setof_age))

#Question 5

radius_circle=30 
_area_of_circle_=3.14 * radius_circle**2  # calculating area of circle
print(_area_of_circle_)
_circum_of_circle_=2*3.14*radius_circle   #calculating circumference of circle
print(_circum_of_circle_)
new_radius=int(input())
print("Area of circle is", 3.14*new_radius**2)


#Question 6

s="I am a teacher and I love to inspire and teach people"
l=s.split(" ") #spliting the s
set_of_unique=set(l) #using the set function ,duplicate words will be filtered
print(set_of_unique)
print(len(set_of_unique)) #length of unique words set


#Question 7

print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")



#Question 8

radius=10
area=3.14*radius**2 #calculating area of circle
print("The area of circle with radius {} is {} meters square.".format(radius,int(area)))  # displaying the output using format()


#Question 9

number=int(input())
l1=[]
n=2
for i in range(number):      #taking input in to the list
    l1.append(int(input()))
l2=[]
for i in l1:                  #taking each lb in l1 list and converting to lbs using this formulae
    v1=i/2.2046
    v1=int(v1*10**n)/10**n
    l2.append(v1)
print(l2)

    

