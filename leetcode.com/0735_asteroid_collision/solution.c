/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#define ABS(x)  ((x > 0) ? x : -x)

int* asteroidCollision(int* asteroids, int asteroidsSize, int* returnSize)
{
    int *queue = malloc(sizeof(int) * asteroidsSize);
    int length = 0;

    for (int i = 0 ; i < asteroidsSize ; i++) {
        if ((asteroids[i] < 0 && (length == 0 || queue[length - 1] < 0)) || asteroids[i] > 0) {
            queue[length++] = asteroids[i];
            continue;
        }

        bool add = true;

        while (length > 0) {
            if (queue[length - 1] < 0)
                break;

            int a = ABS(queue[length - 1]);
            int b = ABS(asteroids[i]);

            if (a < b) {
                length--;
            } else if (a > b) {
                add = false;
                break;
            } else {
                length--;
                add = false;
                break;
            }
        }

        if (add) {
            queue[length++] = asteroids[i];
        }
    }

    *returnSize = length;
    return queue;
}
