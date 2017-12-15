def solve_captcha(captcha_string):
    length_of_captcha_string = len(captcha_string)
    values_to_add=[]
    i = 0
    while i<len(captcha_string):
        if i==(len(captcha_string)-1):
            current_value = captcha_string[i]
            next_value = captcha_string[0]
        else:
            current_value = captcha_string[i]
            next_value = captcha_string[i+1]
        if current_value == next_value:
            values_to_add.append(int(current_value))
        i+=1
    return sum(values_to_add)

def solve_day_1_part_1_challenge_1():
    puzzle_input_file = open('python/day1part1input.txt', 'r')
    puzzle_input = puzzle_input_file.read()
    print(solve_captcha(puzzle_input.strip()))

if __name__ == "__main__":
    solve_day_1_part_1_challenge_1()