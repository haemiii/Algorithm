package com.example.basic;

import java.io.*;
import java.util.StringTokenizer;

public class Problem1267 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        int y = 0;
        int m = 0;
        for (int i = 0; i < N; i++) {
            int time = Integer.parseInt(st.nextToken());
            y += ((time / 30) + 1) * 10;
            m += ((time / 60) + 1) * 15;
        }
        if(y > m){
            bw.write("M" + " " + String.valueOf(m));
        }else if(y < m){
            bw.write("Y" + " " + String.valueOf(y));
        }else{
            bw.write("Y M " + String.valueOf(y));
        }
        bw.flush();
    }
}