using System;
using System.Collections.Generic;
using System.Text;

namespace csharp_solutions.top_interview_questions
{
    class _564_buy_sell_stock
    {

        public _564_buy_sell_stock()
        {
            int[] prices = { 7, 1, 5, 3, 6, 4 };
            int result = MaxProfit(prices);

            Console.WriteLine(result);
        }

        public int MaxProfit(int[] prices)
        {
            int profit = 0;

            for (int i = 1; i < prices.Length; i++)
            {
                if (prices[i] > prices[i - 1])
                {
                    profit += (prices[i] - prices[i - 1]);
                }
            }

            return profit;

        }
    }

    /*
     Time complexity - O(n) since we only make 1 pass ie. prices.Length
     Space - O(1) - constant space
     */
}
