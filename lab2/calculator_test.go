package main

import "testing"

func TestAdd(t *testing.T) {
  expected := 15
  actual := Add(10, 5)
  if actual != expected {
    t.Errorf("Ошибка в Add: ожидалось %d, получено %d", expected, actual)
  }
}

func TestSubtract(t *testing.T) {
  expected := 5
  actual := Subtract(10, 5)
  if actual != expected {
    t.Errorf("Ошибка в Subtract: ожидалось %d, получено %d", expected, actual)
  }
}

func TestMultiply(t *testing.T) {
  expected := 50
  actual := Multiply(10, 5)
  if actual != expected {
    t.Errorf("Ошибка в Multiply: ожидалось %d, получено %d", expected, actual)
  }
}
