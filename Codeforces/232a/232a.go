//https://codeforces.com/contest/282/problem/A
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var input string
	fmt.Scan(&input)
	int_input, _ := strconv.Atoi(input)

	var vals []string = make([]string, int_input)

	for i := 0; i < int_input; i++ {
		fmt.Scan(&vals[i])
	}

	x := 0

	for i := 0; i < int_input; i++ {
		if string(vals[i][1]) == "+" {
			x += 1
		} else {
			x -= 1
		}
	}

	fmt.Printf("%d", x)
}
