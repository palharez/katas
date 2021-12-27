package main

import (
	"fmt"
)

func main() {
	var salarioAtual float64
	var novoSalario float64
	var reajusteGanho float64
	var percentual float64

	fmt.Scanln(&salarioAtual)

	if salarioAtual >= 0 && salarioAtual <= 400.00 {
		percentual = 0.15
	} else if salarioAtual > 400.00 && salarioAtual <= 800.00 {
		percentual = 0.12
	} else if salarioAtual > 800.00 && salarioAtual <= 1200.00 {
		percentual = 0.10
	} else if salarioAtual > 1200.00 && salarioAtual <= 2000.00 {
		percentual = 0.07
	} else {
		percentual = 0.04
	}

	reajusteGanho = salarioAtual * percentual
	novoSalario = salarioAtual + reajusteGanho

	fmt.Printf("Novo salario: %.2f\n", novoSalario)
	fmt.Printf("Reajuste ganho: %.2f\n", reajusteGanho)
	fmt.Printf("Em percentual: %.0f %%\n", percentual*100)
}
