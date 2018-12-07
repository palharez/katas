package main

import (
	"fmt"
	"strconv"
)

func main() {
	var input string
	var aux string

	fmt.Scanln(&input)

	for {
		n, err := strconv.Atoi(input)
		aux = input

		if err != nil {
			break
		}

		if n == 0 {
			fmt.Println("vai ter copa!")
		} else {
			fmt.Println("vai ter duas!")
		}

		fmt.Scanln(&input)
		if input == aux {
			break
		}
	}

}
