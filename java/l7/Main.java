import structures.OrderedList;

import java.util.Date;

public class Main {
    public static void main(String[] args) {
        System.out.println("== Testing OrderedList<Integer> ==");
        OrderedList<Integer> numberList = new OrderedList<>();
        numberList.insert(5);
        numberList.insert(3);
        numberList.insert(7);
        numberList.insert(1);
        numberList.insert(9);
        System.out.println("Initial number list: " + numberList);

        numberList.remove(5);
        System.out.println("After removing 5: " + numberList);
        assert !numberList.search(5) : "5 should have been removed";

        assert numberList.min() == 1 : "Minimum should be 1";
        assert numberList.max() == 9 : "Maximum should be 9";
        assert numberList.size() == 4 : "Size should be 4";
        assert numberList.search(7) : "7 should be in the list";
        assert !numberList.search(5) : "5 should not be in the list";
        assert numberList.at(2) == 7 : "Element at index 2 should be 7";
        assert numberList.index(7) == 2 : "Index of 7 should be 2";

        System.out.print("Iterating over number list: ");
        for (Integer item : numberList) {
            System.out.print(item + " ");
        }
        System.out.println();

        System.out.println("\n== Testing OrderedList<String> ==");
        OrderedList<String> stringList = new OrderedList<>();
        stringList.insert("Banana");
        stringList.insert("Apple");
        stringList.insert("Peach");
        stringList.insert("Cherry");
        System.out.println("Initial string list: " + stringList);

        stringList.remove("Banana");
        System.out.println("After removing 'Banana': " + stringList);
        assert !stringList.search("Banana") : "'Banana' should have been removed";

        assert stringList.min().equals("Apple") : "Minimum should be 'Apple'";
        assert stringList.max().equals("Peach") : "Maximum should be 'Peach'";
        assert stringList.size() == 3 : "Size should be 3";
        assert stringList.search("Apple") : "'Apple' should be in the list";
        assert !stringList.search("Banana") : "'Banana' should not be in the list";
        assert stringList.at(1).equals("Cherry") : "Element at index 1 should be 'Cherry'";
        assert stringList.index("Cherry") == 1 : "Index of 'Cherry' should be 1";

        System.out.print("Iterating over string list: ");
        for (String item : stringList) {
            System.out.print(item + " ");
        }
        System.out.println();

        System.out.println("\n== Testing OrderedList<Date> ==");
        OrderedList<Date> dateList = new OrderedList<>();
        dateList.insert(new Date(100000000));
        dateList.insert(new Date(50000000));
        dateList.insert(new Date(150000000));
        dateList.insert(new Date(75000000));
        System.out.println("Initial date list: " + dateList);

        dateList.remove(new Date(100000000));
        System.out.println("After removing 'Date(100000000)': " + dateList);
        assert !dateList.search(new Date(100000000)) : "'Date(100000000)' should have been removed";

        assert dateList.min().equals(new Date(50000000)) : "Minimum should be 'Date(50000000)'";
        assert dateList.max().equals(new Date(150000000)) : "Maximum should be 'Date(150000000)'";
        assert dateList.size() == 3 : "Size should be 3";
        assert dateList.search(new Date(75000000)) : "'Date(75000000)' should be in the list";
        assert !dateList.search(new Date(100000000)) : "'Date(100000000)' should not be in the list";
        assert dateList.at(2).equals(new Date(150000000)) : "Element at index 2 should be 'Date(150000000)'";
        assert dateList.index(new Date(150000000)) == 2 : "Index of 'Date(150000000)' should be 2";

        System.out.print("Iterating over date list: ");
        for (Date item : dateList) {
            System.out.print(item + " ");
        }
        System.out.println();
    }
}
