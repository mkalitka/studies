import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.GregorianCalendar;
import java.util.Calendar;
import java.util.Locale;

public class CalendarApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(CalendarView::new);
    }
}

class CalendarModel extends AbstractListModel<String> {
    private int year;
    private int month;

    public CalendarModel(int year, int month) {
        this.year = year;
        this.month = month;
    }

    public boolean isJulian() {
        return year < 1582 || (year == 1582 && month < Calendar.OCTOBER);
    }

    public void setYear(int newYear) {
        year = newYear;
        fireContentsChanged(this, 0, getSize() - 1);
    }

    public void changeMonth(int delta) {
        month = month + delta;
        while (month < 0) {
            month += 12;
            year--;
        }
        while (month > 11) {
            month -= 12;
            year++;
        }
        fireContentsChanged(this, 0, getSize() - 1);
    }

    public int getYear() {
        return year;
    }

    public int getMonth() {
        return month;
    }

    private int getDaysInMonth(int year, int month) {
        GregorianCalendar cal = new GregorianCalendar();
        cal.set(Calendar.YEAR, year);
        cal.set(Calendar.MONTH, month);
        cal.set(Calendar.DAY_OF_MONTH, 1);

        if (year == 1582 && month == Calendar.OCTOBER) {
            return 21; // Days from 1-4 and 15-31
        }

        return cal.getActualMaximum(Calendar.DAY_OF_MONTH);
    }

    @Override
    public int getSize() {
        return getDaysInMonth(year, month);
    }

    @Override
    public String getElementAt(int index) {
        GregorianCalendar cal = new GregorianCalendar();
        cal.set(Calendar.YEAR, year);
        cal.set(Calendar.MONTH, month);
        
        // Handle October 1582 transition
        if (year == 1582 && month == Calendar.OCTOBER) {
            if (index < 4) {
                cal.set(Calendar.DAY_OF_MONTH, index + 1);
            } else {
                cal.set(Calendar.DAY_OF_MONTH, index + 11);
            }
        } else {
            cal.set(Calendar.DAY_OF_MONTH, index + 1);
        }

        String monthName = cal.getDisplayName(Calendar.MONTH, Calendar.LONG, Locale.getDefault());
        String dayName = cal.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.getDefault());

        return String.format("%02d %s, %s", cal.get(Calendar.DAY_OF_MONTH), monthName, dayName);
    }
}

class CalendarView extends JFrame {
    private final JLabel yearLabel;
    private final JList<String> prevMonthList;
    private final JList<String> currentMonthList;
    private final JList<String> nextMonthList;
    private final JLabel prevMonthLabel;
    private final JLabel currentMonthLabel;
    private final JLabel nextMonthLabel;
    private final CalendarModel prevMonthModel;
    private final CalendarModel currentMonthModel;
    private final CalendarModel nextMonthModel;

