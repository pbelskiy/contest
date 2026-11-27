#define MAX_ITEMS 1000 + 1
#define MAX_BUDGET 1500 + 1

int **items;
int itemsSize;

int f[MAX_ITEMS];
int cache[MAX_ITEMS][MAX_BUDGET][2];

int get_free(int i)
{
    int t = 0;

    for (int j = 0 ; j < itemsSize ; j++) {
        if (j != i && items[j][0] % items[i][0] == 0)
            t += 1;
    }

    return t;
}

int dfs(int i, int b, int t)
{
    if (cache[i][b][t] != -1)
        return cache[i][b][t];

    if (i == itemsSize)
        return 0;

    int p = items[i][1];

    /* skip */
    int m = dfs(i + 1, b, 0);

    if (b - p >= 0) {
        /* take first */
        if (!t) {
            m = MAX(m, dfs(i, b - p, 1) + 1 + f[i]);
        }

        /* take again */
        m = MAX(m, dfs(i, b - p, 1) + 1);
    }

    return cache[i][b][t] = m;
}

int maximumSaleItems(int **_items, int _itemsSize, int *itemsColSize, int budget)
{
    items = _items;
    itemsSize = _itemsSize;

    memset(f, 0, sizeof(int)*itemsSize);
    for (int i = 0 ; i < itemsSize ; i++)
        f[i] = get_free(i);

    for (int i = 0; i <= itemsSize; i++)
        memset(cache[i], -1, sizeof(int) * 2 * (budget + 1));

    return dfs(0, budget, false);
}

