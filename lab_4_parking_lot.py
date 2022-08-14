moving_cars = int(input())
parking_cars = set()

for _ in range(moving_cars):
    command, car_number = input().split(', ')
    if command == 'IN':
        parking_cars.add(car_number)
    elif command == 'OUT' and car_number in parking_cars:
        parking_cars.remove(car_number)
if parking_cars:
    [print(num) for num in parking_cars]
else:
    print("Parking Lot is Empty")
