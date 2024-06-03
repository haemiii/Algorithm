package com.example.basic;

import java.io.*;

public class Problem2444 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                bw.write(" ");
            }
            for (int j = 0; j <= i; j++) {
                bw.write("*");
            }
            for (int j = 0; j < i; j++) {
                bw.write("*");
            }
            bw.newLine();
        }
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j <= i; j++) {
                bw.write(" ");
            }
            for (int j = 0; j < n - i-1; j++) {
                bw.write("*");
            }
            for (int j = 0; j < n - i - 2; j++) {
                bw.write("*");
            }
            bw.newLine();
        }
        bw.flush();
    }
}