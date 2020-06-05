# import solution

# def test_solution():
#     assert solution.X % solution.Y == solution.X // solution.Y

def test_solution(monkeypatch):
    ret_val1=None

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.X==5
    assert solution.Y==4    