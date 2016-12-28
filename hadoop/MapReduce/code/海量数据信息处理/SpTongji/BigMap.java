package com.hadoop.bigdata;
import java.io.IOException;

//import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

//"2012-07-05 00:06:10	8412672a	183.213.18.16	st.ucweb.com	ucweb	0	0"   1,4,5,6

public class BigMap extends Mapper<LongWritable, Text, Text, Text> {

	
	protected void map(LongWritable key, Text value,Context context)
			throws IOException, InterruptedException {
		String[] strs = value.toString().split("	");
//		for(String str:strs){
//			context.write(new Text(str), new IntWritable(1));
//			}
		
		String UserId = strs[1];  //UserId
		String SpName = strs[4];  //SpName
		String UpTraffic = strs[5];  //UpTraffic
		String DownTraffic = strs[6];  //DownTraffic
		
		String newKey = UserId+"|"+SpName;//组合成新的key：用户名和服务提供商
		String newValue = "1"+"|"+UpTraffic+"|"+DownTraffic;//组合成新的value：访问次数，上下行流量
		
		context.write(new Text(newKey), new Text(newValue));  //要与上面继承Mapper类中标记的泛型一致
			
		}
}



