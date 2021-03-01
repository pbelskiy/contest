package main

import "fmt"

func restoreString(s string, indices []int) string {
	in := []rune(s)
	out := make([]rune, len(s))

	for i := 0 ; i < len(indices) ; i++ {
		out[indices[i]] = in[i]
	}

	return string(out)
}

func main() {
	tc_1 := []int{4,5,6,7,0,2,1,3}

	fmt.Println(restoreString("codeleet", tc_1))
}
