"""Leetcode 721. Accounts Merge
Medium

URL: https://leetcode.com/problems/accounts-merge/

Given a list accounts, each element accounts[i] is a list of strings, where the
first element accounts[i][0] is a name, and the rest of the elements are emails
representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the
same person if there is some email that is common to both accounts. Note that even
if two accounts have the same name, they may belong to different people as people
could have the same name. A person can have any number of accounts initially,
but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first
element of each account is the name, and the rest of the elements are emails in
sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", 
"john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 
'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email
"johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are
used by other accounts.
We could return these lists in any order, for example the answer [['Mary',
'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
would still be accepted.

Note:
- The length of accounts will be in the range [1, 1000].
- The length of accounts[i] will be in the range [1, 10].
- The length of accounts[i][j] will be in the range [1, 30].
"""

class SolutionEmailAccountidsDictDfsRecur(object):
    def _dfs(self, aid, emails, accounts, email_aids_d, visited_aids):
        visited_aids.add(aid)

        # Continue recursive DFS to visit that account id's emails.
        for j in range(1, len(accounts[aid])):
            email = accounts[aid][j]
            emails.add(email)

            for aid_next in email_aids_d[email]:
                if aid_next not in visited_aids:
                    self._dfs(aid_next, emails, accounts, email_aids_d, visited_aids)

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]

        Time complexity: O(|V|+|E|+|V|*log|V|), where
          - |V|: number of emails
          - |E|: number of edges.
        Space complexity: O(|V|).
        """
        from collections import defaultdict

        # Create graph adjacency list to collect email->account ids.
        email_aids_d = defaultdict(list)

        for aid, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_aids_d[email].append(aid)

        # Apply recursive DFS to visit account ids over email_aids_d.
        visited_aids = set()
        result = []

        for aid, account in enumerate(accounts):
            if aid not in visited_aids:
                # Start DFS to visit account id to collect name's emails.
                emails = set()
                self._dfs(aid, emails, accounts, email_aids_d, visited_aids)

                name = account[0]
                result.append([name] + sorted(emails))

        return result


class SolutionEmailParentUnionFind(object):
    def _union(self, i, j):
        i = self._find(i)
        j = self._find(j)
        self.email_parent[i] = j

    def _find(self, i):
        if self.email_parent[i] != i:
            self.email_parent[i] = self._find(self.email_parent[i])
        return self.email_parent[i]

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]

        Time complexity: O(|V|*log|V|), where
          - |V|: number of emails
          - |E|: number of edges.
        Space complexity: O(|V|).
        """
        from collections import defaultdict

        self.email_parent = defaultdict()
        self.email_name = defaultdict()

        for account in accounts:
            name = account[0]

            for j in range(1, len(account)):
                email = account[j]
                if email not in self.email_parent:
                    self.email_parent[email] = email

                self.email_name[email] = name

                self._union(email, account[1])

        result = []
        email_trees = defaultdict(list)

        for email in self.email_parent:
            email_trees[self._find(email)].append(email)

        for parent, emails in email_trees.items():
            result.append([self.email_name[parent]] + sorted(emails))
        return result


def main():
    # Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], 
    #          ["John", "johnnybravo@mail.com"],
    #          ["Mary", "mary@mail.com"]]
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]
    print SolutionEmailAccountidsDictDfsRecur().accountsMerge(accounts)
    print SolutionEmailParentUnionFind().accountsMerge(accounts)


if __name__ == '__main__':
    main()
