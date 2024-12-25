int buttonWithLongestTime(int **events, int eventsSize, int *eventsColSize)
{
    int best_index = events[0][0];
    int best_duration = events[0][1];

    int prev = events[0][1];

    for (int i = 1 ; i < eventsSize ; i++) {
        int duration = events[i][1] - prev;

        if (duration == best_duration && events[i][0] < best_index) {
            best_index = events[i][0];
        }

        if (duration > best_duration) {
            best_index = events[i][0];
            best_duration = duration;
        }

        prev = events[i][1];
    }

    return best_index;
}
