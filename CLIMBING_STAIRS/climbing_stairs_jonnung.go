package main

import (
	"testing"
)

func climbStairs(n int) int {
	if n == 0 {
		return 0
	}

	mem := make([]int, n)
	for i := 0; i < n; i++ {
		if i < 3 {
			mem[i] = i + 1
		} else {
			mem[i] = mem[i-1] + mem[i-2]
		}
	}
	return mem[n-1]
}

func TestClimbStairs(t *testing.T) {
	var tests = []struct {
		input, output int
	}{
		{0, 0},
		{1, 1},
		{2, 2},
		{3, 3},
		{4, 5},
		{5, 8},
		{6, 13},
	}

	for _, tc := range tests {
		result := climbStairs(tc.input)
		if result != tc.output {
			t.Errorf("got %d, expect %d", result, tc.output)
		}
	}
}
