# Given a list of accounts where each element accounts[i] is a list of strings, 
# where the first element accounts[i][0] is a name, and the rest of the elements 
# are emails representing emails of the account. 
# 
#  Now, we would like to merge these accounts. Two accounts definitely belong 
# to the same person if there is some common email to both accounts. Note that even 
# if two accounts have the same name, they may belong to different people as 
# people could have the same name. A person can have any number of accounts initially, 
# but all of their accounts definitely have the same name. 
# 
#  After merging the accounts, return the accounts in the following format: the 
# first element of each account is the name, and the rest of the elements are 
# emails in sorted order. The accounts themselves can be returned in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],[
# "John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John",
# "johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.
# com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email 
# "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses 
# are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] 
# would still be accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin",
# "Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co",
# "Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@
# m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.
# co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.
# co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co",
# "Fern1@m.co","Fern5@m.co"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= accounts.length <= 1000 
#  2 <= accounts[i].length <= 10 
#  1 <= accounts[i][j].length <= 30 
#  accounts[i][0] consists of English letters. 
#  accounts[i][j] (for j > 0) is a valid email. 
#  
# 
#  Related Topics Array Hash Table String Depth-First Search Breadth-First 
# Search Union Find Sorting 👍 7190 👎 1247


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_to_id = {}    # important

        for i, account in enumerate(accounts):
            name, emails = account[0], account[1:]
            for email in emails:
                if email in email_to_id:    # important
                    uf.union(email_to_id[email], i) # important
                else:
                    email_to_id[email] = i

        id_to_emails = defaultdict(list)    # important
        for email, i in email_to_id.items():
            id_to_emails[uf.find(i)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in id_to_emails.items()]
# leetcode submit region end(Prohibit modification and deletion)
