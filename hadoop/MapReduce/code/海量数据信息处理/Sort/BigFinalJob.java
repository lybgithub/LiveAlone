package com.hadoop.bigdata;
//import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
//import org.apache.hadoop.util.GenericOptionsParser;



public class BigFinalJob {
	public static void main(String[] args) throws Exception{
		
		//Configuration conf = new Configuration();
		//String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		
		//Path file = new Path("");   //Map输入文件路径
		//Path outFile = new Path("");  //输出文件路径
		Job job = new Job();      //创建一个新任务
		job.setJarByClass(BigFinalJob.class);    //设置主要工作类
		//job.setJobName("wordCount");
		
		
		FileInputFormat.addInputPath(job, new Path(args[0]));    //添加输入路径到Job
		FileOutputFormat.setOutputPath(job,  new Path(args[1]));	//添加输出路径到Job
		
		job.setMapperClass(BigMap.class);      //设置类和Reducer类
		job.setReducerClass(BigReduce.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		
		job.waitForCompletion(true);	
		
	}

}
