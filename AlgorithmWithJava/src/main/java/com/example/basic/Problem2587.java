package com.example.basic;

import java.io.*;
import java.util.Arrays;

public class Problem2587 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int sum = 0;
        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            sum += arr[i];
        }
        Arrays.sort(arr);
        bw.write(String.valueOf(sum / 5));
        bw.newLine();
        bw.write(String.valueOf(arr[2]));
        bw.flush();
    }
}