int minCost(char *s, int *cost, int costSize)
{
    int total = 0;

    for (int i = 0 ; i < costSize - 1 ; i++) {
        if (s[i] != s[i + 1])
            continue;

        if (cost[i] > cost[i + 1]) {
            total += cost[i + 1];
            int tmp = cost[i];
            cost[i] = cost[i + 1];
            cost[i + 1] = tmp;
        } else {
            total += cost[i];
        }
    }

    return total;
}