    public CalendarView() {
        setTitle("Calendar App");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(800, 600);

        JPanel topPanel = new JPanel(new BorderLayout());
        yearLabel = new JLabel("", SwingConstants.CENTER);
        yearLabel.setFont(new Font("Arial", Font.BOLD, 24));
        topPanel.add(yearLabel, BorderLayout.CENTER);

        JPanel centerPanel = new JPanel(new GridLayout(1, 3));

        GregorianCalendar cal = new GregorianCalendar();
        int currentYear = cal.get(Calendar.YEAR);
        int currentMonth = cal.get(Calendar.MONTH);

        JPanel prevMonthPanel = new JPanel(new BorderLayout());
        JPanel currentMonthPanel = new JPanel(new BorderLayout());
        JPanel nextMonthPanel = new JPanel(new BorderLayout());

        prevMonthLabel = new JLabel("", SwingConstants.CENTER);
        currentMonthLabel = new JLabel("", SwingConstants.CENTER);
        nextMonthLabel = new JLabel("", SwingConstants.CENTER);
        
        prevMonthModel = new CalendarModel(currentYear, currentMonth - 1);
        prevMonthList = new JList<>(prevMonthModel);
        prevMonthList.setCellRenderer(new CalendarCellRenderer());
        
        currentMonthModel = new CalendarModel(currentYear, currentMonth);
        currentMonthList = new JList<>(currentMonthModel);
        currentMonthList.setCellRenderer(new CalendarCellRenderer());
        
        nextMonthModel = new CalendarModel(currentYear, currentMonth + 1);
        nextMonthList = new JList<>(nextMonthModel);
        nextMonthList.setCellRenderer(new CalendarCellRenderer());

        prevMonthPanel.add(prevMonthLabel, BorderLayout.NORTH);
        prevMonthPanel.add(new JScrollPane(prevMonthList), BorderLayout.CENTER);
        currentMonthPanel.add(new JScrollPane(currentMonthList), BorderLayout.CENTER);
        currentMonthPanel.add(currentMonthLabel, BorderLayout.NORTH);
        nextMonthPanel.add(nextMonthLabel, BorderLayout.NORTH);
        nextMonthPanel.add(new JScrollPane(nextMonthList), BorderLayout.CENTER);

        centerPanel.add(prevMonthPanel);
        centerPanel.add(currentMonthPanel);
        centerPanel.add(nextMonthPanel);

        JPanel bottomPanel = new JPanel();
        JButton prevMonthButton = new JButton("< Previous Month");
        JSpinner yearSpinner = new JSpinner(new SpinnerNumberModel(2024, 1, 3999, 1));
        JButton nextMonthButton = new JButton("Next Month >");
        bottomPanel.add(prevMonthButton);
        bottomPanel.add(yearSpinner);
        bottomPanel.add(nextMonthButton);

        add(topPanel, BorderLayout.NORTH);
        add(centerPanel, BorderLayout.CENTER);
        add(bottomPanel, BorderLayout.SOUTH);

        updateLabels();

        prevMonthButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                prevMonthModel.changeMonth(-1);
                currentMonthModel.changeMonth(-1);
                nextMonthModel.changeMonth(-1);
                yearSpinner.setValue(currentMonthModel.getYear());
                updateLabels();
            }
        });

        nextMonthButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                prevMonthModel.changeMonth(1);
                currentMonthModel.changeMonth(1);
                nextMonthModel.changeMonth(1);
                yearSpinner.setValue(currentMonthModel.getYear());
                updateLabels();
            }
        });

        yearSpinner.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                int selectedYear = (int) yearSpinner.getValue();
                prevMonthModel.setYear(selectedYear);
                currentMonthModel.setYear(selectedYear);
                nextMonthModel.setYear(selectedYear);
                updateLabels();
            }
        });

        setVisible(true);
    }

    private void updateLabels() {
        yearLabel.setText(String.format("%d %s", currentMonthModel.getYear(), currentMonthModel.isJulian() ? "(Julian)" : "(Gregorian)"));

        GregorianCalendar cal = new GregorianCalendar();

        cal.set(Calendar.YEAR, currentMonthModel.getYear());

        cal.set(Calendar.MONTH, prevMonthModel.getMonth());
        prevMonthLabel.setText(cal.getDisplayName(Calendar.MONTH, Calendar.LONG, Locale.getDefault()));

        cal.set(Calendar.MONTH, currentMonthModel.getMonth());
        currentMonthLabel.setText(cal.getDisplayName(Calendar.MONTH, Calendar.LONG, Locale.getDefault()));

        cal.set(Calendar.MONTH, nextMonthModel.getMonth());
        nextMonthLabel.setText(cal.getDisplayName(Calendar.MONTH, Calendar.LONG, Locale.getDefault()));
    }
}

class CalendarCellRenderer extends DefaultListCellRenderer {
    @Override
    public Component getListCellRendererComponent(JList<?> list, Object value, int index, boolean isSelected, boolean cellHasFocus) {
        JLabel label = (JLabel) super.getListCellRendererComponent(list, value, index, isSelected, cellHasFocus);
        String text = (String) value;
        if (text.contains("Sunday")) {
            label.setForeground(Color.RED);
        } else {
            label.setForeground(Color.BLACK);
        }
        return label;
    }
}

