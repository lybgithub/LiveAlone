/**
  * Created by ANT on 2016/12/13.
  */
import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.mllib.classification.SVMWithSGD
import org.apache.spark.mllib.util.MLUtils

object SVMDemo {
  def main(args: Array[String]) {
    val conf = new SparkConf()
    val sc = new SparkContext(conf)
    Logger.getRootLogger.setLevel(Level.WARN)

    val trainData = MLUtils.loadLibSVMFile( sc, "trainDataSVM.txt")

    val numIterations = 100
    val model = SVMWithSGD.train(trainData, numIterations)


    val testData = MLUtils.loadLibSVMFile(sc, "testDatanew.txt")

    val result = testData.map(x=>model.predict(x.features))
    result.repartition(1).saveAsTextFile("svm")

    sc.stop()
  }
}
