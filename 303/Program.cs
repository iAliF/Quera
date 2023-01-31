using System;

namespace FirstApp
{
    internal class Program
    {
        public static void Main(string[] args)
        {

            var a = Convert.ToInt64(Console.ReadLine());
            var b = Convert.ToInt64(Console.ReadLine());

            Console.WriteLine(a);
            ShowFibNth(a, b);
        }

        public static void ShowFibNth(long n, long m)
        {
            var x = m - n;
            if (x > 0)
            {
                Console.WriteLine(x);
                ShowFibNth(x, n);
            }
        }
    }
}