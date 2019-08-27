def find_longest(user_id, weeks):
    weeks_sequences = []

    week_sequence = []

    for last_week, cur_week in zip([week for week in weeks[:-1]], [week for week in weeks[1:]]):
        week_sequence.append(last_week)
        if cur_week - last_week == 1:
            continue

        weeks_sequences.append(week_sequence)
        week_sequence = []

    week_sequence.append(cur_week)
    weeks_sequences.append(week_sequence)

    max_sequence = sorted(weeks_sequences, key=lambda x: len(x), reverse=True)[0]

    return [user_id, len(max_sequence), max_sequence[0], max_sequence[-1]]

if __name__ == '__main__':
    result = find_longest(1, [1, 10, 11, 13, 14, 49, 50, 52])
    print(result)
