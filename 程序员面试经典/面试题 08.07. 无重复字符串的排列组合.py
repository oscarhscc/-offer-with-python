'''
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。
'''

class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        if len(S) == 1:
            return [S]
        for i in range(len(S)):
            for j in self.permutation(S[:i] + S[i + 1:]):
                res.append(S[i] + j)
        return res