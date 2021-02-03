/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

int guessNumber(int n)
{
	int min = 1;
    int max = n;
    
    while (true) {
        int value = min + ((max - min) / 2);
    
        printf("min: %d max: %d, value: %d\n", min, max, value);
        
        switch (guess(value)) {
            case -1:
                max = (max != value) ? value : value - 1;
                break;

            case 1:
                min = (min != value) ? value : value + 1;
                break;

            case 0: 
                return value;
        }
    }
}

