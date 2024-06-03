package com.example.basic;

import java.io.*;
import java.util.StringTokenizer;

public class Problem2490 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i = 0; i < 3; i++) {
            int sum_value = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                sum_value += Integer.parseInt(st.nextToken());
            }
            if(sum_value == 3){
                bw.write("A");
            }else if(sum_value == 2){
                bw.write("B");
            }else if(sum_value == 1){
                bw.write("C");
            }else if(sum_value == 0){
                bw.write("D");
            }else if(sum_value == 4){
                bw.write("E");
            }
            bw.newLine();
        }
        bw.flush();

    }
}