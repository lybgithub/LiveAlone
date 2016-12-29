package com.hbase;

import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
import org.apache.hadoop.hbase.mapreduce.TableReducer;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;

public class HbaseTest {

	private static final String targetTable = "hbaseYanbiao";
	static Configuration config = HBaseConfiguration.create();

	public static void createTable(String tablename, String[] cfs)
			throws IOException {
		// �½�һ�� HBaseAdmin ��Ķ��������������Ԫ���ݵĲ�������������ɾ���
		HBaseAdmin admin = new HBaseAdmin(config);
		if (admin.tableExists(tablename)) {
			// ������Ѿ�����
			System.out.println("table already exists");
		} else {
			//��������ڣ�ִ�����¶����½�
			//����һ�� HTableDescriptor ��������������ϸ��Ϣ
			HTableDescriptor tableDesc = new HTableDescriptor(tablename);
			//������һһ�ӵ� tableDesc ������
			for (int i = 0; i < cfs.length; i++) {
				tableDesc.addFamily(new HColumnDescriptor(cfs[i]));
			}
			//������
			admin.createTable(tableDesc);
			System.out.println("create table successly");
		}
	}

	/**
	 * @param args
	 * @throws IOException
	 * @throws ClassNotFoundException
	 * @throws InterruptedException
	 */
	public static void main(String[] args) throws IOException,
			InterruptedException, ClassNotFoundException {
		/*
		 * ʹ�� mapreduce �� HBase ��������
		 */
		// ���������Ϊ colfamily
		
		String[] cfs = { "colfamily" };
		
		//���� zookeeper
		config.set("hbase.zookeeper.quorum", "192.168.83.33");
		// ����һ�� hbasemr ��ֻ��һ������Ϊ colfamily
		createTable(targetTable, cfs);
		
		// �½���ҵ���� mapreduce �� ���ݵ��� hbase
//		final Job job = Job.getInstance(config, HBaseMR.class.getSimpleName());
		Job job = new Job(config, "HbaseTest");
		TableMapReduceUtil.addDependencyJars(job);
		job.setJarByClass(HbaseTest.class);
		
		//������ҵ�� map ��
		job.setMapperClass(InputMapper.class);
		//������ҵ�� reduce ������
		TableMapReduceUtil.initTableReducerJob(targetTable, Reducer.class, job);
		
		//��ҵ����·��
		FileInputFormat.addInputPath(job, new Path(args[0]));
		
		//������ҵ���������
		job.setOutputKeyClass(NullWritable.class);
		job.setOutputValueClass(Text.class);
		
		//�ύ��ҵ
		boolean b = job.waitForCompletion(true);
		if (!b) {
			throw new IOException("error");
		}
	}

	public static class InputMapper extends
			Mapper<Object, Text, NullWritable, Text> {

		public void map(Object key, Text value, Context context)
				throws IOException, InterruptedException {
			// map ��ʲôҲ������ֱ�ӽ�����д��
			context.write(NullWritable.get(), value);
		}
	}

	public static class Reducer extends
			TableReducer<NullWritable, Text, ImmutableBytesWritable> {
		String time;
		String spName;
		String userID;
		String serverIP;
		String hostName;
		String uploadTraffic;
		String downloadTraffic;

		public void reduce(NullWritable key, Iterable<Text> values,
				Context context) throws IOException, InterruptedException {

			for (Text val : values) {
				String line = val.toString();
				String[] fields = line.split("\t");

				time = fields[0];
				userID = fields[1];
				serverIP = fields[2];
				hostName = fields[3];
				spName = fields[4];
				uploadTraffic = fields[5];
				downloadTraffic = fields[6];
				
				//���� rowkey Ϊʱ��ֵ
				Put put = new Put(Bytes.toBytes(time));
				// ���壬�У�ֵ
				put.add(Bytes.toBytes("colfamily"), Bytes.toBytes("userID"),
						Bytes.toBytes(userID));
				put.add(Bytes.toBytes("colfamily"), Bytes.toBytes("serverIP"),
						Bytes.toBytes(serverIP));
				put.add(Bytes.toBytes("colfamily"), Bytes.toBytes("hostName"),
						Bytes.toBytes(hostName));
				put.add(Bytes.toBytes("colfamily"), Bytes.toBytes("spName"),
						Bytes.toBytes(spName));
				put.add(Bytes.toBytes("colfamily"),
						Bytes.toBytes("uploadTraffic"),
						Bytes.toBytes(uploadTraffic));
				put.add(Bytes.toBytes("colfamily"),
						Bytes.toBytes("downloadTraffic"),
						Bytes.toBytes(downloadTraffic));
				
				//������д��
				context.write(null, put);
			}
		}
	}
}

