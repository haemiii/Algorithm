package com.example.basic;

import java.io.*;
import java.util.StringTokenizer;

public class Problem10804 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[20];
        for (int i = 0; i < 20; i++) {
            arr[i] = i+1;
        }
        for (int i = 0; i < 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) -1;
            int b = Integer.parseInt(st.nextToken()) -1;

            int round = (b-a+1)/2;
            for (int j = 0; j < round; j++) {
                int t = arr[a+j];
                arr[a+j] = arr[b-j];
                arr[b-j] = t;
            }
        }
        for (int i = 0; i < 20; i++) {
            bw.write(arr[i] + " ");
        }
        bw.flush();
    }
}
