from Knn import *


def main():
    pointlist: list = []
    predict: Point
    while (True):
        try:
            pointlist.append(
                Point(int(input('Enter x coordinate: ')), int(input('Enter y coordinate: ')), input('Enter class: ')))
        except ValueError:
            print('Invalid input type, please input coordinates in integer value')
        if input('type "y" to continue, if no press Enter ') != 'y':
            break
    print('Enter predict coordinate')
    predict = Point(int(input('Enter x coordinate: ')), int(input('Enter y coordinate: ')))
    classifier = Classifier(pointlist, predict, int(input('Enter radius: ')))
    print(classifier.classify())

if __name__ == "__main__":
    main()
