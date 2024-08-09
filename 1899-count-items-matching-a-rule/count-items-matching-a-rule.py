class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for type_, color, name in items:
                if ruleKey == "type" and type_ == ruleValue:
                    cnt +=1
                if ruleKey == "color" and color == ruleValue:
                    cnt +=1
                if ruleKey == "name" and name == ruleValue:
                    cnt +=1
        return cnt