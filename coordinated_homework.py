### Q-1

# def print_triangle(num , chr):
    
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print(chr,end=" ")
#         print()
# print_triangle(10,"*")



### Q-2

# def volumn(r):
#     v=(4/3)*3.14*(r)**3
#     return v
# result=volumn(5.3)
# print("%.3f"%result)



#### Q-3

# def factorial (n):
#     result=1
#     for i in range(n,0,-1):
#        result=result*i
#     return result
# result=factorial(5)
# print(result)


# ### Q-4

# def number_of_digits(n):
     
#      num=n
#      total_digits=0
#      while num != 0:
#           num=num//10
#           total_digits=total_digits+1
#      return total_digits

# result=number_of_digits(12345)
# print(result)


###Q-5

# def sum_of_digits(n):
#     sum=0
#     num=n
#     while num != 0:
#        sum=sum+num%10
#        num=num//10
#     return sum

# result=sum_of_digits(968)
# print(result)


###Q-6


# def reverse_number (n):
#     num=n
#     revase=0
#     while num!=0:
#         revase= revase*10 + num % 10
#         num=num//10
#     return revase
# result=reverse_number(1234)
# print(result)


####Q-7

# def hcf(a,b):
#     sml=a
#     hcf=0
#     if a>b:
#         sml=b
#     for i in range(1,sml+1):
#         if((a%i == 0) and (b%i == 0)):
#             hcf=i

#     return hcf

# result=hcf(10,8)
# print(result)


###Q-8

# def lcm(a,b):
#     gtr=a
#     lcm=0
#     if b>a:
#        gtr=b
#     while (True):
#         if((gtr%a==0)and(gtr%b==0)):
#               lcm=gtr
#               break
#     return lcm

# result=lcm(10,5)
# print(result)



###Q-9


# num=5
# def prime_number(n):
#     if n>1:
#         for i in range (2,n+1):
#             if(n%i==0):
#                 if(n==i):
#                     return True
#                 else:
#                     return False
#     else:
#         return False
# def perfect_number_result(n):
#     sum=0
#     for i in range(1,n+1):
#           if (n%i==0):
#               sum=sum+1
#     if(sum==n):
#         return True
#     else:
#         return False
# def palendroms(n):
#     num=n
#     revase=0
#     while num!=0:
#         revase= revase*10 + num % 10
#         num=num//10
#     if(revase==n):
#         return True
#     else:
#         return False
# prime_result=prime_number(num)
# perfect_number_result=perfect_number_result(num)
# palendroms_result=palendroms(num)
# print(f"Prime Number: {prime_result}\nPerfect Number: {perfect_number_result}\nPalendroms: {palendroms_result}")

###Q-10

# array=[4,2,6,2,5,9]
# def sort_array(arr):
#     array=arr
#     sorted=[]
#     while len(array)!=0:
#        min=array[0]
#        for i in range(len(array)):
#            if(min>array[i]):
#              min=array[i]
#        sorted.append(min)
#        array.remove(min)
#     print(f"this is sort array: {sorted}") 
# print(f"the main array : {array}")   
# sort_array(array)


###Q-11

# array=[4,2,6,2,5,9]
# def min_max_average(arr):
#     min=arr[0]
#     max=arr[0]
#     sum=0
#     for i in range(len(arr)):
#         if(min>arr[i]):
#             min=arr[i]
#     for i in range(len(arr)):
#         if(max<arr[i]):
#             max=arr[i]
#     for i in range(len(arr)):
#         sum=sum+arr[i]
#     average=sum/len(arr)
#     return min, max,average
# min,max,average=min_max_average(array)
# print(f"Minimum: {min}",f"Maximum: {max}",f"Average: {average:.3f}",sep="\n")


# ### Q-12

# str="We used a list comprehension to iterate over the list of floating-point numbers and passed each number."

# def the_numbers_of_words(str):
#      words_list=str.split(" ")
#      return len(words_list)


# print(the_numbers_of_words(str))


### Q-13

str="We used a list comprehension to iterate over the list of floating-point numbers and passed each number."

def uppercase(str):
     new_str=str.upper()
     return new_str

print(uppercase(str))
