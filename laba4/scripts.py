import random


def find_by_id(_id, data):

    try:
        q_id = int(_id[2:])
    except:
        q_id = 0

    if (q_id and q_id < len(data) and q_id > 0):
        
        while(q_id > 0):
            data_id = data[q_id].split('\t')[0]

            if data_id == _id:
                return create_dict(data[0], data[q_id])
            
            q_id -= 1


    return None


def create_dict(names, data):
    return {x:y for x, y in zip(names.split('\t'), data.split('\t'))}

def find_by_title(title, data):
    ans = []
    
    for row in data:
        if(row.split('\t')[2] == title):
            ans.append(create_dict(data[0], row))

    return ans


def find_by_year(year, data):
    ans = []

    if len(str(year)) != 4:
        return []
    
    for row in data:
        if row.split('\t')[5] == str(year):
            ans.append(create_dict(data[0], row))

    return ans


def _suggest(k, q, data):
    ans = {}

    while(len(ans) <= k):
        temp = get_random(data, q)
        ans[temp[0]] = temp[1]
    
    cache.clear()

    return ans

cache = []
def get_random(data, q):
    while(True):
        i = random.randint(0, len(data) - 1)
        _id = data[i].split('\t')[0]

        if (_id not in q['likes'].keys() and _id not in cache):
            cache.append(_id)
            return _id, random.random()

    



