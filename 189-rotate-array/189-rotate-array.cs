public class Solution {
    public void Rotate(int[] nums, int k) {
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

                for (int i = 0; i < nums.Length; i++)
                {
                    nums[i] = result[i];
                }
            }

    }
}