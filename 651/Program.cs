using System;
using System.Linq;

namespace FirstApp
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var a = Convert.ToInt32(Console.ReadLine());
            var b = Convert.ToInt32(Console.ReadLine());
            var c = Convert.ToInt32(Console.ReadLine());

            var x = To(c, From(b, a));

            Console.WriteLine(
                Convert.ToString(x) == Reverse(Convert.ToString(x)) ? "YES" : "NO"
            );
        }

        public static int From(int from, int num)
        {
            var str = Convert.ToString(num);
            var sum = 0;

            for (var i = 0; i < str.Length; i++)
            {
                sum += (str[str.Length - i - 1] - '0') * (int)Math.Pow(from, i);
            }

            return sum;
        }

        public static int To(int to, int num)
        {
            var s = "";

            while (num != 0)
            {
                s += Convert.ToString(num % to);
                num /= to;
            }

            return Convert.ToInt32(Reverse(s));
        }

        public static string Reverse( string s )
        {
            char[] charArray = s.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }
}