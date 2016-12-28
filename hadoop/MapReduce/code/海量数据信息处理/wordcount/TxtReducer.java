package com.hadoop.test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;




public class TxtReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

	
	protected void reduce(Text key, Iterable<IntWritable> values,Context context)
			throws IOException, InterruptedException {
		int sum = 0;
		Collection c = new ArrayList();
		Iterator<IntWritable> it = values.iterator();
		while(it.hasNext()){
			IntWritable value = it.next();
			sum += value.get();
		}
		
		context.write(key, new IntWritable(sum));	
	}
}

