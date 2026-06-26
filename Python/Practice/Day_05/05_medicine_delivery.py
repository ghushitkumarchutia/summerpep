# A function simulating a medicine delivery system using nested loops.
# It visits every building, every floor within each building, and every room on each floor.
def medicine_delivery(building, floor, room_number):
    # Outer loop: Iterates through each building number from 1 to 'building'
    for i in range(1, building + 1):
        print(f"Building No: {i}")
        
        # Middle loop: For each building, iterates through each floor from 1 to 'floor'
        for j in range(1, floor + 1):
            print(f"              Floor No: {j}")
            
            # Inner loop: For each floor, iterates through each room from 1 to 'room_number'
            for k in range(1, room_number + 1):
                print(f"                         Room No: {k}")
        
# Call the function to simulate delivery across 2 buildings, 3 floors each, and 4 rooms per floor
medicine_delivery(2, 3, 4)