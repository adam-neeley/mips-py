from tabulate import tabulate

headers = "firstrow"
tablefmt = "fancy_grid"


class Table:
    def __init__(self, data):
        # has rows
        if len(data) == 0:
            raise ValueError("Table must have row(s)")

        # find cols
        rows = len(data)
        cols = 0
        for d in data:
            num_cols = len(d)
            if num_cols > cols:
                cols = num_cols

        # has cols
        if cols == 0:
            raise ValueError("Rows must have column(s)")

        # set
        self.__data = data
        self.__rows = rows
        self.__cols = cols

    def get(self, row_num, col_num):
        d = self.__data
        if row_num >= len(d):
            return ""
        r = d[row_num]
        if col_num >= len(r):
            return ""
        return r[col_num]

    def column(self, col_num):
        return [r[col_num] or "" for r in self.__data]

    @property
    def data(self):
        return [
            [str(self.get(j, i)) for i in range(self.__cols)]
            for j in range(self.__rows)
        ]

    def __repr__(self):
        t = tabulate(self.data, headers=headers, tablefmt=tablefmt)
        return t


class Console:

    def log(self, msg):
        print(msg)

    def table(self, data):
        self.log(Table(data))


console = Console()
