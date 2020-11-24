public class Solution {
    public int MinDeletionSize(string[] A)
        {
            int N = A.Length;
            int M = A[0].Length;

            int[,] matrix = new int[A.Length, A[0].Length];

            for(int i = 0; i < N; i++)
            {
                for(int j = 0; j < M; j++)
                {
                    matrix[i, j] = A[i][j];
                }
            }

            int count = 0;

            for (int j = 0; j < M; j++)
            {
                bool flag = true;
                for (int i = 0; i < N-1; i++)
                {
                    if (matrix[i, j] > matrix[i + 1, j])
                    {
                        flag = false;
                        break;
                    }
                }

                if (flag == false)
                {
                    count += 1;
                }
            }

            return count;
        }
}