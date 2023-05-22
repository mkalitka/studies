/*
 * Autor: Mikołaj Kalitka;
 * Nazwa programu: Zad1;
 * Numer listy: 2;
 * Numer zadania na liście: 1;
 * Data wydania: 08.03.2023;
 * Numer wydania: 1;
 * Krótki opis:
 *   Program implementuje klasy InsStream, PrimeStream, RandomStream
 *   oraz RandomWordStream. Są to przykładowe strumienie liczbowe lub tekstowe
 *   które spełniają wytyczne wyznaczone w treści zadania.
 * 
 * System operacyjny: GNU/Linux;
 * Program użyty do kompilacji: mono;
 * Polecenie użyte do kompilacji: "mcs Zad1.cs";
 * Polecenie uruchamiające program: "mono Zad1.exe".
 */

using System;
using System.Text;      // Wykorzystywane w RandomWordStream

// Klasa IntStream to strumień kolejnych liczb naturalnych.
public class IntStream
{
    // Klasa zaczyna od wartości 0.
    protected int value = 0;

    // Zwraca kolejną liczbę naturalną.
    public virtual int next()
    {
        return value++;
    }

    // Sprawdza, czy strumień osiągnął swoją maksymalną wartość.
    public virtual bool eos()
    {
        return value >= int.MaxValue;
    }

    // Resetuje strumień do liczby 0.
    public virtual void reset()
    {
        value = 0;
    }
}

// Klasa PrimeStream to strumień kolejnych liczb pierwszych.
public class PrimeStream : IntStream
{
    // Sprawdza, czy liczba n jest liczbą pierwszą.
    private bool isPrime(int n)
    {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        int ceiling = (int) Math.Floor(Math.Sqrt(n));

        for (int i = 3; i <= ceiling; i+=2)
            if (n % i == 0)
                return false;

        return true;
    }

    // Zwraca kolejną liczbę pierwszą.
    public override int next()
    {
        value++;

        // Jeśli liczba nie jest pierwsza, sprawdź następną.
        if (!isPrime(value))
            return next();
        
        return value;
    }
}

// Klasa RandomStream to strumień losowych liczb całkowitych.
public class RandomStream : IntStream
{
    private Random random = new Random();

    // Zwraca kolejną liczbę losową.
    public override int next()
    {
        return random.Next();
    }

    // Sprawdza, czy strumień osiągnął swoją maksymalną wartość.
    public override bool eos()
    {
        // Strumień liczb losowych nigdy się nie zakończy.
        return false;
    }
}

/* Klasa RandomWordStream to strumień ciągów liter o losowych znakach
   o długości kolejnych liczb pierwszych. */
public class RandomWordStream
{
    private Random random = new Random();

    private PrimeStream primeStream = new PrimeStream();

    private int length = 0;

    // Zwraca losowy znak.
    private char randomChar()
    {
        // Wszystkie możliwe znaki do wylosowania.
        string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        return chars[random.Next(chars.Length)];
    }

    /* Funkcja next w tym wypadku ma za zadanie
       wylosować znak tyle razy, ile wynosi dana długość,
       po czym za każdym razem dodać znak do StringBuildera.
       Na sam koniec, zwraca wszystkie wylosowane znaki w ciągu. */
    public string next()
    {
        // Długościami tekstu są kolejne liczby pierwsze.
        length = primeStream.next();

        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < length; i++)
        {
            stringBuilder.Append(this.randomChar());
        }

        return stringBuilder.ToString();
    }
}

class Program
{
    public static void Main(string[] args)
    {
        IntStream intStream = new IntStream();
        PrimeStream primeStream = new PrimeStream();
        RandomStream randomStream = new RandomStream();
        RandomWordStream randomWordStream = new RandomWordStream();

        for (int i = 0; i < 5; i++)
            System.Console.WriteLine(intStream.next());
        System.Console.WriteLine();

        for (int i = 0; i < 5; i++)
            System.Console.WriteLine(primeStream.next());
        System.Console.WriteLine();

        for (int i = 0; i < 5; i++)
            System.Console.WriteLine(randomStream.next());
        System.Console.WriteLine();

        System.Console.WriteLine(intStream.eos());
        System.Console.WriteLine(primeStream.eos());
        System.Console.WriteLine(randomStream.eos());
        System.Console.WriteLine();

        System.Console.WriteLine(
            "Wartości pierwszych liczb w strumieniach po resecie:"
            );

        intStream.reset();
        primeStream.reset();
        randomStream.reset();

        System.Console.WriteLine(intStream.next());
        System.Console.WriteLine(primeStream.next());
        System.Console.WriteLine(randomStream.next());
        System.Console.WriteLine();

        System.Console.WriteLine("RandomWordStream:");

        for (int i = 0; i < 5; i++)
            System.Console.WriteLine(randomWordStream.next());
    }
}
