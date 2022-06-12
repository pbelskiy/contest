class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = defaultdict(Counter)

        for name, table, food in orders:
            foods.add(food)
            tables[table][food] += 1

        foods = sorted(foods)
        display = [['Table', *foods]]

        for table, items in sorted(tables.items(), key=lambda k: int(k[0])):
            row = [table]

            for food in foods:
                row.append(str(items[food]))

            display.append(row)

        return display
