def groupAnagrams(self, strs):
    """
        Time: O(n)
        Memory: O(n)
    
        Criaremos um hashmap para salvar os grupos 
        Começamos iterando a lista pegando n
        A cadade iteração sortearemos lexograficamente este n
        Faremos a verificaçao se n já está no hashmap
        - Se sim adicionaremos ao n hashmap
        - Se não criaremos uma key nova 

        We'll create a hashmap to save group
        Iterate trhough the strs getting n
        Each iteration we'll sort that n
        Validate if that n already in the hashmap
        - If true we add that n in the hashmap
        - Else we generate a new key on hashmap
    """
    resp = {}

    for n in strs:
        sorted_n = ''.join(sorted(n))

        if not resp.get(sorted_n):
            resp[sorted_n] = []
        
        resp[sorted_n].append(n)

    return resp.values()
