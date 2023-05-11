def picking(a=None, b=2):
    return a+b

def save_doc(doc = None):
    return doc

print(picking(777))

print(save_doc(231312))


num = 100 + 1
def calc_pi_value(x):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    i = 1
    while x > 0:
        i +=1
        if 4*q+r-t < n * t:
            yield n
            x -=1
            q, r, t, k, n, l = 10*q, 10*(r - n * t), t, k, (10*(3*q + r))//t -10 *n, l #
        else:
            q, r, t, k, n, l = q*k, (2*q + r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2 # 
    print("computation is completed \n")
    print("Total iteration is %d\n" %i)

pi_V = [str(n) for n in list(calc_pi_value(num))]
print("%s.%s\n" % (pi_V[0], "".join(pi_V[1:])))
print(len(pi_V))