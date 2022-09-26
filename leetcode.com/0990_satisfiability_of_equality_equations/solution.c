#define CHARS_COUNT 26

int p[CHARS_COUNT];

int find(int x)
{
    if (p[x] == x)
        return x;
    return p[x] = find(p[x]);
}

void _union(int x, int y)
{
    p[find(x)] = find(y);
}

bool equationsPossible(char **equations, int equationsSize)
{
    for (int i = 0 ; i < CHARS_COUNT ; i++)
        p[i] = i;

    /* assign */
    for (int i = 0 ; i < equationsSize ; i++) {
        if (equations[i][1] == '!')
            continue;

        int x = equations[i][0] - 'a';
        int y = equations[i][3] - 'a';
        _union(y, x);
    }

    /* check */
    for (int i = 0 ; i < equationsSize ; i++) {
        if (equations[i][1] == '=')
            continue;

        int x = equations[i][0] - 'a';
        int y = equations[i][3] - 'a';

        if (find(x) == find(y))
            return false;
    }

    return true;
}
