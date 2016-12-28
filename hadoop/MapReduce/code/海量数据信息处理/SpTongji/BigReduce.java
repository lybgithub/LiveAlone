package com.hadoop.bigdata;
import java.io.IOException;
import java.util.Iterator;
//import org.apache.hadoop.io.IntWritable;
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
		int sumCishu = 0;
		int sumUpTraffic = 0;
		int sumDownTraffic = 0;
		Iterator<Text> it = values.iterator();
		while(it.hasNext()){
			Text value = it.next();
			String value1 = value.toString();
			String[] strs = value1.split("|");
			int cishu = Integer.parseInt(strs[0]);    //访问次数
			int upTraffic = Integer.parseInt(strs[1]);  //上行流量
			int downTraffic = Integer.parseInt(strs[2]); //下行流量
			sumCishu = sumCishu+cishu;
			sumUpTraffic = sumUpTraffic+upTraffic;
			sumDownTraffic = sumDownTraffic+downTraffic;
	}
		String cishu = String.valueOf(sumCishu);
		String upTraffic = String.valueOf(sumUpTraffic);
		String downTraffic = String.valueOf(sumDownTraffic);
		String sum = cishu+"|"+upTraffic+"|"+downTraffic;
		context.write(key, new Text(sum));		
	}
}

