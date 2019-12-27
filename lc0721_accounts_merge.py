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

class SolutionEmailAccountidsGraphDfsRecur(object):
    def _dfs(self, aid, emails, accounts, email_aids_graph, visited_aids):
        # accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
        # ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", 
        # "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

        # Check visited account id or not.
        if aid in visited_aids:
            return None

        visited_aids.add(aid)

        # Continue recursive DFS to visit that account id's emails.
        for j in range(1, len(accounts[aid])):
            email = accounts[aid][j]
            emails.add(email)

            for aid_next in email_aids_graph[email]:
                self._dfs(aid_next, emails, accounts, email_aids_graph, visited_aids)

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        # Use dict to collect email->account ids.
        email_aids_graph = defaultdict(list)

        for aid, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_aids_graph[email].append(aid)

        # Apply recursive DFS to visit account ids over email_aids_graph.
        visited_aids = set()
        result = []

        for aid, account in enumerate(accounts):
            if aid in visited_aids:
                continue

            # Start DFS to visit account id, and collect name's emails.
            name = accounts[aid][0]
            emails = set()
            self._dfs(aid, emails, accounts, email_aids_graph, visited_aids)

            result.append([name] + sorted(emails))

        return result


class SolutionEmailParentUnionFind(object):
    def _union(self, ei, ep):
        ei = self._find(ei)
        ep = self._find(ep)
        self.email_parent[ei] = ep

    def _find(self, e):
        if self.email_parent[e] != e:
            self.email_parent[e] = self._find(self.email_parent[e])
        return self.email_parent[e]

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
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
    print SolutionEmailAccountidsGraphDfsRecur().accountsMerge(accounts)
    print SolutionEmailParentUnionFind().accountsMerge(accounts)


if __name__ == '__main__':
    main()
