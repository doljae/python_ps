# https://hooongs.tistory.com/28
# 

from functools import reduce


class Node():
    def __init__(self, key="", count=0, least_count=1):
        self.key = key
        self.count = 1
        self.child = {}


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, gone):
        cur = self.head
        for ch in gone:
            if ch not in cur.child:
                cur.child[ch] = Node(ch, cur.count + 1)
            cur = cur.child[ch]
        cur.child["*"] = True
    def search(self, word):
        cur=self.head
        
        for ch in word:
            if ch not in cur.child:
                return False
            cur=cur.child[ch]
        if '*' in cur.child:
            return True
            
    def search_least_type_count(self, word):
        cur = self.head
        least_type_count = 1
        str1 = ""
        for ch in word:
            # print(ch, least_type_count)
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
            str1 = str1 + ch

            if len(cur.child) >= 2:
                least_type_count = cur.count
                if str1 != word:
                    least_type_count += 1
                else:
                    pass
        return least_type_count
    

def solution(words):
    trie = Trie()
    for item in words:
        trie.insert(item)
    return reduce(lambda acc, cur: acc + trie.search_least_type_count(cur), words, 0)