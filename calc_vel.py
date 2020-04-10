#find Velocity Prime

def find_v_prime1(m1, m2, v1, v2):
  return ((m1 - m2) * v1) / (m1 + m2) + (2*m2*v2) / (m1 + m2)

def find_v_prime2(m1, m2, v1, v2):
  return ((m2 - m1) * v2) / (m1 + m2) + (2*m1*v1) / (m1 + m2)

_m1 = float(input("Mass 1 : "))
_m2 = float(input("Mass 2 : "))
_v1 = float(input("Velocity 1 : "))
_v2 = float(input("Velocity 2 : "))

print("V1 Prime: ", find_v_prime1(_m1, _m2, _v1, _v2))
print("V2 Prime: ", find_v_prime2(_m1, _m2, _v1, _v2))