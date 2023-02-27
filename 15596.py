def solve(a: list):
    ans = 0
    for x in a:
        ans += a[x]
    return ans