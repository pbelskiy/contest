package main

import "fmt"
import "strings"

func wordPattern(pattern string, s string) bool {
    words := strings.Split(s, " ")
    chars := []rune(pattern)
    hash := make(map[rune]string)

    if len(words) != len(chars) {
        return false
    }

    for i, ch := range chars {
        for key, value := range hash {
            if value != words[i] && key == ch {
                return false;
            }

            if value == words[i] && key != ch {
                return false;
            }
        }

        hash[ch] = words[i]
    }

    return true
}

func main() {
    fmt.Printf("%t\n", wordPattern("jquery", "jquery") == false);
    fmt.Printf("%t\n", wordPattern("abba", "dog cat cat dog") == true);
    fmt.Printf("%t\n", wordPattern("abba", "dog dog dog dog") == false);
    fmt.Printf("%t\n", wordPattern("aaa", "aa aa aa aa") == false);
    fmt.Printf("%t\n", wordPattern("abba", "dog cat cat fish") == false);
    fmt.Printf("%t\n", wordPattern("abc", "dog cat dog") == false);
}
