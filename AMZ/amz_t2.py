from copy import deepcopy

def threeProductSuggestions(numProducts, repository, customerQuery):
    original_repo = deepcopy(sorted(repository))
    repository = [ele.lower() for ele in sorted(repository)]
    customerQuery = customerQuery.lower()
    result = []
    for i in range(len(customerQuery)-1):
        query = customerQuery[:i+2]
        selected = []
        for idx, string in enumerate(repository):
            if len(selected)>2:
                break
            if string.startswith(query):
                selected.append(original_repo[idx])
        result.append(selected)
    return result

if __name__ == '__main__':
    repository = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad']
    threeProductSuggestions(5, repository, 'mouse')
