#define MAX_LENGTH  200

char* reformatNumber(char *number)
{
    char *rn = calloc(sizeof(char), MAX_LENGTH + 1);
    int pos = 0, length = 0, written = 0;

    for (int i = 0 ; i < strlen(number) ; i++)
        if (number[i] != ' ' && number[i] != '-')
            length++;

    int three_blocks = 0;
    int d = length;
    while (d > 0) {
        if (d == 2 || d == 4)
            break;

        d -= 3;
        three_blocks += 1;
    }

    // printf("three_blocks = %d, length = %d\n", three_blocks, length);

    for (int i = 0 ; i < strlen(number) ; i++) {
        if (number[i] == ' ' || number[i] == '-')
            continue;

        if (written > 0) {
            if (written % 3 == 0 && three_blocks > 0) {
                // printf("%3: written - %d, three_block = %d\n", written, three_blocks);
                rn[pos++] = '-';
                three_blocks--;
                written = 0;
            } else if (written % 2 == 0 && three_blocks == 0) {
                // printf("%2: written - %d, three_block = %d\n", written, three_blocks);
                rn[pos++] = '-';
            }
        }

        written++;
        rn[pos++] = number[i];
    }

    return rn;
}

int main()
{
    "123 4-567"
    "123 4-5678"
    "12"
    "--17-5 229 35-39475 "
    "9052215-3-0--69-1849664-9585476671151 808 072253110132708288886781683799 715803761083"
    return 0;
}