
class Cube:

    def convert_cube_uv_to_xyz(face, u, v):
        uc = 2 * u - 1
        vc = 2 * v - 1
        if face == 0:
            return (1, vc, -uc)
        elif face == 1:
            return (-1, vc, uc)
        elif face == 2:
            return (uc, 1, -vc)
        elif face == 3:
            return (uc, -1, vc)
        elif face == 4:
            return (uc, vc, 1)
        elif face == 5:
            return (-uc, vc, -1)

    def convert_xyz_to_cube_uv(x, y, z):
        is_x_positive = x > 0
        is_y_positive = y > 0
        is_z_positive = z > 0

        face = 0
        maxAxis = 0

        if is_x_positive and x >= y and x >= z:
            face, maxAxis, uc, vc = 0, x, -z, y

        if not is_x_positive and x >= y and x >= z:
            face, maxAxis, uc, vc = 1, x, z, y

        if is_y_positive and y >= x and y >= z:
            face, maxAxis, uc, vc = 2, y, x, -z

        if not is_y_positive and y >= x and y >= z:
            face, maxAxis, uc, vc = 3, y, x, z

        if is_z_positive and z >= x and z >= y:
            face, maxAxis, uc, vc = 4, z, x, y

        if not is_z_positive and z >= x and z >= y:
            face, maxAxis, uc, vc = 5, z, -x, y

        u = 0.5 * (uc / maxAxis + 1)
        v = 0.5 * (vc / maxAxis + 1)
        return (face, u, v)
