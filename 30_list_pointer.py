#WAP to ask subject and their mark and print their percentage and division

for i in range(1,6):
    subject = input("Enter the subject name: ")
    mark = int(input("Enter the mark: "))


j=0
while j<len(first_list):
    for i in range(0,len(first_list)-1):
        if first_list[i] > first_list[i+1]:
            first_list[i],first_list[i+1] = first_list[i+1],first_list[i]
    j=j+1

print(first_list)



temp = 5
sort_list = [] #[5]
for number in first_list:
    if number > temp:
        sort_list.append(number)
        temp = number
    else:
        sort_list.insert(len(sort_list)-1,number)

print(sort_list)


#assignment to short given list [1,5,9,6,89,1203,4,23]

firs_list = ["nepal","india","usa"] #ram_memory = 0X012A

second_list = firs_list #0X012A 

firs_list.append("japan")
firs_list.clear()

print(second_list)

#assignment to copy list


my_data = {"name":"skill shikshya","location":"kathmandu","district":"bagmati"}
keys = my_data.keys() #this return all keys 
values = my_data.values() #this return all  values

second_data = my_data.copy()
my_data.pop("district")



print(second_data)



subject = {
    "math":54,
    "science":78,
    "nepali":98,
    "english": 90
}

# print(subject["science"])

for key in subject.keys():
    print(f"your mark in {key} subject is {subject[key]}")

    #WAP to ask subject and their mark and print their percentage and division

for i in range(1,6):
    subject = input("Enter the subject name: ")
    mark = int(input("Enter the mark: "))



