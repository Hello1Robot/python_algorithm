package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// 뒤에 오는 글자가 공백이거나, 맨 끝이라면 +1
func main() {

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	x, _ := r.ReadString('\n')
	x = strings.TrimSpace(x)
	cnt := 0
	for idx, r := range x {
		if r == ' ' {
			continue
		}
		if idx == len(x)-1 || x[idx+1] == ' ' {
			cnt++
		}
	}
	fmt.Fprintln(w, cnt)
	w.Flush()
}
