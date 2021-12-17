input="""target area: x=88..125, y=-157..-103"""

input_test = """target area: x=20..30, y=-10..-5"""


def first_star():
    input_list = input.split('=')
    x_str = input_list[1].split(',')[0]
    y_str = input_list[2]
    a_x = list(map(int, x_str.split('..')))
    a_y = list(map(int, y_str.split('..')))
    #finding xs with velocity 0 at the end
    can_x = []
    for x in range(a_x[0], a_x[1] +1):
        l = x
        v = 0
        while(l > 0):
            l -= v
            v += 1
        if l == 0:
            can_x.append(v-1)
    #finding ys
    can_v = []
    for velo in range(-50, 500):
        for x in can_x:
            l = 0
            v = velo
            for v_x in range(x):
                l += v
                v -= 1
            while(l > a_y[0] and l not in range(a_y[0], a_y[1] +1)):
                l+=v
                v -= 1
            if l in range(a_y[0], a_y[1] +1):
                can_v.append((x,velo))
    maxi = max(can_v, key=lambda x: x[1])[1]

    print(f"First star: {maxi*(maxi+1)//2}")




def second_star():
    input_list = input.split('=')
    x_str = input_list[1].split(',')[0]
    y_str = input_list[2]
    a_x = list(map(int, x_str.split('..')))
    a_y = list(map(int, y_str.split('..')))
    # finding xs with velocity 0 at the end
    can_x = []
    for x in range(0, a_x[1] +1):
        v = x
        l = 0
        while(l < a_x[1] and l not in range(a_x[0], a_x[1]+1)) and v > 0:
            l+=v
            v-= 1
        if l in range(a_x[0], a_x[1]+1):
            can_x.append(x)
    can_v = []
    for velo in range(a_y[0], 157):
        for x in can_x:
            l = 0
            x_x = 0
            v = velo
            v_x = x
            while (l > a_y[0] and l not in range(a_y[0], a_y[1] + 1) and x_x <= a_x[1]):
                l += v
                x_x+= v_x
                v_x =max([0, v_x -1])
                v -= 1
            if l in range(a_y[0], a_y[1] + 1) and x_x in range(a_x[0], a_x[1]+1):
                can_v.append((x, velo))
            else:
                #checking the probes that are on the left of the area, but not yet in the area
                while x_x <= a_x[1] and x_x not in range(a_x[0], a_x[1]+1):
                    l += v
                    x_x += v_x
                    v_x = max([0, v_x - 1])
                    v -= 1
                if l in range(a_y[0], a_y[1] + 1) and x_x in range(a_x[0], a_x[1] + 1):
                    can_v.append((x, velo))
    print(f"Second star: {len(can_v)}")



if __name__ == '__main__':
   first_star()
   second_star()

