# -*- coding: utf-8 -*-
#How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

def p029():
    
    res = set(a**b for a in range(2,101) for b in range(2,101))
    return len(res)
    
if __name__ == "__main__":
    
    res = p029()
    print "set size: ", res