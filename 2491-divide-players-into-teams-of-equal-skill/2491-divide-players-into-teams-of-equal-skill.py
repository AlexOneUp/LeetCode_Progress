class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        # No need to use midpt, but good to know when left has crossed it
        # mid = len(skill) / 2
        left = 0
        right = len(skill) - 1

        equalSkill = skill[left] + skill[right]
        
        chemistry = 0

        while left <= right:
            if skill[left] + skill[right] != equalSkill :
                return -1
            else :
                chemistry = chemistry + (skill[left] * skill[right])
                left = left + 1
                right = right-1


        return chemistry
