import org.apache.log4j.{Level, Logger}  
import org.apache.spark.mllib.feature.HashingTF  
import org.apache.spark.mllib.linalg.Vectors  
import org.apache.spark.mllib.regression.LabeledPoint  
import org.apache.spark.mllib.tree.DecisionTree  
import org.apache.spark.mllib.util.MLUtils  
import org.apache.spark.{SparkConf, SparkContext}  
      
    /** 
      * 决策树分类 
      */  
    object TreeDemo {  
      
      def main(args: Array[String]) {  
      
        val conf = new SparkConf()  
        val sc = new SparkContext(conf)  
        Logger.getRootLogger.setLevel(Level.WARN)  
      
        //训练数据  
        val data1 = sc.textFile("trainDataExcel.txt")  
      
        //测试数据  
        val data2 = sc.textFile("testDataExcel.txt")  
      
      
        //转换成向量  
val tree1 = data1.map {line =>  
          val parts = line.split(',')  
          LabeledPoint(parts(6).toDouble, Vectors.dense(Array(parts(0).toDouble,parts(1).toDouble,parts(2).toDouble,parts(3).toDouble,parts(4).toDouble,parts(5).toDouble)))
	}

val tree2 = data2.map { line =>  
          val parts = line.split(',')  
          Vectors.dense(Array(parts(0).toDouble,parts(1).toDouble,parts(2).toDouble,parts(3).toDouble,parts(4).toDouble,parts(5).toDouble))
	}

//tree1.foreach(println)
//println(tree1.count)

val (trainingData, testData) = (tree1, tree2)

val numClasses = 2
val categoricalFeaturesInfo = Map[Int, Int]()  
val impurity = "gini"
//最大深度  
val maxDepth = 7  
//最大分支  
val maxBins = 32 

//模型训练  
val model = DecisionTree.trainClassifier(trainingData, numClasses, categoricalFeaturesInfo,  
  impurity, maxDepth, maxBins) 
 
//预测结果
val labelAndPreds = testData.map { point =>  
  val prediction = model.predict(point)  
  prediction  
} 

labelAndPreds.repartition(1).saveAsTextFile("result")

       }  
      
         }









