//过滤条件：SpName为qq的user
package com.hadoop.filter;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class FilterMapper extends Mapper<LongWritable, Text, Text, Text>{
	
	protected void map(LongWritable key, Text value,Context context)
			throws IOException, InterruptedException {
		String[] strs = value.toString().split("	");
		String UserId = strs[1];  //UserId
		String SpName = strs[4];  //SpName
		String UpTraffic = strs[5];  //UpTraffic
		String DownTraffic = strs[6];  //DownTraffic
		String key1 = UserId+'|'+SpName;
		String value1 = UpTraffic+'|'+DownTraffic;
		if(SpName.equals("qq")||SpName.equals("google")){
			context.write(new Text(key1),new Text(value1));  //输出SpName是qq的SpName	
		}
	}
	
}
