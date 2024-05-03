import cv2
import numpy as np

def analyze_chromatic_aberration(image_path):

    original_image = cv2.imread(image_path) #open image

    b, g, r = cv2.split(original_image) #split image in rgb

    diff_rg = cv2.absdiff(r, g) #calculate difference between rg
    diff_gb = cv2.absdiff(g, b) #calculate difference between gb
    total_diff = cv2.add(diff_rg, diff_gb) #add differences between rg and gb

    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) #convert image to grayscale
    total_norm_diff = cv2.divide(total_diff, gray_image) #divide the difference between rg and gb of each pixel by the grayscale image (=brightness)

    # thresholded_array = np.where(gray_image < np.mean(gray_image), 0, 255) #create array where all pixels with grayscale value lower than threshold are zero
    # total_norm_diff[thresholded_array == 0] = 0 #set all values that are equal to zero in thresholded_array to zero


    total_norm_diff = np.average(total_norm_diff) #take average of each pixel


    return total_norm_diff

if __name__ == "__main__":

    image_path = 'chromatic aberration images/1.jpg'
    total_diff_normalized = analyze_chromatic_aberration(image_path)
    print(f"Average chromatic aberration image 1: {total_diff_normalized:.3f}")

    image_path = 'chromatic aberration images/2.jpg'
    total_diff_normalized = analyze_chromatic_aberration(image_path)
    print(f"Average chromatic aberration image 2: {total_diff_normalized:.3f}")

    image_path = 'chromatic aberration images/3.jpg'
    total_diff_normalized = analyze_chromatic_aberration(image_path)
    print(f"Average chromatic aberration image 3: {total_diff_normalized:.3f}")

    image_path = 'chromatic aberration images/4.jpg'
    total_diff_normalized = analyze_chromatic_aberration(image_path)
    print(f"Average chromatic aberration image 4: {total_diff_normalized:.3f}")

    image_path = 'chromatic aberration images/5.jpg'
    total_diff_normalized = analyze_chromatic_aberration(image_path)
    print(f"Average chromatic aberration image 5: {total_diff_normalized:.3f}")

    image_path = 'chromatic aberration images/6.jpg'
    total_diff_normalized = analyze_chromatic_aberration(image_path)
    print(f"Average chromatic aberration image 6: {total_diff_normalized:.3f}")

    image_path = ('chromatic aberration images/7.jpg')
    total_diff_normalized = analyze_chromatic_aberration(image_path)
    print(f"Average chromatic aberration image 7: {total_diff_normalized:.3f}")

    image_path = 'chromatic aberration images/8.jpg'
    total_diff_normalized = analyze_chromatic_aberration(image_path)
    print(f"Average chromatic aberration image 8: {total_diff_normalized:.3f}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
