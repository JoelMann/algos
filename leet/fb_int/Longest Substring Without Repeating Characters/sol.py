from re import L


class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s) == 0:
    #         return 0
    #     arr_of_possibilities = []
    #     answers = list(s)
    #     input = list(s)
    #     for index, value in enumerate(input):
    #         arr_of_possibilities.append(set())
    #         for sets in arr_of_possibilities:
    #             if value not in sets:
    #                 sets.add(value)
    #             else:
    #                 answers[index] = len(sets)
    #     maxscores = [element for element in answers if isinstance(element, int)]
    #     if maxscores != []:
    #         return max(maxscores)
    #     else:
    #         return 1

    # s= Solution()
    # s.lengthOfLongestSubstring("bob")

    def lengthOfLongestSubstring(self, s: str) -> int:
        leftSide: int = 0
        rightSide: int = 1

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        str_arr = list(s)
        str_arr.append(None)
        print(str_arr)
        lookup_table = set()
        max = 0
        score = 0

        while str_arr[rightSide] is not None and str_arr[leftSide] is not None:
            # compare window to set - add if not.
            for i in range(leftSide, rightSide + 1):
                if (
                    leftSide == rightSide + 1
                ):  # if they are looking at the same point, we want to increase it.
                    rightSide += 1
                    break
                if str_arr[i] not in lookup_table:
                    lookup_table.add(str_arr[i])
                    score += 1
                else:
                    if score > max:
                        max = score
                    lookup_table.remove(str_arr[i])
                    score -= 1
                    leftSide += 1
                    break
            rightSide += 1
            if score >= max:
                max = score

        return max
