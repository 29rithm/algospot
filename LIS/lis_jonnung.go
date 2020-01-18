package	main

import (
	"os"
	"fmt"
	"bufio"
	"strconv"
	"strings"
)

func max(arr []int64) int64 {
	max := int64(0)
	for _, v := range arr {
		if v > max {
			max = v
		}
	}

	return max
}


func solution(size int64, seqc []int64) {
	var mem [500]int64

	for m := int64(0); m < size; m++ {
		mem[m] = 1
	}

	for i := int64(1); i < size; i++ {
		for j := int64(0); j < i; j++ {
			if seqc[i] > seqc[j] {
				compare := [2]int64{mem[i], mem[j] + 1}
				mem[i] = max(compare[:])
			}
		}
	}

	fmt.Println(max(mem[:size]))
}


func main() {
	var c, n int64
	var v string
	var sequence []int64

	input := bufio.NewScanner(os.Stdin)

	// TC 개수 입력
	input.Scan()
	c, _ = strconv.ParseInt(input.Text(), 0, 64)

	for i := int64(0); i < c; i++ {
		// 원소 개수 입력
		input.Scan()
		n, _ = strconv.ParseInt(input.Text(), 0, 64)

		// 길이가 n인 수열 입력
		input.Scan()
		v = input.Text()
		values := strings.Fields(v)
		sequence = make([]int64, len(values))
		for j, num := range values {
			intNum, _ := strconv.Atoi(num)
			sequence[j] = int64(intNum)
		}

		solution(n, sequence)
	}
}