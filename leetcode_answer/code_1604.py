from typing import List

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hashmap = dict()
        for i, name in enumerate(keyName):
            time_list = keyTime[i].split(':')
            time = int(time_list[0]) * 60 + int(time_list[1])
            if name not in hashmap:
                hashmap[name] = [time]
            else:
                hashmap[name].append(time)
        alert_name = []
        for key in hashmap.keys():
            if len(hashmap[key]) < 3:
                continue
            for j in range(2, len(hashmap[key])):
                time_l = sorted(hashmap[key])
                if 0 <= (time_l[j] - time_l[j-2]) <= 60:
                    alert_name.append(key)
                    break
        return sorted(alert_name)

if __name__ == "__main__":
    solution = Solution()
    keyName = ["john","john","john"]
    keyTime = ["23:58","23:59","00:01"]
    res = solution.alertNames(keyName, keyTime)
    print(res)



