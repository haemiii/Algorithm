package com.example.basic;

import java.io.*;
import java.util.Arrays;

public class Problem2309 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[9];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            sum += arr[i];
        }
        Arrays.sort(arr);
        boolean found = false;
        for (int i = 0; i < 9; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (sum - arr[i] - arr[j] == 100) {
                    // 두 명을 제외한 7명의 키 출력
                    for (int k = 0; k < 9; k++) {
                        if (k != i && k != j) {
                            bw.write(arr[k] + "\n");
                        }
                    }
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        bw.flush();
        bw.close();
        br.close();
    }
}