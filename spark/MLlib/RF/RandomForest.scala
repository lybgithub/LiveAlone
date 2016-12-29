import org.apache.spark.{SparkConf, SparkContext}
// $example on$
import org.apache.spark.mllib.tree.RandomForest
import org.apache.spark.mllib.tree.model.RandomForestModel
import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.linalg.Vectors  
// $example off$

object RandomForest1 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
    val sc = new SparkContext(conf)
    // $example on$
    // Load and parse the data file.
    //val data = MLUtils.loadLibSVMFile(sc, "data/mllib/sample_libsvm_data.txt")
    // Split the data into training and test sets (30% held out for testing)
    //val splits = data.randomSplit(Array(0.7, 0.3))

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
    val (trainingData, testData) = (tree1,tree2)

    // Train a RandomForest model.
    // Empty categoricalFeaturesInfo indicates all features are continuous.
    val numClasses = 2
    val categoricalFeaturesInfo = Map[Int, Int]()
    val numTrees = 5000 // Use more in practice.
    val featureSubsetStrategy = "auto" // Let the algorithm choose.
    val impurity = "gini"
    val maxDepth = 8
    val maxBins = 32

    val model = RandomForest.trainClassifier(trainingData, numClasses, categoricalFeaturesInfo,
      numTrees, featureSubsetStrategy, impurity, maxDepth, maxBins)

    // Evaluate model on test instances and compute test error
    val lPreds = testData.map { point =>
      val prediction = model.predict(point)
      prediction
    }
    lPreds.repartition(1).saveAsTextFile("resultRF")


    // val testErr = labelAndPreds.filter(r => r._1 != r._2).count.toDouble / testData.count()
    // println("Test Error = " + testErr)
    // println("Learned classification forest model:\n" + model.toDebugString)

    // // Save and load model
    // model.save(sc, "target/tmp/myRandomForestClassificationModel")
    // val sameModel = RandomForestModel.load(sc, "target/tmp/myRandomForestClassificationModel")
    // $example off$
  }
}