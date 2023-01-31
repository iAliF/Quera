using System;

namespace FirstApp
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var str = "";
            for (int i = 1; i <= 5000; i++)
            {
                str += Convert.ToString(i);
            }

            int index = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(str[index - 1]);
        }

    }
}