import cv2
from skimage.feature import graycomatrix, graycoprops
from sklearn.tree import DecisionTreeRegressor
import numpy as np


class DamageDetector:
    def __init__(self):
        self.distance = [1]
        self.angle = [0]
        self.reg = DecisionTreeRegressor()
<<<<<<< HEAD
=======
        # assuming you have your training data in a pandas DataFrame called 'df'
>>>>>>> origin/master
        # with columns 'Contrast', 'Correlation', 'Energy', 'Homogeneity', and 'Severity'
        X = [[22.152499372917195, 0.9948180354786471, 0.04012856769422608,
              0.47550734466605193], [59.60232353339657, 0.9743965930957489,
                                     0.0498203561916233, 0.4938516699708361], [107.52505175983438,
                                                                               0.9462022215038837, 0.031093890933675, 0.304424081263114],
             [218.8316056910569, 0.971579822396659, 0.019486330390021993,
              0.26919281405188167], [23.447924736308924, 0.9874309245487564,
                                     0.057507228929725325, 0.5671017970769522], [45.3582702625024,
                                                                                 0.9951530872856408, 0.2644295351724016, 0.6054088081724558],
             [47.64696722363048, 0.9929780249067642, 0.06413658839640043,
             0.427539100428598], [201.4649531358482, 0.9777519065538748,
                                  0.02196232501693057, 0.26181723721325917], [98.54021847070507,
                                                                              0.9861207041248978, 0.0375535238921104, 0.3428125593717354],
             [18.349812748542526, 0.9968473973396608, 0.19068699287141758,
             0.6014100542661281], [25.08155129894261, 0.9412243182376638,
                                   0.5324994969437048, 0.761757266630862], [254.6584242517844,
                                                                            0.9552188582011869, 0.3237823221136538, 0.4737464993937011],
             [69.34406570428035, 0.9917353768744535, 0.32982256796756787,
             0.5887479953629757], [98.66750899666822, 0.9868702510813246,
                                   0.032013870616169164, 0.3651489730445611], [51.04021763191313,
                                                                               0.9882350925941793, 0.028344559550332323, 0.3792636601764379],
             [43.44871883977389, 0.9897473497630546, 0.03217376939944195,
             0.4578558481311268], [94.38783715865303, 0.9158359691672621,
                                   0.05943553368974027, 0.36214117370398685], [50.730711605521016,
                                                                               0.9813213638679649, 0.08763601295024892, 0.5448310868375734],
             [12.98149027052682, 0.9970342367625326, 0.052790408626697184,
             0.49425124837749235], [117.57788315879601, 0.9706056930589387,
                                    0.1962151779261175, 0.4344733769331206], [53.36779661016949,
                                                                              0.9186441349843619, 0.07041982157877455, 0.476405157681334],
             [5.296873317851156, 0.9990534670046203, 0.06882986124326303,
             0.6168430343949189], [17.048009506833033, 0.9636622026153062,
                                   0.06846554609353248, 0.48598665692476045], [14.88440585631597,
                                                                               0.9942867828759459, 0.03946947520395291, 0.39208171052955315],
             [108.05902657139835, 0.9680671218056223, 0.07586489981012927,
             0.31245714345299697], [143.0160949252338, 0.9857269418508031,
                                    0.026666828045956572, 0.33471709719772036], [582.200674050177,
                                                                                 0.9110739736351061, 0.019638792040517616, 0.17725262750607113],
             [67.52338736913205, 0.9748448358149123, 0.027890910522131718,
             0.33899303120302327], [431.88598710909525, 0.8114806506934429,
                                    0.012847923535640862, 0.09720047834455488], [576.3397735746729,
                                                                                 0.7744043648950508, 0.01775937289390033, 0.09153932885652279],
             [401.4233204253489, 0.8528328312650517, 0.012897333223869843,
             0.08868177159317311], [166.65700366388853, 0.9694057784423264,
                                    0.014638779460324195, 0.20381192249597105]]
        y = [7, 7, 6, 8, 5, 4, 8, 7, 8, 9, 7, 8, 9, 7, 9, 6,
             5, 3, 2, 2, 3, 2, 1, 2, 9, 7, 6, 5, 6, 5, 5, 9]
        self.reg.fit(X, y)

    def predict_severity(self, image_path):
        # Load the image and convert it to grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Calculate the GLCM
        glcm = graycomatrix(image, distances=self.distance,
                            angles=self.angle, symmetric=True, normed=True)

        # Calculate the texture features
        contrast = graycoprops(glcm, 'contrast')[0][0]
        correlation = graycoprops(glcm, 'correlation')[0][0]
        energy = graycoprops(glcm, 'energy')[0][0]
        homogeneity = graycoprops(glcm, 'homogeneity')[0][0]

        # Make a prediction for the new image
        new_image = np.array([[contrast, correlation, energy, homogeneity]])
        predicted_severity = self.reg.predict(new_image)

        return predicted_severity[0]
