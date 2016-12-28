package com.hadoop.test;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class WordCount {
	//�̳�mapper�ӿڣ�����map����������Ϊ<Object,Text>
	//�������Ϊ<Text,IntWritable>
	public static class Map extends Mapper<Object,Text,Text,IntWritable>{
		//one��ʾ���ʳ���һ��
		private static IntWritable one = new IntWritable(1);
		//word�洢���µĵ���
		private Text word = new Text();
		public void map(Object key,Text value,Context context) throws IOException,InterruptedException{
			//����������д�
			StringTokenizer st = new StringTokenizer(value.toString());
			while(st.hasMoreTokens()){
				word.set(st.nextToken());//���µĵ��ʴ���word
				context.write(word, one);
			}
		}
	}
	//�̳�reducer�ӿڣ�����reduce����������<Text,IntWritable>
	//�������Ϊ<Text,IntWritable>
	public static class Reduce extends Reducer<Text,IntWritable,Text,IntWritable>{
		//result��¼���ʵ�Ƶ��
		private static IntWritable result = new IntWritable();
		public void reduce(Text key,Iterable<IntWritable> values,Context context) throws IOException,InterruptedException{
			int sum = 0;
			//�Ի�ȡ��<key,value-list>����value�ĺ�
			for(IntWritable val:values){
				sum += val.get();
			}
			//��Ƶ�����õ�result
			result.set(sum);
			//�ռ����
			context.write(key, result);
		}
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		Configuration conf = new Configuration();
		//�����������
		String[] otherArgs = new GenericOptionsParser(conf,args).getRemainingArgs();
		if(otherArgs.length != 2){
			System.err.println("Usage WordCount <int> <out>");
			System.exit(2);
		}
		//������ҵ��
		Job job = new Job(conf,"word count");
		//������ҵ������
		job.setJarByClass(WordCount.class);
		job.setMapperClass(Map.class);
		job.setCombinerClass(Reduce.class);
		job.setReducerClass(Reduce.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}

}
