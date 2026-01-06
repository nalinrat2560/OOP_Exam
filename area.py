widht = int(input("กว้าง : "))
height = int(input("ยาว : "))

def area(widht,height):
    t = 0.5 * widht * height
    r = widht * height

    return(t,r)

area_t, area_r = area(widht,height)
print (f"พื้นที่สามเหลี่ยม: {area_t}")
print (f"พื้นที่สี่เหลี่ยม: {area_r}")
