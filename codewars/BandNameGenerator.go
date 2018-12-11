package kata

import (
	"strings"
)

// bandNameGenerator retorna um slice da um string
func bandNameGenerator(word string) string {
	wordTest := strings.ToLower(word)
	if wordTest[0] == wordTest[len(word)-1] {
		wordFinish := wordTest + wordTest[1:]
		return strings.Title(wordFinish)
	}
	wordFinish := "The " + wordTest
	return strings.Title(wordFinish)

}
