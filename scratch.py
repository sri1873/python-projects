class TrieNode:
    # Trie node class
    def _init_(self):
        self.children = [None] * 26
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def _init_(self):
        self.root = self.getNode()

    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index use only 'a' through 'z' and lower case
        return ord(ch) - ord('a')

    def insert(self, key):
        # If not present, inserts key into trie, If the key is prefix of trie node, just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):
        # Search key in the trie
        # Returns true if key presents in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord


# driver function
def main():
    # Input keys (use only 'a' through 'z' and lower case)
    fileObj = open('trial.txt', "r")  # opens the file in read mode
    keys = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    output = ["Not present in trie", "Present in trie"]
    # Trie object
    t = Trie()
    # Construct trie
    dicti = {}
    count = 0
    for key in keys:
        t.insert(key)
        dicti[key] = count
        count = count + 1
    src = input("Enter search key: ")
    # Search for different keys
    print("{} ---- {}".format(src, output[t.search(src)]))
    fileObj = open('trial2.txt', "r")
    t2 = fileObj.read().splitlines()
    fileObj.close()
    if output[t.search(src) != False]:
        print(t2[dicti[src]])

main()
