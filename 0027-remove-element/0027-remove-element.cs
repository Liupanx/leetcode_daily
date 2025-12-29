public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int writeIndex = 0;
        foreach(int num in nums)
        {
            if (num != val)
            {
                nums[writeIndex] = num;
                writeIndex++;
            }
        }
        return writeIndex;
    }
}