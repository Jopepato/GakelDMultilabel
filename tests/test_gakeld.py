import unittest

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from Gakel.gakeld import GakelD
from .classifier_basetest import ClassifierBaseTest

TEST_LABELSET_SIZE = 3


class GakelDTest(ClassifierBaseTest):

    def get_gakeld_with_svc(self):
        return GakelD(
            base_classifier=SVC(probability=True),
            base_classifier_require_dense=[False, True],
            labelset_size=TEST_LABELSET_SIZE
        )

    def get_gakeld_with_nb(self):
        return GakelD(
            base_classifier=GaussianNB(),
            base_classifier_require_dense=[True, True],
            labelset_size=TEST_LABELSET_SIZE
        )

    def test_if_sparse_classification_works_on_non_dense_base_classifier(self):
        classifier = self.get_gakeld_with_svc()
        self.assertClassifierWorksWithSparsity(classifier, 'sparse')
        self.assertClassifierPredictsProbabilities(classifier, 'sparse')

    def test_if_dense_classification_works_on_non_dense_base_classifier(self):
        classifier = self.get_gakeld_with_svc()
        self.assertClassifierWorksWithSparsity(classifier, 'dense')
        self.assertClassifierPredictsProbabilities(classifier, 'dense')

    def test_if_sparse_classification_works_on_dense_base_classifier(self):
        classifier = self.get_gakeld_with_nb()
        self.assertClassifierWorksWithSparsity(classifier, 'sparse')
        self.assertClassifierPredictsProbabilities(classifier, 'sparse')

    def test_if_dense_classification_works_on_dense_base_classifier(self):
        classifier = self.get_gakeld_with_nb()
        self.assertClassifierWorksWithSparsity(classifier, 'dense')
        self.assertClassifierPredictsProbabilities(classifier, 'dense')

    def test_if_works_with_cross_validation(self):
        classifier = self.get_gakeld_with_nb()
        self.assertClassifierWorksWithCV(classifier)


if __name__ == '__main__':
    unittest.main()
