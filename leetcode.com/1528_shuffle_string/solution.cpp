class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string r = s;
        for (auto i = 0 ; i < s.length() ; i++)
            r[indices[i]] = s[i]; 

        return r;
    }
};


