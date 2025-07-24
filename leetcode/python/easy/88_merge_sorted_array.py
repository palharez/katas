def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # if m == 0:
    #     nums1[0] = nums2[0]
    #     return

    """
    Começo no final das duas entrys de dados dois arrays
    na posição m de nums 1 e na posição n de nums2
    no final de length de nums1 eu insiro o menor o valor dos dois
    e decrease no valor respectivo
    """
    final = len(nums1) - 1
    while m or n:
        last_num_1 = nums1[m - 1] if m else 0
        last_num_2 = nums2[n - 1] if n else 0
        print(last_num_1, last_num_2)
        if last_num_1 >= last_num_2:
            print("Here?")
            print(final)
            nums1[final] = last_num_1
            m -= 1
        else:
            nums1[final] = last_num_2
            n -= 1
        final -= 1


if __name__ == "__main__":
    # nums1 = [1, 2, 3, 0, 0, 0]
    # merge(
    #     nums1=nums1,
    #     m=3,
    #     nums2=[2, 5, 6],
    #     n=3,
    # )
    # print(f"{nums1} == [1, 2, 2, 3, 5, 6]")
    nums1 = [0, 0, 0, 0, 0]
    merge(
        nums1=nums1,
        m=0,
        nums2=[1, 2, 3, 4, 5],
        n=5,
    )
    print(f"{nums1} == [1, 2, 3, 4, 5]") #
