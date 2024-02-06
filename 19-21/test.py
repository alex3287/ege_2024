# +5 *3 => 435      1 <= S <= 434
def f(s,m):
    if s>= 27: return m%2 == 0
    if m == 0: return 0
    h = [f(s+1,m-1),f(s+2, m-1), f(s*2, m-1)]
    return any(h) if m%2 != 0 else all(h)
print([s for s in range(1,26) if f(s,2)])
print([s for s in range(1,26) if not f(s,1)])
print([s for s in range(1,26) if f(s,2)])
