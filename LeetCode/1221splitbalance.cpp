class Solution {
public:
    int balancedStringSplit(string s) {
        
        int LR = 0, left = 0, right = 0;
        
        for (int i = 0; i < s.length(); i++)
        {   if (s[i] == s[i + 1])
                if (s[i] == 'L')
                    left ++;
                else
                    right ++;
            else
                 if (s[i] == 'L')
                    left ++;
                else
                    right ++;
            if (left == right)
                LR ++;
        }
        return (LR);
    }
};