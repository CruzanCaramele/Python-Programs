def test_hash_function(func, keys, size):
    results = [] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results


#def bad_hash_string(keyword, buckets):
#    return ord(keyword[0]) % buckets


def hash_string(keyword, buckets):
    hash_tracker = 0
    for keys in keyword:
        hash_tracker += ord(keys) 
    return hash_tracker % buckets
        


#print hash_string('', 12)


def make_hashtable(n_buckets):
    i = 0
    table = []
    while i < n_buckets:
        table.append([])
        i += 1
    return table

def hashtable_get_bucket(hashtable, keyword):
    
    return hashtable[hash_string(keyword, len(hashtable))]

def hashtable_add(hashtable, keyword, value):
    bucket = hashtable_get_bucket(hashtable, keyword)
    bucket.append([keyword,value])


def hashtable_lookup(hashtable, keyword):
    bucket = hashtable_get_bucket(hashtable, keyword)
    for items in bucket:
        if items[0] == keyword:
            return items[1]
    return None
        
def hashtable_update(hashtable, keyword, value):
    bucket = hashtable_get_bucket(hashtable, keyword)
    for item in bucket:
        if item[0] == keyword:
            item[0] = value
            return
    bucket.append([keyword, value])

    

table = make_hashtable(3)
hashtable_update(table, 'udacity', 23)
hashtable_update(table, 'bodacity', 19)
hashtable_update(table, 'audacity', 17)
hashtable_update(table, 'wodacity', 28)

print hashtable_lookup(table, 'audacity')
        
