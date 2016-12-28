import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

import java.io.IOException;

/**
 * Created by youzhi on 2016/10/24.
 */
public class OneWeekFlowCount {
    public static class WordCountMapper extends Mapper<LongWritable,Text,Text,LongWritable>{
        protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            int i=0;
            String line = value.toString();
            String[] words = line.split(",");
            String time = words[1];
            String location = words[2];
            String hour = time.substring(4,6);
            String day = time.substring(0,4);
            String timeAndhourAndlocation = time + "\t" +hour+"\t"+location;

            if(day.equals("1025")||day.equals("1026")||day.equals("1027")||day.equals("1028")||day.equals("1029")||day.equals("1030")||day.equals("1031")){

                context.write(new Text(timeAndhourAndlocation),new LongWritable(1));
            }else {
                return;
            }



        }
    }
    public static class WordCountReducer extends Reducer<Text,LongWritable,Text,LongWritable>{
        @Override
        protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
            long count=0;
            for(LongWritable value:values){
                count +=value.get();
            }
            context.write(key,new LongWritable(count));
        }
    }
    public static void main(String[] args) throws Exception{
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf,"oneweekflowcount");
        job.setJarByClass(OneWeekFlowCount.class);

        job.setMapperClass(WordCountMapper.class);
        job.setReducerClass(WordCountReducer.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);

        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);
        job.setNumReduceTasks(1);//设置只输出一个文件


        FileInputFormat.setInputPaths(job,new Path(args[0]));
        FileOutputFormat.setOutputPath(job,new Path(args[1]));

        job.waitForCompletion(true);


    };
}
