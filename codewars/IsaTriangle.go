package kata

// IsTriangle retorna se é um triângulo
func IsTriangle(a, b, c int) bool {
	if (a > (b-c) && a < (b+c)) && (b > (a-c) && b < (a+c)) && (c > (a-b) && c < (a+b)) {
		return true
	}
	return false
}
