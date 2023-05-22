/*
 * Autor: Mikołaj Kalitka (z pomocą ChatGPT);
 * Nazwa programu: Zad2;
 * Numer listy: 4;
 * Numer zadania na liście: 2;
 * Data wydania: 21.03.2023;
 * Numer wydania: 1;
 * Krótki opis:
 *   Program implementuje klasę SlowaFibonacciego, która 
 *   generuje słowa złożone z dwóch liter: a i b. Słowa definiowane są
 *   w następujący sposób:
 *   Sn = {b : n = 1
 *         a : n = 2
 *         S(n-1) + S(n-2) : n > 2}.
 *   Klasa SlowaFibonacciego wykorzystuje interfejs IEnumerable<T>.
 * 
 * System operacyjny: GNU/Linux;
 * Program użyty do kompilacji: mono;
 * Polecenie użyte do kompilacji: "mcs Zad2.cs";
 * Polecenie uruchamiające program: "mono Zad2.exe".
 */

using System;
using System.Collections;
using System.Collections.Generic;


public class SlowaFibonacciego : IEnumerable<string>
{
    private int n; // Liczba słów do wygenerowania.

    public SlowaFibonacciego(int n)
    {
        this.n = n;
    }

    public IEnumerator<string> GetEnumerator()
    {
        string s1 = "b"; // Pierwsze słowo w ciągu Fibonacciego.
        string s2 = "a"; // Drugie słowo w ciągu Fibonacciego.
        string s3; // Trzecie słowo w ciągu Fibonacciego.

        /* W kodzie poniżej używamy `yield return`.
         * Pozwala to nam w leniwy sposób generować kolejne elementy,
         * dzięki czemu nie musimy tworzyć osobnego interfejsu
         * IEnumerator, tylko wykorzystujemy funkcję,
         * która jest "generatorem sekwencji".
         * Użycie operatora `yield return` zaproponował ChatGPT.
         */
        for (int i = 0; i < n; i++)
        {
            if (i == 0)
            {
                yield return s1;
            }
            else if (i == 1)
            {
                yield return s2;
            }
            else
            {
                s3 = s2 + s1;
                yield return s3;
                s1 = s2;
                s2 = s3;
            }
        }
    }

    // Funkcja wymagana przez klasę IEnumerable.
    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator(); // Zwracamy "generator" Enumeratora.
    }
}

// Testowe użycie klasy SlowaFibonacciego.
class Program
{
    public static void Main(string[] args)
    {
        SlowaFibonacciego sf = new SlowaFibonacciego(20);
        foreach(string s in sf)
            Console.WriteLine(s);
    }
}
