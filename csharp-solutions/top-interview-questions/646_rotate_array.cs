using System;
using System.Collections.Generic;
using System.Text;

namespace csharp_solutions.top_interview_questions
{
    class _646_rotate_array
    {

        public _646_rotate_array()
        {
            List<int> nums = new List<int> { 1, 2, 3, 4, 5, 6, 7 };
            int k = 3;

            Rotate(nums.ToArray(), k);
            RotateSmart(nums.ToArray(), k);

            nums = new List<int> { -1, -100, 3, 99 };
            k = 2;

            Rotate(nums.ToArray(), k);
            RotateSmart(nums.ToArray(), k);
        }

        // Brute force + inplace
        public void Rotate(int[] nums, int k)
        {
            k %= nums.Length;

            if (k % nums.Length != 0)
            {
                while (k != 0)
                {
                    for (int i = nums.Length - 1; i > 0; i--)
                    {
                        int tmp = nums[i];
                        nums[i] = nums[i - 1];
                        nums[i - 1] = tmp;
                    }

                    k--;
                }
            }

            // this part is for us
            for (int i = 0; i < nums.Length; i++)
            {
                Console.Write(nums[i].ToString() + ",");
            }
            Console.WriteLine("");

        }

        // smarter way - extra space?
        public void RotateSmart(int[] nums, int k)
        {
            k %= nums.Length;

            if (k != 0)
            {
                List<int> result = new List<int>();

                for (int i = nums.Length - k; i < nums.Length; i++)
                {
                    result.Add(nums[i]);
                }

                for (int i = 0; i < nums.Length - k; i++)
                { 
                    result.Add(nums[i]);
                }

                // manual assignment 
                for (int i = 0; i < nums.Length; i++)
                {
                    nums[i] = result[i];
                }
            }

            // this part is for us
            for (int i = 0; i < nums.Length; i++)
            {
                Console.Write(nums[i].ToString() + ",");
            }
            Console.WriteLine("");
        }
        /*
        Note: we cannot just do  nums = result.ToArray() since 
        that would only update LOCAL "nums" variable not the LEETCODE global "nums" variable
         */
    }
}
