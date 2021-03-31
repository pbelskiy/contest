#define MAX_CHARS   26

bool isAnagram(char *s, char *t)
{
    int s_len = strlen(s);
    int t_len = strlen(t);

    if (s_len != t_len)
        return false;

    int ch[MAX_CHARS] = {0,};

    for (int i = 0 ; i < s_len ; i++)
        ch[s[i] - 'a']++;

    for (int i = 0 ; i < t_len ; i++)
        ch[t[i] - 'a']--;

    for (int i = 0 ; i < MAX_CHARS ; i++)
        if (ch[i])
            return false;

    return true;
}
