package com.hadoop.filter;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class FilterJob2 {

	public static void main(String[] args) throws Exception {
//		Configuration conf = new Configuration();
//		GenericOptionsParser optionparser = new GenericOptionsParser(conf, args);
//		conf = optionparser.getConfiguration();
		Job job = new Job();      //创建一个新任务
		job.setJarByClass(FilterJob2.class);    //设置主要工作类
		//job.setJobName("wordCount");
		
		
		FileInputFormat.addInputPath(job, new Path(args[0]));    //添加输入路径到Job
		FileOutputFormat.setOutputPath(job, new Path(args[1]));	//添加输出路径到Job
		
		job.setMapperClass(FilterMapper.class);      //设置类和Reducer类
		//job.setReducerClass(FilterReducer.class);
		//job.setNumReduceTasks(conf.getInt("reduce_num", 0));
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		
		job.waitForCompletion(true);	
	}

}
