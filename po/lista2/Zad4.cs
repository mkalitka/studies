/*
 * Autor: Mikołaj Kalitka;
 * Nazwa programu: Zad4;
 * Numer listy: 2;
 * Numer zadania na liście: 4;
 * Data wydania: 08.03.2023;
 * Numer wydania: 1;
 * Krótki opis:
 *   Program implementuje klasy LazyIntList oraz LazyPrimeList,
 *   które są obiektami dynamicznie zwiększających się list,
 *   kolejno ciągu liczb naturalnych i ciągu liczb pierwszych.
 * 
 * System operacyjny: GNU/Linux;
 * Program użyty do kompilacji: mono;
 * Polecenie użyte do kompilacji: "mcs Zad4.cs";
 * Polecenie uruchamiające program: "mono Zad4.exe".
 */

using System;
using System.Collections.Generic;

public class LazyIntList
{
    protected List<int> list;
    protected int listSize;

    // Przy konstrukcji obiektu tworzy listę i ustawia jej rozmiar na 0.
    public LazyIntList()
    {
        list = new List<int>();
        listSize = 0;
    }

    /* Wypisuje i-ty element i dodaje do listy kolejne liczby całkowite,
       Jeśli i-ty element nie istnieje. */
    public virtual int element(int i)
    {
        // Indeksowanie elementów listy zaczyna się od 1.
        if (i < 1)
            throw new IndexOutOfRangeException();

        if (i > listSize)
        {
            for (int j = listSize + 1; j <= i; j++)
                list.Add(j);
            listSize = i;
        }

        return list[i - 1];
    }

    // Zwraca rozmiar listy.
    public int size()
    {
        return listSize;
    }
}

class LazyPrimeList : LazyIntList
{
    // Funkcja zwraca n-tą liczbę pierwszą za pomoca sita Erastotenesa.
    private int nthPrimeNumber(int n)
    {
        int count = 0;
        int num = 2;

        while (count < n)
        {
            bool isPrime = true;

            for (int i = 2; i <= Math.Sqrt(num); i++)
            {
                if (num % i == 0)
                {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime)
                count++;

            num++;
        }

        return num - 1;

    }

    /* Wypisuje i-ty element i dodaje do listy kolejne liczby pierwsze,
       Jeśli i-ty element nie istnieje. */
    public override int element(int i)
    {
        // Indeksowanie elementów listy zaczyna się od liczby 1.
        if (i < 1)
            throw new IndexOutOfRangeException();

        if (i > listSize)
        {
            for (int j = listSize + 1; j <= i; j++)
                list.Add(nthPrimeNumber(j));

            listSize = i;
        }

        return list[i - 1];
    }
}

class Program
{
    public static void Main(string[] args)
    {
        LazyIntList lazyIntList = new LazyIntList();
        LazyPrimeList lazyPrimeList = new LazyPrimeList();

        System.Console.WriteLine(lazyIntList.element(30));
        System.Console.WriteLine(lazyIntList.size());
        System.Console.WriteLine(lazyIntList.element(40));
        System.Console.WriteLine(lazyIntList.size());
        System.Console.WriteLine(lazyIntList.element(20));
        System.Console.WriteLine(lazyIntList.size());
        System.Console.WriteLine();

        System.Console.WriteLine(lazyPrimeList.element(3));
        System.Console.WriteLine(lazyPrimeList.size());
        System.Console.WriteLine(lazyPrimeList.element(10));
        System.Console.WriteLine(lazyPrimeList.size());
        System.Console.WriteLine(lazyPrimeList.element(7));
        System.Console.WriteLine(lazyPrimeList.size());
    }
}
