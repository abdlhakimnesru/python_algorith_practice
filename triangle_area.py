# def area_triangle(x,y):
#     if isinstance(x,(int,float)) and isinstance(y,(int,float)):
#        return (x*y)/2
#     else:
#         print("x and y must be  number")
# area = area_triangle("d",6)
# print(area)

# def area_triangle(base, height):
#     area = (base * height) / 2
#     print("Area of triangle:", area)

# base = float(input("Enter base: "))
# height = float(input("Enter height: "))

# area_triangle(base, height)





def km_met_conv(km,met):
    result = (km*1000) + met
    if isinstance(km, (int , float)) and  isinstance(met, (int , float)):
        return result
    else:
        print("min and sec must be number ")

total_met= km_met_conv(6,0)
  
print(f"is {total_met} meter ")

# def min_sec_conv(min,sec):
#     result=(min*60 ) + sec
#     if isinstance(min, (int,float)) and isinstance(sec, (int, float)):
#         return result
#     else:
#         print("mim and sec  must be number")

# min_sec=min_sec_conv(5,0)
# print(min_sec)
  

