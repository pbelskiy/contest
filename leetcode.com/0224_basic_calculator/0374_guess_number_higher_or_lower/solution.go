/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
    var min, max, value int = 1, n, 0
    
    for true {
        value = min + ((max - min) / 2)
        switch (guess(value)) {
        case -1: max = value - 1
        case  1: min = value + 1
        case  0: return value
        }
    }
    
    return value
}


