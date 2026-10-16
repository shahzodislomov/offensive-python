def almost_equal(a, b, rel_tol=1e-9, abs_tol=0.0):
     return abs(a-b) <= max(rel_tol * max(abs(a),abs(b)), abs_tol)
print(almost_equal(0.1 + 0.2, 0.3))
print(almost_equal(10.0, 10.000000001))
