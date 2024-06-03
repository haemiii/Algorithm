package com.example.basic;

import java.io.*;
import java.util.StringTokenizer;

public class Problem10093 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        long min, max;

        if(A==B){
            bw.write(String.valueOf(0));
        }else {
            if (A >= B) {
                min = B;
                max = A;
            } else {
                min = A;
                max = B;
            }
            bw.write(String.valueOf(max - min - 1));
            bw.newLine();
            for (long i = min + 1; i < max; i++) {
                bw.write(String.valueOf(i) + " ");
            }
        }
        bw.flush();
    }
}
