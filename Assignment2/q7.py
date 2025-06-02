def has_antipodal(points):
    points.sort()
    angles = set(points)
    for angle in points:
        if (angle + 180) % 360 in angles:
            return True
    return False

print(has_antipodal([0, 90, 180, 270])) 
