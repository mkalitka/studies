# Autor: Mikołaj Kalitka (z pomocą ChatGPT);
# Nazwa programu: zad1;
# Numer listy: 9;
# Numer zadania na liście: 1;
# Data wydania: 13.05.2023;
# Numer wydania: 1;
# Krótki opis:
#   Program implementuje klasę Funkction z metodami value,
#   zero, field oraz deriv. Klasa ta reprezentuje funkcję, która
#   jako argument przyjmuje funkcję zadaną blokiem, a metody
#   zdefiniowane w klasie obliczają wartość, miejsca zerowe,
#   pole powierzchni między wykresem a osią OX dla danych argumentów
#   oraz przybliżoną wartość pochodnej.
#
# System operacyjny: GNU/Linux;
# Program użyty do uruchomienia: ruby w wersji 3.2.2;
# Polecenie uruchamiające program: "ruby zad1.rb".


class Function
  # Konstruktor, jako argument przyjmujemy funkcję w bloku jednoparametrowym.
  def initialize(&block)
    @function = block
  end

  # Oblicza wartość funkcji dla danego argumentu x.
  def value(x)
    @function.call(x)
  end

  # Oblicza miejsce zerowe funkcji w danym przedziale a,b z dokładnością e.
  # Zwraca nil jeśli miejsce zerowe nie zostanie znalezione.
  # Funkcja ta oblicza miejsce zerowe metodą połowienia przedziałów.
  def zero(a, b, e)
    return nil unless @function.call(a) * @function.call(b) < 0

    while (b - a).abs > e
      midpoint = (a + b) / 2.0
      if @function.call(midpoint).abs <= e
        return midpoint
      elsif @function.call(midpoint) * @function.call(a) < 0
        b = midpoint
      else
        a = midpoint
      end
    end

    nil
  end

  # Oblicza przybliżone pole powierzchni między wykresem a osią OX
  # w przedziale [a, b].
  def field(a, b)
    n = 1000
    delta_x = (b - a) / n.to_f
    sum = 0.0

    (1..n).each do |i|
      x = a + i * delta_x
      sum += delta_x * @function.call(x).abs
    end

    sum
  end

  # Oblicza przybliżoną wartość pochodnej w punkcie x.
  def deriv(x)
    h = 0.0001
    (value(x + h) - value(x - h)) / (2 * h)
  end

end


# Testy

f = Function.new { |x| x + 2 }

puts f.value(2)
puts f.zero(-1, 3, 0.001)
puts f.field(1, 2)
puts f.deriv(1)
f.draw_ascii_plot(-5, 5, 0.1)
