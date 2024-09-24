def save_bookings(book_lst, file_name):
    with open(file_name, 'w') as f:
        for booking in book_lst:
            for part in booking:
                f.write(f'{part}:')
            f.write('\n')

def load_lines(file_name):
    try:
        with open(file_name) as f:
            return f.readlines()
    except FileNotFoundError:
        return f'The file {file_name} could not be found'

def split_lines(booking_lines):
    for i in range(len(booking_lines)):
        booking_lines[i] = booking_lines[i].split(':')
        booking_lines[i].remove(booking_lines[i][-1])
        for j in range(len(booking_lines[i])):
            part = booking_lines[i][j]
            try:
                booking_lines[i][j] = int(part)
            except ValueError:
                if j in (1, 2, 4, 5):
                    return f'An int was expected instead of {part}'
    return booking_lines

def check_schedule(booking_items, num_lanes):
    hour_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    minute_list = [0, 15, 30, 45]
    meridiem_list = ['AM', 'PM']
    for item in booking_items:
        if len(item[0]) < 3:
            raise ValueError
        if item[1] not in hour_list or item[4] not in hour_list:
            raise ValueError
        if item[2] not in minute_list or item[5] not in minute_list:
            raise ValueError
        if item[3] not in meridiem_list or item[6] not in meridiem_list:
            raise ValueError
        for i in range(7, len(item)):
            if item[i] > num_lanes:
                raise ValueError

def make_schedule(booking_items, num_lanes):
    schedule_string = ''''''
    schedule_list = [['LANES    ']]
    hour = 7
    minute = 0
    meridiem = 'AM'
    for i in range(num_lanes):
        schedule_list[0].append('~~~')
    while hour != 5:
        time_list = [f'{hour:02d}:{minute:02d} {meridiem}']
        for i in range(1, num_lanes + 1):
            for item in booking_items:
                if item[1] == hour and item[2] == minute and i in item[7:]:
                    time_list.append(item[0][:3])
                    break
                if item[4] == hour and item[5] == minute and i in item[7:]:
                    time_list.append('~~~')
                    break
            else:
                if schedule_list[-1][i] == '~~~':
                    time_list.append('~~~')
                else:
                    time_list.append(schedule_list[-1][i])
        schedule_list.append(time_list)
        minute += 15
        if minute == 60:
            minute = 0
            if hour == 12:
                hour = 0
            hour += 1
            if hour == 12:
                meridiem = 'PM'
    for i in range(1, num_lanes + 1):
        schedule_list[0][i] = f'{i}  '
    for time_list in schedule_list:
        if time_list == schedule_list[0]:
            schedule_string += ' '.join(time_list) + '\n'
        else:
            schedule_string += ' '.join(time_list) + ' \n'
    return schedule_string
