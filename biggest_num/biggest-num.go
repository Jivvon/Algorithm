package biggest_num

import (
	"fmt"
	"sort"
	"strconv"
)

func Solution(numbers []int) string {
	m := map[string]string{}
	k := make([]string, len(numbers))
	for i, n := range numbers {
		s := strconv.Itoa(n)
		key := fmt.Sprint("%s%s%s", s, s, s)
		m[key] = s
		k[i] = key
	}
	//
	//sort.Sort(sort.Reverse(sort.StringSlice(k)))
	//return
}