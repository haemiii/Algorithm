package com.example.basic;

import java.io.*;
import java.util.StringTokenizer;

public class Problem2480 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        if(a == b && b == c){
            bw.write(String.valueOf(10000 + a*1000));
        }else if(a == b){
            bw.write(String.valueOf(1000 + a * 100));
        }else if(b == c){
            bw.write(String.valueOf(1000 + b * 100));
        }else if(c == a){
            bw.write(String.valueOf(1000 + c * 100));
        }else{
            if(a >= b && a >= c){
                bw.write(String.valueOf(a * 100));
            }else if(b >= a &&  b >= c){
                bw.write(String.valueOf(b * 100));
            }else{
                bw.write(String.valueOf(c * 100));
            }
        }
        bw.flush();
    }
}