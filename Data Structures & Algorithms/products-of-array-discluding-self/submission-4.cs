public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
    int zeroCount = nums.Count(n => n == 0);

    int[] result;

    if (zeroCount > 1)
    {
        // Two or more zeros -> every position's product without self still includes a zero
        result = new int[nums.Length];
    }
    else if (zeroCount == 1)
    {
        // Exactly one zero -> only the zero index gets the product of all other items
        int nonZeroProduct = nums.Where(n => n != 0).Aggregate(1, (acc, val) => acc * val);
        result = nums.Select(x => x == 0 ? nonZeroProduct : 0).ToArray();
    }
    else
    {
        // No zeros -> your original total-product division logic works safely
        int totalProduct = nums.Aggregate(1, (acc, val) => acc * val);
        result = nums.Select(x => totalProduct / x).ToArray();
    }

    return result;

    }
}
