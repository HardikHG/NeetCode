class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_b = text.count('b')
        count_a = text.count('a')
        count_l = text.count('l')
        count_o = text.count('o')
        count_n = text.count('n')

        result = min(
            count_b,
            count_a,
            count_l // 2,   # because "balloon" needs 2 l's
            count_o // 2,   # because "balloon" needs 2 o's
            count_n
        )

        return result
                