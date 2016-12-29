package com.hadoop.bigdata;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class BigReduce extends Reducer<Text, Text, Text, Text> {

	
	protected void reduce(Text key, Iterable<Text> values,Context context)
			throws IOException, InterruptedException {
//		int sum = 0;
//		Iterator<IntWritable> it = values.iterator();
//		while(it.hasNext()){
//			IntWritable value = it.next();
//			sum += value.get();
//		}
//		context.write(key, new IntWritable(sum));
//<userid|spName,1|upTraffic|downTraffic>
		
		Iterator<Text> it = values.iterator();
		String old_key = key.toString();
		Map<String, Integer> map = new HashMap<String, Integer>();
		try{
		while(it.hasNext()){
			String value = it.next().toString();
			String[] strs = value.split(",");
			String map_key = old_key+'|'+strs[0]+'|'+strs[1];
			String map_value0 = strs[2];
			int map_value = Integer.parseInt(map_value0);
			map.put(map_key, map_value);
		}
		//System.out.println(map);
		}
		catch(Exception e){
			System.out.println("kong");
		}
		
		
		List<Entry<String,Integer>> list =new ArrayList<Entry<String,Integer>>(map.entrySet()); 
	        Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {  
	            //Ωµ–Ú≈≈–Ú  
	            @Override  
	            public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {  
	                //return o1.getValue().compareTo(o2.getValue());  
	                return o1.getValue().compareTo(o2.getValue());  
	            }  
	        });  
	  
	        for (Map.Entry<String, Integer> mapping : list) {  
	            //System.out.println(mapping.getKey() + ":" + mapping.getValue());
	        	Text key1 = new Text(mapping.getKey());
	        	String value1 = String.valueOf(mapping.getValue());
	        	context.write(key1, new Text(value1));
	        }  
	
	}
}

		
	

