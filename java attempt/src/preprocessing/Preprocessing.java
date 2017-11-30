package preprocessing;

import java.io.BufferedReader;
import java.io.FileReader;
import weka.core.Instance;
import weka.core.Instances;
import weka.filters.unsupervised.attribute.ReplaceMissingValues;
import weka.filters.supervised.instance.SMOTE;
import weka.filters.unsupervised.instance.Randomize;
import weka.filters.unsupervised.attribute.Normalize;

public class Preprocessing {

	// TODO
	/* Function to Read the Arff file to Instances */
	public Instances readArffFile(String filename) {

	}

	// TODO
	/*
	 * Replaces missing values using mean and mode imputation method for given
	 * Instances Returns the new Instances mean and mode values replaced for missing
	 * value instance
	 */

	public Instances replaceMissingValues(Instances data) throws Exception {

	}

	/*
	 * Use SMOTE with given percentage and kValue Returns the new set of Instances
	 * after applying SMOTE
	 */
	// TODO
	public Instances balanceDataSMOTE(Instances newData, double percentage, int kValue) throws Exception {

	}

	// TODO
	/*
	 * Function Randomizes the given Instances. Done after SMOTE Returns the
	 * randomized Instances
	 */
	public Instances AfterSmoteDataRandomize(Instances data) throws Exception {

	}
	// TODO

	/*
	 * Function normalizes numeric attributes in the given Instances. Returns the
	 * normalized Instances
	 */
	public Instances NormalizedData(Instances data) throws Exception {

	}
	// TODO

	/* Function removes missing value instances from given Instances */
	public Instances removeMissingInstances(Instances data) {
	}
}
