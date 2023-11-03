class Solution:
    def rankTeams(self, votes: List[str]) -> str:
#         print(votes)
#         ballots = {team : 0 for team in votes[0]}
        
        
        
#         if len(votes) < 2:
#             return votes[0]
        d = {}

        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1

        voted_names = sorted(d.keys())
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))
