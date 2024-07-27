coordinates = [1, 2, 3]

for coordinate1 in coordinates:
    for coordinate2 in coordinates:
        print(f'{coordinate1} x {coordinate2}')

print("\n\n\n")

coordinates_outer = [1, 2, 3]
coordinates_inner = ['a', 'b', 'c']
for coordinate1 in coordinates_outer:
    for coordinate2 in coordinates_inner:
        print(f'{coordinate1} x {coordinate2}')
