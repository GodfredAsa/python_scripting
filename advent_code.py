

class Position:
    def __init__(self, depth=0, fordward=0) -> None:
        self.depth = depth
        self.forward = fordward
        
    def __str__(self) -> str:
        return "Fordward position: {} and Depth: {}".format(self.forward, self.depth)
    
    
    def calculate_position(self, direction: str, direction_value: int):
        directions = ['down', 'up', 'forward']
        new_direction : str = direction.lower()
        if new_direction.lstrip() == "" or new_direction not in directions:
             print("You did not specify direction")
        elif new_direction == "forward":
            self.forward += direction_value
        elif new_direction == "down":
            self.depth += direction_value
        elif new_direction == "up":
            self.depth -= direction_value
            
            


position = Position()
position.calculate_position("forward", 10)
position.calculate_position("down", 10)
# print(position)

position.calculate_position("up", 16)
# position.calculate_position("try", 10)



print(position)



def get_square_feet_wrapper(eqn_str: str):
    l, w, h = [int(t) for t in eqn_str.split("x")]
    area_list = [l * w, l * h, w * h]
    smallest_area = min(area_list)
    return "{} square feet, smallest area: {}".format(2 * sum(area_list) + smallest_area, smallest_area )
    


print(get_square_feet_wrapper("2x3x4"))
print(get_square_feet_wrapper("1x1x10"))



def get_max_min_diff(numbers: list) -> str:
    
    min_number, max_number = min(numbers), max(numbers)
    diff = max_number - min_number
    return f"Max number: {max_number}, minimum number: {min_number} and difference: {diff}"


print(get_max_min_diff([1,3,5,9]))





def upcode(numbers: list):
    num_list_4 = numbers[0:4]
    numbers[3] = numbers[num_list_4[1]] + numbers[num_list_4[2]]
    numbers[0] = numbers[3] * numbers[11]
    return numbers

print(upcode([1,9,10,3,2,3,11,0,99,30,40,50]))