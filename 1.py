def f(s: str, t: str) -> int:
    s_len = len(s)
    t_len = len(t)
    t_idx = 0
    count = 0
    
    while t_idx < t_len:
        s_idx = 0
        find = False
        while s_idx < s_len and t_idx < t_len:
            if s[s_idx] == t[t_idx]:
                t_idx += 1
                find = True
            s_idx += 1
        if not find:
            return -1
        count += 1
    
    return count


print(f("abc", "abcbc"))
print(f("abc", "acdbc"))
print(f("xyz", "xzyxz"))



