from datetime import datetime


parking_time_tracking = [
    ('09:00', '13:00'),
    ('05:15', '08:59'),
    ('01:10', '04:18'),
    ('04:30', '15:00'),
    ('00:30', '02:18'),
    ('01:16', '01:48'),
    ('01:37', '09:48'),
    ('18:32', '22:22'),
    ('19:25', '23:18'),
    ('22:01', '22:18'),
]


def time_parsing(time_periods: str) -> datetime:
    return datetime.strptime(time_periods, '%H:%M')


def mark_and_sort(time_periods: list) -> list:
    time_sets = []

    for single_car_period in time_periods:
        start_time, end_time = single_car_period
        time_sets.append((time_parsing(start_time), 'start'))
        time_sets.append((time_parsing(end_time), 'end'))

    return sorted(time_sets)


def get_max_car_count(time_sets: list) -> int:
    marked_times = mark_and_sort(time_sets)

    count = 0
    max_count = 0

    for time in marked_times:
        if 'start' in time:
            count += 1
        else:
            count -= 1
        max_count = max(count, max_count)
    return max_count


if __name__ == '__main__':
    print(
        f'Максимальное количество автотранспорта, находящегося одновременно на парковке: '
        f'{get_max_car_count(parking_time_tracking)}'
    )

