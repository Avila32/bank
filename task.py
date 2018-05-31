class Params(object):
    def __init__(self):
        self.sum = float(15000)
        self.percent1 = float(0.15)
        self.percent2 = float(0.09)
        self.check_cost = float(80)
        self.matrix = [[735, 15], [225, 25]]


class Solver(Params):
    def solve(self):
        s1 = float(self.matrix[0][0] + self.matrix[0][1])
        s2 = float(self.matrix[1][0] + self.matrix[1][1])
        win_pass = self.matrix[0][0] / s1
        lose_pass = self.matrix[0][1] / s1 
        win_fail = self.matrix[1][0] / s2 
        lose_fail = self.matrix[1][1] / s2

        p_pass = s1 / (s1 + s2)
        p_fail = 1 - p_pass
        p_lose = (self.matrix[0][1] + self.matrix[1][1]) / (s1 + s2)
        p_win = 1 - p_lose

        denied = float(self.percent2 * self.sum)

        profit_without_check = max((denied, self.percent1 * self.sum * p_win - self.sum * p_lose))
        profit_with_check = -self.check_cost + \
                          p_pass * (max((denied, self.percent1 * self.sum * win_pass - self.sum * lose_pass))) + \
                          p_fail * (max((denied, self.percent1 * self.sum * win_fail - self.sum * lose_fail)))

        return profit_with_check, profit_without_check
