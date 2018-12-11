package main

import (
	"fmt"
	"strconv"
	"strings"
)

func HighAndLow(in string) string {
	arr := strings.Split(in, " ")
	smaller := 0
	biggest := 0
	for i := 0; i < len(arr); i++ {
		num, _ := strconv.Atoi(arr[i])
		if num > biggest {
			biggest = num
		}
		if num < smaller {
			smaller = num
		}
		if i == 0 {
			smaller = num
			biggest = num
		}
	}
	ret := strconv.Itoa(biggest) + " " + strconv.Itoa(smaller)
	return ret
}

func main() {
	fmt.Println(HighAndLow("1 9 3 4 -5"))
}
