# Copyright (c) 2020 Kapitonov Stanislav <delphi.troll@mail.ru>

from vector import Vector2d, Vector3d

v1 = Vector3d(3, -1, 2)
v2 = Vector3d(-1, 2, 1)
v3 = Vector3d(0, -2, 1)
v4 = Vector3d(-1, 1, 3)
dif = v3 - v4

# Find projection of vector v3 - v4 for vector v2
pr = dif.project(v2)
print('Projection of vector v3 - v4 for vector v2: ' + pr)

# Find space of triangle with sides v1 and v2
s = v1 * v2 / 2
print('Space of triangle with sides v1 and v2: ' + s)

# Mixed production of v1, v2 and dif
mp = v1 * v2 * dif
print('Mixed production of v1, v2 and dif: ' + mp)
