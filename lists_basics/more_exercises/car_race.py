sequence_of_numbers_list = input().split()

left_timings_list = []
right_timings_list = []
left_total_time = 0
right_total_time = 0
winner = ''
winner_time = 0

for left in range(len(sequence_of_numbers_list) // 2):
    left_timings_list.append(sequence_of_numbers_list[left])

for right in range(len(sequence_of_numbers_list) - 1, len(sequence_of_numbers_list) // 2, -1):
    right_timings_list.append(sequence_of_numbers_list[right])

for left_timing in left_timings_list:
    if int(left_timing) == 0:
        left_total_time *= 0.8
    left_total_time += int(left_timing)

for right_timing in right_timings_list:
    if int(right_timing) == 0:
        right_total_time *= 0.8
    right_total_time += int(right_timing)

if left_total_time < right_total_time:
    winner = 'left'
    winner_time = left_total_time
elif right_total_time < left_total_time:
    winner = 'right'
    winner_time = right_total_time

print(f'The winner is {winner} with total time: {winner_time:.1f}')
