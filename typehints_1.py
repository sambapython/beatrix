def fun(a: int, b: int|None=0) -> float:
    if not b:
        b=14
    res= a+b
    return res
r1=fun(12, None)
r1=fun(12)
print(r1)
employee: list[str | int] = ["emp1", "emp2", "emp3", "emp4",123]