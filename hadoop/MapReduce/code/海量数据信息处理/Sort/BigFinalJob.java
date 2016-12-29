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
		
		//Path file = new Path("");   //Map�����ļ�·��
		//Path outFile = new Path("");  //����ļ�·��
		Job job = new Job();      //����һ��������
		job.setJarByClass(BigFinalJob.class);    //������Ҫ������
		//job.setJobName("wordCount");
		
		
		FileInputFormat.addInputPath(job, new Path(args[0]));    //�������·����Job
		FileOutputFormat.setOutputPath(job,  new Path(args[1]));	//������·����Job
		
		job.setMapperClass(BigMap.class);      //�������Reducer��
		job.setReducerClass(BigReduce.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		
		job.waitForCompletion(true);	
		
	}

}
