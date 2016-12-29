package com.shujuliliang;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Hello world!
 * 成功实现
 */
public class RulerTestWord
{
	/**
	 * main函数
	 **/
    public static void main( String[] args )
    {
        
        System.out.println( "Hello World!" );        
        ArrayList<String> zhengze = readFileByLines("C:/Users/gujie/Desktop/zhengze.txt");
        ArrayList<String> yuandata = readFileByLines("C:/Users/gujie/Desktop/yuandata.txt");
        testRegexJD(zhengze,yuandata);
        System.out.println("Done");
        //testRegexMogujie();
    }
    
    /**
     * 验证正则表达式’
     * @param regexStr 正则表达式
     * @param testStr 测试字符串
     * @return 返回为空ArrayList 或者 ArrayList
     **/
    private static ArrayList<String> validateRegex(String regexStr1, String testStr, boolean isExtract){
        System.out.println("源字符串：" + testStr);
        //针对特殊正则表达式进行转换---搜索关键词
        String regexStr = new String();
        if (regexStr1.contains("<<>>")){
        	regexStr = regexStr1.replaceAll("<<>>","(?<kw>[^=&]+)");
        	System.out.println(regexStr);
        	
        }
        else{
        	regexStr = regexStr1;
        }
        
        Pattern pattern = Pattern.compile(regexStr);
        System.out.println("正则字符串：" + pattern.toString());
        Matcher matcher = pattern.matcher(testStr);
        String[] styleList=new String[]{"model","series","dealer","mtypes","kw"};
        ArrayList<String> match = new ArrayList<String>();
        if (matcher.find()) {
			if (isExtract){
				for (int i = 0; i < styleList.length; i++){
					//System.out.println(regexStr.contains("<"+styleList[i]+">"));
				    if (regexStr.contains("<"+styleList[i]+">")){
					   //System.out.println("OK");
	                   match.add(styleList[i]+':'+matcher.group(styleList[i]));
				    }
				}
			}
			           //return "series"+':'+matcher.group("series")+" type"+':'+matcher.group("type");
        else{
        	match.add(matcher.group());
        }
				    } 
		else {
        	match.add("null");
       }
        return match;
    }
    
    public static  ArrayList<String> readFileByLines(String FileName) {
    	/**
    	 * 读取文件
    	 * 按行读取
    	 * @param FileName 文件路径
    	 * 返回ArrayList
    	 */
        File file = new File(FileName);
        BufferedReader reader = null;
        ArrayList<String> List = new ArrayList<String>();  
        try {
            System.out.println("以行为单位读取文件内容，一次读一整行：");
            reader = new BufferedReader(new FileReader(file));
            String tempString = null;
            // 一次读入一行，直到读入null为文件结束
            while ((tempString = reader.readLine()) != null) {
                List.add(tempString);
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e1) {
                }
            }
        }
       return List;
	}
    
    /**
     * JAVA正则表达式 批量匹配
     * @param zhengzeList 正则表达式ArrayList 由文件输入返回得到
     * @param yuandataList 同上 测试字符串源数据ArrayList
     */
    private static void testRegexJD(ArrayList<String> zhengzeList,ArrayList<String> yuandataList) {
    	for (int j=0;j < zhengzeList.size() ; j++){
    	String	zhengze= zhengzeList.get(j);
    	String  yuandata= yuandataList.get(j);
        System.out.println("汽车规则正则输出========");
    	//System.out.println(zhengze);
        System.out.println("汽车PC端规则========");
        //System.out.println(yuandata);
        
        //调用匹配函数
        System.out.println("汽车商品编号：" + validateRegex(zhengze,yuandata, true)+"\n");
    	}
    }
}
