package main

import (
	"bufio"
	"fmt"
	"os"
)

var stdio = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout),
)

func main() {
	defer stdio.Flush()

	var x string
	fmt.Fscan(stdio, &x)
	runes := []rune(x)
	flag := true
	for i := 0; i <= int(len(runes)/2); i++ {
		if runes[i] != runes[len(runes)-1-i] {
			flag = false
		}
	}
	if flag {
		fmt.Fprintln(stdio, 1)
	} else {
		fmt.Fprintln(stdio, 0)
	}
}