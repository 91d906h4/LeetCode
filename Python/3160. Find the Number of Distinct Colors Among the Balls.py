class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        counter = 0
        index_color = {}
        color_count = {}
        result = []

        for [index, color] in queries:
            if index not in index_color:
                index_color[index] = color
            else:
                color_count[index_color[index]] -= 1

                if color_count[index_color[index]] == 0:
                    del color_count[index_color[index]]
                    counter -= 1

                index_color[index] = color

            if color not in color_count:
                counter += 1
                color_count[color] = 1
            else:
                color_count[color] += 1

            result.append(counter)

        return result
