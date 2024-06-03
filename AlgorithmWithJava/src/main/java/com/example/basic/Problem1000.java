package com.example.basic;

import java.io.*;
import java.util.StringTokenizer;

public class Problem1000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer tokenizer = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(tokenizer.nextToken());
        int b = Integer.parseInt(tokenizer.nextToken());

        bw.write(String.valueOf(a + b));
        bw.flush();
        bw.close();
    }
}
