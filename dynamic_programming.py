from pprint import pprint


def backpack_problem_solution(
        tools: list[tuple[str, int, int]], capacity: int
) -> str:
    items_count = len(tools)
    table = [
        [[0, []] for _ in range(capacity + 1)] for _ in range(items_count + 1)
    ]
    for row_number in range(1, items_count + 1):
        name, mass, experiments = tools[row_number - 1]
        for volume in range(1, capacity + 1):
            if mass <= volume:
                total_experiments_with_current_tool = (
                    experiments + table[row_number - 1][volume - mass][0]
                )
                previous_result = table[row_number - 1][volume][0]
                if total_experiments_with_current_tool > previous_result:
                    table[row_number][volume][0] = (
                        total_experiments_with_current_tool
                    )
                    table[row_number][volume][1] = list.copy(
                        table[row_number - 1][volume - mass][1]
                    )
                    table[row_number][volume][1].append(name)
                else:
                    table[row_number][volume] = table[row_number - 1][volume]
            else:
                table[row_number][volume] = table[row_number - 1][volume]
    pprint(table)
    return ', '.join(table[-1][-1][-1])


if __name__ == '__main__':
    tools = [
        ('гигрометр', 1, 3),
        ('масс-спектрометр', 4, 6),
        ('нивелир', 3, 4),
        ('интерферометр', 1, 4)
    ]
    result = backpack_problem_solution(tools, 4)
    print(result)
