package com.example.basic;

import java.io.*;

public class Problem2562 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[9];
        int max_value = 0;
        int max_index = 0;

        for (int i = 0; i < 9; i++){
            arr[i] = Integer.parseInt(br.readLine());
            if (max_value < arr[i]) {
                max_value = arr[i];
                max_index = i;
            }
        }
        bw.write(String.valueOf(max_value));
        bw.newLine();
        bw.write(String.valueOf(max_index+1));
        bw.flush();
    }
}
