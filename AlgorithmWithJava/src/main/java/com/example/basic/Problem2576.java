package com.example.basic;

import java.io.*;
import java.util.StringTokenizer;

public class Problem2576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int sum = 0;
        int min = 101;
        for (int i = 0; i < 7; i++) {
            int value = Integer.parseInt(br.readLine());
            if(value % 2 != 0){
                sum += value;
                if(min > value){
                    min = value;
                }
            }
        }

        if(min == 101){
            bw.write(String.valueOf(-1));
        }else{
            bw.write(String.valueOf(sum));
            bw.newLine();
            bw.write(String.valueOf(min));
        }
        bw.flush();
    }
}