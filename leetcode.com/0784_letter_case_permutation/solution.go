package main

import "fmt"
import "math"
import "unicode"

func letterCasePermutation(S string) []string {
	cases := []string{S}
	letters := 0

	for _, ch := range S {
		if !unicode.IsNumber(ch) {
			letters++;
		}
	}

	count := 1
    if letters > 0 {
        count = int(math.Pow(2, float64(letters)))
	}

	for i := 1 ; i < count ; i++ {
		current := []rune(cases[i - 1])

        for j := len(S) - 1 ; j >= 0 ; j-- {
            if (unicode.IsDigit(current[j])) {
                continue
			}

            if (unicode.IsLower(current[j])) {
                current[j] = unicode.ToUpper(current[j])
                break
            }

            current[j] = unicode.ToLower(current[j])
        }

		cases = append(cases, string(current))
	}

	return cases;
}

func main() {
	cases := letterCasePermutation("a1b2");

	fmt.Printf("%+q\n", cases);
}