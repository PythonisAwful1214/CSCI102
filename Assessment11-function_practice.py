#   Nicolas Callier
#   CSCI102 - SECTION H
#   ASSESSMENT 11
#   TIME IT TOOK: 30 MINUTES

import math

def print_output(string):
    print("OUTPUT", string)


def cylinder_vol(radius, height):
    volume = 3.1415 * radius**2 * height
    print_output(f"{volume:.2f}")


def lbs_to_kg(pounds):
    kg = pounds * 0.4536
    print_output(f"{kg:.4f}")


def polar_coords(x, y):
    r = (x**2 + y**2)**0.5
    theta = math.degrees(math.atan2(y, x))
    print_output(f"r: {r:.2f}")
    print_output(f"theta: {theta:.2f}")


def yen_to_dollars(yen):
    dollars = yen * 0.0068
    print_output(f"{dollars:.2f}")


def quad_form(a, b, c):
    d = (b**2 - 4*a*c)**0.5
    x1 = (-b - d) / (2*a)
    x2 = (-b + d) / (2*a)
    if x1 < x2:
        print_output(str(round(x1)))
        print_output(str(round(x2)))
    else:
        print_output(str(round(x2)))
        print_output(str(round(x1)))