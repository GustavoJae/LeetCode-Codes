def TwoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # a idéia é armazenar em um dicionario os numero que eu já passei
    # e testar se o complementar está nesse dicionario
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map: # testa se existe {complement: index_complement}
            return [num_map[complement], index]
        
        # armazeno o numero que passei junto com seu index, na forma {num : index}
        num_map[num] = index