package main

import "fmt"

func main() {
  fmt.Println("Лабораторная работа №2")
  fmt.Println("Запуск функций:")
  
  resAdd := Add(10, 5)
  resSub := Subtract(10, 5)
  resMul := Multiply(10, 5)

  fmt.Printf("Результат сложения (10 + 5): %d\n", resAdd)
  fmt.Printf("Результат вычитания (10 - 5): %d\n", resSub)
  fmt.Printf("Результат умножения (10 * 5): %d\n", resMul)
}
