class BinarySearch:
    def bisect_left(self, arr, value, begin, end):
        """

        :param arr: 정렬된 배열
        :param value:
        :param begin:
        :param end:
        :return: 범위 [0, len(arr)], 정렬된 상태를 유지한채로 value를 insert할 수 있는 왼쪽 index를 반환한다
        """
        if begin >= end:
            return begin
        mid = begin + (end - begin) // 2
        if arr[mid] < value:
            return self.bisect_left(arr, value, mid + 1, end)
        else:
            return self.bisect_left(arr, value, begin, mid)

    def bisect_right(self, arr, value, begin, end):
        if begin >= end:
            return begin
        mid = begin + (end - begin) // 2
        if arr[mid] > value:
            return self.bisect_right(arr, value, begin, mid)
        else:
            return self.bisect_right(arr, value, mid + 1, end)
