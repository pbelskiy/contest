#define MAX_RODS    100

int countPoints(char *rings)
{
    int rods[MAX_RODS] = {0,};

    for (int i = 0 ; i < strlen(rings) - 1 ; i += 2) {
        switch (rings[i]) {
            case 'R':
                rods[rings[i + 1]] |= 1 << 1;
                break;
            case 'G':
                rods[rings[i + 1]] |= 1 << 2;
                break;
            case 'B':
                rods[rings[i + 1]] |= 1 << 3;
                break;
        }
    }

    int total = 0;

    for (int i = 0 ; i < MAX_RODS ; i ++) {
        if (rods[i] == 14)
            total += 1;
    }

    return total;
}
