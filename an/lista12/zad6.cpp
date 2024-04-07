#include <iostream>
#include <functional>
using namespace std;

function<long double(long double)> f = [](long double x){
  return x * x;
};

vector<long long> ToPowerForm(vector<long long> zeroes)
{
  size_t n = zeroes.size();
  vector<long long> coefficients(n + 1, 0);

  coefficients[0] = 1;
  coefficients[1] = -zeroes[0];
  for (size_t i = 1; i < n; i++)
  {
    vector<long long> copy_coefficients = coefficients;
    for (size_t j = 1; j <= i + 1; j++)
    {
      coefficients[j] += copy_coefficients[j - 1] * (-zeroes[i]);
    }
  }

  return coefficients;
}

vector<long long> Horner(vector<long long> coefficients_a, long long zero)
{
  size_t n = coefficients_a.size() - 1;
  vector<long long> coefficients_b(n, 0);

  coefficients_b[0] = 1;
  for (int i = 1; i < n; i++)
  {
    coefficients_b[i] = coefficients_a[i] + coefficients_b[i - 1] * zero;
  }

  return coefficients_b;
}

long double IntegratePolynomial(vector<long long> coefficients)
{
  int n = (int)coefficients.size() - 1;
  long double res = 0.0;

  long long power = n;
  for (int i = n; i >= 0; i--)
  {
    res += (long double)coefficients[i] * 1.0 / (n - i + 1.0) * (long double)power;
    power *= n;
  }

  return res;
}

unsigned long long Factorial(long long n)
{
  unsigned long long res = 1;
  for (int i = 2; i <= n; i++)
  {
    res *= i;
  }

  return res;
}

long double QNC(long double a, long double b, long long n)
{
  vector<long long> zeroes(n + 1, 0);
  for (int i = 0; i <= n; i++)
  {
    zeroes[i] = i;
  }

  vector<long long> power_form(ToPowerForm(zeroes));

  vector<long double> A(n + 1, 0);
  long double h = (b - a) / (long double)n;
  int L = 0, R = (int)n;
  while (L <= R)
  {
    A[L] = A[R] = (pow(-1.0, (n - L) % 2) * h) / (long double)(Factorial(L) * Factorial(n - L)) * IntegratePolynomial(Horner(power_form, L));
    L++; R--;
  }

  long double res = 0.0;
  for (int i = 0; i <= n; i++)
  {
    res += A[i] * f(a + i * h);
  }

  return res;
}

int main()
{
  for (int i = 2; i <= 24; i++)
  {
    cout << "n = " << i << " : " << QNC(-1.0, 1.0, i) << endl;
  }
}
