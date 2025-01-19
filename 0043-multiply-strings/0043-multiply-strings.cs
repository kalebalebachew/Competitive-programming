public class Solution {
    public string Multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }
        
        int[] result = new int[num1.Length + num2.Length];
        
        for (int i = num1.Length - 1; i >= 0; i--) {
            for (int j = num2.Length - 1; j >= 0; j--) {
                int digit1 = num1[i] - '0';
                int digit2 = num2[j] - '0';
                
                int sum = digit1 * digit2 + result[i + j + 1];
                result[i + j + 1] = sum % 10;
                result[i + j] += sum / 10;
            }
        }
    
        StringBuilder sb = new StringBuilder();
        foreach (int r in result) {
            if (!(sb.Length == 0 && r == 0)) {
                sb.Append(r);
            }
        }
        
        return sb.Length == 0 ? "0" : sb.ToString();
    }
}
