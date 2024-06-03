package com.example.basic;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

// X보다 작은 수
public class Problem10871 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer firstLine = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(firstLine.nextToken());
        int X = Integer.parseInt(firstLine.nextToken());

        StringTokenizer secondLine = new StringTokenizer(br.readLine());
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(secondLine.nextToken());
        }

        for(int i=0; i < N; i++){
            if(A[i] < X){
                wr.write(A[i] + " ");
            }
        }
        wr.flush();
        wr.close();
//        System.out.println(Arrays.toString(A));
    }
}
