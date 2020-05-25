#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * read_file(const char *file_path, unsigned int *b_size)
{
    FILE *fh = fopen(file_path, "r");

    fseek(fh, 0, SEEK_END);
    unsigned int size = ftell(fh);
    fseek(fh, 0, SEEK_SET);

    char *data = (char *) malloc(size * sizeof(char));
    fread(data, size, sizeof(unsigned char), fh);
    fclose(fh);

    *b_size = size;
    return data;
}

void bubble_sort(char **pool, unsigned words_count)
{
    bool sorted = false;
    char *tmp_pointer;

    while (!sorted) {
        sorted = true;
        for (int i = 0 ; i < words_count - 1; i++)

            /* swap */
            if (strcmp(pool[i], pool[i + 1]) > 0) {
                tmp_pointer = pool[i];
                pool[i] = pool[i + 1];
                pool[i + 1] = tmp_pointer;
                sorted = false;
            }
    }
}

int calc_score(char *name)
{
    int sum = 0;

    for (int i = 0 ; i < strlen(name) ; i++)
        sum += name[i] - '@';

    return sum;
}

int main()
{
    unsigned int words_count;
    unsigned int size;
    unsigned int p;
    char **name_pool = NULL;
    bool open = false;

    char *data = read_file("22.txt", &size);

    /* two actions */
    for (int a = 0 ; a < 2 ; a++) {
        p = 0;
        words_count = 0;

        while (p < size) {
            if (data[p] == ',')
                data[p - 0] = '\0';

            if (data[p] == '"') {
                open = (open) ? false : true;

                if (a > 0 && open) {
                    name_pool[words_count] = &data[p + 1];
                }

                if (open) words_count++;
            }
            p++;
        }

        /* allocate pointer pool */
        if (a == 0)
            name_pool = (char **) malloc(words_count * sizeof(char *));
    }

    /* remove '"' at the end of each name' */
    for (int i = 0 ; i < words_count ; i++)
        name_pool[i][strlen(name_pool[i]) - 1] = '\0';

    bubble_sort(name_pool, words_count);

    /* print names */
    int total_sum = 0;

    for (int i = 0 ; i < words_count ; i++) {
        int score = calc_score(name_pool[i]);
        total_sum += score * (i + 1);

        // printf("%d - %s (%d)\n", i + 1, name_pool[i], score * (i + 1));
    }

    printf("\nTotal score is: %d\n", total_sum);

    free(data);
    free(name_pool);
    return 0;
}